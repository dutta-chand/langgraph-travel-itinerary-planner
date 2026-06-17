from bs4 import BeautifulSoup
import requests


def get_page_content(url):

    try:

        response = requests.get(
            url,
            timeout=10
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        text = soup.get_text(
            separator=" ",
            strip=True
        )

        return text[:5000]

    except Exception:

        return ""