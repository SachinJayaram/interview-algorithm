#!/usr/bin/env python


# import module
from art import *
  
# Return ASCII text with block font
# If font=None then there is no block
Art = text2art("GFG", font='block', chr_ignore=True)
  
print(Art)