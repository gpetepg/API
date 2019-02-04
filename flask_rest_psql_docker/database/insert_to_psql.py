from sqlite_testing.database_funcs import insert_csv_to_db
import os
import pandas as pd


def main():
    insert_csv_to_db(
        'postgresql+psycopg2://test:password@localhost:5432/testdb',
        pd.read_csv(os.path.join(os.environ["API_FILES"], 'people.csv')),
        table="people",
    )
    print("successful added .csv data to Docker image's psql")


if __name__ == '__main__':
    main()
