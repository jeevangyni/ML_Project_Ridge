## Created this in as there is an error in downloading the California Dataset 
# from sklearn as it asks for the verification of the url

import requests
import os

url = 'https://ndownloader.figshare.com/files/5976036'
response = requests.get(url, verify=False)
with open(os.path.expanduser('~/scikit_learn_data/cal_housing.tgz'), 'wb') as f:
    f.write(response.content)