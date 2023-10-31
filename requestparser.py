import requests
import json
from urllib.parse import urlparse
from urllib.parse import parse_qs


def getResponses(valid_auth_tokens, request):
    result= []
    for req in request:
        if req[0] == 'GET':
            url = req[1]
            parsed_url = urlparse(url)
            try:
                token = parse_qs(parsed_url.query)['token'][0]
                if token not in valid_auth_tokens:
                    result.append("Invalid")
                    continue
                # get other parameters
                params = parse_qs(parsed_url.query)
                params.pop('token')
                s=""
                s+="Valid"+","
                for key, value in params.items():
                    
                    s+=key+","+value[0]+","
                result.append(s[0:-1])
            except:
                result.append("Invalid")
                continue
         
        elif req[0] == 'POST':
            url = req[1]
            parsed_url = urlparse(url)
            try:
                token = parse_qs(parsed_url.query)['token'][0]
                csrf=parse_qs(parsed_url.query)['csrf'][0]
                if token not in valid_auth_tokens or not valid_csrf_tokens(csrf):
                    result.append("Invalid")
                    continue
                
                # get other parameters
                params = parse_qs(parsed_url.query)
                params.pop('token')
                params.pop('csrf')
                s=""

                # result.append('Valid')
                s+="Valid"+","
                for key, value in params.items():
                    s+=key+","+value[0]+","
                result.append(s[0:-1])
            except:
                result.append("Invalid")
                continue
            
    return result


def getter(url,valid_auth_tokens):
    # url = 'https://example.com/?token=et51u8i9p1q7&id=2e3rt&name=alex'   
    parsed_url = urlparse(url)
    token = parse_qs(parsed_url.query)['token'][0]
    if token not in valid_auth_tokens:
        print("Invalid")
        return 
    # get other parameters
    params = parse_qs(parsed_url.query)
    params.pop('token')
    # print key value pairs
    print('Valid',end=' ')
    for key, value in params.items():
        print(key, value[0], end=' ')
    print()

def poster(url, valid_auth_tokens):
    result=[]
    parsed_url = urlparse(url)
    token = parse_qs(parsed_url.query)['token'][0]
    csrf=parse_qs(parsed_url.query)['csrf'][0]
    if token not in valid_auth_tokens or not valid_csrf_tokens(csrf):
        print("Invalid")
        return 
    
    # get other parameters
    params = parse_qs(parsed_url.query)
    params.pop('token')
    # print key value pairs
    print('Valid',end=' ')
    for key, value in params.items():
        print(key, value[0], end=' ')
    print()
def valid_csrf_tokens(token:str):
    # alphanumeric and atlease 9 characters long
    if(len(token) < 8):
        return False
    return token.isalnum()
 
valid_auth_tokens = ['et51u8i9p1q7','b8nn5j4om76v','r5b019lmlp09']
requests=[['GET',"https://example.com/?token=et51u8i9p1q7&id=2e3rt&name=alex"],['POST',"https://example.com/?token=r5b019lmlp09&csrf=ia+09&id=u78we&name=evan"]]
# print(valid_csrf_tokens(valid_auth_tokens[0]))
print(getResponses(valid_auth_tokens,requests))