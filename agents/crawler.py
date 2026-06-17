from utils.crawler_utils import crawl_site


def crawl_node(state):

    graph = crawl_site(
        state["url"],
        max_pages=20
    )

    return {
        "sitemap": graph
    }