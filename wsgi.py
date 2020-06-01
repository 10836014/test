def application(environ, start_response):
    status = '200 OK'
    output = b'Hello OMG!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]

import sys
sys.path.insert(0, 'C:\\test\\')
from test import app as application