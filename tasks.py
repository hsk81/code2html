#!bin/python
###############################################################################

from celery import Celery
import subprocess

###############################################################################
celery = Celery (__name__, broker='redis://', backend='redis://')
###############################################################################

@celery.task
def convert (ext):

    if not security_check (ext):
        return "invalid extension"

    source = 'static/source.%s' % ext
    target = 'fly/%s-source.html' % ext

    with open ('stdout.log', 'w') as stdout:
        with open ('stderr.log', 'w') as stderr:

            subprocess.check_call (['pygmentize',
                '-f', 'html','-O', 'full', '-o', 'templates/' + target, source
            ], stdout=stdout, stderr=stderr)

    return target

def security_check (ext):

    return ext.lower () in ['c','cpp', 'h']

###############################################################################
###############################################################################
