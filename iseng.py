uang = int(input("Nilai uang (Rp) : "))
lembar = int(input("Lembar Rp.10000,- yang diberikan: "))
enough = False
tampung = 0

while enough == False:
	tampung = round(uang/10000)
	if lembar >= tampung:
		enough = True
	else:
		enough = False
		break

print("Lembar Rp.10000,- yang digunakan: ",tampung)
print("Cukup?",enough)