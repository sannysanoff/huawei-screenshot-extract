import os

import easyocr
import sys
import time
from datetime import datetime

from PIL import Image

import numpy as np


reader = easyocr.Reader(['ru', 'en'])  # this needs to run only once to load the model into memory
result = reader.readtext(sys.argv[1])
#print(result)
for i, res in enumerate(result):
   strval = res[1]
   try:
        maybeY =  int(strval)
        if (maybeY >= 100 and maybeY <= 200):
            print("maybey ",maybeY,res[0][0][1])
   except:
        # Raise an error if the value cannot be converted
        pass

for i, res in enumerate(result):
   s = res[1]
   s = s.replace('.', ':')
   s = s.replace('::', ':')
   if len(s) == 8  and s[2] == ':' and s[5] == ':':
      x0 = res[0][0][0]
      x1 = res[0][1][0]
      print("exactx ",s,(x1+x0)/2)
