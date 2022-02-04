import datetime
import logging
from babyapps.collector.producer_conf import producers

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )


class CephStats:
    def __init__(self):
        pass

    @staticmethod
    def get_status(self):
        item = CephStats._dequeue('get_status')
        if item:
            logging.info('Consumed [ceph status] at %s, details:%s' %(str(datetime.datetime.now()), item.__dict__))


    @staticmethod
    def get_osd_stats(self):
        item = CephStats._dequeue('get_osd_stats')
        if item:
            logging.info('Consumed [OSD statistics] at %s, details:%s' %(str(datetime.datetime.now()), item.__dict__))

    @staticmethod
    def _dequeue(name):
        q = producers[name]['queue']
        q_backup = producers[name]['queue_backup']

        # As we do mandate to feed data every 30s (or pollster choice),
        # we might have a situation where our producer queue is empty
        # if producer is running behind at the frequency slower than
        # us. In that case, we do want to say that data is not there.
        # We want to return old data with assistance of backup queue.
        # Let us see how it unfolds!
        item = None
        if not q.empty():
            item = q.get()
            if not q_backup.empty():
                q_backup.get()
            q_backup.put(item)
        else:
            if not q_backup.empty():
                logging.info('Prime queue empty, pulling [%s] from backup queue!!!!!!!!!!!!!!!' %name)
                item = q_backup.get()
                q_backup.put(item)
            else:
                logging.info('Both prime and backup queue are empty for [%s]...' %name)
        return item
