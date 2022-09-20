water=int(input("enter water level"))
if water<1:
	print("need to fill")
elif water>=1 and water <10:
	print("no need to fill")
else:
	print("over flow")
	