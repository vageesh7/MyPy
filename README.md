# Python scripts

Assortment of scripts that run on the Pycharm studio to create/update/delete of Employee records using MongoDB on Windows.


## Description

### `Records.py`
For a given user input, this script goes through the user_collection table in the MongoDB for each 'name'. if the 'name' doesnt exist, a new record will be created and will ask the user whether the details needs to be modified if the 'name' exists. 

Similarly, The record will be deleted based on the user input and displays the current record details. 

## Installation

**Windows**: You will need to install one of the 3.x versions available at [python.org](http://www.python.org/getit/).
**PyCharm**: You will need to install one of the latest versions (2018) available at (https://www.jetbrains.com/pycharm/download/#section=windows)
**MongoDB**: You will need to install one of the 3.x versions or current release available at (https://www.mongodb.com/download-center/community)


## Dependencies

Some of the scripts may require additional Python packages or depend on certain tools being installed and appropriately configured to run on the MongoDB. 
**pymongo**: You need to install pymongo drivers/packages either externally through open source or internally via pycharm package installer. 


## General usage information

1. Download the [ZIP package]() and unzip it.
2. 
 * the script will run by simply typing `python ` followed by the file name of the script, e.g. `python theScript.py`.
 * If the script is in a different directory from which you are trying to run it, you will need to provide the full path to the script’s file, e.g. `python /Users/myself/foldername/theScript.py`.
