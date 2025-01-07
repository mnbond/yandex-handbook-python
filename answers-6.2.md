# Ответы и решения задач из хэндбука Яндекс «Основы Python», параграф 6.2

### 6.2. Модуль pandas

A. Длины всех слов — 2
```python
import pandas as pd


def length_stats(text):
    text = "".join([x for x in text.lower() if x.isalpha() or x == " "])
    stats = pd.Series({x: len(x) for x in text.split()}).sort_index()
    return stats
```

B. Длины всех слов по чётности
```python
import pandas as pd


def length_stats(text):
    text = "".join([x for x in text.lower() if x.isalpha() or x == " "])
    stats = pd.Series({x: len(x) for x in text.split()}).sort_index()
    return stats[stats % 2 != 0], stats[stats % 2 == 0]
```

C. Чек — 2
```python
import pandas as pd


def cheque(price_list, **order):
    df = pd.DataFrame({"product": order.keys(), 
                       "price": [price_list[x] for x in order.keys()],
                       "number": order.values(),
                       "cost": [price_list[x] * order[x] for x in order.keys()]})
    return df.sort_values("product").reset_index(drop=True)
```

D. Акция
```python
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
```

E. Длинные слова
```python
import pandas as pd


def get_long(data, min_length=5):
    return data[data >= min_length]
```

F. Отчёт успеваемости
```python
import pandas as pd


def best(journal):
    return journal[(journal["maths"] > 3) & (journal["physics"] > 3) & (journal["computer science"] > 3)]
```

G. Отчёт неуспеваемости
```python
import pandas as pd


def need_to_work_better(journal):
    return journal[(journal["maths"] == 2) | (journal["physics"] == 2) | (journal["computer science"] == 2)]
```

H. Обновление журнала
```python
import pandas as pd


def update(journal):
    updated_journal = journal.assign(average=lambda x: (x["maths"] + x["physics"] + x["computer science"]) / 3)
    return updated_journal.sort_values(["average", "name"], ascending=[False, True])
```

I. Бесконечный морской бой
```python
import pandas as pd


left, top = map(int, input().split())
right, bottom = map(int, input().split())
df = pd.read_csv('data.csv')
filtered_df = df.query('x >= @left and x <= @right and y >= @bottom and y <= @top')
print(filtered_df)
```

J. Экстремум функции
```python
import numpy as np
import pandas as pd


def values(func, start, end, step):
    index = np.arange(start, end + step, step)
    result = pd.Series(map(func, index), index)
    return result


def min_extremum(data):
    return data[data == data.min()].index[0]


def max_extremum(data):
    return data[data == data.max()].index[0]
```