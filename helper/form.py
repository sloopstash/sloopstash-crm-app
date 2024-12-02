##
# -*- coding: utf-8 -*-
##
##
# Form helper.
##

# Import custom modules.
from helper import is_text,is_email,is_phone,is_password,is_integer


# Form schema.
schema = {
  'account_create':{
    'organization':['text',True],'email':['email',True],'phone':['phone',True]
  },
  'account_update':{
    'organization':['text',True],'email':['email',True],'phone':['phone',True]
  },
  'contact_create':{
    'name':['text',True],'email':['email',True],'status':['integer',True],'account_id':['integer',True]
  },
  'contact_update':{
    'name':['text',True],'email':['email',True],'status':['integer',True],'account_id':['integer',True]
  }
}

# Process form data.
def process(id,data):
  if id in schema:
    form = {}
    form['error'] = {}
    for field,attr in schema[id].iteritems():
      type = attr[0]
      required = attr[1]
      if type=='text':
        output = is_text(data[field])
      elif type=='email':
        output = is_email(data[field])
      elif type=='phone':
        output = is_phone(data[field])
      elif type=='password':
        output = is_password(data[field])
      elif type=='integer':
        output = is_integer(data[field])
      else:
        raise Exception('Invalid input data.')
      if output is True:
        form[field] = data[field]
      else:
        if required is False and data[field]=='':
          form[field] = None
        else:
          form['error'][field] = output
    return form
  else:
    return
