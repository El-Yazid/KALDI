with open("lexicon.txt","r",encoding="utf-8")as fi:
	with open("text2","w",encoding="utf-8")as fi1:
		liste=[]
		lines=fi.readlines()
		for i in lines:
			# ~ print(i)
			text=i.split(" ")
			f=text[1:-1]
			for k in f:
				# ~ print(k)
				if k not in liste:
					print(k)
					liste.append(k)
# ~ for t in liste:
	# ~ print(t)
			# ~ fi1.write(f)

