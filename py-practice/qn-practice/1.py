def productfunc(n1, n2):
    product = n1 * n2
    if(product <= 1000):
        return product
    else:
        return n1 + n1

print(productfunc(20, 30))