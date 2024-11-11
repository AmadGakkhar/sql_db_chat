from langchain_community.utilities import SQLDatabase


def load_db(db_name: str):

    sqlite_uri = f"sqlite:///./db/{db_name}.db"
    db = SQLDatabase.from_uri(sqlite_uri)
    return db


def get_schema(db):
    schema = db.get_table_info()
    return schema


def run_query(db, query):
    result = db.run(query)
    return result


if __name__ == "__main__":
    db = load_db("test")
    schema = get_schema(db)
    print(schema)
