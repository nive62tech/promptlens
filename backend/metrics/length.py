def score_length(text: str) -> dict:
    words = len(text.split())
    chars = len(text)
    return {"words": words, "chars": chars}