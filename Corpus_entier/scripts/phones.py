fich= open("lexicon.txt","r")
fich1= open("lexicon1.txt","w")
l=fich.readlines()
tab=[]
for line in l:
	ph=line.split()
	phon=ph[1:]
	for k in phon:
		if k not in tab:
			tab.append(k)
for j in tab:
	fich1.write(j+"\n")
