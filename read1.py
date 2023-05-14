#文字計數
data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f :
    	data.append(line)
    	count += 1
    	if count % 100000 == 0:
    	    print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')	


wc = {} #world_count 
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 #新增key進字典

for word in wc:
    if wc[word] > 10000:
        print(word, wc[word])

print(len(wc))

while True:
    word = input('請問你想查什麼字')
    if word == 'q'
        break
    if word in wc:
        print(word, '出現過的次數為: ', wc[word])
    else:
        print('這個字沒有出現過')

print('感謝使用')


        













#sum_len = 0
#for d in data:
	#sum_len = sum_len + len(d)

#print('每筆留言平均長度為', sum_len/len(data))

#new = [] #建立一個新清單
#for d in data: #將清單中的東西一個一個拿出來
    #if len(d) < 100:
    	#new.append(d) #長度小於100的留言 裝入新清單裡面
#print('一共有', len(new), '筆留言長度小於100')
#print(new[0])
#print(new[1])


#good = [] 
#for d in data: 
    #if 'good' in d:
    	#good.append(d)
#print('一共有', len(good), '筆留言提到good')
#print(good[0])
#print(good[1])

#good = [d for d in data if 'good' in d] 
#快寫法 最前面的d就是append(d)中那個d,也可不用d,放不同東西進清單
#print(good[2])