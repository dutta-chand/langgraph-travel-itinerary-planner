import json
import re

from utils.llm import llm


def relevance_node(state):

    interest = state["interest"]

    results = []

    pages = state["page_contents"]

    for page in pages:

        content = page["text"][:3000]

        prompt = f"""
User Interest:
{interest}

Analyze this webpage.

Page Content:
{content}

Return ONLY valid JSON.

Example:

{{
    "score": 8,
    "reason": "The page discusses machine learning applications."
}}

Rules:
- score must be between 0 and 10
- reason must be one short sentence
"""

        try:

            response = llm.invoke(prompt)

            raw = response.content

            print("\nRAW RESPONSE:")
            print(raw)

            match = re.search(
                r"\{.*\}",
                raw,
                re.DOTALL
            )

            if match:

                data = json.loads(
                    match.group()
                )

                results.append(
                    {
                        "url": page["url"],
                        "score": int(
                            data.get(
                                "score",
                                0
                            )
                        ),
                        "reason": data.get(
                            "reason",
                            "No explanation"
                        )
                    }
                )

            else:

                results.append(
                    {
                        "url": page["url"],
                        "score": 0,
                        "reason": "Could not parse LLM response"
                    }
                )

        except Exception as e:

            print(
                f"ERROR: {e}"
            )

            results.append(
                {
                    "url": page["url"],
                    "score": 0,
                    "reason": str(e)
                }
            )

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return {
        "relevant_pages": results
    }