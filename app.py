from graph.workflow import (
    create_workflow
)


def main():

    url = input(
        "Website URL: "
    )

    interest = input(
        "Topic of interest: "
    )

    workflow = create_workflow()

    result = workflow.invoke(
        {
            "url": url,
            "interest": interest
        }
    )

    print(
        result["report"]
    )

    print("\nTop Matches:\n")

    for page in result.get(
        "relevant_pages",
        []
    )[:10]:

        print(
            f"[{page['score']}] "
            f"{page['url']}"
    )


if __name__ == "__main__":
    main()