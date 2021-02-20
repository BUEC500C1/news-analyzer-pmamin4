from Textnlp import *

define test_nlp():

    assert create_document(rad,'...') == 'invalid document type'
    assert create_document(pdf,'...') == 'uploaded'
    assert create_document(pdf,...) == 'invalid characters'
    assert def save_document(file.docx) == 'document saved'
    assert def save_document(file) == 'invalid type'
    assert view_document(file.docx) == 'document opened'
    assert view_document(file) == 'invalid document form'
    assert hyperlink('google',google.com) == 'source linked'
    assert hyperlink(32,google.com) == 'invalid text'
    assert hyperlink('google',google.lkj) == 'invalid url'
    assert math_operations(e,'+',e) == 'invalid numbers'
    assert math_operations(1,'+',1) == 2
    assert math_operations(3,'-',1) == 2
    assert math_operations(3,'*',2) == 6
    assert math_operations(6,'/',3) == 2
