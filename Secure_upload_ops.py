Class upload

  type()
  form()
  viewer()
  editor()
  commentator()
  

def upload(file):
  
  create log
  if filetype is invalid:
    return 'invalid type'
  if filetype is valid:
    log(file)
    return 'saved'

def convert_to_type(file, new_type):

  if new_type is invalid:
    return 'invalid new type'
  elif file.type() is invalid:
    return 'invalid file'
  else:
    file.type() = new_type
    return 'type updated'


def enable_viewing(file, viewer):

  if file not valid:
    return 'invalid file'

  elif viewer not valid email:
    return 'invalid email'

  else:
      file.viewer = viewer
      return "viewer enabled"


def enable_editing(file, editor):

  enable_viewing(file,editor)
  file.editor = editor
  return 'editor enabled'


def enable_commenting(file, commentator):
   
   enable_viewing(file,commentator)
   file.commentator = commentator
   return 'commentator enabled'


