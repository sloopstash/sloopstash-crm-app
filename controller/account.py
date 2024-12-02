##
# -*- coding: utf-8 -*-
##
##
# Account controller.
##

# Import community modules.
from flask import render_template
from werkzeug.exceptions import NotFound,BadRequest

# Import custom modules.
from controller import root_web_controller


# Account web controller.
class account_web_controller(root_web_controller):

  # HTTP GET method processor.
  def get(self,*args,**kwargs):
    return render_template('main.html',var=self.var)
