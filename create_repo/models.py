#!/usr/bin/env python

from create_repo import db

class User(db.Model):
    username = db.Column(db.String(30), primary_key=True, unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)

    def __repr__(self):
        #return ("User({username},{passsword})".format(username={self.username}, {password=self.password}))
        return "(%s, %s)" % (self.username, self.password)
