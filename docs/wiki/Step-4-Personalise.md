**English** · [Dansk](Step-4-Personalise-da) · [Bahasa Malaysia](Step-4-Personalise-ms)

# Step 4: Make it your own

Replace the name, the headline, the links and the portrait, and change the background image. In this project the text comes from a `Profile` object built from `constants.py`, and the template only shows it. The HTML5 UP credit stays in the footer.

The portrait is sized to fit the card, so it sits centred on the line as in the template. The background shows software development, AI and machine learning: code, a small neural network and binary digits. A script that uses only the Python standard library draws it as an SVG (`tools/background/generate.py`), and the card's own rules live in `card.css`, so the template stylesheet `main.css` stays untouched.

![Step 4: the personalised card](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-name-card/raw/branch/main/docs/screenshots/step-4-personalised-card.png)

## What we gained

- Keeping content (constants) apart from layout (template) makes later changes small.
- A custom portrait and background make the template a real name card.
- A picture that is wider than its container breaks the layout; size the image to the container.
- Overrides in a separate stylesheet keep the downloaded template easy to update.
- Respecting a licence is part of finishing a project.

Next: [Run and test](Run-and-Test)
