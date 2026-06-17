from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import requests


def crawl_site(start_url, max_pages=20):

    visited = set()
    queue = [start_url]

    domain = urlparse(start_url).netloc

    graph = {}

    while queue and len(visited) < max_pages:

        current = queue.pop(0)

        if current in visited:
            continue

        visited.add(current)

        try:

            response = requests.get(
                current,
                timeout=5
            )

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            graph[current] = []

            for a in soup.find_all(
                "a",
                href=True
            ):

                link = urljoin(
                    current,
                    a["href"]
                )

                if urlparse(link).netloc == domain:

                    graph[current].append(
                        {
                            "url": link,
                            "text": a.get_text(strip=True)
                        }
                    )

                    if link not in visited:
                        queue.append(link)

        except:
            pass

    return graph