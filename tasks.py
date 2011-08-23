#!/usr/bin/env python

# set username and password
user = ""
pswd = ""

import re               # regular expression processing
import mechanize        # web scraping
import argparse         # parse command-line arguments

# parse command-line arguments
parser = argparse.ArgumentParser(description='A command-line interface for GoodTodo.')
parser.add_argument('-a,--add', action='store', nargs='+', metavar='TASK', help='Add a new task to the list')
args = parser.parse_args()

# login to GoodTodo
br = mechanize.Browser()
br.open("https://goodtodo.com/login.php")
br.select_form(nr=0)
br["username"] = user
br["password"] = pswd
response = br.submit()
page = response.read()

# add a task
if vars(args)['a,__add']:
    # convert the task into a string
    task = ""
    for arg in vars(args)['a,__add']:
        task += arg+' '
    task = task[:-1]
    br.select_form(nr=0)
    br["title"] = task
    response = br.submit()
    page = response.read()
# set the username and password
# Open the Google sign-in page and sign-in to the user's Google account using mechanize
taskPattern = re.compile(r'												(.+)<span class')
for task in re.findall(taskPattern, page):
    print(' - '+task)
