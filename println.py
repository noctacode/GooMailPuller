#----------------------------------------------------------------------------------------------------
# Authur: creativeJoe007
# Website: https://creativejoe007.com
#----------------------------------------------------------------------------------------------------
# A Google bot that allows anyone search for businesses using a keyword
# We extract the website title, description, email (if any), mobile number (if any), web-link
# An ideal bot for marketers looking to find leads/prospects
#----------------------------------------------------------------------------------------------------
import os

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def println(text, _type='fail'):
  os.system('color')
  if _type == 'red':
    print(f"{FAIL} {text} {ENDC}")
  elif _type == 'yellow':
    print(f"{WARNING} {text}  {ENDC}")
  elif _type == 'green':
    print(f"{OKGREEN} {text}  {ENDC}")
  elif _type == 'blue':
    print(f"{OKBLUE} {text}  {ENDC}")
  elif _type == 'bold':
    print(f"{BOLD} {text}  {ENDC}")
