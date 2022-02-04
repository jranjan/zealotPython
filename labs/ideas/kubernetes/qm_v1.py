import random
import uuid
import logging
import threading
import time
import Queue


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

"""
class HttpServiceRequestStatus(Enum):


    UNKNOWN = -1
    WAITING = 1
    DEQUEUED = 2
    INPROGRESS = 3
    FAILED = 4
    SUCCESS = 5
"""

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
        self.wait_q = Queue.PriorityQueue()
        self.live_q = Queue.PriorityQueue()
        self.completed_q = Queue.PriorityQueue()
        self.error_q = Queue.PriorityQueue()
        self.total_requests = 0

    def callback(self, request):
        if not self.live_q.empty():
           curr_r = self.live_q.get()
           while curr_r != request:
                next_r = self.live_q.get()
                self.live_q.put(curr_r)
                curr_r = next_r
           print(str('.') * 66)
           curr_r.status = 2  # Completed
           curr_r.display()
           print("wait_q length = ", self.wait_q.qsize())
           print("live_q length = ", self.live_q.qsize())
           print("Done at :", time.time())
           print(str('=') * 66)

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
                                   self.wait_q,
                                   self.live_q)
        self.processorThreadID_2 = uuid.uuid1()
        self.processorThread_2 = \
            RequestProcessorThread(self.processorThreadID_2,
                                   "HttpRequestProcessor-thread-2",
                                   self.wait_q,
                                   self.live_q)

        self.processorThread_1.start()
        self.processorThread_2.start()

    def stop_request_procesor(self):
        self.processorThread_1.shutdown_flag.set()
        self.processorThread_1.join()
        self.processorThread_2.shutdown_flag.set()
        self.processorThread_2.join()


class RequestProcessorThread(threading.Thread):
    def __init__(self, threadID, name, wait_q, live_q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.wait_q = wait_q
        self.live_q = live_q
        self.shutdown_flag = threading.Event()

    def check_serial_reuqest_livq(self):
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

    def run(self):
        while not self.shutdown_flag.is_set():
            if not self.wait_q.empty():
                r = self.wait_q.get()
                if r.serial:
                    serial = self.check_serial_reuqest_livq()
                    if serial:
                        self.wait_q.put(r) # put it back
                    else:
                        if r.status == 1: # Waiting
                            self.live_q.put(r)
                            r.status = 3
                            r.execute(r)
                else:
                    if r.status == 1:  # Waiting
                        self.live_q.put(r)
                        r.status = 3
                        r.execute(r)
                    else:
                        raise e

if __name__ == "__main__":
    m = Manager()
    m.handle_one_serial_followed_by_two_parallel()
    print(str('-') * 66)
    time.sleep(3)
    m.start_request_procesor()
    time.sleep(60)
    print(str('^') * 66)
    m.stop_request_procesor()

