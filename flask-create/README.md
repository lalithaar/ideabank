# Flask-Create ⚡

> Stop copying app.py from your last project

A CLI that scaffolds Flask apps so you can skip the boring setup and get straight to building.

## What it does

Creates a proper Flask project structure in seconds instead of copy-pasting the same boilerplate every time.

```bash
$ flask-create my-awesome-api

? Is this an API-only project or full-stack? API-only
? Database? SQLite  
? Authentication? JWT
? Want some example routes? Yes please

✨ Created my-awesome-api/
   ├── app.py          # Flask app with your config
   ├── models.py       # Database models ready to go
   ├── routes/         # Organized route blueprints
   ├── requirements.txt # All dependencies included  
   └── README.md       # How to run this thing

🚀 cd my-awesome-api && flask run
```

## Sample output

Instead of writing this same code for the 47th time:

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['JWT_SECRET_KEY'] = 'your-secret-key'

db = SQLAlchemy(app)
jwt = JWTManager(app)

# ... 20 more lines of the same setup you've written before
```

You get a complete, working Flask app with sensible defaults and proper structure.

## Status

🚧 **Work in Progress** 🚧

Born from the frustration of setting up the same Flask project structure every single assignment in sophomore year. There has to be a better way than copy-pasting from last semester's project.

## Want to help build it?

Email me: **24f2006078@ds.study.iitm.ac.in**

Looking for folks who are also tired of writing `app = Flask(__name__)` for the hundredth time.

## License

GPL v3 - Because good tools should stay free.

---

*"Why am I manually creating app.py again?"* - Every CS student, ever
