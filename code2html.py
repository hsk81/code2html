#!bin/python
###############################################################################

from flask import Flask
from flask import render_template
from celery import Celery

import time
import tasks

###############################################################################
app = Flask (__name__)
###############################################################################

@app.route("/")
def index ():

    return render_template ('index.html',
        keywords = 'new tab, source, code, pygments',
        description = 'Show source file in their own tabs',
        debug = app.debug)

@app.route("/pre/<ext>-source.html")
def pre_source (ext):

    if not tasks.security_check (ext):
        return "invalid extension"

    return render_template ('pre/%s-source.html' % ext)

@app.route("/fly/<ext>-source.html")
def fly_source (ext):

    asr = tasks.convert.delay (ext)
    while not asr.ready ():

        time.sleep (0.005)

    return render_template (asr.result)

###############################################################################
if __name__ == "__main__":
###############################################################################

    app.run (host='0.0.0.0', port=5001, debug=True)
