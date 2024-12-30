import csv
import pandas as pd
import matplotlib.pyplot as plt

finalList = []
priceList = []
commentList = []
with open ('newshops.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        price = row['人均价格']
        price = price.replace('￥', '')
        comment = row['评论总数']
        comment = comment.replace('条评价', '')
        if price != '0' and float(price) <= 125 and "鸡" in row['店铺名']:
            if comment != '-':
                priceList.append(float(price))
                commentList.append(int(comment))
                priceDict = {'store': str(row['店铺名']), 'price': float(price), 'comments': int(comment)}
                finalList.append(priceDict)


finalList.sort(key=lambda x: x['price'])
print("cheapest:"+str(finalList[0]))
print("costliest:"+str(finalList[-1]))

# plt.scatter(priceList, commentList, c='red', s=50, alpha=0.5, label='Data points')
# plt.title('Prices vs Comments')
# plt.xlabel('Prices')
# plt.ylabel('Comments')
# plt.show()

# plt.hist(priceList, bins = 10, color = 'blue', alpha = 0.7)
# plt.title('Average Price')
# plt.xlabel('Price')
# plt.ylabel('Shops')
# plt.show()
bins = list(range(0, 126, 10))


plt.hist(priceList, bins = bins, weights = commentList, color = 'blue', alpha = 0.7)
plt.title('Prices vs Comments')
plt.xlabel('Price')
plt.ylabel('Comments')
plt.show()