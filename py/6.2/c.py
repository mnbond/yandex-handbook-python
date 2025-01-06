import pandas as pd


def cheque(price_list, **order):
    df = pd.DataFrame({"product": order.keys(), 
                       "price": [price_list[x] for x in order.keys()],
                       "number": order.values(),
                       "cost": [price_list[x] * order[x] for x in order.keys()]})
    return df.sort_values("product").reset_index(drop=True)