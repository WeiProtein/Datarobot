#!/usr/bin/env python

import os
import subprocess
import getpass
from github import Github
from flask import Flask, render_template, url_for, flash
from forms import InfoForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'gmvjdusampa99vh5'


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

#creating remote branch to push to master
def create_origin(user_name, repo_name, repo_dir):
    cmd = 'git remote add origin https://github.com/' + user_name + '/' + repo_name + '.git'
    execute(cmd, repo_dir)

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
"""

@app.route("/",methods=['GET', 'POST'])
@app.route("/home",methods=['GET', 'POST'])
def home():
    #return render_template('home.html')
    form = InfoForm()
    if form.validate_on_submit():
        flash('Repo has been created for %s!'% ({form.username.data}),'success')
        username = {form.username.data}
    return render_template('info.html', title='GitHub Info', form=form)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)

print username







