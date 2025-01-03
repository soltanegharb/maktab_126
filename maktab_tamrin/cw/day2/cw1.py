import base64

def base64encoder(string):
    
    string_byte = string.encode('ascii')
    
    return base64.b64encode(string_byte)
print(base64encoder('hello'))
