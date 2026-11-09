[English](Step-2-Flask-Server) · **Dansk** · [Bahasa Malaysia](Step-2-Flask-Server-ms)

# Trin 2: Opret Flask-serveren

Opret projektet og et virtuelt miljø, og installér Flask. Opret de to mapper, Flask forventer: `templates/` til HTML og `static/` til CSS, JavaScript, fonte og billeder. Flyt filerne ind, og server siden på rodruten:

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

Hvis stierne står som i den hentede `index.html`, beder browseren Flask om `/assets/css/main.css` og får 404. Siden vises som ren tekst:

![Trin 2: Flask serverer siden, men stierne er forkerte](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-name-card/raw/branch/main/docs/screenshots/step-2-flask-unfixed-paths.png)

## Det lærte vi

- Hvordan en Flask-app, en rute og `render_template` hænger sammen.
- Hvorfor mappenavnene `templates` og `static` er vigtige.
- Hvordan du læser en ødelagt side: browserens netværksfane viser, hvilken URL der gav 404.

Næste: [Trin 3: Peg siden mod static-mappen](Step-3-Static-Files-da)
