from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import os

class FlaskGenerator:
    def __init__(self, config):
        self.config = config
        self.template_dir = Path(__file__).parent / "templates"
        self.env = Environment(loader=FileSystemLoader(self.template_dir))
    
    def generate(self):
        project_path = Path.cwd() / self.config["project_name"]
        project_path.mkdir(exist_ok=True)
        
        # Generate main files
        self._generate_file("app.py.j2", project_path / "app.py")
        self._generate_file("requirements.txt.j2", project_path / "requirements.txt")
        self._generate_file("README.md.j2", project_path / "README.md")
        
        # Generate templates directory
        templates_dir = project_path / "templates"
        templates_dir.mkdir(exist_ok=True)
        self._generate_file("flask_templates/index.html.j2", templates_dir / "index.html")
        
        # Generate database files if needed
        if self.config["database"]:
            self._generate_file("models.py.j2", project_path / "models.py")
        
        # Generate sample routes if needed
        if self.config["sample_routes"]:
            routes_dir = project_path / "routes"
            routes_dir.mkdir(exist_ok=True)
            (routes_dir / "__init__.py").touch()
            self._generate_file("routes/sample.py.j2", routes_dir / "sample.py")
        
        return project_path
    
    def _generate_file(self, template_name, output_path):
        template = self.env.get_template(template_name)
        content = template.render(**self.config)
        output_path.write_text(content)