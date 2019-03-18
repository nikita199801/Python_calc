import sys
def vvod(stroka):
	global sum
	if stroka == 'exit':
		sys.exit()
	for i in stroka:
		if i == '+':
			num=stroka.split("+")
			sum=int(num[0])+int(num[1])
		elif i == '-':
			num =stroka.split('-')
			sum=int(num[0])-int(num[1])
		elif i =='*':
			num =stroka.split('*')
			sum=int(num[0])*int(num[1])
		elif i =='/':
			num =stroka.split('/')
			sum=int(num[0])/int(num[1])
	#print ('Ответ: ', sum)