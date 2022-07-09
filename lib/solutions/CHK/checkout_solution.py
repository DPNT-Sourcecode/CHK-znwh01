

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
        if amount != 2 and amount > 0:
            price = amount*30
            return price
        if amount == 2:
            price = 45
            return price
        else: return -1
    elif item == "C":
        if amount > 0:
            price = amount*20
            return price
        else: return -1
    elif item == "D":
        if amount > 0:
            price = amount*15
            return price
        else: return -1
    else: return -1