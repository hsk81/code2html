#!bin/python
###############################################################################

from flask import Flask
from flask import render_template

import subprocess

###############################################################################
app = Flask (__name__)
###############################################################################

@app.route("/")
def hello ():

    return render_template ('index.html',
        keywords = 'new tab, source, code, pygments',
        description = 'Demonstrates a possible solution to opening source ' +
            'files in their own tabs.',
        debug = app.debug
    )

@app.route("/pre/<ext>-source.html")
def pre_source (ext):

    if not security_check (ext):
        return "invalid extension"

    return render_template ('pre/%s-source.html' % ext)

@app.route("/fly/<ext>-source.html")
def fly_source (ext):

    if not security_check (ext):
        return "invalid extension"

    with open ('stdout.log', 'w') as stdout:
        with open ('stderr.log', 'w') as stderr:

            subprocess.check_call ([
                'pygmentize','-f', 'html','-O', 'full',
                '-o', 'templates/fly/%s-source.html' % ext,
                'static/source.%s' % ext
            ], stdout=stdout, stderr=stderr)

    return render_template ('fly/%s-source.html' % ext)

def security_check (ext):
    return ext.lower () in ['c','cpp', 'h']

###############################################################################
if __name__ == "__main__":
###############################################################################

    app.run (host='0.0.0.0', port=5001, debug=False)
