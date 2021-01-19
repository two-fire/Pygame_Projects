# 一本书封面价格￥24.95，书店可获得40%折扣。船费第一次3元，之后每多一本￥0.75，60本批发价多少

def book_cost(num):
    return 24.95*0.6*num

def Ship_cost(num):
    sum = num * 0.75
    return sum

print(book_cost(60)+Ship_cost(60))
