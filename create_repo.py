#!/usr/bin/env python

import os
import getpass
from github import Github

#user input for username and password to user's profile
userName = raw_input('Please enter Github username: ')
password = getpass.getpass('Please enter your password: ')

g = Github(userName, password)

#print out all repos in user's github
for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)

#using shell to execute git command
def execute(cmd, work_dir):
     pipe = subprocess.Popen(cmd, shell=True, cwd=work_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, error) = pipe.communicate()
    print out, error
    pipe.wait()

#adds file to index
def git_add(file_path, repo_dir):
    cmd = 'git add ' + file_path
    execute(cmd, repo_dir)
