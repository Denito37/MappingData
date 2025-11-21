from config.database import engine

async def load_data(tablename, data):
    data.to_sql(
        name = tablename,
        con=engine,
        if_exists='replace',
        index=False,
        chunksize=2500,
        method='multi'
    )
    return 0