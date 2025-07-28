from openai import OpenAI, APIError


def summarize_with_gpt(text: str, api_key: str, model: str = "gpt-3.5-turbo") -> str | None:
    """Summarize ``text`` using the OpenAI chat completion API."""
    client = OpenAI(api_key=api_key)
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a research assistant. Summarize this paper in 3 paragraphs."},
                {"role": "user", "content": text},
            ],
        )
    except APIError as e:
        print(f"OpenAI API Error: {e}")
        return None
    return response.choices[0].message.content
