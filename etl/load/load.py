from sqlalchemy import create_engine

url = 'sqlite:///Resources.db'
engine = create_engine(url,echo=True)
async def load_data(tablename, data):
    data.to_sql(
        name = tablename,
        con=engine,
        if_exists='replace',
        index=False
    )
    return 0