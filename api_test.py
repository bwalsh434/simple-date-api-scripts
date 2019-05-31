import argparse
import time
import requests


# Run script like this: python3 --url http://34.95.112.0/date

# NOTE: The "req_per_second" is not true requests per second. It's simply the sleep time in between requests. We could
#       execute true requests per second by calling the GET with something like Go concurrency or general multithreading

def api_test(url, req_per_second):
    """
    Runs x requests per second to a supplied URL

    :param url: The URL that will be tested with GET requests
    :param req_per_second: The amount of requests per second to execute.
    """

    wait_time = 1 / req_per_second

    while True:
        t0 = time.time()
        try:
            r = requests.get(url=url, timeout=10)
        except requests.exceptions.Timeout:
            print("FAILURE: The request timed out")
            time.sleep(wait_time)
            continue
        t1 = time.time()
        ttlb = round(((t1 - t0) * 1000), 1)
        if r:
            result = "SUCCESS"
        else:
            result = "FAILURE"
        print("{res}, ttlb: {req_time}ms".format(res=result, req_time=ttlb))
        time.sleep(wait_time)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--url',
        required=True,
        help='URL to fire a GET request to')
    parser.add_argument(
        '--req_per_second',
        default=1,
        help='The amount of requests per second to call out to the URL')

    args = parser.parse_args()
    api_test(args.url, args.req_per_second)
