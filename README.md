# API Wizardry
## A Crash Course in Using Web APIs

### Quick Start Brick Stacking
To start the Quick Start notebook, first click this button: [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/WPRDC/api-training/master)
and then click on the quick-trick-brick-stack notebook file to start it.

The Jupyter notebook has code cells and documentation cells. When you first open a Jupyter notebook, none of the code has been run (though you may see the saved output from previous runs). Click on a cell to select it. Use shift-return to execute the code or just the return key to edit the code. You can also run all the code cells by choosing "Run all" under the "Cells" menu.

[Here's](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Jupyter_Notebook_Cheat_Sheet.pdf) a cheat sheet for using Jupyter notebooks, and [here's](https://medium.com/codingthesmartway-com-blog/getting-started-with-jupyter-notebook-for-python-4e7082bd5d46) a brief tutorial.

### Port Authority TrueTime API
In this notebook, you will:
* Look up a bus stop
* Get predicted arrival times for the next bus coming to that bus stop
* Display the bus and the bus stop on a web map

To start the Port Authority TrueTime notebook, first click this button: [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/WPRDC/api-training/master)
and then click on the port-authrority-examples notebook file to start it.

This API requires an API key which you can get on their [TrueTime website](http://truetime.portauthority.org/bustime/login.jsp).  You will need to create an account and request an API key from them. 
Once you have an account, you can log in and browse the documentation.

We use a local settings file in this example to protect our secret API key.
See [Using your own settings file](#using-your-own-settings-file), to see how to make your own.
Or you can simply supply your own API key in the code per the instructions in the notebook.


### Other Things to Try
Click this button to access all our sample notebooks: [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/WPRDC/api-training/master)

#### Ideas Using WPRDC Datasets 
* [Right-of-way Requests](https://data.wprdc.org/dataset/right-of-way-permits) ⇒ Post notification of road closures delivered to Reddit
* [Arrests](https://data.wprdc.org/dataset/arrest-data)/[Non-traffic citations](https://data.wprdc.org/dataset/non-traffic-citations)/[Police blotter](https://data.wprdc.org/dataset/police-incident-blotter) (updates daily) ⇒  Daily crime report for your neighborhood by Twitter
* [Fire incidents](https://data.wprdc.org/dataset/fire-incidents-in-city-of-pittsburgh) (updates daily) ⇒  Notification of all of yesterday's five-alarm fires in Pittsburgh
* [BigBurgh Social Services Listings](https://data.wprdc.org/dataset/bigburgh-social-service-listings) (updates monthly) ⇒  Post local social services and relevant events to Reddit
* [311 Data](https://data.wprdc.org/dataset/311-data) (updates every 10 minutes) ⇒  Look for spikes in Snow/Ice removal requests and send yourself dangerous-road-conditions text messages
* [311 Data](https://data.wprdc.org/dataset/311-data) (updates every 10 minutes) ⇒ Generate Spotify list inspired by recent 311 complaints
* [Library locations + hours of operation](https://data.wprdc.org/dataset/libraries) ⇒  Send complementary pizzas to a random library location if it's open.
* [City-Wide Revenues and Expenses](https://data.wprdc.org/dataset/city-revenues-and-expenses) ⇒  Build a budget ticker that shows how much the city of Pittsburgh government spent each day.

### Tools
- [JSON viewer extension for Chrome](https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh?hl=en-US)



### Popular Web APIs

- [CKAN API documentation](http://docs.ckan.org/en/latest/api/index.html)
  * [WPRDC CKAN instance](https://data.wprdc.org) (where you can get lots of open data)
  * [Python wrapper for CKAN API](https://github.com/ckan/ckanapi)
  * [R wrapper for CKAN API](https://github.com/ropensci/ckanr)


### Using Your Own Settings File
For several notebooks, we use a local settings file called `settings.py` to hide our secret information during demonstartions.
You can easily make your own by renmaing `settings-example.py` to `settings.py` and changing our fake values to your real values.

In macOS and linux terminals, you can use the command below, or simple rename it like you would any other file.
```bash
mv settings-example.py settings.py
```

The settings file is full of comments explaining what each variable is and how to go about changing it.