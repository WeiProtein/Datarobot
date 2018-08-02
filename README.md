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
Eventually, I settled with saving the user's input as static variables. From there all 
backend functions can be viewed in routes.py. 

BLOCKERS:

The first issue I encountered was around user security with passwords. I originally wanted
to hash a user's passwords, but I quickly realized that there would be a need for unhashing
in order to push to a user's repo. 

Secondly,
I realized that this new version of Github caches username and passwords so I had to take in
a user's original password without hashing. I realize that this in itself is a security risk.

Thirdly,
I was able to create an empty repo for a user but because of the cached credentials, I was 
unable to input the user's password once prompted by the git push function. I tried a few 
methods such as the Popen method to input the user's password once prompted. 

Fourth,
I originally wanted to host on GitHub pages site, but due to time constraints I was unable to
host the final project online.
