from utils.content_extractor import (
    get_page_content
)


def content_node(state):

    pages = []

    sitemap = state["sitemap"]

    visited = set()

    for links in sitemap.values():

        for link in links:

            url = link["url"]

            if url in visited:
                continue

            visited.add(url)

            content = get_page_content(url)

            pages.append(
                {
                    "url": url,
                    "text": content
                }
            )

    return {
        "page_contents": pages
    }