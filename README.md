# DM-Assignment-1_SOFE4620U

In this assignment, the objective was to scrape data from a website, and export that data into either a CSV or JSON file or as a MongoDB database.


## Description

For my assignment,I scraped data from the UOIT.ca website, more related to the events that happened in 2017 from `events.uoit.ca`.Once I scraped the data, I exported it as a CSV file called `uoit-events.csv`.

## Setup (Repository and dependencies)
```sh
    git clone git@github.com:Varun-Gopikrishna/DM-Assignment-1.git
    cd DM-Assignment-1

    virtualenv venv
    source venv -r requirements.txt
```
Once this is done, you should be all set to run the scraping code and get the .csv file.

## Folder Structure
```
───DM-Assignment-1
|   |   setup.py
|   |   README.md
|   |   requirements.txt
│   └───venv
|   |
│   └───scrape-assigment
|       |   __init__.py
│       └───api-scrape
|           |   
|           |   scrape.py
|           |   __init__.py
│           └───uoit-events.csv
```
## Scraping and export data to a csv file
```
cd scrape-assignment/api-scrape/
python3 scrape.py
```
This should scrape the data from `events.uoit.ca`, then export it into a csv file, `uoit-events.csv`. 





