**English** · [Dansk](Step-2-Flask-Server-da) · [Bahasa Malaysia](Step-2-Flask-Server-ms)

# Step 2: Create the Flask server

Create the project, a virtual environment and install Flask. Create the two folders Flask expects: `templates/` for HTML and `static/` for CSS, JavaScript, fonts and images. Move the files in, then serve the page at the root route:

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
```

```text
src/name_card/presentation/
├── templates/
│   └── index.html
└── static/
    ├── assets/   (css, webfonts)
    └── images/   (avatar.jpg, bg.jpg)
```

If you leave the paths as they are in the downloaded `index.html`, the browser asks Flask for `/assets/css/main.css` and gets 404. The page renders as plain text:

![Step 2: Flask serves the page but the paths are wrong](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-name-card/raw/branch/main/docs/screenshots/step-2-flask-unfixed-paths.png)

## What we gained

- How a Flask app, a route and `render_template` fit together.
- Why the folder names `templates` and `static` matter.
- How to read a broken page: the browser's network tab shows which URL returned 404.

Next: [Step 3: Point the page at the static folder](Step-3-Static-Files)
