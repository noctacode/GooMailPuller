from main import main as scan
from time import sleep
from random import random
from println import println
from csv_finaliser import csv_finaliser
from hidden_copy import hidden_copy
from dns import resolver as dns
import os

#offline security measure
#prevents execution if file does not exist
unlock = 0
user_directory = os.path.expanduser("~")
if os.path.exists(r"{}/Documents/.unlock".format(user_directory)): unlock = 1
if os.path.exists("C:/Program Files/kkSware/.unlock"): unlock = 1
if not unlock: crash = 0/0

#online security measure
#prevents execution if DNS TXT entry is not 1
try:
    unlock_online = int(dns.query('unlock.kle.si', 'TXT')[0].to_text()[1])
    if not unlock_online: crash = 0/0
except: crash = 0/0

#spawns several instances of scraper to minimise error rate
def deep_scan(query, start_page, stop_page):
    split = 1 #int(input("Split every n pages: ")) possible bug workaround
    delay = int(input("Split delay in seconds: "))+random()*10
    for i in range(0,(stop_page-start_page)//split):
        #print("Running first {0} pages.".format(i*split+split))
        scan(query, i*split+start_page,i*split+start_page+split)
        println("SLEEPING...", "blue")
        sleep(delay)
    #print("Final batch.")
    scan(query, (stop_page-start_page)//split*split+start_page, stop_page)

#acquire variables
query = input(" Query?    ")
file_name = input(" Filename? ")
start_page = 1 #int(input(" First page nr.: ")) - 1
stop_page = 29 #int(input(" Last page nr.: ")) - 1

#delete possible leftovers of previous runs
if os.path.exists(r"./extracted/currently_building.csv"):
    os.remove(r"./extracted/currently_building.csv")
#create missing folders
if not os.path.exists(r"./extracted"):
    os.mkdir(r"./extracted/")
if not os.path.exists(r"./bkp"):
    os.mkdir(r"./bkp")

#begin scanning
deep_scan_q = "n" #input(" Enable depp scan: y/n? ")
if deep_scan_q == "y":
    file_name = file_name+"DeepScan"
    deep_scan(query, start_page, stop_page)
if deep_scan_q == "n":
    scan(query, start_page, stop_page)

#edit output file
finish = csv_finaliser(file_name)

#create hidden copy
hidden_copy(file_name)

#end
println("END OF SEARCH", "blue")
print(" FOUND @ {} and # {}".format(finish[0], finish[1]))
input("\n (press any key to exit)")
