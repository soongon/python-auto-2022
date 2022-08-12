import requests

headers = {
    'X-Naver-Client-Id': 'qETZsbwJwM9t9UgHth18',
    'X-Naver-Client-Secret': 'fNyQreU2jy',
}

text = '''
In his first public statement since federal agents searched 
former President Donald Trump's home at Mar-a-Lago earlier this week, 
Attorney General Merrick Garland on Thursday said that the Justice Department had filed 
in court a request that the search warrant and property receipt from the search be unsealed.
'''

data = {
    'source': 'en',
    'target': 'ko',
    'text': text,
}

res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)

print(res.text)