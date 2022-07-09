

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price = 0
    A, B, C, D = 0
    i = 0
    while i < len(skus):
        if skus[i] != "," and i != " ":
            if skus[i] == "A":
                A = A + 1
            elif skus[i] == "B":
                B = B + 1
            elif skus[i] == "C":
                C = C + 1
            elif skus[i] == "D":
                D = D + 1
            else:
                return -1
        i = i + 1

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
        price = price + D * 15

    return price


