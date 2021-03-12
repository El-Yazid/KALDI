with open("utt2spk","r",encoding="utf-8")as fi:
	with open("text2","w",encoding="utf-8")as fi1:
		lines=fi.readlines()
		for i in lines:
			text=i.split(" ")
			f=text[1][:-1]+" "+text[0]+"\n"
			# ~ f=i[:-1]+" "+text[0]+"\n"
			fi1.write(f)

