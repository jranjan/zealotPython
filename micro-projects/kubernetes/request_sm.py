import random
import uuid
import logging
import threading
import time
import Queue


class Request(object):
    """A base class for any request. It defines core-field."""

    def __init__(self, num):
        """Class initializer."""
        self.num = num
        self.prev_state = None
        self.current_state = None

class StateHandler(object):

    def __init__(self):
        pass

    def set_start_state(self, request):
        request.prev_state = None
        request.current_state = self.s1_start

    def s1_start(self, request):
        request.num = request.num
        request.prev_state = request.current_state
        request.current_state = self.s1_add

    def s1_add(self, request):
        request.num = request.num + request.num
        request.prev_state = request.current_state
        request.current_state = self.s1_multiply

    def s1_multiply(self, request):
        request.num = request.num * request.num
        request.prev_state = request.current_state
        request.current_state = self.s1_div_by_2

    def s1_div_by_2(self, request):
        request.num = request.num /2
        request.prev_state = request.current_state
        request.current_state = self.s1_completion

    def s1_completion(self, request):
        request.prev_state = request.current_state
        request.current_state = None
        print(request.num)

    def start_sm(self, request):
        """Start state machine to process the request."""
        while request.current_state is not None:
            request.prev_state = request.current_state
            request.current_state(request)

if __name__ == "__main__":
    sh = StateHandler()
    r = Request(4)
    sh.set_start_state(r)
    sh.start_sm(r)
