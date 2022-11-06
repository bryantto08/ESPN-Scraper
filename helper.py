import base64
import urllib.parse

def dataURI_decode(uri):
    if uri.startswith('data:'):
        dataFormat, data = uri.split(',', 1)
        mimetype, *attrs = dataFormat.split(';')
        if attrs and attrs[-1] == 'base64':
            return mimetype, base64.b64decode(data)
        else:
            return mimetype, urllib.parse.unquote_to_bytes(data)
