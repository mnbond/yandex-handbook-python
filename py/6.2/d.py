import pandas as pd


def cheque(price_list, **order):
    df = pd.DataFrame({"product": order.keys(), 
                       "price": [price_list[x] for x in order.keys()],
                       "number": order.values(),
                       "cost": [price_list[x] * order[x] for x in order.keys()]})
    return df.sort_values("product").reset_index(drop=True)


def discount(cheque):
    with_discount = cheque.copy()
    with_discount.loc[with_discount["number"] > 2, "cost"] *= 0.5
    return with_discount