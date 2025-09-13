import typer
from rich.console import Console
from rich.prompt import Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.tree import Tree
from pathlib import Path
import time
from .generator import FlaskGenerator

app = typer.Typer(help="🚀 Create Flask projects with style")
console = Console()

@app.command()
def create(
    project_name: str = typer.Argument(..., help="Name of your Flask project")
):
    """Create a new Flask project"""
    
    # Welcome message
    console.print(f"\n🚀 [bold blue]Creating Flask project:[/bold blue] [bold green]{project_name}[/bold green]\n")
    
    # Interactive prompts
    console.print("🗃️  [bold]Database Setup[/bold]")
    console.print("   We'll use SQLite + SQLAlchemy")
    database = Confirm.ask("   Would you like to set up a database?", default=True)
    
    console.print("\n🛤️  [bold]Sample Routes[/bold]")
    console.print("   Include example API endpoints")
    sample_routes = Confirm.ask("   Want some example routes to get you started?", default=True, choices=["Yes please", "No"])
    
    # Configuration
    config = {
        "project_name": project_name,
        "database": database,
        "sample_routes": sample_routes,
        "author": "lalithaar"
    }
    
    # Generate project with progress bar
    console.print(f"\n✨ [bold green]Creating {project_name}/[/bold green]")
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Setting up your Flask project...", total=None)
        
        generator = FlaskGenerator(config)
        project_path = generator.generate()
        
        # Simulate some work for better UX
        time.sleep(0.5)
        progress.update(task, description="Creating templates...")
        time.sleep(0.3)
        progress.update(task, description="Installing dependencies...")
        time.sleep(0.2)
    
    # Success message with file tree
    console.print(f"\n✨ [bold green]Created {project_name}/[/bold green]")
    
    tree = Tree(f"📁 {project_name}/")
    tree.add("📄 app.py          [dim]# Flask app with your config[/dim]")
    if database:
        tree.add("📄 models.py       [dim]# Database models ready to go[/dim]")
    
    # Templates folder
    templates_node = tree.add("📁 templates/")
    templates_node.add("📄 index.html    [dim]# Beautiful landing page[/dim]")
    
    if sample_routes:
        routes_node = tree.add("📁 routes/")
        routes_node.add("📄 sample.py    [dim]# Example API endpoints[/dim]")
    
    tree.add("📄 requirements.txt [dim]# All dependencies included[/dim]")
    tree.add("📄 README.md       [dim]# How to run this thing[/dim]")
    
    console.print(tree)
    
    # Next steps
    console.print(f"\n🚀 [bold yellow]Next steps:[/bold yellow]")
    console.print(f"   [cyan]cd {project_name}[/cyan]")
    console.print(f"   [cyan]pip install -r requirements.txt[/cyan]")
    console.print(f"   [cyan]flask run[/cyan]")
    console.print(f"\n💡 Your app will be running at [link]http://localhost:5000[/link]")

if __name__ == "__main__":
    app()