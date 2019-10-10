# initialize
gol1, gol2, gol3 = 1000, 2000, 3000
#gardu1, gardu2, gardu3 = [], [], []

masukan1 = 0
masukan2 = 0
masukan3 = 0
total_gardu1 = 0
total_gardu2 = 0
total_gardu3 = 0
total_gol1 = 0
total_gol2 = 0
total_gol3 = 0

# process gate 1
while masukan1 != -1:
	isi_gardu1 = int(input("Gardu 1: "))
	masukan1 = isi_gardu1
	if (isi_gardu1 == 1):
		total_gardu1 += gol1
		total_gol1 += 1
	elif (isi_gardu1 == 2):
		total_gardu1 += gol2
		total_gol2 += 1
	elif (isi_gardu1 == 3):
		total_gardu1 += gol3
		total_gol3 += 1
print("Total gardu 1: {}".format(total_gardu1),end="\n")

#process gate 2
while (masukan2 != -1):
	isi_gardu2 = int(input("Gardu 2: "))
	masukan2 = isi_gardu2
	if (isi_gardu2 == 1):
		total_gardu2 += gol1
		total_gol1 += 1
	elif (isi_gardu2 == 2):
		total_gardu2 += gol2
		total_gol2 += 1
	elif (isi_gardu2 == 3):
		total_gardu2 += gol3
		total_gol3 += 1
print("Total gardu 2: {}".format(total_gardu2),end="\n")

#process gate 3
while (masukan3 != -1):
	isi_gardu3 = int(input("Gardu 3: "))
	masukan3 = isi_gardu3
	if (isi_gardu3 == 1):
		total_gardu3 += gol1
		total_gol1 += 1
	elif (isi_gardu3 == 2):
		total_gardu3 += gol2
		total_gol2 += 1
	elif (isi_gardu3 == 3):
		total_gardu3 += gol3
		total_gol3 += 1
print("Total gardu 3: {}".format(total_gardu3),end="\n")

# finishing
print("Total pendapatan: %d" %(total_gardu1+total_gardu2+total_gardu3))
print("Gol 1: {}".format(total_gol1))
print("Gol 2:",total_gol2)
print("Gol 3: %d" %total_gol3)