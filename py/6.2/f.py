import pandas as pd


def best(journal):
    return journal[(journal["maths"] > 3) & (journal["physics"] > 3) & (journal["computer science"] > 3)]
