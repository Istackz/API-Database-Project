import json
from urllib import urlopen
import sqlite3

#Issac Rodriguez sprint 2
#Take api and put data into SQL database table
#Page 4
conn=sqlite3.connect('GithubJobs.db')
c=conn.cursor()

def loading():
    url = 'https://jobs.github.com/positions.json?page=4'  # URL for API 1-5json_obj = urllib.urlopen(url)
    response = urlopen(url)
    data = json.load(response)  # loads the url and set it into data variable

    for item in data[0].keys():
        return data  # Get the keys

def createDB(data):
    conn = sqlite3.connect('GithubJobs.db')
    c = conn.cursor()
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS comp
        (description text primary key, title text ,url text,compnay_logo text, company text ,id text ,company_url text,how_to_apply text, location text, type text ,created_at timestamp
        )''') #company, compnay_logo text ,company_url text,created_at timestamp,description,how_to_apply text ,id text,location text,title text,type text ,url text 
    temp_values = list(tuple())
    for item in data:
        list_of_values = [v for k, v in item.items()]
        tuple_of_values = tuple(list_of_values)
        temp_values.append(tuple_of_values)


    c.executemany('INSERT INTO comp VALUES (?,?,?,?,?,?,?,?,?,?,?)', temp_values)
    conn.commit()
    print("Table Sucessfull! page 4")

def ParseData():
    c.execute(""" SELECT * FROM comp """)
    data=c.fetchall
    for row in data(): #automated test to show data being stored in database
        print(len(row)) #automated test to show how many rows in database stored 
        print("Rows Sucessfully stored in Database")

def main():
    data = loading()
    createDB(data)

main()
ParseData()

