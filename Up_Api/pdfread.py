import PyPDF2 as pypdf
import pdfplumber
import tabula

pdfobject=open('dummy.pdf','rb')
pdf=pypdf.PdfFileReader(pdfobject, strict = False)
pdfobject2=open('table.pdf','rb')
pdf2=pypdf.PdfFileReader(pdfobject2, strict = False)
pdfobject3=open('A Sample PDF.pdf','rb')
pdf3=pypdf.PdfFileReader(pdfobject3, strict = False)
pdfobject4=open('112.pdf','rb')
pdf4=pypdf.PdfFileReader(pdfobject4, strict = False)
print(pdf.getDocumentInfo())
print(pdf2.getDocumentInfo())
print(pdf3.getDocumentInfo())
print(pdf4.getDocumentInfo())