def check(freq):
	pass
	import datetime
	f=0;i=1
	while freq>0:
		rem=freq%2
		f=f+(i*rem)
		freq=freq/2
		i=i*10
	day={'Sunday':1000000,'Monday':100000,'Tuesday':10000,'Wednesday':1000,'Thursday':100,'Friday':10,'Saturday':1,}
	f=f/day.get(datetime.datetime.now().strftime("%A"))
	if f%10:
		return True
	else:
		return False
