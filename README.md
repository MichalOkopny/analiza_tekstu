# Aplikacja Django do Przetwarzania Tekstu

Aplikacja po przeczytaniu pliku .txt miesza litery w każdym słowie zostawiając pierwszą i ostatnią.


## Wymagania

- Python 3.8+
- Django 4.0

## Technologie
Projekt wykorzystuje:
- **Python** — język programowania,
- **Django** — framework webowy,
- **HTML** — do struktury interfejsu.

## Instalacja

```bash
git clone https://github.com/MichalOkopny/analiza_tekstu.git
cd Walidacja_PESEL
python3 -m venv .venv
source .venv/bin/activate  # Linux / macOS
.venv\Scripts\activate     # Windows
python manage.py migrate
python manage.py runserver
