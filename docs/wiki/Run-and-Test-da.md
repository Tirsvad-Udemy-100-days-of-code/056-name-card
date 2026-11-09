[English](Run-and-Test) · **Dansk** · [Bahasa Malaysia](Run-and-Test-ms)

# Kør og test

Opret og brug en lokal `.venv`, opgradér pip, installér projektet med test-tilvalget, kør det, test det og byg Doxygen-dokumentationen. Skærmbillederne tages i en Docker-container med en headless browser, så der ikke åbnes noget vindue på dit skrivebord.

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

## Det lærte vi

- En gentagelig opsætning, som alle kursister kan følge.
- Test af ruten og af de statiske filer.
- API-dokumentation fra Doxygen-kommentarer.
