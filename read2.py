data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		# if count % 1000 == 0: # can be used
		# 	print(len(data)) # can be used
print('Total number of reviews: ', len(data))

sum_len = 0
for d in data:
	sum_len += len(d)
avg = sum_len / len(data)
print('Average wording is: ', avg)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('the number of reviews with less than 100 words: ', len(new))
print(new[0])
print(new[1])