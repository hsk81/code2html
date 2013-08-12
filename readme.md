code2html
=========

If people want to show a source file in a new tab, it usually works for text files. But if **CPP**, **H** files or like are involved then those are offered as a download! One possible solution to this problem is to convert those source files to HTML using tools like [pygments](http://pygments.org/faq/), which allows you a conversion like:

* `pygmentize -f html -O full -o cpp-source.html source.cpp`

This will create an HTML file *cpp-source.html* from *source.cpp*, where the latter can then be served with whatever method. **code2html** is a small web application demonstrating this approach; follow the instructions below to get it running:

    $ git clone git://github.com/hsk81/code2html.git code2html.git

Clones the GIT repository **code2html** from GitHub; you'll only have read access.

    $ cd code2html.git

Switches to the repository folder *code2html.git*, which has been created at the first step.

    $ ./setup.sh ## requires `virtualenv` for Python 2.x!

Installs the **code2html** dependencies **Flask** and **Pygments**. For this step to work you need a `python` interpreter with the `virtualenv` environment builder properly set-up.

    $ source bin/activate

Activates `virtualenv` for the project; this step is necessary since the previous one has installed our dependencies into a virtual environment.

    $ ./code2html.py

Executes the **code2html** web application; you should see an output like `running on http://0.0.0.0:5001/`. Point your browser to the address and play around with the demonstration.

The *pre-converted* examples should just work, but for the *on-the-fly* examples to deliver anything you need to activate a [Celery](http://www.celeryproject.org/) worker by executing additionally the following command in a second terminal:

    $ source bin/activate && celery worker --app=tasks

After you're done with the demonstration hit **CTRL+C** and run `deactivate` to exit the virtual environment.
