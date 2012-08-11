code2html
=========

If people want to show a source file in a new tab, it usually works for text files. But if *cpp*, *h* files or like are involved then those are offered as a download. One possible solution to this problem is to convert those source files to HTML using tools like pygments: E.g.

  ```pygmentize -f html -O full -o cpp-source.html source.cpp```

This will create an HTML file `cpp-source.html` from `source.cpp`, where the latter can then be served with whatever method.
