Tracking Nutrition Data
======

-Flasky webapp to input and track nutrition.

Libraries Used
======

1.Certifi
-----------

Certifi is a carefully curated collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts.

2.Click
-----------

A simple wrapper around optparse for powerful command line utilities.

3.Dominate
-----------

Dominate is a Python library for creating and manipulating HTML documents using an elegant DOM API.
It allows you to write HTML pages in pure Python very concisely, which eliminates the need to learn another template language, and lets you take advantage of the more powerful features of Python

4.Flask==0.12.2
-----------

Flask is a microframework for Python based on Werkzeug and Jinja 2. Flask aims to keep the core simple but extensible.

5.Flask-Bootstrap
-----------

This makes some new templates available, mainly bootstrap_base.html and bootstrap_responsive.html. These are blank pages that include all bootstrap resources, and have predefined blocks where you can put your content. The core block to alter is body_content, otherwise see the source of the template for more possiblities.

The url-endpoint bootstrap.static is available for refering to Bootstrap resources, but usually, this isn’t needed. A bit better is using the bootstrap_find_resource template filter, which will CDN settings into account.


6.Flask-Script
-----------

The Flask-Script extension provides support for writing external scripts in Flask. This includes running a development server, a customised Python shell, scripts to set up your database, cronjobs, and other command-line tasks that belong outside the web application itself.

Flask-Script works in a similar way to Flask itself. You define and add commands that can be called from the command line to a Manager instance.

7.Flask-SQLAlchemy
-----------

Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy to your application. It requires SQLAlchemy 0.8 or higher. It aims to simplify using SQLAlchemy with Flask by providing useful defaults and extra helpers that make it easier to accomplish common tasks.

8.Flask-WTF
-----------

Simple integration of Flask and WTForms, including CSRF, file upload, and reCAPTCHA.

9.Jinja2
-----------

A small but fast and easy to use stand-alone template engine written in pure python.

Jinja2 is a template engine written in pure Python. It provides a Django inspired non-XML syntax but supports inline expressions and an optional sandboxed environment.

10.MarkupSafe
-----------

Implements a XML/HTML/XHTML Markup safe string for Python.

11.Werkzeug
-----------

Werkzeug is a comprehensive WSGI web application library. It began as a simple collection of various utilities for WSGI applications

Data Importing and Access
======

-Collection through web UI
-Database is updated when new User and food data is entered through the web form.
-A simple count of food data in the database can be accessed through the web UI as well

Author
======

-Dave Owen

License
======

This project is licensed under the MIT License - see the LICENSE.txt file for details.
