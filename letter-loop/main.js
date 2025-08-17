// Function to send weekly prompt emails
function sendWeeklyPrompts() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Prompts");
  const prompts = sheet.getRange("A:A").getValues().flat().filter(String);
  
  const randomPrompt = prompts[Math.floor(Math.random() * prompts.length)];
  
  const participantsSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Participants");
  const participants = participantsSheet.getRange("A2:B").getValues().filter(row => row[0] && row[1]);
  
  for (const [name, email] of participants) {
    MailApp.sendEmail({
      to: email,
      subject: "Weekly Prompt",
      body: `Hi ${name},\n\nYour prompt for this week is:\n\n"${randomPrompt}"\n\nPlease reply to this email with your response.`
    });
  }
  
  // Record the prompt sent in the Responses sheet
  const responsesSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Responses");
  responsesSheet.appendRow([new Date(), randomPrompt]);
}

// Function to collect responses from email replies
function collectEmailResponses() {
  const threads = GmailApp.search('subject:"Weekly Prompt" newer_than:1w');
  const responsesSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Responses");
  const participantsSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Participants");

  // Load participants data from Participants sheet
  const participantsData = participantsSheet.getRange('A2:B').getValues(); // Fetch Name (A) and Email (B)

  threads.forEach(thread => {
    const messages = thread.getMessages();
    messages.forEach(message => {
      const senderEmail = message.getFrom().match(/<(.*?)>/)[1]; // Extract sender's email address
      const response = message.getPlainBody(); // Get plain text body of the email
      
      // Find participant name associated with sender's email
      let senderName = "";
      participantsData.forEach(participant => {
        if (participant[1] === senderEmail) { // Check against Email (column B)
          senderName = participant[0]; // Assign participant name from Name (column A)
          return; // Exit forEach loop
        }
      });
      
      if (senderName) {
        // Check if response is already recorded
        const data = responsesSheet.getDataRange().getValues(); // Fetch all data
        const headers = data[0]; // Assuming first row is headers
        
        // Find index of participant column
        const columnIndex = headers.indexOf(senderName);
        
        if (columnIndex !== -1) {
          const lastRow = responsesSheet.getLastRow() + 1;
          responsesSheet.getRange(lastRow, 1).setValue(new Date()); // Column A: Date
          responsesSheet.getRange(lastRow, 2).setValue(responsesSheet.getRange(lastRow - 1, 2).getValue()); // Column B: Question
          
          // Set response in the correct column dynamically
          responsesSheet.getRange(lastRow, columnIndex + 1).setValue(response); // columnIndex + 1 to account for Date and Question columns
        } else {
          Logger.log(`Participant ${senderName} not found in headers.`);
        }
      }
    });
  });
}

// Function to send consolidated email
function sendConsolidatedEmail() {
  const responsesSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Responses");
  const lastRow = responsesSheet.getLastRow();
  const lastResponseRow = responsesSheet.getRange(lastRow, 1, 1, responsesSheet.getLastColumn()).getValues()[0];
  
  const [date, question, ...responses] = lastResponseRow;
  const participantsSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Participants");
  const participants = participantsSheet.getRange("A2:B").getValues().filter(row => row[0] && row[1]);
  
  let emailContent = `Question: ${question}\n\n`;
  
  participants.forEach(participant => {
    const [name, email] = participant;
    const participantResponse = responsesSheet.getRange(lastRow, 3 + participants.indexOf(participant)).getValue();
    emailContent += `${name}: ${participantResponse}\n\n`;
  });
  
  // Get all participant emails
  const recipientEmails = participants.map(participant => participant[1]).filter(email => email).join(",");
  
  MailApp.sendEmail({
    to: recipientEmails, // Send to all participants
    subject: "Crackheads Unite",
    body: emailContent
  });
}

// Function to set up weekly triggers
function setUpTriggers() {
  ScriptApp.newTrigger('sendWeeklyPrompts')
    .timeBased()
    .everyWeeks(1)
    .onWeekDay(ScriptApp.WeekDay.MONDAY)
    .atHour(9)
    .create();
  
  ScriptApp.newTrigger('collectEmailResponses')
    .timeBased()
    .everyDays(1)
    .atHour(18)
    .create();
  
  ScriptApp.newTrigger('sendConsolidatedEmail')
    .timeBased()
    .everyWeeks(1)
    .onWeekDay(ScriptApp.WeekDay.SATURDAY)
    .atHour(18)
    .create();
}
