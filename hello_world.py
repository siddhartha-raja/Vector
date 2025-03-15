from prometheus_client import start_http_server, Summary
import random
import time

# Create a metric to track the duration of some process
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric
@REQUEST_TIME.time()
def process_request():
    """A dummy function that simulates processing a request."""
    time.sleep(random.random())

if __name__ == '__main__':
    # Start up the server to expose the metrics
    start_http_server(8080)
    while True:
        process_request()
