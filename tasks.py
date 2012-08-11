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

    with open ('stdout.log', 'w') as stdout:
        with open ('stderr.log', 'w') as stderr:

            subprocess.check_call ([
                'pygmentize','-f', 'html','-O', 'full',
                '-o', 'templates/fly/%s-source.html' % ext,
                'static/source.%s' % ext
            ], stdout=stdout, stderr=stderr)

    return 'fly/%s-source.html' % ext

def security_check (ext):

    return ext.lower () in ['c','cpp', 'h']

###############################################################################
###############################################################################
