import textstat

def score_readability(text: str) -> dict:
    return {
        "flesch_reading_ease": textstat.flesch_reading_ease(text),
        "grade_level": textstat.flesch_kincaid_grade(text)
    }