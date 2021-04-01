import pymongo
from pymongo import MongoClient
import PyPDF2 as pypdf
import pdfplumber
import tabula
import json
from PyPDF2 import PdfFileReader


def docuinfo(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f, strict = False)
        information = pdf.getDocumentInfo()

    cstring = json.dumps(information)
    dstring = json.loads(cstring)
    return dstring
