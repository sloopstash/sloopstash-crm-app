##
# -*- coding: utf-8 -*-
##
##
# User controller.
##

# Import community modules.
from flask import render_template
from werkzeug.exceptions import NotFound,BadRequest

# Import custom modules.
from controller import root_web_controller


# User web controller.
class user_web_controller(root_web_controller):

  # HTTP GET method processor.
  def get(self,*args,**kwargs):
    return render_template('main.html',var=self.var)
