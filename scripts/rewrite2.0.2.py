from mitmproxy import http

import time

def request(flow):
    rewrite = False
    mockresp = open("mock/success.json", "r").read()

    flow.request.oldpath = flow.request.path;
    # if flow.request.path.endswith("/api/2/account/api/"):
    #     flow.request.path = "/api/2/account/myapitest"
    if flow.request.path.startswith("/api/2/account/my/profile/plan/circlesswitch/upgrade/"):
        rewrite = False
    if flow.request.path.startswith("/api/2/account/my/profile/id/digits/verify/get/"):
        mockresp = open("mock/my_profile_id_digits_verify_get.json", "r").read()
        rewrite = False
    if flow.request.path.startswith("/api/2/account/my/portin/request/cancel/"):
        rewrite = False

    print("\nRequest : " + str(flow.request.oldpath)+"\n")
    # print("Request Rewrite : " + str(flow.request.path)+"\n")
    print("\nRequest Body : " + str(flow.request.content)+"\n")

    if rewrite:
        time.sleep(0.3)
        resp = HTTPResponse(
            "HTTP/1.1", 200, "OK",
            Headers(Content_Type="application/json; charset=utf-8"),
            mockresp)
        flow.reply(resp)
        print("\nResponse : " + str(flow.response.content)+"\n")

def response(flow: http.HTTPFlow) -> None:
    rewrite = False

    # if flow.request.oldpath.endswith("/revision?"):
    # 	mockjson = open("mock/revision.json", "r")
    #     rewrite = True
    # if flow.request.oldpath.startswith("/api/2/account/my/portin/request/active/"):
    # 	mockjson = open("mock/my_portin_request_active.json", "r")
    #     rewrite = True
    # if flow.request.oldpath.startswith("/api/2/account/my/profile/details/get/"):
    # 	mockjson = open("mock/my_profile_details_get.json", "r")
    #     rewrite = True
    if flow.request.oldpath.startswith("/api/2/account/batch/"):
        mockjson = open("mock/account_batch.json", "rb")
        rewrite = True
        #print("\nResponse : " + str(mockjson.read())+"\n")

    if rewrite:
        time.sleep(0.3)            
        flow.response.content = mockjson.read()
        flow.response.reason = "OK";
        flow.response.status_code = 200;
        print("\nResponse Tuype: " + str(flow.response.content)+"\n")
