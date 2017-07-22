from i2b import check
from extract import openmyxlsx
from send import sendmail
import time
start=time.time()
send2=[]
sheetlist = openmyxlsx('food.xlsx')
for x in sheetlist:
	if check(x[2]):
		send2.append([x[0],x[1]])
sendmail('ae16b020@smail.iitm.ac.in','9912474815',send2,'you are nice boy','\n you are going to be become an engineer!')
end=time.time()
elapsed=end-start
print 'done'
