

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price = 0
    i = 0
    A, B, C, D = 0

    while i < len(skus):
        if i == "A":
            A = A + 1
        elif i == "B":
            B = B + 1
        elif i == "C":
            C = C + 1
        elif i == "D":
            D = D + 1
        else: return -1

    if A == 3:
        price = price + 130
    elif A > 0:
        price = price + A * 50

    if B == 2:
        price = price + 45
    elif B > 0:
        price = price + B * 30

    if C > 0:
        price = price + C * 20

    if D > 0:
        price = price + D * 20

    return price


