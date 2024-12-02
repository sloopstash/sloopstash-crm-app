##
# -*- coding: utf-8 -*-
##
##
# Bootstrap CRM app service.
##

# Import custom modules.
from config import main_conf

# Import community modules.
import sys

# Append App specific Python paths.
sys.path.append('model')
sys.path.append('controller')
sys.path.append('helper')

# Import community modules.
import argparse
from flask import Flask,request

# Import custom modules.
from controller.user import user_web_controller
from controller.account import account_web_controller
from controller.contact import contact_web_controller


# Health web controller.
def health_web_controller():
  return str('OK')

# Create account.
def create_account():
  if request.method=='GET':
    return account_web_controller(request).get()
  elif request.method=='POST':
    return account_web_controller(request).post()
  else:
    return None

# Update account.
def update_account(arg_0):
  if request.method=='GET':
    return account_web_controller(request).get(str(arg_0))
  elif request.method=='POST':
    return account_web_controller(request).post(str(arg_0))
  else:
    return None

# Create contact.
def create_contact(arg_0):
  if request.method=='GET':
    return contact_web_controller(request).get(str(arg_0))
  elif request.method=='POST':
    return contact_web_controller(request).post(str(arg_0))
  else:
    return None

# Update contact.
def update_contact(arg_0,arg_1):
  if request.method=='GET':
    return account_web_controller(request).get(str(arg_0),str(arg_1))
  elif request.method=='POST':
    return account_web_controller(request).post(str(arg_0),str(arg_1))
  else:
    return None


# Initialize Flask app.
app = Flask('CRM app',template_folder='view')

# App routes.
app.add_url_rule('/health',view_func=health_web_controller)
app.add_url_rule('/dashboard',view_func=dashboard)
app.add_url_rule('/account/create',view_func=create_account)
app.add_url_rule('/account/<int:arg_0>/update',view_func=update_account)
app.add_url_rule('/account/<int:arg_0>/contact/create',view_func=create_contact)
app.add_url_rule('/account/<int:arg_0>/contact/<int:arg_1>/update',view_func=update_contact)


if __name__=='__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--port',type=int,default=2000)
  parser.add_argument('--host',default='0.0.0.0')
  args = parser.parse_args()
  try:
    print 'Starting CRM app service...'
    app.run(debug=True,host=args.host,port=args.port)
  except KeyboardInterrupt:
    print 'Stopping CRM app service...'
  finally:
    pass
