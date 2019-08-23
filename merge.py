#!/usr/bin/env python
# coding: utf-8
import sys
import math
def main():
	try:
		filenames,outputfile = sys.argv[1:-1],sys.argv[-1]
		pass
	except Exception as e:
		print("merge <file1> <file2> ... <outputfile>")
		raise e
	if len(filenames)==0:
		print("as least one inputfile")
		sys.exit(-1)
	fw = open(outputfile,'w',encoding='utf8')
	for file in filenames:
		with open(file,'r',encoding='utf8') as fr:
			for line in fr:
				fw.write(line)
	fw.close()
if __name__ == '__main__':
	main()