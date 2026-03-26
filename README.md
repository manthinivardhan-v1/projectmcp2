# MCP SQL Pipeline (DeepSeek R2 + MCP + PostgreSQL)

## Overview
This project implements a Natural Language to SQL pipeline using the DeepSeek R2 cloud model integrated with the Model Context Protocol (MCP) to enable efficient querying of a PostgreSQL database. It allows users to interact with structured data using plain English, automatically converting queries into SQL, validating them for safety, executing them against the database, and returning structured, human-readable results in real time.

## Pipeline Flow
English Query → Prompt Builder  
Prompt → DeepSeek R2 (via MCP client)  
LLM generates SQL  
SQL Validator checks safety  
Query executes on PostgreSQL  
Results returned to user  

## Project Structure
```
mcp_pro/
│── main.py              # Entry point
│── db.py                # Database connection
│── mcp_client.py        # MCP client logic
│── ollama_client.py     # LLM interaction
│── prompt_builder.py    # Prompt construction
│── schema.py            # Schema handling
│── sql_validator.py     # SQL validation layer
│── config.py            # Configuration
│── requirements.txt     # Dependencies
```

## Setup and Run

### 1. Create Virtual Environment
```bash
python3 -m venv venv
```

### 2. Activate Environment
Mac/Linux:
```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:

```
DATABASE_URL=postgresql://username:password@localhost:5432/dbname
DEEPSEEK_API_KEY=your_api_key
OLLAMA_URL=https://ollama.com
OLLAMA_API_KEY=your_api_key
OLLAMA_MODEL=your_ollama_cloud_model
```

### 5. Run the Application
```bash
python3 main.py
```

## Example Usage
```
Ask: Show top 5 highest transactions
```

The system generates the SQL query, validates it, executes it on PostgreSQL, and returns the results in a structured format.
