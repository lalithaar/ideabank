# letter-loop

## About spreadsheet

https://docs.google.com/spreadsheets/d/1n4YLDlD8ItIqovygIw7n90JhTfPBJ82pepECaB7rY6Y/edit?usp=sharing

1. _Prompts_ : List of prompts in a single column, out of which one is randomly sent out every monday.
2. _Participants_ : List of participants with their name and associated email id's. Format - | Name | Email |
3. _Responses_ : Table to collect replies to "prompt" email and store it. Format - | Date | Question | Name 1 | Name 2 | Name 3 |

## workflow
  similar to that of https://www.letterloop.co/
1. Send out an email with a randomly generated prompt to all the participants ( function sendWeeklyPrompts )
2. On Saturday, Collect responses _replies to the email sent on monday_ and store it in the spreadsheet ( function collectEmailResponses )
3. On Saturday, Send a consolidated email to all the participants with collected emails ( function sendConsolidatedEmail ) _(in a similar format as https://www.letterloop.co/see-a-letterloop)_ 

# Debug
1. On emails, we can ignore the CSS and formatting for now, I want to get the functionality right
2. _sendWeeklyPrompts_ works fine and it sends the email
3. _collectEmailResponses_ - Here is the issue, the question and date is stored but replies to the email is not stored.
   _A possible issues_ :
     Every email usually has a name associated to it, if the function matches the replies based on it - it could be an error. For ex: My email name associated is Lalitha A R, but the name stored in sheets is Lalitha. Is it the issue ?
4. _sendConsolidatedEmail_ works fine and sends the email as a collection of all responses for the question

## how-it-works

1. Define the function collectEmailResponses():
   - This function is triggered automatically to run every week or as per the set schedule.

2. Retrieve the list of emails matching the subject "Weekly Prompt" received in the last week:
   - Use GmailApp.search('subject:"Weekly Prompt" newer_than:1w') to find relevant emails.

3. Access the "Responses" sheet in the Google Sheets document:
   - Get the sheet using SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Responses").

4. Iterate through each email thread retrieved:
   - For each email thread, retrieve individual messages.

5. For each message in the thread:
   - Check if the sender's email matches any participant's email in the "Participants" sheet.
   - Extract the sender's name from the email header and map it to a participant's name.

6. Append the response to the "Responses" sheet:
   - Check if the response (message body) from the email is already recorded for the current week's prompt.
   - If not recorded, append a new row to the "Responses" sheet:
     - Record the current date, the prompt/question of the week, and the participant's response under their respective column.

7. Save and log the operation:
   - Save the updated sheet.
   - Log successful operations or any errors encountered during the process.

8. Ensure triggers are set:
   - Set up triggers in the Google Apps Script editor to run the collectEmailResponses() function on schedule (e.g., weekly).

9. Testing and monitoring:
   - Test the script by manually triggering it from the script editor.
   - Monitor the Logs in the script editor to verify responses are correctly logged under the participant names in the "Responses" sheet.

