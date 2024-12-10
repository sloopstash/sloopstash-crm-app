##
# -*- coding: utf-8 -*-
##
##
# Contact controller.
##

# Import community modules.
from flask import render_template

# Import custom modules.
from controller import root_web_controller


# Contact web controller.
class contact_web_controller(root_web_controller):

  # HTTP GET method processor.
  def get(self,*args,**kwargs):
    return render_template('main.html',var=self.var)
