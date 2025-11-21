from config.database import engine
from sqlalchemy.orm import Session, sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def query_db_all(tableName):
    data = session.query(tableName).all
    return data

def query_db_filtered(tableName,column,filterBy):
    data = session.query(tableName).filter_by(
        column=filterBy
        ).all()
    return data