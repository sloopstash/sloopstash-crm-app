##
# -*- coding: utf-8 -*-
##
##
# Root controller.
##

# Import custom modules.
from config import main_conf,static_conf
from database import redis


# Root web controller.
class root_web_controller(object):

  # Initializer.
  def __init__(self,request):
    self.request = request
    self.main_conf = main_conf
    self.static_conf = static_conf
    self.redis = redis
    self.var = {}
    self.var['static'] = self.static_conf
