import json
from urllib import urlopen
import sqlite3

#Issac Rodriguez sprint 2
#Take api and put data into SQL database table
#Page 4

def loading():
    url = 'https://jobs.github.com/positions.json?page=4'  # URL for API 1-5json_obj = urllib.urlopen(url)
    response = urlopen(url)
    data = json.load(response)  # loads the url and set it into data variable

    for item in data[0].keys():
        return data  # Get the keys

def createDB(data):
    conn = sqlite3.connect('SQLTABLE.db')
    c = conn.cursor()
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS comp
        (id text primary key, type text, url text,created_at timestamp, company text, company_url text, location text, title text, description text, how_to_apply text, company_logo text
        )''')
    temp_values = list(tuple())
    for item in data:
        list_of_values = [v for k, v in item.items()]
        tuple_of_values = tuple(list_of_values)
        temp_values.append(tuple_of_values)


    c.executemany('INSERT INTO comp VALUES (?,?,?,?,?,?,?,?,?,?,?)', temp_values)
    conn.commit()
    print("Table Sucessfull! page 4")

def main():
    data = loading()
    createDB(data)



main()