#!/usr/bin/env python3
"""Generate EN/DE/PL coming-soon pages (no language switcher). Title 'Coming soon...' stays English."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "index.html"

TRANSLATIONS = {
    "en": {
        "lang": "en",
        "description": "This case study is still being prepared. The full write-up will be published soon.",
        "home_href": "../../en/",
        "brand_aria": "PROFITAD — back to home",
        "back": "← Home",
        "eyebrow": "Case in progress",
        "sub": "We haven't published this case yet",
        "cta_cases": "See other cases",
        "cta_form": "Leave a request",
        "cases_href": "../../en/#cases",
        "form_href": "../../diagnostic/en/",
    },
    "de": {
        "lang": "de",
        "description": "Dieser Case wird noch ausgearbeitet. Die vollständige Ausarbeitung erscheint bald.",
        "home_href": "../../de/",
        "brand_aria": "PROFITAD — zur Startseite",
        "back": "← Startseite",
        "eyebrow": "Case in Bearbeitung",
        "sub": "Wir haben diesen Case noch nicht ausgearbeitet",
        "cta_cases": "Andere Cases ansehen",
        "cta_form": "Anfrage senden",
        "cases_href": "../../de/#cases",
        "form_href": "../../diagnostic/de/",
    },
    "pl": {
        "lang": "pl",
        "description": "Ten case jest jeszcze w przygotowaniu. Pełny opis wkrótce opublikujemy.",
        "home_href": "../../pl/",
        "brand_aria": "PROFITAD — wróć na stronę główną",
        "back": "← Strona główna",
        "eyebrow": "Case w przygotowaniu",
        "sub": "Jeszcze nie przygotowaliśmy tego case'u",
        "cta_cases": "Zobacz inne case'y",
        "cta_form": "Zostaw zgłoszenie",
        "cases_href": "../../pl/#cases",
        "form_href": "../../diagnostic/pl/",
    },
}


def replace_once(html: str, old: str, new: str) -> str:
    if old not in html:
        raise SystemExit(f"Missing string to replace:\n{old[:140]}")
    return html.replace(old, new, 1)


def translate(html: str, t: dict) -> str:
    html = html.replace('lang="ru"', f'lang="{t["lang"]}"', 1)
    html = replace_once(
        html,
        'content="Этот кейс ещё в оформлении. Скоро опубликуем полный разбор."',
        f'content="{t["description"]}"',
    )
    # Title stays "Coming soon..." for all languages
    pairs = [
        (
            '<a class="brand" href="../" aria-label="PROFITAD — на главную">\n        <img src="logo.webp" alt="PROFITAD" width="112" height="72" decoding="async" fetchpriority="high">\n      </a>',
            f'<a class="brand" href="{t["home_href"]}" aria-label="{t["brand_aria"]}">\n        <img src="../logo.webp" alt="PROFITAD" width="112" height="72" decoding="async" fetchpriority="high">\n      </a>',
        ),
        (
            '<a class="back-link" href="../">← На главную</a>',
            f'<a class="back-link" href="{t["home_href"]}">{t["back"]}</a>',
        ),
        ("> Case in progress<", f'> {t["eyebrow"]}<'),
        (">Мы ещё не оформили этот кейс<", f'>{t["sub"]}<'),
        (
            '<a class="btn" href="../#cases">Смотреть другие кейсы</a>',
            f'<a class="btn" href="{t["cases_href"]}">{t["cta_cases"]}</a>',
        ),
        (
            '<a class="btn btn-ghost" href="../diagnostic/">Оставить заявку</a>',
            f'<a class="btn btn-ghost" href="{t["form_href"]}">{t["cta_form"]}</a>',
        ),
    ]
    for old, new in pairs:
        html = replace_once(html, old, new)
    return html


def main():
    source = SRC.read_text(encoding="utf-8")
    for code, t in TRANSLATIONS.items():
        dest_dir = ROOT / code
        dest_dir.mkdir(parents=True, exist_ok=True)
        out = translate(source, t)
        (dest_dir / "index.html").write_text(out, encoding="utf-8")
        print(f"Wrote coming-soon/{code}/index.html")


if __name__ == "__main__":
    main()
