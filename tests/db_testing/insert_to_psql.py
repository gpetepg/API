from flask_rest_psql_docker.database.database_funcs import insert_csv_to_db
import os
import pandas as pd


def main():
    insert_csv_to_db(
        'postgresql+psycopg2://localhost/tylerguo',  # Localhost Postgresql
        # 'postgresql+psycopg2://test:password@localhost:5432/testdb',  # Localhost for Docker Postgresql
        pd.read_csv(os.path.join(os.environ["APP_TEST_FILES"], 'people.csv')),
        table="people",
    )
    print("successful added .csv data to Postgresql")


if __name__ == '__main__':
    main()
