from flask_rest_psql_docker.database.database_funcs import insert_csv_to_db, check_if_sqlite_exists
import os
import pandas as pd


def main():
    check_if_sqlite_exists()
    insert_csv_to_db(
        'sqlite:///people.sqlite',
        pd.read_csv(os.path.join(os.environ["APP_TEST_FILES"], 'people.csv')),
        table="people",
        test=True,
    )


if __name__ == '__main__':
    main()
