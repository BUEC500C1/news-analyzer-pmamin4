import pymongo
from pymongo import MongoClient
import PyPDF2 as pypdf
import pdfplumber
import tabula
import json
from pdfdata import *

client = pymongo.MongoClient("localhost", 27017)

mydb = client["database1"]
mycoll = mydb["table1"]

list2 = [{"id":0, "filename":"a", "filetype":"pdb", "owner": "purvis","editor":"jayson", "viewer":"naith"}, 
        {"id":1, "filename":"b", "filetype":"trf", "owner": "jayson","editor":"naith", "viewer":"Purvis"},
        {"id":2, "filename":"c", "filetype":"docx", "owner": "nate","editor":"Place", "viewer":"Jayson"},
        {"id":3, "filename":"d", "filetype":"pfvgb", "owner": "pujayis","editor":"jays", "viewer":"naith"}, 
        {"id":4, "filename":"e", "filetype":"tqwerttyurf", "owner": "jaydon","editor":"nth", "viewer":"Purvis"},
        {"id":5,"filename":"f", "filetype":"docnbvccx", "owner": "nattee","editor":"Purvis", "viewer":"Jayson"}
        ]


pdfobject=open('dbtxt.pdf','rb')
pdf=pypdf.PdfFileReader(pdfobject, strict = False)
pdfobject2=open('sample.pdf','rb')
pdf2=pypdf.PdfFileReader(pdfobject2, strict = False)


rer = {"id":5,"filename":"f", "filetype":"docnbvccx", "owner": "nattee","editor":"Purvis", "viewer":"Jayson"}
rad = {'/CreationDate': "D:20210313141744-05'00'", '/ModDate': "D:20210313141744-05'00'", '/Producer': 'Skia/PDF m91 Google Docs Renderer', '/Title': 'dbtxt'}

#pdfinfo = pdf.getDocumentInfo()
#pdf2info = pdf2.getDocumentInfo()
#print(pdf2info)
#x55 = json.dumps(pdf2info)
#res = json.loads(x55)
#x1 = mycoll.insert_one(res)

#dblist = client.list_database_names()

#print(dblist)
#x4 = mycoll.delete_many({"id":4})
#x3 = mycoll.delete_many({"id":3})
#x2 = mycoll.delete_many({"id":2})
#x1 = mycoll.delete_many({"id":1})
#x0 = mycoll.delete_many({"id":0})

#pdfobject=open('dummy.pdf','rb')
#pdf=pypdf.PdfFileReader(pdfobject, strict = False)
#x66 = json.dumps(pdf.getDocumentInfo())
#x67 = json.loads(x66)
#pdfobject2=open('table.pdf','rb')
#pdf2=pypdf.PdfFileReader(pdfobject2, strict = False)
#x68 = json.dumps(pdf2.getDocumentInfo())
#x69 = json.loads(x68)
#pdfobject3=open('A Sample PDF.pdf','rb')
#pdf3=pypdf.PdfFileReader(pdfobject3, strict = False)
#x70 = json.dumps(pdf3.getDocumentInfo())
#x71 = json.loads(x70)
#pdfobject4=open('112.pdf','rb')
#pdf4=pypdf.PdfFileReader(pdfobject4, strict = False)
#x72 = json.dumps(pdf4.getDocumentInfo())
#x73 = json.loads(x72)

#mycoll.insert_one(x67)
#mycoll.insert_one(x69)
#mycoll.insert_one(x71)
#mycoll.insert_one(x73)


#for x in mycoll.find():
#    print(x)


print(docuinfo("dummy.pdf"))
print(docuinfo("table.pdf"))
print(docuinfo("dbtxt.pdf"))
print(docuinfo("112.pdf"))