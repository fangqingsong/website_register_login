number = "1370681"

with open("hm.txt","w") as f:
	for i in range(0001, 9999):
		ok = number + "{:0>4d}".format(i) + "\n"
		f.write(ok)

