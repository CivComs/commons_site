Installation
============

Here is how to pull and build a local copy of the system::

    git clone git://github.com/CivComs/commons.git
    virtualenv -p python2.7 --no-site-packages commons
    cd commons
    source bin/activate
    cd commons
    pip install --requirement requirements.txt
    ./manage.py syncdb
    ./manage.py migrate commons

Here is how to deploy to ep.io::

    epio upload
    epio django syncdb
    epio django migrate commons
