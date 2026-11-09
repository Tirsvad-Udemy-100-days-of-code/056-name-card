**English** · [Dansk](Step-3-Static-Files-da) · [Bahasa Malaysia](Step-3-Static-Files-ms)

# Step 3: Point the page at the static folder

Static files are served under `/static/`. Change every `assets/...` and `images/...` link in the HTML so that it starts with `static/`, or better, let Flask build the URL with `url_for`:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='assets/css/main.css') }}" />
<img src="{{ url_for('static', filename='images/avatar.jpg') }}" alt="Portrait" />
```

The page now has its styles, fonts and images. If you still see the old look, the browser has cached the CSS: hard-refresh with Ctrl+Shift+R.

![Step 3: the paths are fixed](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-name-card/raw/branch/main/docs/screenshots/step-3-static-paths-fixed.png)

## What we gained

- How `url_for('static', filename=...)` keeps links correct wherever the app is mounted.
- Browsers cache static files, so a hard refresh is the first fix when a change does not show.
- The tests check that every `/static/` link on the page returns HTTP 200.

Next: [Step 4: Make it your own](Step-4-Personalise)
