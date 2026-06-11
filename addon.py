from mitmproxy import http


def request(flow):
    flow.response = http.Response.make(200)
