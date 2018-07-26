#!/usr/bin/env python

from flask import Flask, render_template, url_for, flash, redirect, request
from create_repo import app,db
from create_repo.forms import InfoForm
from create_repo.models import User
import os
import getpass
import subprocess
from subprocess import Popen, PIPE


#routes start
@app.route("/",methods=['GET', 'POST'])
@app.route("/home",methods=['GET', 'POST'])
def home():
    #return render_template('home.html')
    form = InfoForm()
    if form.validate_on_submit():
        #probably don't need to save to db
        user = User(username=form.username.data, password=form.password.data)
        db.drop_all()
        db.create_all()
        db.session.add(user)
        db.session.commit()
        flash('Repo has been created for %s!'% (form.username.data),'success')
        #return redirect(url_for('home'))

        ######BEGIN GIT REPLICATION HERE########

        user_name = str(form.username.data)
        password = str(form.password.data)

        #using shell to execute git command
        def execute(cmd, work_dir):
            pipe = subprocess.Popen(cmd, shell=True, cwd=work_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            (out, error) = pipe.communicate()
            print out, error
            pipe.wait()

        #cloning original repository & move into that directory
        def git_clone(repo_dir):
            cmd = 'git clone https://github.com/weiprotein/self-replicating-repo.giti && cd create_repo'
            execute(cmd, repo_dir)

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

        #git push - ensure that credentials are deleted first if keychain access enabled
        def git_push(repo_dir):
            cmd_1 = 'git credential-osxkeychain erase'
            cmd_2 = 'host=github.com'
            cmd_3 = 'protocol=https'
            execute(cmd_1, repo_dir)
            execute(cmd_2, repo_dir)
            execute(cmd_3, repo_dir)

            cmd_4 = 'git push -u origin master'
            execute(cmd_4, repo_dir)

        #get the user's pwd
        pwd = os.getcwd()

        git_init(pwd)
        print "====PAST STEP 1===="

        git_add(pwd)
        print "============PAST STEP 2============"

        git_commit('Testing gitupload via script.', pwd)
        print "============================WE HAVE GIT COMMIT========================"

        create_repo(user_name,'script_test', pwd)
        #repo = Popen(['curl', '-u', str(user_name), 'https://api.github.com/user/repos', '-d', '\'{"name":"script_test"}\''], stdin=PIPE)
        #repo.communicate(password)
        print "===============================REPO HAS BEEN CREATED======================="

        create_origin(user_name, 'script_test', pwd)
        git_push(pwd)
        #cmd = Popen(['git', 'push', '-u', 'origin', 'master'], stdin=PIPE)
        #cmd.communicate(password)
        print "===========================================GIT PUSH HAS OCCURED========================"


        """
        #giving the command line username and password
        execute(user_name, pwd)
        execute(password, pwd)
        execute(password, pwd)
        execute(password, pwd)
        """

        ######END GIT REPLICATION HERE######

    return render_template('info.html', title='GitHub Info', form=form)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html",result = result)
