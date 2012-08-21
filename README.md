GoodTodo-CLI
============

GoodTodo-CLI is a command-line tool, written in Python, to view and manage your GoodTodo tasks in the terminal.

[**Download it!**](https://raw.github.com/tdeitch/goodtodo-cli/master/tasks.py)

![screenshot](https://raw.github.com/tdeitch/goodtodo-cli/master/screenshot.png)

Installation
------------
GoodTodo-CLI depends on Mechanize. After installing that, edit `tasks.py` to include your username and password in the `user` and `pswd` variables. Run `tasks.py -h` for help.

Usage
-----
    -h                    Display the help message
    -a TASK               Add a new task to today's list
    -c NUMBER             Check a task off the list
    -d YYYYMMDD [TASK]    View or add tasks on a given date
    -n DAYS [TASK]        View or add tasks a certain number of days away
    -l                    List all tasks, including completed ones
    -o                    Open today's task list in a web browser
    -v                    View a task's details in a web browser
