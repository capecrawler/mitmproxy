from mitmproxy.models import HTTPResponse
from netlib.http import Headers

def request(context, flow):
    flow.request.oldpath = flow.request.path;
    print("\nRequest : " + str(flow.request.oldpath)+"\n")
    # print("\nRequest Body : " + str(flow.request.content)+"\n")


def response(context, flow):
    rewrite = False

    if flow.request.oldpath.startswith("/api/2/account/my/portin/request/active/"):
    	rewrite = True
        flow.response.content = open("mock/portin_request_active.json", "r").read()
    if flow.request.oldpath.startswith("/api/2/account/my/profile/details/get/"):
    	rewrite = True
        flow.response.content = open("mock/my_profile_details_get.json", "r").read()
    # if flow.request.oldpath.startswith("/api/2/account/batch/"):
    #     rewrite = True
    #     mockjson = open("mock/account_batch.json", "r")
    #     flow.response.content = mockjson.read()

    if rewrite:
        flow.response.reason = "OK";
        flow.response.status_code = 200;
        # print("\nResponse : " + str(flow.response.content)+"\n")