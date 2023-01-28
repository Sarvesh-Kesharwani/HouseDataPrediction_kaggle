import requests
import numpy as np
url = "http://127.0.0.1:5000/predict"
data = {"sepal_length" : 10,
        "sepal_width" : 0.1,
        "petal_length" : 0,
        "petal_width" : 10
        }

# data = np.array(data)
# print(data)

response = requests.post(url, json = data)
print(response)
print(response.text)


