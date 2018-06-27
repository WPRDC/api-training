# API Wizardry
#### A Crash Course in Using Web APIs

## Quick Start Brick Stacking
To start the Quick Start notebook, first click this button: [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/WPRDC/api-training/master)
and then click on the `quick-trick-brick-stack.ipynb` notebook file to start it.

The Jupyter notebook has code cells and documentation cells. When you first open a Jupyter notebook, none of the code has been run (though you may see the saved output from previous runs). Click on a cell to select it. Use shift-return to execute the code or just the return key to edit the code. You can also run all the code cells by choosing "Run all" under the "Cells" menu.

[Here's](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Jupyter_Notebook_Cheat_Sheet.pdf) a cheat sheet for using Jupyter notebooks, and [here's](https://medium.com/codingthesmartway-com-blog/getting-started-with-jupyter-notebook-for-python-4e7082bd5d46) a brief tutorial.

## Cat API
This is a simple example to demonstrate how `requests` works and how to make `GET` requests.

To start this notebook, first click this button: [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/WPRDC/api-training/master)
and then click on the `cat_api.ipynb` notebook file to start it.

## Pizza API
In this notebook, you will use an API to:
* Find the nearest Domino's Pizza.
* Explore its menu
* Send an order to that store.
* Track the order as it's delivered to you.

To start this notebook, first click this button: [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/WPRDC/api-training/master)
and then click on the `pizza.ipynb` notebook file to start it.

Thanks to [RIAEvangelist](https://github.com/RIAEvangelist) for compiling all of this information 
into a [node tool](https://github.com/RIAEvangelist/node-dominos-pizza-api) for ordering pizza.

## Pizza tracker
This short notebook, is a slightly modified copy of the last few cells of the Pizza API notebook.
In it, you can run a loop that will check the status of a pizza order every 3 seconds. 

To start this notebook, first click this button: [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/WPRDC/api-training/master)
and then click on the `pizza-tracker.ipynb` notebook file to start it.

## Port Authority TrueTime API
In this notebook, you will:
* Look up a bus stop
* Get predicted arrival times for the next bus coming to that bus stop
* Display the bus and the bus stop on a web map

To start the Port Authority TrueTime notebook, first click this button: [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/WPRDC/api-training/master)
and then click on the `port-authrority-examples.ipynb` notebook file to start it.

This API requires an API key which you can get on their [TrueTime website](http://truetime.portauthority.org/bustime/login.jsp).  You will need to create an account and request an API key from them. 
Once you have an account, you can log in and browse the documentation.

We use a local settings file in this example to protect our secret API key.
See [Using your own settings file](#using-your-own-settings-file), to see how to make your own.
Or you can simply supply your own API key in the code per the instructions in the notebook.


## Other Things to Try
Click this button to access all our sample notebooks: [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/WPRDC/api-training/master)

### Ideas Using WPRDC Datasets 
* [Right-of-way Requests](https://data.wprdc.org/dataset/right-of-way-permits) ⇒ Post notification of road closures delivered to Reddit
* [Arrests](https://data.wprdc.org/dataset/arrest-data)/[Non-traffic citations](https://data.wprdc.org/dataset/non-traffic-citations)/[Police blotter](https://data.wprdc.org/dataset/police-incident-blotter) (updates daily) ⇒  Daily crime report for your neighborhood by Twitter
* [Fire incidents](https://data.wprdc.org/dataset/fire-incidents-in-city-of-pittsburgh) (updates daily) ⇒  Notification of all of yesterday's five-alarm fires in Pittsburgh
* [BigBurgh Social Services Listings](https://data.wprdc.org/dataset/bigburgh-social-service-listings) (updates monthly) ⇒  Post local social services and relevant events to Reddit
* [311 Data](https://data.wprdc.org/dataset/311-data) (updates every 10 minutes) ⇒  Look for spikes in Snow/Ice removal requests and send yourself dangerous-road-conditions text messages
* [311 Data](https://data.wprdc.org/dataset/311-data) (updates every 10 minutes) ⇒ Generate Spotify list inspired by recent 311 complaints
* [Library locations + hours of operation](https://data.wprdc.org/dataset/libraries) ⇒  Send complementary pizzas to a random library location if it's open.
* [City-Wide Revenues and Expenses](https://data.wprdc.org/dataset/city-revenues-and-expenses) ⇒  Build a budget ticker that shows how much the city of Pittsburgh government spent each day.

## Tools
- [JSON viewer extension for Chrome](https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh?hl=en-US)
- [Postman](https://www.getpostman.com/) - graphical interface for exploring APIs
- [curl](https://curl.haxx.se/) - command line interface for making HTTP requests
- [requests](http://docs.python-requests.org/en/master/) - python library making HTTP requests
- [fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) - JS methods for making HTTP requests


## Popular Web APIs

- [CKAN API documentation](http://docs.ckan.org/en/latest/api/index.html)
  * [WPRDC CKAN instance](https://data.wprdc.org) (where you can get lots of open data)
  * [Python wrapper for CKAN API](https://github.com/ckan/ckanapi)
  * [R wrapper for CKAN API](https://github.com/ropensci/ckanr)
- [Port Authority TrueTime](http://truetime.portauthority.org/bustime/login.jsp) - you need to make an account to see documentation
- [Spotify API homepage](https://developer.spotify.com/)
  * [Documentation](https://developer.spotify.com/documentation/)
  * [API Console](https://developer.spotify.com/console/)
- [Twilio API Documentation](https://www.twilio.com/docs/)
- [Reddit API Documentation](https://old.reddit.com/dev/api) - they haven't updated with their design changes, but it should still work
  * [r/redditdev](https://www.reddit.com/r/redditdev/) - subreddit for people using reddit API
- [Twitter API Documentation](https://developer.twitter.com/en/docs.html)
- [World Cup API](https://worldcup.sfg.io) - made by someone on HackerNews


## Online Resources
- [WPRDC](https://www.wprdc.org)
- [Mozilla's HTTP overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [OAuth 2.0 Docs](https://oauth.net/2/)
- [REST Wikipedia article](https://en.wikipedia.org/wiki/Representational_state_transfer) - a special class of web APIs


## Using Your Own Settings File
For several notebooks, we use a local settings file called `settings.py` to hide our secret information during demonstartions.
You can easily make your own by renmaing `settings-example.py` to `settings.py` and changing our fake values to your real values.

In a Jupyter notebook, you can rename it by selecting the checkbox to the left of `settings-example.py` and clicking the `Rename` button in the toolbar.  You can then enter your own information into that file and you'll be good to go!

In macOS and linux terminals, you can use the command below, or simple rename it like you would any other file.
```bash
mv settings-example.py settings.py
```

The settings file is full of comments explaining what each variable is and how to go about changing it.
