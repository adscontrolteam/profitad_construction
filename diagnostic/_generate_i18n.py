#!/usr/bin/env python3
"""Generate EN/DE/PL diagnostic form pages from diagnostic/index.html (no language switcher)."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "index.html"

TRANSLATIONS = {
    "en": {
        "lang": "en",
        "title": "PROFITAD — Diagnostics request",
        "description": "Request a 30-minute PROFITAD diagnostic session on e-commerce revenue growth.",
        "home_href": "../../en/",
        "brand_aria": "PROFITAD — back to home",
        "back": "← Home",
        "eyebrow": "30 minutes · Growth diagnostic",
        "h1": "We'll find revenue growth points for your business",
        "lead": "Fill in a short form. We'll review your current situation and reach out on Telegram to schedule a diagnostic session.",
        "side_aria": "What happens in the diagnostics",
        "side_h2": "What we'll cover on the call",
        "side_p": "No generic theory — only your product, current economics, and real growth opportunities.",
        "b1_t": "Point A",
        "b1_d": "Current revenue, traffic, funnel, and constraints.",
        "b2_t": "Point B",
        "b2_d": "Business goal and a realistic path to reach it.",
        "b3_t": "Growth plan",
        "b3_d": "Priority hypotheses for the next 60–90 days.",
        "note_small": "Format",
        "note_strong": "Not just ads. We look at the offer, website, creatives, analytics, and the full sales funnel.",
        "form_h2": "Tell us about your business",
        "form_p": "It takes about 2 minutes to fill in.",
        "step": "1 form · 6 questions",
        "name": "Your name",
        "name_ph": "For example: Sergey",
        "telegram": "Telegram username",
        "product": "Link to your product",
        "rev_now": "Current revenue? Point A",
        "rev_now_ph": "For example: €30,000 / mo",
        "rev_goal": "Revenue goal? Point B",
        "rev_goal_ph": "For example: €100,000 / mo",
        "traffic": "Which traffic sources do you use now?",
        "chip_partner": "Partner traffic",
        "chip_other": "Other",
        "consent_before": "I have read the ",
        "consent_offer": "offer agreement",
        "consent_and": " and the ",
        "consent_privacy": "privacy policy",
        "consent_after": ", and I consent to the processing of personal data.",
        "submit": "Submit diagnostics request",
        "after": "After you submit, we'll contact you on Telegram.",
        "success": 'The form UI is ready. Connect your endpoint in the <code>action</code> attribute so requests go to CRM or Telegram.',
        "support": "Telegram support ↗",
        "offer_href": "../../offer.html",
        "privacy_href": "../../privacy.html",
    },
    "de": {
        "lang": "de",
        "title": "PROFITAD — Anfrage zur Diagnose",
        "description": "Anfrage für eine 30-minütige PROFITAD-Diagnosesession zum Umsatzwachstum im E-Commerce.",
        "home_href": "../../de/",
        "brand_aria": "PROFITAD — zur Startseite",
        "back": "← Startseite",
        "eyebrow": "30 Minuten · Growth diagnostic",
        "h1": "Wir finden Umsatz-Wachstumspunkte für Ihr Business",
        "lead": "Füllen Sie das kurze Formular aus. Wir prüfen Ihre aktuelle Situation und melden uns per Telegram, um die Diagnosesession zu vereinbaren.",
        "side_aria": "Was in der Diagnose passiert",
        "side_h2": "Was wir im Call besprechen",
        "side_p": "Keine allgemeine Theorie — nur Ihr Produkt, die aktuelle Ökonomie und reale Wachstumschancen.",
        "b1_t": "Punkt A",
        "b1_d": "Aktueller Umsatz, Traffic, Funnel und Engpässe.",
        "b2_t": "Punkt B",
        "b2_d": "Business-Ziel und ein realistischer Weg dorthin.",
        "b3_t": "Wachstumsplan",
        "b3_d": "Prioritäre Hypothesen für die nächsten 60–90 Tage.",
        "note_small": "Format",
        "note_strong": "Nicht nur Ads. Wir schauen auf Angebot, Website, Creatives, Analytics und den gesamten Sales-Funnel.",
        "form_h2": "Erzählen Sie von Ihrem Business",
        "form_p": "Das Ausfüllen dauert etwa 2 Minuten.",
        "step": "1 Formular · 6 Fragen",
        "name": "Ihr Name",
        "name_ph": "Zum Beispiel: Sergey",
        "telegram": "Telegram username",
        "product": "Link zu Ihrem Produkt",
        "rev_now": "Aktueller Umsatz? Punkt A",
        "rev_now_ph": "Zum Beispiel: €30 000 / Monat",
        "rev_goal": "Umsatzziel? Punkt B",
        "rev_goal_ph": "Zum Beispiel: €100 000 / Monat",
        "traffic": "Welche Traffic-Quellen nutzen Sie aktuell?",
        "chip_partner": "Partner-Traffic",
        "chip_other": "Andere",
        "consent_before": "Ich habe den ",
        "consent_offer": "Angebotsvertrag",
        "consent_and": " und die ",
        "consent_privacy": "Datenschutzrichtlinie",
        "consent_after": " gelesen und willige in die Verarbeitung personenbezogener Daten ein.",
        "submit": "Diagnose-Anfrage senden",
        "after": "Nach dem Absenden melden wir uns bei Ihnen in Telegram.",
        "success": 'Das Formular-UI ist bereit. Verbinden Sie Ihren Endpoint im Attribut <code>action</code>, damit Anfragen an CRM oder Telegram gehen.',
        "support": "Telegram-Support ↗",
        "offer_href": "../../offer.html",
        "privacy_href": "../../privacy.html",
    },
    "pl": {
        "lang": "pl",
        "title": "PROFITAD — Zgłoszenie na diagnostykę",
        "description": "Zgłoszenie na 30-minutową sesję diagnostyczną PROFITAD dotyczącą wzrostu przychodu e-commerce.",
        "home_href": "../../pl/",
        "brand_aria": "PROFITAD — wróć na stronę główną",
        "back": "← Strona główna",
        "eyebrow": "30 minut · Growth diagnostic",
        "h1": "Znajdziemy punkty wzrostu przychodu Twojego biznesu",
        "lead": "Wypełnij krótki formularz. Przejrzymy Twoją obecną sytuację i skontaktujemy się na Telegramie, by umówić sesję diagnostyczną.",
        "side_aria": "Co będzie na diagnostyce",
        "side_h2": "Co omówimy na spotkaniu",
        "side_p": "Bez ogólnej teorii — tylko Twój produkt, bieżąca ekonomia i realne możliwości wzrostu.",
        "b1_t": "Punkt A",
        "b1_d": "Bieżący przychód, ruch, lejek i ograniczenia.",
        "b2_t": "Punkt B",
        "b2_d": "Cel biznesu i realistyczny scenariusz jego osiągnięcia.",
        "b3_t": "Plan wzrostu",
        "b3_d": "Priorytetowe hipotezy na najbliższe 60–90 dni.",
        "note_small": "Format",
        "note_strong": "Nie tylko reklama. Patrzymy na ofertę, stronę, kreacje, analitykę i cały lejek sprzedaży.",
        "form_h2": "Opowiedz o swoim biznesie",
        "form_p": "Wypełnienie zajmie około 2 minut.",
        "step": "1 formularz · 6 pytań",
        "name": "Twoje imię",
        "name_ph": "Na przykład: Sergey",
        "telegram": "Telegram username",
        "product": "Link do Twojego produktu",
        "rev_now": "Jaki jest przychód teraz? Punkt A",
        "rev_now_ph": "Na przykład: €30 000 / mies.",
        "rev_goal": "Jaki jest cel przychodu? Punkt B",
        "rev_goal_ph": "Na przykład: €100 000 / mies.",
        "traffic": "Jakie źródła ruchu wykorzystujesz teraz?",
        "chip_partner": "Ruch partnerski",
        "chip_other": "Inne",
        "consent_before": "Zapoznałem/am się z ",
        "consent_offer": "umową oferty",
        "consent_and": " i ",
        "consent_privacy": "polityką prywatności",
        "consent_after": " oraz wyrażam zgodę na przetwarzanie danych osobowych.",
        "submit": "Wyślij zgłoszenie na diagnostykę",
        "after": "Po wysłaniu zgłoszenia skontaktujemy się z Tobą na Telegramie.",
        "success": 'UI formularza jest gotowe. Podłącz endpoint w atrybucie <code>action</code>, aby zgłoszenia trafiały do CRM lub Telegrama.',
        "support": "Wsparcie Telegram ↗",
        "offer_href": "../../offer.html",
        "privacy_href": "../../privacy.html",
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
        'content="Заявка на 30-минутную диагностическую сессию PROFITAD по росту выручки e-commerce бизнеса."',
        f'content="{t["description"]}"',
    )
    html = replace_once(
        html,
        "<title>PROFITAD — Заявка на диагностику</title>",
        f"<title>{t['title']}</title>",
    )

    pairs = [
        (
            '<a class="brand" href="../" aria-label="PROFITAD — на главную">PROFITAD<span></span></a>',
            f'<a class="brand" href="{t["home_href"]}" aria-label="{t["brand_aria"]}">PROFITAD<span></span></a>',
        ),
        (
            '<a class="back-link" href="../">← На главную</a>',
            f'<a class="back-link" href="{t["home_href"]}">{t["back"]}</a>',
        ),
        ("> 30 минут · Growth diagnostic<", f'> {t["eyebrow"]}<'),
        (
            "<h1 id=\"page-title\">Найдём точки роста выручки вашего бизнеса</h1>",
            f'<h1 id="page-title">{t["h1"]}</h1>',
        ),
        (
            "<p class=\"lead\">Заполните короткую форму. Мы изучим вашу текущую ситуацию и свяжемся с вами в Telegram, чтобы договориться о диагностической сессии.</p>",
            f'<p class="lead">{t["lead"]}</p>',
        ),
        ('aria-label="Что будет на диагностике"', f'aria-label="{t["side_aria"]}"'),
        (">Что разберём на встрече<", f'>{t["side_h2"]}<'),
        (
            "<p>Без общей теории — только ваш продукт, текущая экономика и реальные возможности роста.</p>",
            f'<p>{t["side_p"]}</p>',
        ),
        (">Точка А<", f'>{t["b1_t"]}<'),
        (">Текущая выручка, трафик, воронка и ограничения.<", f'>{t["b1_d"]}<'),
        (">Точка Б<", f'>{t["b2_t"]}<'),
        (">Цель бизнеса и реалистичный сценарий её достижения.<", f'>{t["b2_d"]}<'),
        (">План роста<", f'>{t["b3_t"]}<'),
        (">Приоритетные гипотезы на ближайшие 60–90 дней.<", f'>{t["b3_d"]}<'),
        (">Формат<", f'>{t["note_small"]}<'),
        (
            ">Не просто реклама. Смотрим на оффер, сайт, креативы, аналитику и всю воронку продаж.<",
            f'>{t["note_strong"]}<',
        ),
        (">Расскажите о своём бизнесе<", f'>{t["form_h2"]}<'),
        (">Заполнение займёт около 2 минут.<", f'>{t["form_p"]}<'),
        (">1 форма · 6 вопросов<", f'>{t["step"]}<'),
        (">Ваше имя <", f'>{t["name"]} <'),
        ('placeholder="Например: Сергей"', f'placeholder="{t["name_ph"]}"'),
        (">Telegram username <", f'>{t["telegram"]} <'),
        (">Ссылка на ваш продукт <", f'>{t["product"]} <'),
        (">Какая выручка сейчас? Точка А <", f'>{t["rev_now"]} <'),
        ('placeholder="Например: €30 000 / мес"', f'placeholder="{t["rev_now_ph"]}"'),
        (">Какая цель по выручке? Точка Б <", f'>{t["rev_goal"]} <'),
        ('placeholder="Например: €100 000 / мес"', f'placeholder="{t["rev_goal_ph"]}"'),
        (">Какие источники трафика используете сейчас?<", f'>{t["traffic"]}<'),
        (">Партнёрский трафик<", f'>{t["chip_partner"]}<'),
        (">Другие<", f'>{t["chip_other"]}<'),
        (
            '<span>Ознакомлен(а) с <a href="../offer.html" target="_blank" rel="noopener">договором-офертой</a> и <a href="../privacy.html" target="_blank" rel="noopener">политикой конфиденциальности</a>, выражаю согласие на обработку персональных данных.</span>',
            f'<span>{t["consent_before"]}<a href="{t["offer_href"]}" target="_blank" rel="noopener">{t["consent_offer"]}</a>{t["consent_and"]}<a href="{t["privacy_href"]}" target="_blank" rel="noopener">{t["consent_privacy"]}</a>{t["consent_after"]}</span>',
        ),
        (">Отправить заявку на диагностику<", f'>{t["submit"]}<'),
        (">После отправки заявки мы свяжемся с вами в Telegram.<", f'>{t["after"]}<'),
        (
            ">Форма визуально готова. Подключите ваш текущий endpoint в атрибуте <code>action</code>, чтобы заявки отправлялись в CRM или Telegram.<",
            f'>{t["success"]}<',
        ),
        (">Поддержка в Telegram ↗<", f'>{t["support"]}<'),
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
        dest = dest_dir / "index.html"
        dest.write_text(out, encoding="utf-8")
        print(f"Wrote {dest.relative_to(ROOT.parent)}")


if __name__ == "__main__":
    main()
