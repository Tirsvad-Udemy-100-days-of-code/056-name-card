[English](Step-2-Flask-Server) · [Dansk](Step-2-Flask-Server-da) · **Bahasa Malaysia**

# Langkah 2: Cipta pelayan Flask

Cipta projek, persekitaran maya dan pasang Flask. Cipta dua folder yang dijangka Flask: `templates/` untuk HTML dan `static/` untuk CSS, JavaScript, fon dan imej. Alihkan fail ke dalamnya, kemudian sajikan halaman pada laluan akar:

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

Jika laluan dibiarkan seperti dalam `index.html` yang dimuat turun, pelayar meminta `/assets/css/main.css` daripada Flask dan mendapat 404. Halaman dipaparkan sebagai teks biasa:

![Langkah 2: Flask menyajikan halaman tetapi laluan salah](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-name-card/raw/branch/main/docs/screenshots/step-2-flask-unfixed-paths.png)

## Apa yang kita peroleh

- Bagaimana aplikasi Flask, laluan (route) dan `render_template` berfungsi bersama.
- Mengapa nama folder `templates` dan `static` penting.
- Cara membaca halaman yang rosak: tab rangkaian pelayar menunjukkan URL mana yang memberi 404.

Seterusnya: [Langkah 3: Halakan halaman ke folder static](Step-3-Static-Files-ms)
