from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import textract
import argparse
import sys

def extract_toc(file, toc_page):
	output = PdfFileWriter()
	input1 = PdfFileReader(open(file,'rb'))
	start, stop = toc_page
	for i in range(start,stop+1):
		output.addPage(input1.getPage(i))
	output.write(open("TOC.pdf",'wb'))
	text = textract.process("TOC.pdf").decode('utf-8')
	new_text = ''
	for line in text.split('\n'):
		temp = line.replace('.','@',1).replace('.','')
		new_text += temp + '\n'
	open("TOC.txt",'w').write(new_text)
	#os.system("rm TOC.pdf")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="extract TCO")
	filename = sys.argv[1]
	print(filename)
	start_page = int(sys.argv[2]) if sys.argv[2] else 0
	stop_page = int(sys.argv[3]) if sys.argv[3] else 0
	page = (start_page, stop_page)
	extract_toc(filename, page)