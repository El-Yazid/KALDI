with open("text","r",encoding="utf-8")as fi:
	with open("text2","w",encoding="utf-8")as fi1:
		lines=fi.readlines()
		for i in lines:
			text=i.split(" ")
			f=' '.join(text[1:])
			# ~ f=text[0]+"\n"
			# ~ print(f)
			fi1.write(f)

