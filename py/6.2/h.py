import pandas as pd


def update(journal):
    updated_journal = journal.assign(average=lambda x: (x["maths"] + x["physics"] + x["computer science"]) / 3)
    return updated_journal.sort_values(["average", "name"], ascending=[False, True])