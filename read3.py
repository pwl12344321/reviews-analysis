data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		# if count % 1000 == 0:
		# 	print(len(data))
print('Total number of reviews: ', len(data))

print(data[0])

wc = {} # word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 100000:
		print(word, wc[word])

print(len(wc))
print(wc['Sam'])

while True:
	word = input('check word: ')
	if word == 'q':
		break
	if word in wc:
		print(wc[word])
	else:
		print('No this word')