def amicable(a,b):
	s=0
	for k in range(1,a):
		if a%k==0:
			s=s+k
	if s==b:
		s=0
		for i in range(1,b):
			if b%i==0:
				s=s+i
		if s==a:
			return 1
		else:
			return 0
	return 0
l1=[]
for i in range(2,10000000):
	count = 0
	if i not in l1:
		s=0
		for k in range(1,i):
			if i%k==0:
				s=s+k
		if (i!=s and amicable(i,s) and count < 11):
			l1.append(i)
			l1.append(s)
			print("(",i,",",s,")")
			count= count + 1
	else:
		continue

