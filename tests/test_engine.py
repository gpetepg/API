"""Test local connection to psql container"""

from sqlalchemy import create_engine


engine = create_engine(
        # 'postgresql+psycopg2://test:password@localhost:5432/testdb',
        'postgresql+psycopg2://localhost/tylerguo',  # Local host
        echo=False,  # Set True to see raw SQL
    )

conn = engine.connect()
conn.close()
