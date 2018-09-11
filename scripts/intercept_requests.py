"""
This example shows how to send a reply from the proxy immediately
without sending any data to the remote server.
"""
from mitmproxy import http

# tuple indexes
api_path = 0
mock_response = 1
response_json_path = 2

# Uses tuple (api_path=String, mock_response=Boolean, response_json_path=String)
apiconfig = [
    ("loyalty/v3/programs", True, "mock/loyalty_program.json"),
    ("api/v3/reports/get_latest_transaction", False, "mock/get_latest_transaction.json")
]

def request(flow: http.HTTPFlow) -> None:
    # pretty_url takes the "Host" header of the request into account, which
    # is useful in transparent mode where we usually only have the IP otherwise.

    for api in apiconfig:        
        if api[api_path] in flow.request.pretty_url and api[mock_response] == True:
            print(api[api_path])
            mockjson = open(api[response_json_path], "r").read()
            print("response: ",  mockjson)
            flow.response = http.HTTPResponse.make(
                400,  # (optional) status code
                mockjson,  # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers
            )
            break

