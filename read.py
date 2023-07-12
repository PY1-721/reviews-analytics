data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))
print(data[0])
print('檔案讀取完了，總共有', len(data), '筆資料')


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言包含good')


bed = [d for d in data if 'bad' in d ] # 清單快寫法
print('一共有', len(bed), '筆留言包含bad')
sun_len = 0
for d in data:
	sun_len += len(d)
print('留言平均長度是', sun_len / len(data))
#文字記數
wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key
for word in wc: #提取字典的key
	if wc[word] > 1000000:
		print(word, wc[word])
while True:
	word = input('請問要查什麼字：')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現的次數為：', wc[word])
	else:
		print('這個字沒有出現過！')
print('感謝使用本查詢系統')

