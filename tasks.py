#!/usr/bin/env python

# set username and password
user = ""
pswd = ""

import re               # regular expression processing
import mechanize        # web scraping
import argparse         # parse command-line arguments
import datetime         # handle time-delayed tasks
import webbrowser       # open pages in the web browser

# parse command-line arguments
parser = argparse.ArgumentParser(description='A command-line interface for GoodTodo.')
parser.add_argument('-a', action='store', nargs='+', metavar='TASK', help='Add a new task to today\'s list')
parser.add_argument('-c', action='store', metavar='NUMBER', type=int, help='Check a task off the list')
parser.add_argument('-d', action='store', nargs='+', metavar='YYYYMMDD TASK', help='View or add tasks on a given date')
parser.add_argument('-n', action='store', nargs='+', metavar='DAYS TASK', help='Add a task a certain number of days away')
parser.add_argument('-l', action='store_true', help='List all tasks, including completed ones')
parser.add_argument('-o', action='store_true', help='Open today\'s task list in a web browser')
parser.add_argument('-v', action='store', metavar='NUMBER', type=int, help='View a task\'s details in a web browser')
args = parser.parse_args()

# login to GoodTodo and get the todo page
br = mechanize.Browser()
br.open("https://goodtodo.com/login.php")
br.select_form(nr=0)
br["username"] = user
br["password"] = pswd
response = br.submit()
page = response.read()

# complete a task
if vars(args)['c']:
    tasknum = vars(args)['c']
    idPattern = re.compile(r'src="images/CheckboxUnchecked.gif" border="0" id="(\d+)" /></span>[\r\n]+												.+<span class')
    id = re.findall(idPattern, page)[tasknum-1]
    br.open("https://goodtodo.com/detail.php?id="+id)
    br.select_form(nr=0)
    br.find_control("done").items[0].selected=True
    response = br.submit()
    page = response.read()

# add a task
if vars(args)['a']:
    # convert the task into a string
    task = ""
    for arg in vars(args)['a']:
        task += arg+' '
    task = task[:-1]
    br.open("https://goodtodo.com/new.php")
    br.select_form(nr=0)
    br["title"] = task
    response = br.submit()
    page = response.read()

# view or add tasks at a given future date
if vars(args)['d']:
    # convert the task into a string
    task = ""
    for arg in vars(args)['d']:
        task += arg+' '
    date = task[:10]
    task = task[11:-1]
    br.open("https://goodtodo.com/new.php?edate="+date)
    if task is not '':
        br.select_form(nr=0)
        br["title"] = task
        response = br.submit()
        page = response.read()

# view or add tasks a given number of days in the future
if vars(args)['n']:
    # convert the task into a string
    task = ""
    for arg in vars(args)['n']:
        task += arg+' '
    (days,x,task) = task.partition(' ')
    date = datetime.date.today() + datetime.timedelta(int(days))
    if task is not '':
        br.open("https://goodtodo.com/new.php?edate="+str(date))
        br.select_form(nr=0)
        br["title"] = task
        response = br.submit()
        page = response.read()
    else:
        response = br.open("https://goodtodo.com/home.php?edate="+str(date))
        page = response.read()

# open today's todo list in the default web browser
if vars(args)['o']:
    webbrowser.open('http://www.goodtodo.com/home.php')

# open a task's details view in the default browser
if vars(args)['v']:
    tasknum = vars(args)['v']
    idPattern = re.compile(r'src="images/CheckboxUnchecked.gif" border="0" id="(\d+)" /></span>[\r\n]+												.+<span class')
    id = re.findall(idPattern, page)[tasknum-1]
    webbrowser.open("https://goodtodo.com/detail.php?id="+id)

# use a regex to pick the individual tasks off of the page
taskPattern = re.compile(r'src="images/CheckboxUnchecked.gif" border="0" id="\d+" /></span>[\r\n]+												(.+)<span class')

# print each task with a number beside it
tasknum = 1
for task in re.findall(taskPattern, page):
    print(str(tasknum)+'. '+task)
    tasknum += 1

# print a list of completed tasks
if vars(args)['l']:
    completedTaskPattern = re.compile(r'src="images/CheckboxChecked.gif" border="0" id="\d+" /></span>[\r\n]+												(.+)<span class')
    print('\nCompleted Tasks:')
    for task in re.findall(completedTaskPattern, page):
        print(' - '+task)
