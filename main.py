# Forked from: creativeJoe007

'''
usage: run.py [-h] [--start START] [--stop STOP] --file FILE
              [--browser BROWSER] [--driver DRIVER]
              query
run.py: error: the following arguments are required: query, --file
'''

import argparse
from browser import determine_browser
from extractor import Extractor
from println import println

def main(query, start_page, stop_page):
  executor_url = ""
  session_id = ""
  selected_browser = "chrome"
  browser_driver_path = ""
  max_page = 100

  if start_page < 0: start_page = 0 # If the user puts in 0, we auto make it one
  elif (stop_page - start_page) > max_page:
    println("Hardcoded limit is {} pages.".format(max_page))

 # Determine what browser to use for this tool
  driver = determine_browser(selected_browser, browser_driver_path)
  if type(driver) == str:
    print("", end="") #println(driver)
  else:
    executor_url = driver.command_executor._url
    session_id = driver.session_id

    # Maximize chrome height to highest
    driver.set_window_size(1920, 8000)

    print("", end="") #println(f"Google's Query: {query}", "normal")
    extractor = Extractor(driver, query, start_page, stop_page)
    driver.close()
