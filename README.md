# 📸 FotoBudka — Dzień Otwarty

Interaktywna aplikacja webowa z kamerą, przygotowana w **Streamlit**.
Uczestnik może zrobić zdjęcie, dodać ramkę, podpis i kod QR, a następnie pobrać gotową pamiątkę w JPG.

Aplikacja działa w przeglądarce (desktop + telefon).

---

## 🚀 Funkcje

- robienie zdjęcia bezpośrednio w przeglądarce
- trzy style ramki: Eco / Tech / Art
- podpis na zdjęciu (domyślnie: `Dołączam do ZS nr4 w Nowym Sączu`)
- kod QR (domyślnie: `https://zsnr4.net`)
- logo szkoły w lewym górnym rogu (wersja biała)
- pobieranie gotowego obrazu jako JPG
- licznik zdjęć:
  - sesyjny (bieżąca sesja użytkownika)
  - globalny (wszystkie zdjęcia zapisane przez aplikację)

---

## 🧱 Technologie

- Python 3.10+
- Streamlit
- Pillow
- qrcode
- SQLite (wbudowane w Python, do globalnego licznika)

---

## ▶️ Uruchomienie

```bash
pip install -r requirements.txt
streamlit run photobooth.py
```

---

## 📂 Pliki

- `photobooth.py` — główna aplikacja
- `requirements.txt` — zależności Pythona
- `photobooth_stats.sqlite3` — baza SQLite z globalnym licznikiem zdjęć

---

## ℹ️ Uwagi

- Globalny licznik jest trwały lokalnie (zapis do pliku `photobooth_stats.sqlite3`).
- Jeśli aplikacja działa na środowisku tymczasowym (np. resetowany kontener), licznik globalny może się wyzerować po restarcie środowiska.
