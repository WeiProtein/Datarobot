#!/usr/bin/env python

import os
import getpass
from github import Github

#user input for username and password to user's profile
userName = raw_input('Please enter Github username: ')
password = getpass.getpass('Please enter your password: ')

g = Github(userName, password)

for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
