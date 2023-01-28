# downloading pkl model file from GCP's cloud_storage service node
# to be able to use here in GCP's app_engine service node
import pickle
from google.cloud import storage
storage_client = storage.Client()
bucket = storage_client.get_bucket('model-bucket-iris-sk')
blob = bucket.blob('Iris_SV_Classfier.pkl')
blob.download_to_filename('/tmp/Iris_SV_Classfier.pkl')
model = pickle.load(open('/tmp/Iris_SV_Classfier.pkl', 'rb'))


#
import requests 
def predict(request):
    if request.method == 'GET':
        return 'please send post request!'
    elif request.method == 'POST':
        input_paras = request.get_json()
        
        sepal_length = input_paras['sepal_length']
        sepal_width = input_paras['sepal_width']
        petal_length = input_paras['petal_length']
        petal_width = input_paras['petal_width']
        
        import numpy as np
        input = np.array([[sepal_length, sepal_width, petal_length, petal_width]]) 
        # so basically this 2d array in input ka mutlib ye hai ki, this 1d array in [] is nothing
        # but a row, being passed for prediction to model
        
        prediction = model.predict(input)
        return str(prediction)