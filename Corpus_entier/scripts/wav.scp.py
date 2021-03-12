with open("wav.scp","r",encoding="utf-8")as fi:
	with open("text2","w",encoding="utf-8")as fi1:
		lines=fi.readlines()
		for i in lines:
			tab=i.split("_")
			t="_".join(tab[:-1])
			fi1.write(i[:-1]+" /home/el-yazid/kaldi/egs/cream/cream_audio/train/"+t+"/"+i)
