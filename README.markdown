GoodTodo-CLI
============

GoodTodo-CLI is a command-line tool, written in Python, to view and manage your GoodTodo tasks in the terminal.

Installation
------------
GoodTodo-CLI depends on Mechanize. After installing that, edit `tasks.py` to include your username and password in the `user` and `pswd` variables. Run `tasks.py --help` for help.

Usage
-----
    -h                    Display the help message
    -a TASK               Add a new task to today's list
    -c NUMBER             Check a task off the list
    -d YYYYMMDD [TASK]    View or add tasks on a given date
    -n DAYS [TASK]        View or add tasks a certain number of days away
    -l                    List all tasks, including completed ones