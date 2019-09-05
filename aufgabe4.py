import random
start = input('请输入你想要的开始数字:')
end = input('请输入你想要的结尾数字:')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1
	num = input('请猜数字:')
	num = int(num)
	if num == r:
		print('你终于猜对了! ')
		print('这是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('这是你猜的第', count, '次')
