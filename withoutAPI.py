def KMP_String(pattern, text):
    a = len(text)
    b = len(pattern)
    prefix_arr = get_prefix_arr(pattern, b)
  
    initial_point = 0
    m = 0
    n = 0
  
    while m != a:
       
        if text[m] == pattern[n]:
            m += 1
            n += 1
      
        else:
            n = prefix_arr[n-1]
       
        if n == b:
            initial_point+=1
            n = prefix_arr[n-1]
        elif n == 0:
            m += 1   
    return initial_point

def get_prefix_arr(pattern, b):
    prefix_arr = [0] * b
    n = 0
    m = 1
    while m != b:
        if pattern[m] == pattern[n]:
            n += 1
            prefix_arr[m] = n
            m += 1
        elif n != 0:
                n = prefix_arr[n-1]
        else:
            prefix_arr[m] = 0
            m += 1
    return prefix_arr

import requests
import csv

with open('test.csv', newline='') as csvfile:
  data = csv.DictReader(csvfile)
  for row in data:
    src_ip=row['src_ip']
    x=requests.get('https://www.abuseipdb.com/check/'+src_ip)
    response_txt = x.content
    txt = response_txt.decode('utf-8')
    pat = "has been reported a total"
    initial_point = KMP_String(pat, txt)
    if initial_point > 0:
        print(src_ip + " is abused")