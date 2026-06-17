import json
import os

def report_node(state):

    os.makedirs(
        "outputs",
        exist_ok=True
    )

    with open(
        "outputs/relevant_pages.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            state["relevant_pages"],
            f,
            indent=4,
            ensure_ascii=False
        )

    print("\nTop Relevant Pages:\n")

    for page in state["relevant_pages"][:10]:

        print(
            f"Score: {page['score']}"
        )

        print(
            f"URL: {page['url']}"
        )

        print(
            f"Reason: {page.get('reason', 'No explanation available')}\n"        
        )
        print("-" * 50)

    return {
        "report":
        "Generated outputs/relevant_pages.json and outputs/site_map.png"
    }