Google Analytics Auto-script
==================================
This script checks the Google Analytics account and returns a printable PDF with the relevant data. For now, it works with Social and E-mail Campaigns reports.

To run:

You need to get your 'client_secrets.json' first! [here](http://www.marinamele.com/use-google-analytics-api-with-python) is a very good tutorial of how to get it.

Fist, you need to install the following packages:

    $ sudo apt-get install python-dev libjpeg-dev zlib1g-dev virtualenv

Create a new virtual environment and install the dependencies

    $ virtualenv env
    $ source env/bin/activate
    (env) $ pip install -r requirements.txt
    (Installing)

To run all the scripts: 

    (env) $ python main.py

To run only one script:

    (env) $ python get_mail.py

And that's it.

Note:
=====
Ignore the "from private_data import profile_id" parts, that's the file where I get my profile's id. You should replace that with your own profile id.
