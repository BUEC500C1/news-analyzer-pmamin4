import PyPDF2 as pypdf

pdfobject=open('tax1.pdf','rb')

pdf=pypdf.PdfFileReader(pdfobject)

information = pdf.getDocumentInfo()

page = pdf.getPage(1)


print(pdf.numPages)
pdf.getFormTextFields()
