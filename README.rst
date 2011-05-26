To follow along this project, check out https://www.pivotaltracker.com/projects/279659

Prerequisites
-------------

* Setuptools (allows you to easy_install) - http://pypi.python.org/pypi/setuptools
* Virtualenv - easy_install virtualenv - http://pypi.python.org/pypi/virtualenv
* Python 2.6 or 2.7 - http://python.org/download/

Installation
------------

Here is how to pull and build a local copy of the system::
    
    git clone git@github.com:CivComs/commons_site.git
    virtualenv -p python2.7 --no-site-packages commons_site
    cd commons_site
    source bin/activate
    cd commons_project
    pip install --requirement requirements.txt
    ./manage.py syncdb
    ./manage.py migrate commons_core
    
Here is how to deploy to ep.io for the first time::

    First, change the app name in .epio-app to one you control
    
    epio upload
    epio django syncdb #this will ask to create a superuser. Say 'yes'.
    epio django migrate commons_core
    
Here is how to add a superuser on ep.io::
    
    epio django createsuperuser
    
If you've made changes to a static file (javascript, css, images, etc), you'll also need to::
    
    ./manage.py collectstatic
    
This should happen *before* the epio upload
