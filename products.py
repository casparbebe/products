products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	products.append([name, price])
print(products)

# 簡潔的寫法 products.append([name, price])
# p = []
	# p.append(name)
	# p.append(price)
	# products.append(p)

for product in products:
	print(product[0], '的價格是', product[1])


with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '元' + '\n')