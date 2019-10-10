# tes = int(input("Nilai : "))
# print("Hasil inputan : {}".format(tes))
#tes = int(input())
#print("Hasil %d" % tes)

#member, a, b, c, d, e = input().split() #memisahkan berdasarkan spasi

# Trying to multiple input by user
# member, a, b, c, d, e = str(input()).split()
# print("membership : {}".format(member))
# print("nilai a : %s" % (int(a)*4))
# print("nilai b : {}".format(b))
# print("nilai c : ", c)
# print("nilai d : %s" % d)
# print("nilai e : ",e)

# Test Case
member, a, b, c, d, e = str(input("Data poin: ")).split()
maks_cashback = 35
maks_diskon = 50
a, b, c, d, e = int(a), int(b), int(c), int(d), int(e)

if ((a%2 == 1) and (b%2 == 1) and (c%2 == 1) and (d%2 == 1) and (e%2 == 1)):
	cashback = 0
	diskon = 1.7 * (c+d+e)
	diskon_fix = diskon
	if (member == "Yes" or member == "yes"):
		diskon_baru = diskon * 0.15
		diskon_fix = diskon_baru+diskon
	if (diskon_fix > maks_diskon):
		diskon_fix = maks_diskon
	print("Cashback: {}".format(cashback))
	print("Diskon: {}".format(diskon_fix))
elif ((a%2 == 0) and (b%2 == 0) and (c%2 == 0) and (d%2 == 0) and (e%2 == 0)):
	diskon = 0
	cashback = 3.1 * (a+b+c)
	cashback_fix = cashback
	if (member == "Yes" or member == "yes"):
		cashback_baru = cashback * 0.15
		cashback_fix = cashback_baru+cashback
	if (cashback_fix > maks_cashback):
		cashback_fix = maks_cashback
	print("Cashback: {}".format(cashback_fix))
	print("Diskon: {}".format(diskon))
else:
	cashback = 3.1 * (a+b+c)
	diskon = 1.7 * (c+d+e)
	cashback_fix = cashback
	diskon_fix = diskon
	if (member == "Yes" or member == "yes"):
		cashback_baru = cashback * 0.15
		diskon_baru = diskon * 0.15
		cashback_fix = cashback_baru + cashback
		diskon_fix = diskon_baru + diskon
	if (cashback_fix > maks_cashback and diskon_fix > maks_diskon):
		cashback_fix = maks_cashback
		diskon_fix = maks_diskon
	elif (cashback_fix > maks_cashback):
		cashback_fix = maks_cashback
	elif (diskon_fix > maks_diskon):
		diskon_fix = maks_diskon
	print("Cashback: {}".format(round(cashback_fix,2)))
	print("Diskon: {}".format(round(diskon_fix,2)))