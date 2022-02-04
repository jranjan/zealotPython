import threading
import thread
import datetime
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )


class Pollster(threading.Thread):
    def __init__(self,
                 checks,
                 polling_interval):
        super(Pollster, self).__init__()
        self.checks = checks
        self.polling_interval = polling_interval
        return

    def run(self):
        while True:
            logging.info('Polling started at: %s' %datetime.datetime.now())
            for name in self.checks.keys():
                try:
                    thread.start_new_thread(self.checks[name], (name,))
                except:
                    logging.error('Scan for %s failed' %name)
            time.sleep(self.polling_interval)
        return
