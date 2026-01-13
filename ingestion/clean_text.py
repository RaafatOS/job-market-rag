import re
from bs4 import BeautifulSoup

def clean_text(raw_html: str) -> str:
    text = BeautifulSoup(raw_html, "html.parser").get_text()
    text = re.sub(r"\s+", " ", text)
    return text.strip()
