import os

fname= 'traininglabels.csv'

with open(fname) as f:
    content = f.readlines()

content = [x.strip() for x in content] 


dict ={'0':[],'1':[]}

for item in content:
	if item.split(',')[1]== '0':
			dict['0'].append(item.split(',')[0])
	elif item.split(',')[1]== '1':
			dict['1'].append(item.split(',')[0])

			
yesst = '"'+dict['1'][0]+'"'
nost = '"'+dict['0'][0]+'"'

for i in range(1,500):
	yesst =yesst + ' ' + '"'+dict['1'][i]+'"'
	nost = nost +  ' ' + '"'+dict['0'][i]+'"'
	
print(len(dict['0']))
print(len(dict['1']))
print(len(dict['0']) + len(dict['1']))	
#print(nost)	


for i in range(0,500):
	print(dict['0'][i])
	bshcmd1 = 'cp ./' + dict['0'][i] + ' ./no'
	bshcmd2 = 'cp ./' + dict['1'][i] + ' ./yes'
	print(bshcmd1)
	os.system(bshcmd1)
	os.system(bshcmd2)
	bshcmd3 = 'ls -1 | wc -l'
	os.system(bshcmd3)

