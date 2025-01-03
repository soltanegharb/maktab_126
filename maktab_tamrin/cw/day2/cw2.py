import base64

def base64decoder(string_encoded):

    try:
        return base64.b64decode(string_encoded)
    except:
        print('not a base64 string')

