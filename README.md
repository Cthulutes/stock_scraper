# Stock Scraper

## Table of Contents
* [Requirements](#requirements)
* [Installation](#installation)
* [Configuration](#configuration)
* [Usage](#usage)

<a name="requirements"></a>
## Requirements
This module was built on python 3.5.2 but should work with any version of Python 3

<a name="installation"></a>
## Installation
To install required modules run:
```bash
$ python -m pip install -r requiements.txt
```

<a name="configuration"></a>
## Configuration
There are three main configuration variables that can be found in **app.py**

Variables:
* *POLLING*: An integer that determines how often (in ms) the store pages are checked
* *WEBPAGES*: A list of tuples that identify the store pages to check. Each list entry is a tuple of the form ('**STORE NAME**', '**STORE_URL**'). The **STORE_NAME** is how the item will appear on the webpage when loaded
* *KEYWORDS*: A list of keyword that will be checked on each page to determine if the item is in stock. This set will be checked on *every* page indiciated by WEBPAGES. Spelling and Case **DO** matter. Some starter key-words are already listed for the following sites
    * B&H
    * Amazon
    * Newegg
    * Best Buy

<a name="usage"></a>
## Usage 
To launch the webserver run the following from a command line:
```bash
$ python app.py
```

Once launched, the page can be loaded at http://localhost:5000