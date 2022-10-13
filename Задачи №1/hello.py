productsString = "(Name: Bananas, Price: 0.56, Count: 13)|(Price: 0.78, Name: Rosen, Count: 28)|(Count: 7, Name: Dragonfruit, Price: 2.35)"

productStrings = [productString[1:-1] for productString in productsString.split("|")]
allGoodsValue = 0

for productString in productStrings:
    productKV_pairs = productString.split(", ")
    productPrice = 0
    productCount = 0

    for productKV in productKV_pairs:
        productKV_info = productKV.split(": ")
        productKey = productKV_info[0]
        productValue = productKV_info[1]

        if productKey == "Price":
            productPrice = float(productValue)
        elif productKey == "Count":
            productCount = int(productValue)

        print(f"{productKey} --> {productValue}")
    
    goodsValue = productPrice * productCount
    print(f"Total value of the goods: {goodsValue:.2f}")
    allGoodsValue += goodsValue
    print()

if allGoodsValue > 100 or len(productStrings) != 3 and allGoodsValue > 25:
    print("Everything is great")

someVar = None
print(someVar)

if not someVar:
    print("Some var is none")
else:
    print("Some var is something")

def someFunction():
    print("Some var or something")

someFunction()
    
    


