#!/usr/bin/env python
# coding: utf-8
import sys
import math
def main():
	try:
		filename,num = sys.argv[1:]
		num = int(num)
		pass
	except Exception as e:
		raise e
	if num==0:
		print("num must > 0")
		sys.exit(-1)
	rows = 0
	with open(filename,'r',encoding='utf8') as fr:
		for line in fr:
			rows+=1
	if rows==0:return
	div = math.ceil(rows/num)
	print("total %s rows divide into %s parts"%(rows,num))
	with open(filename,'r',encoding='utf8') as fr:
		fix = None
		name = None
		if len(filename.split('.'))>1:
			res = filename.split('.')
			fix = res[-1]
			name = '.'.join(res[:-1])
		else:
			name = filename
		outputfile = None
		line_num = 0
		fw = None
		for line in fr:
			if line_num%div==0:
				div_no = int(line_num/div)+1
				if fw!=None:
					fw.close()
					print("part %s:%s"%(div_no-1,outputfile))
				if fix!=None:
					outputfile = '%s%02d.%s' % (name,div_no,fix)
				else:
					outputfile = '%s%02d' % (name,div_no	)
				fw = open(outputfile,'w',encoding='utf8')
			fw.write("%s"%line)
			line_num+=1
		if fw:
			fw.close()
			print("part %s:%s"%(div_no,outputfile))	
if __name__ == '__main__':
	main()