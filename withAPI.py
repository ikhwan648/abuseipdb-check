# output = []

# f = open( 'test.csv', 'rU' ) #open the file in read universal mode
# for line in f:
#     cells = line.split( "," )
#     output.append( ( cells[ 0 ], cells[1], cells[2]) ) #since we want the first, second and third column

# f.close()

# print(output)

# import csv
 
# # opening the CSV file
# with open('test.csv', mode ='r')as file:
   
#   # reading the CSV file
#   csvFile = csv.reader(file)
 
#   # displaying the contents of the CSV file
#   for lines in csvFile:
#         print(lines)
import csv
import requests
import json

with open('test.csv', newline='') as csvfile:
  data = csv.DictReader(csvfile)
  for row in data:
    src_ip=row['src_ip']
    url = "https://api.abuseipdb.com/api/v2/check?ipAddress="
    headers = {"Key": " ", "Accept": "application/json"}
    response = requests.get(url+src_ip, headers=headers)
    x = response.json()
    abusedScore = x['data']['abuseConfidenceScore']
    if abusedScore > 50:
      print(src_ip + " is abused")
