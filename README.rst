Django Pipeline Handlebars
==========================

django-pipeline-handlebars is a compiler for `django-pipeline <https://github.com/cyberdelia/django-pipeline>`_.

This compiler will produce a JS using the widely used JST model.

It basically compiles and appends to the window.JST JSON array the template that you request (through django-pipeline) using for example `Backbone.js <https://github.com/documentcloud/backbone>`_ or `Spine.js <https://github.com/maccman/spine>`_
.

Installation
~~~~~~~~~~~~
Add repository url to your requirements or buildout.cfg, then run
.. code-block:: sh
    pip install -r requirements
or
.. code-block:: sh
    buildout

Add these lines in your django `settings.py`:

.. code-block:: python

    PIPELINE_JS = {
        'application': {
            'source_filenames': (
            	# Your other JS files...
                'path/to/your/templates/*.hbs',#save your handlebars templates with hbs extension
            ),
            'output_filename': 'js/application.js'
        }
    }

    PIPELINE_COMPILERS = (
        'pipeline_handlebars.compiler.HandlebarsCompiler',
    )

Usage
~~~~~
If the paths are set correctly (try to play a bit depending on your static files situation), the handlebars templates will be compiled in a JS file and included automatically by pipeline.


Inspired by
~~~~~~~~~~~~~~~~~~
* `django-pipeline-eco <https://github.com/vshjxyz/django-pipeline-eco>`_ (eco compiller for pipeline)