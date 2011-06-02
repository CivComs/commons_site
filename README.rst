To follow along this project, check out https://www.pivotaltracker.com/projects/279659

Prerequisites
-------------

* Setuptools (allows you to easy_install) - http://pypi.python.org/pypi/setuptools
* Virtualenv - easy_install virtualenv - http://pypi.python.org/pypi/virtualenv
* Python 2.6 or 2.7 - http://python.org/download/

Installation
------------

Here is how to pull a local copy of the system::
    
    git clone git@github.com:CivComs/commons_site.git

Turn the cloned commons_site folder into a virtualenv::

    virtualenv -p python2.7 --no-site-packages commons_site

Activate the virtualenv::

    cd commons_site
    source bin/activate

Pull all the package dependencies::

    cd commons_project
    pip install --requirement requirements.txt

Initialize the local DB (locally we use sqlite). This will prompt you to create
a superuser in the DB, so say 'yes'.::

    ./manage.py syncdb
    ./manage.py migrate

Gather all static resources::

    ./manage.py collectstatic

Run the local instance::

    ./manage.py runserver

Here is how to deploy to ep.io::

    First, if you are not a member of the Civic Commons team, change the app
    name in .epio-app to one you control.

    We recommend that all of the following steps be done on each deployment,
    and that a deployment only be done after pulling (and if necessary,
    merging) the latest version and pushing your own changes to the repository.
    
    ./manage.py collectstatic
    epio upload
    epio django syncdb
    epio django migrate
    
If this is a new instance of the commons web app, you will be prompted to
create a superuser. If it is an existing app, here is how to add an additional
superuser on ep.io from the command-line::
    
    epio django createsuperuser

NOTE: If you create a superuser by this method, you will break the site until
you log into the admin interface (at /admin) and add a Profile for that user.
All users (other than the AnonymousUser) must have a profile.
