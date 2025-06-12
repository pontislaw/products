# 記帳程式

products = []
while True:
	name = input("請輸入商品名稱：")
	if name == "q":
		break
	price  = input("請輸入商品價格：")
	products.append([name, price])
	
print(products)
print(f"你總共建立了{len(products)}個商品的清單")
print(f"商品{products[0][0]}價值{products[0][1]}元")

for p in products:
	print(f"{p[0]}的價格是{p[1]}")