from sqlalchemy import create_engine


engine = create_engine(
        'postgresql+psycopg2://testusr:password@localhost:5432/testdb',
        echo=False,  # Set True to see raw SQL
    )
conn = engine.connect()


result = conn.execute("select * from people")
for row in result:
    print(row)

conn.close()
