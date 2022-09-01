from mitmproxy import http


mitm_urls = [
    "https://work.shiep.edu.cn/default/work/shiep/xslfxsq/lxRedirect.jsp",
    "https://work.shiep.edu.cn/default/work/shiep/xslfxsq/fxRedirect.jsp"
]


def response(flow: http.HTTPFlow) -> None:
    req_url = flow.request.pretty_url
    if req_url in mitm_urls:
        body = flow.response.text
        if req_url.endswith("lxRedirect.jsp"):
            body = body.replace("hibit.gif", "out.gif")
        elif req_url.endswith("fxRedirect.jsp"):
            body = body.replace("hibit.gif", "enter.gif")
        flow.response.text = body
