from nose.tools import assert_true, eq_
import requests


def test_scan_api():
    # Send a request to the API server and store the response.
    response = requests.get('http://127.0.0.1:2000/scan/123/1234/1236')
   
    # Confirm that the request-response cycle completed successfully.
    eq_(response.json(), [{'port': 1234, 'state': 'close'}, {'port': 1235, 'state': 'close'}, {'port': 1236, 'state': 'close'}])




