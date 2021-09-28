def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines): #轉換
	person = None
	J_word_count = 0
	J_sticker_count = 0
	J_image_count = 0
	S_word_count = 0
	S_sticker_count = 0
	S_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'J':
			if s[2] == '貼圖':
				J_sticker_count += 1
			elif s[2] == '圖片':
				J_image_count +=1
			else:
				for m in s[2:]:
					J_word_count += len(m)
		elif name == '紹安-2':
			if s[2] == '貼圖':
				S_sticker_count += 1
			elif s[2] == '圖片':
				S_image_count += 1
			else:
				for m in s[2:]:
					S_word_count += len(m)
	print('J說了', J_word_count, '個字, 傳了', J_sticker_count, '個貼圖, ', J_image_count, '張圖片')
	print('紹安說了', S_word_count, '個字, 傳了', S_sticker_count, '個貼圖, ', S_image_count, '張圖片')
		# print(s)


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('com.txt')
	lines = convert(lines)
	# write_file('output.txt', lines)


main()