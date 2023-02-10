from typing import Optional
from gpt_index import GPTSimpleVectorIndex, GPTListIndex, DiscordReader
import os


def repl(index_path):
    print("ask any questions, press CTRL+C to quit...")
    index = GPTSimpleVectorIndex.load_from_disk(index_path)
    while True:
        question = input(">>> ")
        res = index.query(question)
        print(res.response)


def load(index_path):
    discord_token = os.getenv("DISCORD_TOKEN")
    channel_ids = [
        1032788394893398026,
        1012766561947373588,
        895926429039075328,
        899174129629016065,
        895926400970801173,
        1001205045028733068,
        994018635410575440,
        1016788083104026664,
        1037828164434542603,
        991097457079361627,
        1037828427765522582,
        1037829431688966316,
        1009233584227364986,
        928533641489969203,
        935733580938768444,
        906951493784072252,
        982411454550507540,
        1009233584227364986,
        928533641489969203,
        935733580938768444,
        906951493784072252,
        982411454550507540,
        1033477382616653885,
        1037445461818228736,
        1042148985474924576,
        954211865737707540,
        895926354728603659,
        941044521909780500,
        958870078143733770,
    ]

    if os.path.exists(index_path):
        print("loading index from disk...")
        index = GPTSimpleVectorIndex.load_from_disk(index_path)
    else:
        print("initializing index, this may take a moment...")
        documents = DiscordReader(discord_token=discord_token).load_data(
            channel_ids=channel_ids
        )
        index = GPTSimpleVectorIndex(documents)
        index.save_to_disk(index_path)
    return index


class Reader:
    def init(self, index_path):
        self.index = load(index_path)

    def query(self, question):
        print("question received: ", question)
        return self.index.query(question)


if __name__ == "__main__":
    load(os.getenv("INDEX_PATH"))
    repl(os.getenv("INDEX_PATH"))
