#!/usr/bin/env python

import os
import subprocess
import getpass
from github import Github
import bs4 as bs
import urllib2
from flask import render_template, url_for, flash, redirect, request
from create_repo import app

"""
#user input for username and password to user's profile
user_name = raw_input('Please enter Github username: ')
password = getpass.getpass('Please enter your password: ')
"""

###CHANGE BACK AFTER COMPLETE###
user_name = 'weiprotein'
password = 'd9p8ckva'
###

g = Github(user_name, password)

"""
#print out all repos in user's github
for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
"""

#using shell to execute git command
def execute(cmd, work_dir):
    pipe = subprocess.Popen(cmd, shell=True, cwd=work_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, error) = pipe.communicate()
    print out, error
    pipe.wait()

#git init
def git_init(repo_dir):
    cmd = 'git init'
    execute(cmd, repo_dir)

#adds file to index
def git_add(repo_dir):
    cmd = 'git add .'
    execute(cmd, repo_dir)

#commit to git
def git_commit(msg, repo_dir):
    cmd = 'git commit -m \'' + msg + '\''
    execute(cmd, repo_dir)

#create repo in user's github
def create_repo(user_name, repo_name, repo_dir):
    cmd = 'curl -u ' + user_name + ' https://api.github.com/user/repos -d \'{"name":"' + repo_name + '"}\''
    execute(cmd, repo_dir)

#delete any existing remote branches & create remote branch to push to master
def create_origin(user_name, repo_name, repo_dir):
    cmd1 = 'git remote rm origin'
    execute(cmd1,repo_dir)
    cmd2 = 'git remote add origin https://github.com/' + user_name + '/' + repo_name + '.git'
    execute(cmd2, repo_dir)

#git push
def git_push(repo_dir):
    cmd = 'git push -u origin master'
    execute(cmd, repo_dir)

#get the user's pwd
pwd = os.getcwd()

"""
git_init(pwd)
git_add(pwd)
git_commit('Testing gitupload via script.', pwd)
create_repo(user_name,'script_test', pwd)
create_origin(user_name, 'script_test', pwd)
git_push(pwd)

sauce = urllib2.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

print soup.title
"""


if __name__ == '__main__':
    app.run(debug=True)








