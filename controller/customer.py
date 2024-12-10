##
# -*- coding: utf-8 -*-
##
##
# Customer controller.
##

# Import community modules.
import math
from decimal import Decimal
from flask import render_template,jsonify,redirect

# Import custom modules.
from controller import root_web_controller
from model.customer import customer


# Customer web controller.
class customer_web_controller(root_web_controller):

  # HTTP GET method processor.
  def get(self,*args,**kwargs):
    if self.request.path=='/customers':
      if self.request.args.get('count'):
        customers = customer().count()
        if customers>0:
          limit = Decimal(5.0)
          pages = math.ceil(customers/limit)
          return jsonify({'status':'success','result':{'count':customers,'pages':int(pages)}})
        else:
          return jsonify({'status':'failure','message':'Not available.'})
      else:
        limit = 5
        offset = (int(self.request.args.get('page'))*limit)-limit if self.request.args.get('page') else 0
        customers = customer().list(offset=offset,limit=limit)
        return jsonify({'status':'success','result':{'items':customers}})
    elif self.request.path=='/customer/create':
      return render_template('customer/create.html',var=self.var)
    elif self.request.path=='/customer/'+args[0]+'/update':
      customer_id = args[0]
      self.var['customer'] = customer().get(customer_id)
      return render_template('customer/update.html',var=self.var)
    elif self.request.path=='/customer/'+args[0]+'/dashboard':
      customer_id = args[0]
      self.var['customer'] = customer().get(customer_id)
      return render_template('customer/dashboard.html',var=self.var)
    else:
      return render_template('error.html',var=self.var)

  # HTTP POST method processor.
  def post(self,*args,**kwargs):
    if self.request.path=='/customer/create':
      data = {
        'name':self.request.form.get('name'),
        'email':self.request.form.get('email'),
        'phone':self.request.form.get('phone'),
        'website':self.request.form.get('website'),
        'description':self.request.form.get('description')
      }
      if customer().create(data) is True:
        return redirect('/dashboard')
      else:
        return render_template('error.html',var=self.var)
    elif self.request.path=='/customer/'+args[0]+'/update':
      data = {
        'name':self.request.form.get('name'),
        'email':self.request.form.get('email'),
        'phone':self.request.form.get('phone'),
        'website':self.request.form.get('website'),
        'description':self.request.form.get('description')
      }
      data['customer_id'] = args[0]
      if customer().update(data) is True:
        return redirect('/dashboard')
      else:
        return render_template('error.html',var=self.var)
    else:
      return render_template('error.html',var=self.var)
