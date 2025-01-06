import pandas as pd


def need_to_work_better(journal):
    return journal[(journal["maths"] == 2) | (journal["physics"] == 2) | (journal["computer science"] == 2)]
