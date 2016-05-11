import csv
import urllib2
from bs4 import BeautifulSoup

new_rows_list = []

with open('joco.csv', 'rb') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='"')

  #with open('joco_content.csv', 'wb') as new_csv:
  #  writer = csv.writer(new_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

  for row in reader:
    
    print "URL: " + row[0]

    f = urllib2.urlopen( row[0] )
    html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    print "Title"
    print soup.title

    title = ""
    if soup.title is not None:
      title = str(soup.title)
      title = title.replace('<title>', '')
      title = title.replace('</title>', '')
      title = title.strip()
 
    print "Getting h1"
    print soup.find_all('h1')

    h_one = ""
    if soup.find_all('h1'):
      h_one = soup.find_all('h1')[0]

    print "Getting h2"
    print soup.find_all('h2')
 
    h_two = ""
    if soup.find_all('h2'):
      h_two = soup.find_all('h2')[0] 

    new_rows_list.append( [row[0], title, h_one, h_two] )

  csvfile.close()

new_file = open('joco.csv', 'wb')
writer = csv.writer(new_file)
writer.writerows(new_rows_list)
new_file.close()
