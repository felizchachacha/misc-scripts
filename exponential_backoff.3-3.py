#!/usr/bin/env python3.5
"""
Python 3.5
"""

import requests
from time import sleep
from random import randint


class Output:
    def __init__(self, backoff, retries, response):
        self.backoff = backoff
        self.retries = retries
        self.response = response
    def __str__(self):
        return self.response


class Error:
    def __init__(self, error_type, backoff, retries):
        self.error_type = error_type
        self.backoff = backoff
        self.retries = retries

    def __str__(self):
        return self.error_type


class RequestHandler:

    def __init__(self, url, max_backoff_bound, max_retries, slot_time, debug=False):
        self.url = url
        self.max_backoff_bound = max_backoff_bound
        self.max_retries = max_retries
        self.current_backoff = 0
        self.current_iteration = 0
        self.is_debug = debug
        self.slot_time = slot_time
        self.error_type = None
        self.response = None

    def newRequest(self):
        is_success = False

        while self.current_iteration < self.max_retries:

            if self.current_iteration > 0:
                self.current_backoff = self.get_backoff_time()
                if not self.current_backoff:
                    self.current_iteration += 1
                    continue
                sleep(self.current_backoff)

            try:
                result = requests.get(REQUEST_URL)
                if result.status_code == 200:
                    is_success = True
                    self.response = result.text
                    if self.is_debug:
                        print('success {}'.format(self.current_iteration))
                    break

            except requests.HTTPError:
                self.error_type = 'http error'
                if self.is_debug:
                    print('http error')
                continue

            except requests.exceptions.ConnectionError:
                self.error_type = 'connection error'
                if self.is_debug:
                    print('connection error')
                continue

            finally:
                if not is_success:
                    self.current_iteration += 1
                    if self.is_debug:
                        print('backoff: {} sec.\niteration: {}\n'.format(self.current_backoff, self.current_iteration))

        if is_success:
            current_output = Output(self.current_backoff, self.current_iteration, self.response)
            result = current_output, None
        else:
            e = Error(self.error_type, self.current_backoff, self.current_iteration)
            result = None, e

        return result

    def get_backoff_time(self):
        get_time_max_retries = 20
        counter = 0

        # задержка равна случайному числу от 0 до 2 в степени _текущая попытка_ * фиксированный промежуток времени

        while counter < get_time_max_retries:
            backoff = randint(0, 2 ** self.current_iteration) * self.slot_time

            if backoff < self.max_backoff_bound:
                break
            counter += 1
        else:
            return None

        return backoff


REQUEST_URL = 'https://google.com'
MAX_BACKOFF_SEC = 30
MAX_RETRIES = 20
SLOT_TIME = 1
DEBUG = True


rh = RequestHandler(REQUEST_URL, MAX_BACKOFF_SEC, MAX_RETRIES, SLOT_TIME, DEBUG)
output, error = rh.newRequest()

if error:
    print('Error: {}'.format(error.error_type))
elif output:
    print('Connection - success! \nBackoff: {} sec. \nRetries: {}'.format(output.backoff, output.retries))
    print(output)



