import PyPDF2

merger = PyPDF2.PdfMerger()


files = ["1.pdf", "2.pdf"]

for file in files:
    pdfFile = open(file, "rb")
    reader = PyPDF2.PdfReader(pdfFile)
    merger.append(reader)
    pdfFile.close()

merger.write("merged.pdf")
