import csv
import collections
import httplib2
from URL import URL


# Define list to store data directly from list
url_data = collections.defaultdict(set)

# Define list to store objects of URLs
urls = []

# Define source data file and reader
data_file = open('data.csv', 'r')
my_reader = csv.reader(data_file)

# Put from csv file into list
for row in my_reader:
    url_data[row[0]].add(row[1])

# Form objects from data and put into list
for url in url_data:
    print(url, "-->", url_data[url])
    new_url = URL(url, url_data[url])
    urls.append(new_url)


# for url in url_data:
#     connection = httplib2.HTTPConnectionWithTimeout('google.com')
#     connection.request("HEAD", '')
#     print(connection.getresponse().status)
