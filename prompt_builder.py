from schema import SCHEMA

FEW_SHOTS = """
Q: Top 5 companies by employees
A: SELECT company_name FROM companies ORDER BY employee_size DESC LIMIT 5;

Q: Companies in California
A: SELECT company_name FROM companies WHERE state = 'CA';
"""

def build_prompt(question: str) -> str:
    return f"""
You are a PostgreSQL expert.

Convert the user question into SQL.

Rules:
- Only return SQL
- No explanation
- Use LIMIT for top queries
- Use correct column names

{FEW_SHOTS}

Schema:
{SCHEMA}

Question:
{question}
"""