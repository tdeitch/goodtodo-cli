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
parser.add_argument('-c,--complete', action='store', metavar='NUMBER', type=int, help='Check a task off the list')
parser.add_argument('-l,--list-all', action='store_true', help='List all tasks, including completed ones')
args = parser.parse_args()

# login to GoodTodo and get the todo page
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
    br.open("https://goodtodo.com/new.php")
    br.select_form(nr=0)
    br["title"] = task
    response = br.submit()
    page = response.read()

# use a regex to pick the individual tasks off of the page
taskPattern = re.compile(r'src="images/CheckboxUnchecked.gif" border="0" id="\d+" /></span>[\r\n]+												(.+)<span class')

# print each task with a number beside it
tasknum = 1
for task in re.findall(taskPattern, page):
    print(str(tasknum)+'. '+task)
    tasknum += 1

# print a list of completed tasks
if vars(args)['l,__list_all']:
    completedTaskPattern = re.compile(r'src="images/CheckboxChecked.gif" border="0" id="\d+" /></span>[\r\n]+												(.+)<span class')
    print('\nCompleted Tasks:')
    for task in re.findall(completedTaskPattern, page):
        print(' - '+task)
