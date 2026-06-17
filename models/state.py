from typing import TypedDict


class SiteMapState(TypedDict):

    url: str

    interest: str

    sitemap: dict

    page_contents: list

    relevant_pages: list

    report: str