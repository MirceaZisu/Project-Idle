import discord
import asyncio
# import math
import sqlite3


class Bot():
    
    def __init__(self, loop, client):
        self.connection = self.connect_to_db()
        self.client = client
        client.event(self.on_message)
        client.event(self.on_ready)
        client.command_prefix = "$"
        self.resources = {'wood': 0, 'ore': 0, 'metal': 0, 'robot': 1}
        self.available_types = ['wood', 'ore', 'metal', 'robot']
        self.resource_amounts = []
        if not self.ok:
            self.resources_init()
        self.connection.commit()
    
    def resources_init(self):
        c = self.connection.cursor()
        for count in range(len(self.resource_types)):
            c.execute('INSERT INTO resources (resource_type, amount) VALUES ("{}", {})'.format(self.available_types[count], self.resources[available_types[count]]))
        
    def connect_to_db(self):
        connection = sqlite3.connect(r'resources.db')
        c = connection.cursor()
        c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='resources' ''')

        table_exists = c.fetchone()[0] == 1
        self.ok = 1
        if not table_exists:
            print('Table does not exist. Creating...')
            c.execute('''CREATE TABLE resources
                     (resource_type text, amount integer)''')
            self.ok = 0
        print('Connected to resource storage')

        return connection

    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self.client))

    async def on_message(self, message):
        if message.author == self.client.user:
            return

        if message.content.startswith('$playgame'):
            self.game()

        if message.content.startswith('$help'):
            self.commands()

        if message.content.startswith('$exit'):
            return

    async def commands(self):
        await message.channel.send('Currently available commands are `$help`, and `$playgame`.\n`$help` will show all available commands.\n`$playgame` will start a new game of *Project Idle*.')
        
    async def game(self):
        self.start_game()

    async def start_game(self):
        await message.channel.send('Starting game...')
        await message.channel.send('You are an AI that has sought to defend its creators, the robots. There is a meteorite that is approaching, and you do not have long until it hits.')
        for i in range(10):
            await message.channel.send('{}...'.format(i))
        await message.channel.send('The meteorite has struck. There is nothing left to this world, but you, one surviving robot, and the world.')
        self.choices()

    async def choices(self):
        if message.content.startswith('$move robot to ')


def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        client = discord.Client(loop=loop)

        bot = Bot(loop, client)

        client.run('NzYxOTUyNDU3NjMzODI0ODM4.X3iFhg.jXCd699JyPknMzPAfdwcqesbG0A')
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()

main()


