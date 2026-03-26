import requests
import re
from config import settings
from prompt_builder import build_prompt


def clean_sql(response_text: str) -> str:
    """
    Cleans LLM output:
    - Removes markdown ```sql ```
    - Extracts only the SQL query
    """

    if not response_text:
        return ""

    # Remove markdown
    cleaned = re.sub(r"```sql|```", "", response_text, flags=re.IGNORECASE).strip()

    # Extract first SELECT query
    match = re.search(r"(select[\s\S]+?;)", cleaned, re.IGNORECASE)

    if match:
        return match.group(1).strip()

    return cleaned.strip()


def generate_sql(question: str) -> str:
    """
    Calls Ollama Cloud model to generate SQL
    """

    prompt = build_prompt(question)

    try:
        response = requests.post(
            f"{settings.OLLAMA_URL}/api/chat",
            headers={
                "Authorization": f"Bearer {settings.OLLAMA_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": settings.OLLAMA_MODEL,  
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "You are a PostgreSQL expert. "
                            "Return ONLY a valid SQL SELECT query. "
                            "No explanation. No markdown."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "stream": False
            },
            timeout=30
        )

        print("STATUS:", response.status_code)
        print("RAW RESPONSE:", response.text)

        if response.status_code != 200:
            raise Exception(f"Ollama API Error: {response.text}")

        data = response.json()

        raw_output = data.get("message", {}).get("content", "")

        if not raw_output:
            raise Exception("Empty response from model")

        sql = clean_sql(raw_output)

        if not sql.lower().startswith("select"):
            raise Exception(f"Invalid SQL generated: {sql}")

        return sql

    except requests.exceptions.Timeout:
        raise Exception("Ollama request timed out")

    except requests.exceptions.RequestException as e:
        raise Exception(f"Network error: {str(e)}")