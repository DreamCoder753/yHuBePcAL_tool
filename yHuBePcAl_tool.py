#yHuBepcaL tool on python
#
# 	by DreamCoder753
#
print("Выберите режим работы:")
print("c - калькулятор")
print("s - площадь")
print("p - периметр")
rezhim = input()
#calculator:
if rezhim == 'c':
	print("Введите пример (со знаком, например: 10+11)")
	print(eval(input()))
#square
if rezhim == 's':
	s1 = int(input("Введите ширину "))
	s2 = int(input("Введите длину "))
	print("Площадь: ")
	print(s1*s2)
#perimetr
if rezhim == 'p':
	p1 = int(input("Введите ширину "))
	p2 = int(input("Введите длину "))
	p3 = int(p1 * 2)
	p4 = int(p2 * 2)
	print("Периметр: ")
	print(p3 + p4)
	
input("Нажмите ENTER чтобы выйти")