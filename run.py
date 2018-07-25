#!/usr/bin/env python

import os
import subprocess
import getpass
from flask import render_template, url_for, flash, redirect, request
from create_repo import app

if __name__ == '__main__':
    app.run(debug=True)
