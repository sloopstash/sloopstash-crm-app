##
# -*- coding: utf-8 -*-
##
##
# User controller.
##

# Import community modules.
from flask import render_template

# Import custom modules.
from controller import root_web_controller


# User web controller.
class user_web_controller(root_web_controller):

  # HTTP GET method processor.
  def get(self,*args,**kwargs):
    if self.request.path=='/dashboard':
      return render_template('user/dashboard.html',var=self.var)
    else:
      return render_template('error.html',var=self.var)
