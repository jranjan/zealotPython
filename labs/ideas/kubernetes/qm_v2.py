import random
import uuid
import logging
import threading
import time
import Queue
import exception
from enum import Enum


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class HttpServiceRequestStatus(Enum):
    UNKNOWN = -1
    WAITING = 1
    LIVE = 2
    FAILED = 3
    SUCCESS = 4
    FAILED_DONE = 5
    SUCCESS_DONE = 6


class RequestManager(object):
    """Responsible for request management.

    It acts a queue managers (think like a person taking a order request
    in restaurant). It takes order and serves the  request as per internal
    defined logic. It needs to ensure the following:

        - requests are asked to process in order of arrival.
        - only on serial request is processed at a time.
        - multiple parallel request can be served in paralllel.
        - request management is thread safe (n future, we might like to see
          it as multi-processor safe) even if there are more than one
          entity i.e. threads (process in future) serving requests.

    Internal data structure:

    It uses set of queue for various purpose and does request hoping from one
    queue to another queue as and when asked. It uses priority queue to retain
    the ordering of queue. The below is given more detail.

        Types of queue:

            -  wait_q: list of request if it can not be executed now
            -  live_q: list of request in-flight request
            -  completed_q: list of completed request
            -  error_q: list of errored request

        Queue processing rules:

            - Check for the following :
                    - if it is a serial type and there is one in-flight
                    - if threshold of request count to be process in
                      parallel has reached
            - If any of above condition meets then then put it in wait_q.
              Or else, start processing and put it in live_q.

        Dependency:

            - Relies on two attributes of requests: serial and status. Any change
              in request object needs to be accomodated here.

    """

    def __init__(self):
        """Class initializer."""
        self.total_requests = 0
        self._initialize_queues()

    def _initialize_queues(self):
        """Creates queue data structure."""
        self.wait_q = Queue.PriorityQueue()
        self.live_q = Queue.PriorityQueue()
        self.completed_q = Queue.PriorityQueue()
        self.error_q = Queue.PriorityQueue()

    def add_new(self, r):
        """Adds a new request to inventory.

        It adds new requests only if it is in UNKNOWN state which
        indicates that request has not started processing or processed
        already. It raises exception if it can not taken any more
        order to process requests.
        """
        if r.status == HttpServiceRequestStatus.UNKNOWN:
            r.status = HttpServiceRequestStatus.WAITING
            self.wait_q.put(r)
        else:
            raise Exception("Could not add request because of it's status")

    def ready(self):
        """Gets a request which can be processed as of now.

        It implements following rules:

            - Check for the following :
                    - if it is a serial type and there is one in-flight
                    - if threshold of request count to be process in
                      parallel has reached
            - If any of above condition meets then then put it in wait_q.
              Or else, start processing and put it in live_q.
        """
        result = Nonoe
        if not self.wait_q.empty():
            r = self.wait_q.get()
            if r.status != HttpServiceRequestStatus.WAITING:
                raise Exception("Request should not be here %s" %(str(r)))
            if r.serial:
                serial = self._check_serial_reuqest_livq()
                if serial:
                    self.wait_q.put(r)  # put it back
                else:
                    if r.status == HttpServiceRequestStatus.WAITING:
                        r.status = HttpServiceRequestStatus.LIVE
                        self.live_q.put(r)
                        result = r
            else:
                if r.status == HttpServiceRequestStatus.WAITING:
                    r.status = HttpServiceRequestStatus.LIVE
                    self.live_q.put(r)
                    result = r
                else:
                    raise  Exception("Any request in wait queue should have WAITING status.")
        return result

    def add_processed(self, r):
        if self.live_q.qsize:
            self._pop(self.live_q, r)
        else:
            raise Exception("Only requests in processed state is allowed")

        if r.status == HttpServiceRequestStatus.FAILED_DONE:
            self.error_q.put(r)
        elif r.status == HttpServiceRequestStatus.SUCCESS_DONE:
            self.completed_q.put(r)
        else:
            raise Exception("Impropoer addition of requestes!")

    def _pop(self, q, r):
        pass

    def count_live_request(self):
        return self.live_q.qsize()

    def count_total_request(self):
        return self.live_q.qsize() + self.wait_q.qsize()

    def count_waiting_request(self):
        return self.wait_q.qsize()

    def count_completed_request(self):
        return self.completed_q.qsize()

    def count_errored_request(self):
        return self.error_q.qsize()

    def count_total_processed_request(self):
        return self.completed_q.qsize() + self.error_q.qsize()

    def _check_serial_reuqest_livq(self):
        if not self.live_q.empty():
            first_r = self.live_q.get()
            self.live_q.put(first_r)
            if first_r.serial:
                return True
            else:
                next_r = self.live_q.get()
                while first_r != next_r:
                    if first_r.serial:
                       self.live_q.put(first_r)
                       return True
            return False

class Request(object):
    def __init__(self, receiver, value, serial=False):
        self.receiver = receiver
        self.value = value
        self.serial = serial
        self.id = uuid.uuid4()
        self.status = -1
        self.total_requests = 0

    def display(self):
        print("id = ", self.id)
        print("serial = ", self.serial)
        print("value = ", self.value)
        print("status = ", str(self.status))

    def execute(self, request):
        self.receiver.do(request)


class Receiver(object):
    def __init__(self, callback):
        self.callback = callback
        pass

    def do(self, request):
        print("Started request id: %s at %s" %(str(request.id), time.time()))
        duration = random.randint(2, 4)
        if request.serial:
            duration = 10
        time.sleep(duration)
        print("\tProcessed request id: %s at %s in %s seconds" %(str(request.id), time.time(), str(duration)))
        self.callback(request)


class Manager(object):
    def __init__(self):
        self.queueManager = RequestManager()

    def callback(self, request):
        try:
            r = self.queueManager.pop(request)
            r.status = 2
            r.display()
            print("Done at :", time.time())
            print(str('=') * 66)
        exception as e:
            raise e

    def handle(self):
        receiver =  Receiver(self.callback)
        print("create requests in following order...")
        serialFlicker = random.randint(1, 10)
        self.total_requests = self.total_requests - 1
        if serialFlicker % 2  == 0 or serialFlicker % 5 == 0:
            r = Request(receiver, random.random(), True)
        else:
            r = Request(receiver, random.random(), False)
        r.display()
        self.wait_q.put(r, self.total_requests)

    def handle_all_serial(self):
        receiver = Receiver(self.callback)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), True)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), True)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), True)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), True)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), True)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), True)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

    def handle_multiple_serial_followed_by_multiple_parallell(self):
        receiver = Receiver(self.callback)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), True)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), True)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

    def handle_multiple_parallel_followed_by_multiple_serial(self):
        receiver = Receiver(self.callback)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), True)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), True)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

    def handle_all_parallel(self):
        receiver = Receiver(self.callback)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

    def handle_alternate_parallel_and_serial(self):
        receiver = Receiver(self.callback)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), True)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), True)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), True)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

    def handle_alternate_serial_and_parallel(self):
        receiver = Receiver(self.callback)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), True)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), True)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), True)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

    def handle_one_serial_followed_by_two_parallel(self):
        receiver = Receiver(self.callback)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), True)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), True)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), True)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)

        self.total_requests = self.total_requests - 1
        r = Request(receiver, random.random(), False)
        r.status = 1
        r.display()
        self.wait_q.put(r, self.total_requests)


    def start_request_procesor(self):
        self.processorThreadID_1 = uuid.uuid1()
        self.processorThread_1 = \
            RequestProcessorThread(self.processorThreadID_1,
                                   "HttpRequestProcessor-thread-1",
                                   self.queueManager)
        self.processorThreadID_2 = uuid.uuid1()
        self.processorThread_2 = \
            RequestProcessorThread(self.processorThreadID_2,
                                   "HttpRequestProcessor-thread-2",
                                   self.queueManager)

        self.processorThread_1.start()
        self.processorThread_2.start()

    def stop_request_procesor(self):
        self.processorThread_1.shutdown_flag.set()
        self.processorThread_1.join()
        self.processorThread_2.shutdown_flag.set()
        self.processorThread_2.join()


class RequestProcessorThread(threading.Thread):
    def __init__(self, threadID, name, queue_manager):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.queueManager = queue_manager
        self.shutdown_flag = threading.Event()

    def run(self):
        while not self.shutdown_flag.is_set():
            r = self.queueManager.get()
            if r:
                r.execute(r)

if __name__ == "__main__":
    m = Manager()
    m.start_request_procesor()
    time.sleep(60)
    print(str('^') * 66)
    m.stop_request_procesor()

