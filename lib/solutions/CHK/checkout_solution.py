

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price=0
    amount = skus[0]
    item = skus[1]
    if item == "A":
        if amount != 3 and amount > 0:
            price = amount*50
            return price
        if amount == 3:
            price = 130
            return price
        else: return -1
    elif item == "B":
        if amount != 3 and amount > 0:
            price = amount*50
            return price
        if amount == 3:
            price = 130
            return price
        else: return -1