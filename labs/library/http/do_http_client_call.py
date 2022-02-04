import requests


def do_http_get_request(url, fail_msg=None, success_msg=None):
    response = requests.get(url)
    if response.status_code == 200:
        print(success_msg)
        return response.text
    else:
        print(fail_msg)
        raise


if __name__ == "__main__":
    result = do_http_get_request("http://www.google.com",
                                 'Bad luck...................',
                                 'Great to know......................')
    print result
