import time
import threading
import thread
import logging
import Queue

BUF_SIZE = 6
q = Queue.Queue(BUF_SIZE)


logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )


class PorbeRepeater(object):
    def __init__(self, interval, function):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function()

    def start(self):
        if not self.is_running:
            self._timer = threading.Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


class ProducerThread(threading.Thread):
    def __init__(self, producers):
        super(ProducerThread, self).__init__()
        self.producers = producers
        return

    def run(self):
        self._probe_forever()

    def _probe_forever(self):
        for name in self.producers.keys():
            r = PorbeRepeater(self.producers[name]['frequency'],
                              self.producers[name]['scanner'])

