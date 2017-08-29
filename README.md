# wolframalphaapi

wolframalphaapi is a Python wrapper for the Wolfram|Alpha APIs, mainly for Spoken Result API and Short Answers API.


## Installation


With pip::

    $ pip install wolframalphaapi

or easy_install::

    $ easy_install wolframalphaapi


## Dependencies


wolframalphaapi requires the `requests <https://pypi.python.org/pypi/requests>`_ package.


## Usage


In test.py, replace the key value with your Wolfram|Alpha API key, then run:

	python test.py

This uses spoken_results method to get a text string from the Spoken Result API. If no result get, it will try the Short Answers API automatically. These APIs are free to use for up to 2,000 calls per month. For speech_recognition and full_results, you will need to upgrade your Wolfram|Alpha API Key.


For a complete overview of the APIs, please refer to the [Wolfram|alpha API Documentation](https://products.wolframalpha.com/spoken-results-api/documentation/)
