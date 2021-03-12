with open("wav.scp","r",encoding="utf-8")as fi:
	with open("text2","w",encoding="utf-8")as fi1:
		lines=fi.readlines()
		for i in lines:
			f=(i[:-1]+".wav"+"\n")
			# ~ text=i.split("_")
			# ~ f=i[:-1]+" "+"_".join(text[:-1])
			# ~ f=text[1][:-1]+" "+text[0]+"\n"
			# ~ f=i[:-1]+" "+text[0]+"\n"
			fi1.write(f)

