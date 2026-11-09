[English](Run-and-Test) · [Dansk](Run-and-Test-da) · **Bahasa Malaysia**

# Jalankan dan uji

Cipta dan gunakan `.venv` setempat, naik taraf pip, pasang projek dengan tambahan ujian, jalankannya, ujinya dan bina dokumentasi Doxygen. Tangkapan skrin diambil dalam bekas Docker dengan pelayar tanpa kepala, jadi tiada tetingkap dibuka pada desktop anda.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
python -m name_card              # open http://127.0.0.1:5000/
python -m pytest
doxygen Doxyfile
bash tools/screenshots/run.sh    # screenshots, in Docker
```

## Apa yang kita peroleh

- Persediaan boleh diulang yang boleh diikuti oleh semua peserta kursus.
- Ujian untuk laluan dan untuk fail statik.
- Dokumentasi API daripada komen Doxygen.
