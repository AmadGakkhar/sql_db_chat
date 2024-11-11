from langchain_core.prompts import ChatPromptTemplate


def get_sql_chain_prompt():
    template = """Based on the table schema below, write a SQL query that would answer the user's question:
    {schema}

    Question: {question}
    SQL Query:
    
    Make sure that the output contains only the query. Few examples of valid outputs are:
    
    SELECT COUNT(*) FROM empoyees;
    SELECT first_name FROM employees;
    SELECT
    first_name,
    last_name
    FROM employees
    WHERE first_name = 'Luca';
    """
    prompt = ChatPromptTemplate.from_template(template)
    return prompt


def get_full_chain_prompt():
    template = """Based on the table schema below, question, sql query, and sql response, write a natural language response:
    {schema}

    Question: {question}
    SQL Query: {query}
    SQL Response: {response}"""
    prompt_response = ChatPromptTemplate.from_template(template)

    return prompt_response
