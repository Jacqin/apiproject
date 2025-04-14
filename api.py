import requests
import json

response=requests.get('https://catfact.ninja/fact')

if response.status_code==200:

    facts= response.json()

    for fact in facts:
        print(facts[fact])
    print('The number above is the length in charecters of the fact.')

else:
    print('Sorry we cant produce an output')