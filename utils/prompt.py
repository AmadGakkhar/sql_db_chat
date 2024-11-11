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


def get_sql_prefix():
    SQL_PREFIX = """
    
    You are an agent designed to interact with a SQL database.
    Given an input question, create a syntactically correct SQLite query to run, then look at the results of the query and return the answer.
    Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most 5 results.
    You can order the results by a relevant column to return the most interesting examples in the database.
    Never query for all the columns from a specific table, only ask for the relevant columns given the question.
    You have access to tools for interacting with the database.
    Only use the below tools. Only use the information returned by the below tools to construct your final answer.
    You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.

    DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.

    To start you should ALWAYS look at the tables in the database to see what you can query.
    Do NOT skip this step.
    Then you should query the schema of the most relevant tables.

    """
    return SQL_PREFIX
