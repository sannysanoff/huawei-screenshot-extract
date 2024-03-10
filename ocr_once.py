import os

import easyocr
import sys
import time
from datetime import datetime

from PIL import Image

import numpy as np


reader = easyocr.Reader(['ru', 'en'])  # this needs to run only once to load the model into memory
result = reader.readtext(sys.argv[1])
print(result)
