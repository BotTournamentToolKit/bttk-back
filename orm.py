import asyncio
from gino import Gino
from config import POSTGRES_PASSWORD
db = Gino()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    nickname = db.Column(db.Unicode(), default='noname')


async def example_db():
    await db.set_bind(f'postgresql://postgres:{POSTGRES_PASSWORD}@localhost/bttk')
    print(await db.gino.create_all())
    print(await User.query.gino.all())
    # further code goes here

    await db.pop_bind().close()


# asyncio.get_event_loop().run_until_complete(main())
