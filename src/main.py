import csv
import collections
import httplib2
from URL import URL
import urllib.request

from SrcubOrigUrls import scrub_orig_urls

# Define list to store data directly from list
url_data = collections.defaultdict(set)

# Define list to store objects of URLs
urls = []

# Define source data file and reader
url_data_file = open('data.csv', 'r')
my_reader = csv.reader(url_data_file)

# Put from csv file into list
print("Getting data from file...")
for row in my_reader:
    url_data[row[0]].add(row[1])

print("Done getting data from file!")
# Form objects from data and put into list
print("Putting objects in list...")
for url in url_data:
    new_url = URL(url, url_data[url])
    urls.append(new_url)
print("Done putting objects in list!")
del urls[0]
scrub_orig_urls(urls)