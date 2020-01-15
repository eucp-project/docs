#! /usr/bin/env python3

"""Poor man's attempt at providing a "HTML site generator"

This wraps the output from ASCIIDoctor with a standard structure,
following the EUCP website. It will run `asciidoctor`, with the option
to leave off all header and footer parts, and wrap that output inside
a template to roughly match the EUCP website.

There is no attempt to use the ASCIIDoctor API (or the Python 3
version of ASCIIDoc): it is simply run using subprocess, grabbing the
output and wrapping that.

"""

import sys


flags = {'style': False, 'header': False, 'footer': False}
for line in sys.stdin:
    if '</style>' in line:
        flags['style'] = False
        continue
    if flags['style']:
        continue
    if '<style>' in line:
        flags['style'] = True
        print("""\
<link rel="stylesheet" id="bootstrap-css" href="https://www.eucp-project.eu/wp-content/themes/tentered/css/bootstrap.css?ver=1.0" type="text/css" media="all">
<link rel="stylesheet" id="bootstrap-theme-css" href="https://www.eucp-project.eu/wp-content/themes/tentered/css/bootstrap-theme.css?ver=1.0" type="text/css" media="all">
<link rel="stylesheet" id="ecup-extra-css" href="https://lab.eucp-project.eu/hub/static/css/eucp.css" type="text/css" media="all">
""")
        continue
    if flags['header']:
        flags['header'] = False
        continue
    if '<div id="header">' in line:
        print("""\
<div id="header">
<div class="content menu">
<a href="https://lab.eucp-project.eu/help">help</a> | <a href="https://eucp-project.eu/">main site</a> | <a href="https://www.eucp-project.eu/the-eucp-wiki/">eucp - wiki</a>
</div>
</div>
<a href="https://eucp-project.eu"><img class="logo" src="https://lab.eucp-project.eu/hub/logo" alt="EUCP home" title="EUCP home"></a>
""")
        flags['header'] = True
        continue
    print(line, end="")
