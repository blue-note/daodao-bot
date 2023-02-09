from gpt_index import GPTSimpleVectorIndex, GPTListIndex, DiscordReader
import os


def load():
    discord_token = os.getenv("DISCORD_TOKEN")
    channel_ids = [1032788394893398026]
    documents = DiscordReader(discord_token=discord_token).load_data(
        channel_ids=channel_ids
    )
    index = GPTSimpleVectorIndex(documents)
    index.save_to_disk("indices/daodao.json")


def query(question):
    index_path = "indices/daodao.json"
    index = GPTSimpleVectorIndex.load_from_disk(index_path)
    return index.query(question)
