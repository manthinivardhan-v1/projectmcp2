from fastapi import FastAPI
from mcp_client import ask

app = FastAPI()

@app.get("/query")
def query(q: str):
    return ask(q)


# CLI mode
if __name__ == "__main__":
    while True:
        q = input("\nAsk: ")
        if q.lower() in ["exit", "quit"]:
            break

        response = ask(q)
        print("\nResponse:\n", response)