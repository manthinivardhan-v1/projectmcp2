from ollama_client import generate_sql
from sql_validator import validate_sql
from db import run_query

def ask(question: str):
    try:
        sql = generate_sql(question)

        print("\nGenerated SQL:\n", sql)

        safe_sql = validate_sql(sql)

        result = run_query(safe_sql)

        return {
            "question": question,
            "sql": safe_sql,
            "result": result
        }

    except Exception as e:
        return {
            "error": str(e)
        }