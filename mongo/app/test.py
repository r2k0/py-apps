import csv
from datetime import datetime
import pymongo

def testMongo():
  """ to test mongodb connection and pymongo """
  client = pymongo.MongoClient("localhost",27017)
  db = client.test
  print (db.name)
  print (db.my_collection)

def parse(raw_file, delimiter):
  """ 
    parses CSV file
    input: raw_file, delimiter
    output: parsed data
  """
  csvfile = open(raw_file,'r')
  csv_data = csv.reader(csvfile, delimiter=delimiter)

  pdata = []
  keys = csv_data.next()
  for items in csv_data:
    pdata.append(dict(zip(keys,items)))
  csvfile.close()
  return pdata

def main():
  spy_data = parse("spy_2013.csv",",")
  print(spy_data)
  testMongo()

if __name__ == "__main__":
  main()
	 
