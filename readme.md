code2html
=========

If people want to show a source file in a new tab, it usually works for text
files. But if **CPP**, **H** files or like are involved then those are offered
as a *download*. One possible solution to this problem is to convert those
source files to HTML using tools like [pygments](http://pygments.org/faq/),
which allows you a conversion like:

    * ```pygmentize -f html -O full -o cpp-source.html source.cpp```

This will create an HTML file `cpp-source.html` from `source.cpp`, where the
latter can then be served with whatever method.

`code2html` is a small web application demonstrating this approach; follow the
instructions below the get it running:

    1. `git clone git://github.com/hsk81/code2html.git code2html.git`

       Clone the GIT repository `code2html` from GitHub; you'll only have read
       access.

    2. `cd code2html.git`

       Switch to the repository folder `code2html.git`, which has been created
       at the first step.

    3. `./setup.sh`

       This installs the `code2html` dependencies `Flask` and `Pygments`. For
       this step to work you need a `python` interpreter with the `virtualenv`
       environment builder properly set-up.

    4. `source bin/activate`

       This activates `virtualenv` for the project; this step is necessary since
       the previous step one has installed our dependencies into a virtual
       environment.

    5. `./code2html.py`

       Execute the `code2html` web application; you should see an output like
       `running on http://127.0.0.1:5000/`. Point your browser to the address
       and play around with the demonstration.

    6. After you're done with the demonstration hit CTRL+C to kill `code2html`
       and run `deactivate` to exit the virtual environment.