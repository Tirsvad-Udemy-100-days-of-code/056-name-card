[English](Step-3-Static-Files) · [Dansk](Step-3-Static-Files-da) · **Bahasa Malaysia**

# Langkah 3: Halakan halaman ke folder static

Fail statik disajikan di bawah `/static/`. Ubah setiap pautan `assets/...` dan `images/...` dalam HTML supaya bermula dengan `static/`, atau lebih baik, biarkan Flask membina URL dengan `url_for`:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='assets/css/main.css') }}" />
<img src="{{ url_for('static', filename='images/avatar.jpg') }}" alt="Portrait" />
```

Kini halaman mempunyai gaya, fon dan imejnya. Jika anda masih melihat rupa lama, pelayar telah menyimpan CSS dalam cache: paksa muat semula dengan Ctrl+Shift+R.

![Langkah 3: laluan telah dibetulkan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-name-card/raw/branch/main/docs/screenshots/step-3-static-paths-fixed.png)

## Apa yang kita peroleh

- Bagaimana `url_for('static', filename=...)` memastikan pautan betul walau di mana aplikasi diletakkan.
- Pelayar menyimpan fail statik dalam cache, jadi muat semula paksa ialah pembaikan pertama apabila perubahan tidak kelihatan.
- Ujian memeriksa bahawa setiap pautan `/static/` pada halaman memberi HTTP 200.

Seterusnya: [Langkah 4: Jadikan ia milik anda](Step-4-Personalise-ms)
