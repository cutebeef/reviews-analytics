data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f :
    	data.append(line)
    	count += 1
    	if count % 100000 == 0:
    	    print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')	

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('每筆留言平均長度為', sum_len/len(data))

new = [] #建立一個新清單
for d in data: #將清單中的東西一個一個拿出來
    if len(d) < 100:
    	new.append(d) #長度小於100的留言 裝入新清單裡面
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])


good = [] 
for d in data: 
    if 'good' in d:
    	good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])
print(good[1])