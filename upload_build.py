from Secure_upload_ops import *

define test_upload():

    assert upload(file.ghh) == 'invalid type'
    assert upload(file.pdf) == 'saved'
    assert convert_to_form(file.docx,pdf) == 'type updated'
    assert convert_to_form(file.docx,asd) == 'invalid new type'
    assert convert_to_form(file.asdf,pdf) == 'invalid file'
    assert enable_viewing(file.docx, veiwer@bu.edu) == 'viewer enabled'  
    assert enable_viewing(file.docx, viewer) == 'invalid email'  
    assert enable_viewing(fileasd, viewer@bu.edu) == 'invalid file'  
    assert enable_editor(file.docx, editor@bu.edu) == 'editor enabled'  
    assert enable_editor(file.adsf, editor@bu.edu) == 'invalid file'
    assert enable_editor(file.docx, editor) == 'ivalid email'
    assert enable_commenting(file.docx, commentator@bu.edu) == 'commentator enabled'
    assert enable_commenting(file, commentator@bu.edu) == 'invalid file'
    assert enable_commenting(file.docx, commentator) == 'invalid email'
