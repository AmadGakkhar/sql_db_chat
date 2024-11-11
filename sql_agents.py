from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_core.messages import SystemMessage
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from utils.llm import get_model
from utils.db_funcs import load_db, get_schema, run_query
from utils.prompt import get_sql_prefix

llm = get_model()
db = load_db("test")
SQL_PREFIX = get_sql_prefix()

toolkit = SQLDatabaseToolkit(db=db, llm=llm)

tools = toolkit.get_tools()


system_message = SystemMessage(content=SQL_PREFIX)


agent_executor = create_react_agent(llm, tools, state_modifier=SQL_PREFIX)

responses = []
for s in agent_executor.stream(
    {
        "messages": [
            HumanMessage(
                content="from autotraders inventory, what is the minimum price? Ignore non-numeric prices"
            )
        ]
    }
):
    print(s)
    print("----")
    responses.append(s)
print("Final Response")
print(responses[-1]["agent"]["messages"][0].content)
