from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    # Example condition: intercept requests to a specific host
    print(f"Intercepted request to: {flow.request.url}")

    flow.request.host = "telekomunikacja.agh.edu.pl"
