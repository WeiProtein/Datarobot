#!/usr/bin/env python

import os
import subprocess
import getpass
from github import Github

#user input for username and password to user's profile
user_name = raw_input('Please enter Github username: ')
password = getpass.getpass('Please enter your password: ')

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
    excute(cmd, repo_dir)

#creating remote branch to push to master
def create_origin(user_name, repo_dir):
    cmd = 'git remote add origin https://github.com/' + user_name + '/Datarobot.git'
    execute(cmd, repo_dir)

#git push
def git_push(repo_dir):
    cmd = 'git push -u origin master'
    execute(cmd, repo_dir)

git_init('/Users/Timothy.Wei-Ming.Koh@ibm.com/Documents/Dev/DataRobot')
git_add('/Users/Timothy.Wei-Ming.Koh@ibm.com/Documents/Dev/DataRobot')
git_commit('Testing gitupload via script.', '/Users/Timothy.Wei-Ming.Koh@ibm.com/Documents/Dev/DataRobot')
create_repo('weiprotein','script_test','/Users/Timothy.Wei-Ming.Koh@ibm.com/Documents/Dev/DataRobot')
create_origin('weiprotein','/Users/Timothy.Wei-Ming.Koh@ibm.com/Documents/Dev/DataRobot')
git_push('/Users/Timothy.Wei-Ming.Koh@ibm.com/Documents/Dev/DataRobot')




