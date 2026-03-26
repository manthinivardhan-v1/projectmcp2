def validate_sql(query: str) -> str:
    query_clean = query.strip().lower()

    if not query_clean.startswith("select"):
        raise ValueError("Only SELECT queries allowed")

    blocked = ["drop", "delete", "insert", "update", "alter", "truncate"]

    for word in blocked:
        if word in query_clean:
            raise ValueError(f"Blocked keyword detected: {word}")

    return query