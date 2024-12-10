##
# -*- coding: utf-8 -*-
##
##
# Customer model.
##

# Import community modules.
import json

# Import custom modules.
from database import redis


# Customer main model.
class customer(object):

  # Initializer.
  def __init__(self):
    self.redis = redis

  # Create customer.
  def create(self,data):
    try:
      id = self.redis.engine.incr(
        self.redis.conf['key_prefix']['customer']['counter']
      )
      self.redis.engine.hset(
        self.redis.conf['key_prefix']['customer']['main'],id,json.dumps(data)
      )
    except Exception as error:
      return False
    else:
      return True

  # Update customer.
  def update(self,data):
    try:
      id = data['customer_id']
      self.redis.engine.hset(
        self.redis.conf['key_prefix']['customer']['main'],id,json.dumps(data)
      )
    except Exception as error:
      return False
    else:
      return True

  # Get customer.
  def get(self,id):
    data = self.redis.engine.hget(
      self.redis.conf['key_prefix']['customer']['main'],id
    )
    if data:
      item = {
        'id':id
      }
      item.update(json.loads(data))
      return item
    else:
      return

  # Count of customers.
  def count(self):
    count = self.redis.engine.hlen(
      self.redis.conf['key_prefix']['customer']['main']
    )
    return count

  # List customers.
  def list(self,**kwargs):
    offset = kwargs['offset'] if kwargs.has_key('offset') else 0
    limit = kwargs['limit'] if kwargs.has_key('limit') else 5
    data = self.redis.engine.hgetall(
      self.redis.conf['key_prefix']['customer']['main']
    )
    items = []
    for key,value in data.items():
      item = {
        'id':key
      }
      item.update(json.loads(value))
      items.append(item)
    return items
