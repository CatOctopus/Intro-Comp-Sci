def ugh(a):
	count=0
	for i in range(len(a)-1):
		for x in range ((len(a)-1)-i):
			if a[i]==a[i+x+1]:
				count=count+1
			else:
				count=count
	if count>0:
		return True
	else:
		return False
