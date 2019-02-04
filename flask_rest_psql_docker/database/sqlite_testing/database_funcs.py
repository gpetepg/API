import os
import pandas as pd
from sqlalchemy import create_engine

import sqlite3
from sqlite3 import Error


def create_sqlite_db(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()


def check_if_sqlite_exists():
    if not os.path.isfile(os.path.join(os.getcwd(), "people.sqlite")):
        create_sqlite_db(os.path.join(os.getcwd(), "people.sqlite"))


def insert_csv_to_db(engine_str, df, table=None, exist_option="append", test=False):
    """Insert pandas.DataFrame data via pandas.DataFrame.to_sql and SQLAlchemy engine.

    :param engine_str: str; SQLAlchemy formatted host string
    :param df: pandas.DataFrame; DataFrame to insert
    :param exist_option: str; set option is table exists
    """

    engine = create_engine(
        engine_str,
        echo=False,  # Set True to see raw SQL
    )

    conn = engine.connect()

    df.to_sql(
        name=table,
        con=engine,
        index=False,
        if_exists=exist_option,  # "replace" will recreate table if it exists and then insert
    )

    if test:
        data = engine.execute(f"SELECT * FROM {table}").fetchall()
        print(data)

    conn.close()


# Run main if testing
def main():
    check_if_sqlite_exists()
    insert_csv_to_db(
        'sqlite:///people.sqlite',
        pd.read_csv(os.path.join(os.environ["API_FILES"], 'people.csv')),
        table="people",
        test=True,
    )


if __name__ == '__main__':
    main()
