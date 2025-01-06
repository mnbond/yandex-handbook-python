import pandas as pd


def length_stats(text):
    text = "".join([x for x in text.lower() if x.isalpha() or x == " "])
    stats = pd.Series({x: len(x) for x in text.split()}).sort_index()
    return stats