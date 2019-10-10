def fibo(x):
	if x == 0:
		return 0
	elif x == 1:
		return 1
	elif x == 2:
		return 1
	elif x > 2:
		return fibo(x-1)+fibo(x-2)

konstanta = 2.236
masukan = 0
while masukan >= 0:
	masukan = int(input())
	if masukan >= 0:
		# i = 0
		# Sn = 0
		# while i <= masukan:
		# 	Sn += ((1/konstanta)*(0.5*((1+konstanta)**masukan)-((1-(0.5*(1+konstanta)))**masukan)))
		# 	i += 1
		Sn = fibo(masukan)
		print(Sn)
	else:
		print("Selesai")