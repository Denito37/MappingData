from sqlalchemy import create_engine, Column, String, text
from sqlalchemy.orm import declarative_base

url = 'sqlite:///Resources.db'
engine = create_engine(url)

with engine.connect() as connect:
    connect.execute(text('PRAGMA journal_mode = WAL;'))

Base = declarative_base()

class Fountain(Base):
    __tablename__ = 'Fountains'
    id = Column(String, primary_key=True)
    updated_at = Column(String)
    located_at = Column(String)
    borough = Column(String, index=True)
    department = Column(String, index=True)
    status = Column(String)
    coordinates = Column(String)

class Tree(Base):
    __tablename__='Trees'
    id = Column(String, primary_key=True)
    updated_at = Column(String)
    name = Column(String)
    borough = Column(String, index=True)
    district = Column(String, index=True)
    status = Column(String)
    geometry = Column(String)

Base.metadata.create_all(engine)

async def load_data(tablename, data):
    data.to_sql(
        name = tablename,
        con=engine,
        if_exists='replace',
        index=False,
        chunksize=100
    )
    return 0
