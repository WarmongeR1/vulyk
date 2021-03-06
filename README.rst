Crowdsourcing platform for various tasks
========================================

.. image:: https://badge.fury.io/py/vulyk.png
    :target: http://badge.fury.io/py/vulyk

.. image:: https://travis-ci.org/mrgambal/vulyk.png?branch=master
        :target: https://travis-ci.org/mrgambal/vulyk

.. image:: https://readthedocs.org/projects/vulyk/badge/?version=latest
        :target: https://vulyk.readthedocs.org/en/latest/


License
-------

-  Free software: BSD license
-  Documentation: https://vulyk.readthedocs.org.

What is it?
-----------

We have a lot of tasks that can only be done manually. 
Those includes digitizing of scanned assets declarations, 
manual verification of results produced by different NLP software, stalking and so on.
So, we decided to generalize those tasks a bit and build a platform with basic support for crowdsourcing using
knowledge and chunks of code from the `unshred.it <http://unshred.it>`__
project. We don't use anything extraordinary: Flask, MongoDB, Bootstrap,
jQuery etc (all trademarks are the property of their respective owners,
don't forget that).

How it's build
--------------

Vulyk itself is a platform that can be stuffed with various plugins (check `this <https://github.com/hotsyk/vulyk-tagging/>`__ `two <https://github.com/hotsyk/vulyk-declaration>`__ for example).

Vulyk providing basic facilities to manage tasks, users, has simple but effective system of groups and permissions, also can load tasks in format of json lines and export results. For admin purposes we have a nice (not really) CLI tool that gives admin an access to users management, tasks management, results management, stats, etc.

Vulyk is also doing dirty job to collect assets for plugin, to provide registration/login via social networks for end users and has leaderboard.


What for?
---------

-  digitize assets declarations of ukrainian officials for `Declarations project <http://declarations.com.ua>`__
-  improve the current state of Ukrainian NLP by creating a simple and
   robust solution for various NLP tasks that require human input.
-  process and manually verify existing results from
   `PullEnti <http://pullenti.ru>`__ (by Konstantin Kuznetsov) and
   morphological analyzer (by Andriy Rysin, Mariana Romanyshyn, et al.).
-  build tagged corpora of different kinds using manually processed
   results.
-  for the sake of The Great Justice of course!

But, God, how?
--------------

We provide some kind of playground where any interested (or
procrastination-addicted) person could spent some time doing some manual tasks. 
Site will show you, mr. Solver, some tasks of a given type, which you'll need to solve

In the best case we'll add some gamification (badges, achievement... you
name it).

Leaderboard is already in place!

How could I participate?
------------------------

You just need to contact me mr_gambal@outlook.com or `@dchaplinsky <http://github.com/dchaplinsky>`__ via
chaplinsky.dmitry@gmail.com. One day we'll find one brave heart who'll
create a list of issues so the process will be simplified. But not now...

Running it locally
------------------
You'll need MongoDB, Python 2.7 and virtualenv and with little bit of instructions you'll be able to run the Beast (with two real plugins)!

First of all, check out all required components:

.. code:: bash

    mkdir vulyk
    git clone https://github.com/mrgambal/vulyk.git
    git clone https://github.com/hotsyk/vulyk-declaration.git
    git clone https://github.com/hotsyk/vulyk-tagging.git

Then create virtual environment and install all three of them there in editable mode (unfortunatelly we don't have any of them released on pypi yet)

.. code:: bash

    mkdir sandbox
    cd sandbox
    virtualenv venv && source venv/bin/activate
    pip install -e ../vulyk
    pip install -e ../vulyk-declaration
    pip install -e ../vulyk-tagging


Then let's set things up. Edit local_settings.py and add some stuff into it:

.. code:: python

    # This one only works to log in via http://localhost:5000
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

    # This one works for both, http://localhost:5000 and http://127.0.0.1:5000
    SOCIAL_AUTH_TWITTER_KEY = ''
    SOCIAL_AUTH_TWITTER_SECRET = ''

    # This one only works to log in via http://localhost:5000
    SOCIAL_AUTH_FACEBOOK_KEY = ''
    SOCIAL_AUTH_FACEBOOK_SECRET = ''

    # This one only works to log in via http://localhost:5000
    SOCIAL_AUTH_VK_OAUTH2_KEY = ''
    SOCIAL_AUTH_VK_OAUTH2_SECRET = ''


    MONGODB_SETTINGS = {
        'DB': "vulyk",
    }

    ENABLED_TASKS = {
        'vulyk_declaration': 'DeclarationTaskType',
        'vulyk_tagging': 'TaggingTaskType',
    }

You'll need to register you localhost app in one of social networks (and fill corresponding credentials in local_settings.py!) to make it work locally.

Then you should be able to init the app using CLI, load some tasks and run it locally.

.. code:: bash

    cp `which manage.py` .  # FUgly, I know!
    python ./manage.py  init declaration_task tagging_task
    
That'll create default user group and give users of this group an access to two task types that we've installed before.

Then:

.. code:: bash

    python ./manage.py db load declaration_task --batch 01_declaration decl_tasks.json
    python ./manage.py db load tagging_task --batch 01_tagging tagging_tasks.json

And finally you should create run.py and put some stuff into it:

.. code:: python

    from vulyk.app import app

    if __name__ == '__main__':
        app.run()


.. code:: bash

    python run.py
    
Then open http://localhost:5000 and you are set!

Easy, isn't it?! Well, we'll smoothen some rough edges soon, we promise.
