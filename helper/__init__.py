##
# -*- coding: utf-8 -*-
##
##
# Common helper.
##

# Import community modules.
import re
from phonenumbers import parse,is_valid_number


# Validate text.
def is_text(value):
  if value:
    if re.match(r'^[a-zA-Z0-9.\s\-@/]+$',value):
      return True
    else:
      return 'Invalid text. Only lowercase, uppercase, integer, space, @, /, and - characters are allowed.'
  else:
    return 'Cannot accept empty value.'

# Validate email address.
def is_email(value):
  if value:
    if re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',value):
      return True
    else:
      return 'Invalid email address.'
  else:
      return 'Cannot accept empty value.'

# Validate phone number.
def is_phone(value):
  if value:
    try:
      value = parse(value)
      if is_valid_number(value):
        return True
      else:
        return 'Invalid phone number.'
    except Exception as error:
      return 'Invalid phone number.'
  else:
    return 'Cannot accept empty value.'

# Validate password.
def is_password(value):
  if value:
    if re.match(r'(?=.{10,})(?=.*?[^\w\s])(?=.*?[0-9])(?=.*?[A-Z]).*?[a-z].*',value):
      return True
    else:
      return 'Invalid password. Should contain lowercase, uppercase, integer, and special characters.'
  else:
    return 'Cannot accept empty value.'

# Validate integer.
def is_integer(value):
  if value:
    if re.match(r'^[0-9]+$',value):
      return True
    else:
      return 'Invalid integer. Only integer characters are allowed.'
  else:
    return 'Cannot accept empty value.'
