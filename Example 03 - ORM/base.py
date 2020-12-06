from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
        "mssql+pyodbc://python:python@localhost/AdventureWorksLT2019?driver=ODBC+Driver+17+for+SQL+Server")
session_factory = sessionmaker(bind=engine)

metadata = MetaData(schema='saleslt')
Base = declarative_base(metadata=metadata)
