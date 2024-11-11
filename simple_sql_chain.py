from langchain.chains import create_sql_query_chain
from langchain_core.runnables import RunnablePassthrough
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from utils.db_funcs import load_db, get_schema, run_query
from utils.llm import get_model
from utils.prompt import get_sql_chain_prompt, get_full_chain_prompt
from langchain_core.output_parsers import StrOutputParser


def run_sql_chain(llm, db, question):

    sql_chain = (
        {
            "question": lambda x: x["question"],
            "schema": lambda x: get_schema(db),
        }
        | get_sql_chain_prompt()
        | llm.bind(stop=["\nSQL Query:"])
        | StrOutputParser()
    )

    full_chain = (
        {
            "question": lambda x: x["question"],
            "schema": lambda x: get_schema(db),
            "query": lambda x: sql_chain.invoke({"question": x["question"]}),
            "response": lambda x: run_query(
                db, sql_chain.invoke({"question": x["question"]})
            ),
        }
        | get_full_chain_prompt()
        | llm.bind(stop=["\nSQL Response:"])
        | StrOutputParser()
    )

    response = full_chain.invoke({"question": question})
    return response


if __name__ == "__main__":
    llm = get_model()
    db = load_db("test")
    user_question = "from autotraders inventory, which dealership has most cars?"
    response = run_sql_chain(llm, db, user_question)
    print(response)
