# API-Database-Project
# ISSAC RODRIGUEZ , Sprint 1 (JsonJobs.py)
# This program takes the API for 5 different pages and prints out all the data into a log.txt file
# Two automated tests one to show how many entries were found in each page & the second to locate a specfic job in log.txt
# calls each API in an array varaible data[]
# imports needed are import json from urllib import urlopen import subprocess import sys
------------------------------------------------------------------------------------------------------------------
# ISSAC RODRIGUEZ, Sprint 2
# Sprint 2 code is located all and only in the file "SQLDataEntry(1-5).py"
# This code takes the github API Jobs and creates an SQL Database table.
# It Calls each key in the API into a seperate collumn
# Imports needed are: from json import load, import urllib ,import sqlite3   
# Automated tests check how many data entries were in each API page & Checks to see if a specic job is found in database
------------------------------------------------------------------------------------------------------------------------
# ISSAC RODRIGUEZ , Sprint 3
# Sprint 4 is located in the GeoMap.py & GITHUB.py (CSV.py is not needed to run the code needed for sprint 4)
# GeoMap.py takes all of the jobs from stacksoverflow & Github raw CSV file and plots them using plotly
# This code also opens up a github csv file to search for the jobs in the ploty map
# Csv.py was used to create csv files from the data taken by the two sites, It is not needed to run the code.
# Imports needed for this code are: import pandas as pd , import webbrowser , import plotly.express as px
# The jobs cannot be constantly up to date so it grabs from the latest time the csv file was made.
# Both Files from both sites were then merged together in excel to have Github.py read from one data source
# The Fulltime/partime for Stacksoverflowfeed was not taken when pulling the data so it is set as N/A
# Was unable to make the data taken from both sites stay up to date for each new day.
------------------------------------------------------------------------------------------------------------------
