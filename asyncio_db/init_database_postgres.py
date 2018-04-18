import asyncio
import sqlalchemy as sa
from aiopg.sa import create_engine


metadata = sa.MetaData()

messages = sa.Table('messages', metadata,
               sa.Column('gid', sa.Integer, primary_key=True),
               sa.Column('from_client', sa.String(255), nullable=False),
               sa.Column('to_client', sa.String(255), nullable=False),
               sa.Column('text', sa.String(255), nullable=False))

async def create_tables(conn):
    await conn.execute('DROP TABLE IF EXISTS messages')
    await conn.execute('''CREATE TABLE messages (
                              gid serial PRIMARY KEY,
                              from_client varchar(253),
                              to_client varchar(253),
                              text varchar(255))''')

async def fill_data(conn):
    async with conn.begin():
        await conn.execute(messages.insert().values(from_client='client1', to_client='client2', text='This is message from client1 to client2'))

        async for row in conn.execute(messages.select()):
            print(row.gid, row.from_client, row.to_client, row.text)

async def init_database():
    engine = await create_engine(user='postgres',
                                 database='geekbrains',
                                 host='127.0.0.1',
                                 password='xxXX1234')
    async with engine:
        async with engine.acquire() as conn:
            await create_tables(conn)
            await fill_data(conn)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_database())