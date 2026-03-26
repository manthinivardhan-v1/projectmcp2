SCHEMA = """
Table: companies

Columns:
- id (varchar, primary key)
- company_name (varchar)
- address (varchar)
- city (varchar)
- state (varchar)
- zipcode (varchar)
- county_name (varchar)
- website (varchar)
- phone (varchar)
- email (varchar)
- contact_name (varchar)
- primary_naics_code (varchar)
- naics_description (text)
- primary_sic_code (varchar)
- sic_description (text)
- employee_size (int)
- sales_volume (float)
- year_established (int)
- latitude (float)
- longitude (float)

Rules:
- Use ONLY this table
- Do NOT hallucinate columns
"""