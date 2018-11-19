from PyPDF2 import PdfFileReader as Reader, PdfFileWriter as Writer

off_set = 29

def add_bookmark(pdf, bookmarks):

	for title, page in bookmarks:
		if title.count('\t') == 0:
			x = pdf.addBookmark(title, page, parent=None)
		elif title.count('\t') == 1:
			title = title.strip()
			y = pdf.addBookmark(title, page, parent=x)
		elif title.count('\t') == 2:
			title = title.strip()
			z = pdf.addBookmark(title, page, parent=y)
		elif title.count('\t') == 3:
			w = pdf.addBookmark(title, page, parent=z)



def extract_bookmark(bm_file):
	bookmarks = []
	with open(bm_file, 'r') as toc:
		for line in toc:
			if line and '@' in line:
				line = line.split('@')
				bookmarks.append( (line[0], int(line[1]) + off_set) )
	return bookmarks

def pdf_process(origin_pdf, bm_file):
	pdf_in = Reader(open(origin_pdf,'rb'))
	pdf_out = Writer()
	pdf_out.cloneDocumentFromReader(pdf_in)
	bookmarks = extract_bookmark(bm_file)
	add_bookmark(pdf_out, bookmarks)
	out_name = origin_pdf[:-4] + "-with_bookmark.pdf"
	with open(out_name, 'wb') as fout:
		pdf_out.write(fout)

if __name__ == '__main__':
	import sys
	pdf_process(sys.argv[1],sys.argv[2])