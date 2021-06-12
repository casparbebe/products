import os # operating system

# 讀取檔案
products = []
if os.path.isfile('products.csv'): # 檢查檔案在不在
	print('yeah! 找到檔案了!')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 跳到下回合
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('找不到檔案......')

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')  # 簡潔的寫法 products.append([name, price])
	if name == 'q':                  # p = []
		break
	price = input('請輸入商品價格: ') # p.append(name)
	price = int(price)               # p.append(price)
	products.append([name, price])   # products.append(p)	
print(products)

# 印出所有購買紀錄
for product in products:
	print(product[0], '的價格是', product[1])

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')