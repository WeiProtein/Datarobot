INTRO:

Prerequesites:

- Flask
- flask_wtf
- os
- subprocess
- getpass


SETUP:

git clone https://github.com/weiprotein/self-replicating-repo.git && cd self-replicating-repo


PROCESS:

The thought process behind tackling this problem was to build back end functionality of taking
a repository and copying to a user's own GitHub. Once this was built, a front end was to be 
designed and hosted on GitHub pages. The front end was to take in a user's GitHub username and
password and replicate my original repo to the user's new repository. the tricky part was saving
a user's username and password on the front end in order to execute my backend instructions.
There was also the issue of security with a user's password. I will explain in the blockers
section of this post.

PROGRESS:

I was able to package my front end to take in username and password with password verification 
(ie the passwords entered do in fact match). Once taken in, I played around with the idea of 
creating a database of users and calling the database in order to make the backend call. 
Eventually 
