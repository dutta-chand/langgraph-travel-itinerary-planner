from langgraph.graph import (
    StateGraph,
    END
)

from models.state import SiteMapState

from agents.crawler import crawl_node
from agents.content_agent import content_node
from agents.relevance_agent import relevance_node
from agents.reporter import report_node


def create_workflow():

    graph = StateGraph(
        SiteMapState
    )

    graph.add_node(
        "crawl",
        crawl_node
    )

    graph.add_node(
        "content",
        content_node
    )

    graph.add_node(
        "relevance",
        relevance_node
    )

    graph.add_node(
        "report",
        report_node
    )

    graph.set_entry_point(
        "crawl"
    )

    graph.add_edge(
        "crawl",
        "content"
    )

    graph.add_edge(
        "content",
        "relevance"
    )

    graph.add_edge(
        "relevance",
        "report"
    )

    graph.add_edge(
        "report",
        END
    )

    return graph.compile()