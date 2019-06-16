import json
import requests

d = {"nginx":
         {"Time taken for tests": "2.315",
          "Requests per second": "43187.61",
          "Time per request": "1.158",
          "Time per request(all)": "0.023",
          "Transfer rate": "35889.22"},
     "httpd": {"Time taken for tests": "2.315",
               "Requests per second": "43187.61",
               "Time per request": "1.158",
               "Time per request(all)": "0.023",
               "Transfer rate": "35889.22"}

     }

requests.post(url,d)
print(d.keys())
