stock = {
    "name" : "GOOG",
    "shares" : 100,
    10 : 490.10
}
stock['total']=20e3
print(stock)

if 10 in stock:
    p = stock[10]
else:
    p = 0.0
print(p)

p = stock.get(10,0.0) # same with upper "if ~~~"
print(p)

syms = list(stock)
print(syms)

del stock["total"]
print(stock)
