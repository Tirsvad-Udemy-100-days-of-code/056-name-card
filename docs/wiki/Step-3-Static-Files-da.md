[English](Step-3-Static-Files) · **Dansk** · [Bahasa Malaysia](Step-3-Static-Files-ms)

# Trin 3: Peg siden mod static-mappen

Statiske filer serveres under `/static/`. Ret hvert `assets/...`- og `images/...`-link i HTML'en, så det starter med `static/`, eller lad hellere Flask bygge URL'en med `url_for`:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='assets/css/main.css') }}" />
<img src="{{ url_for('static', filename='images/avatar.jpg') }}" alt="Portrait" />
```

Nu har siden sine typografier, fonte og billeder. Ser du stadig det gamle udseende, har browseren cachet CSS-filen: tving en opdatering med Ctrl+Shift+R.

![Trin 3: stierne er rettet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-name-card/raw/branch/main/docs/screenshots/step-3-static-paths-fixed.png)

## Det lærte vi

- Hvordan `url_for('static', filename=...)` holder links korrekte, uanset hvor appen ligger.
- Browsere cacher statiske filer, så en tvungen opdatering er første løsning, når en ændring ikke vises.
- Testene kontrollerer, at hvert `/static/`-link på siden giver HTTP 200.

Næste: [Trin 4: Gør det til dit eget](Step-4-Personalise-da)
