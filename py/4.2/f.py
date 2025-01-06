def order(*preferences):
    recipes = {
        "Эспрессо": {"coffee": 1},
        "Капучино": {"coffee": 1, "milk": 3},
        "Макиато": {"coffee": 2, "milk": 1},
        "Кофе по-венски": {"coffee": 1, "cream": 2},
        "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
        "Кон Панна": {"coffee": 1, "cream": 1}
    }
    for drink in preferences:
        ingredients = recipes[drink]
        find_in_stock = dict(filter(lambda x: in_stock[x[0]] >= x[1], ingredients.items()))
        if len(ingredients) == len(find_in_stock):
            for i in ingredients:
                in_stock[i] -= ingredients[i]
            return drink
    return "К сожалению, не можем предложить Вам напиток"
