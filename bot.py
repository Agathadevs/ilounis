import discord

from dotenv import load_dotenv
load_dotenv()

import os
from typing import Any

class Bot(discord.Bot):
    def __init__(self, description=None, *args, **options):
        super().__init__(description, *args, **options)

    # bot event
    async def on_ready(self) -> None:
        """
        The event that is triggered when the bot is ready.
        """
        print(f"Login as {self.user} ({self.user.id}).")

    async def close(self) -> None:
        """
        Closes the bot.
        """
        print("Closing the bot...")
        await super().close()
        print("Bot is offline.")

    def run(self, token: str) -> None:
        """
        Starts the bot.
        """
        print("Starting the bot...")
        super().run(token)


if __name__ == "__main__":
    bot = Bot(intents=discord.Intents.all())
    
    for key, value in bot.load_extension("Cogs", recursive=True, store=True).items():
        if value == True:
            print(f"成功載入插件 {key}")
        else:
            print(f"載入插件 {key} 失敗: {value}")
    bot.run(os.getenv("token"))