##
# -*- coding: utf-8 -*-
##
##
# Database helper.
##

# Import community modules.
import redis as _redis

# Import custom modules.
from config import redis_conf


# Redis database helper.
class redis(object):

  # Instances.
  _instances = dict()

  # Constructor.
  def __new__(self):
    if 'instance' in redis._instances:
      return redis._instances['instance']
    else:
      self.conf = redis_conf
      self.engine = _redis.Redis(connection_pool=_redis.ConnectionPool(
        host=self.conf['endpoint'],
        port=self.conf['port'],
        max_connections=10,
        db=0
      ))
      return super(redis,self).__new__(self)

  # Initializer.
  def __init__(self):
    redis._instances['instance'] = self


# Launch database helpers.
redis = redis()
