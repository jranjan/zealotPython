import random
import time
import datetime
import logging
from babyapps.collector.metric import Metric
import babyapps.collector.producer_conf


class CephStatsProducers:
    def __init__(self):
        pass

    @staticmethod
    def get_status():
        logging.info('Produced [ceph status] at %s' %str((datetime.datetime.now())))
        data = {
            'message': 'OK',
            'value': 100
        }
        metric = Metric('cephlm.ceph.status',
                        str(datetime.datetime.now()),
                        data)
        CephStatsProducers._queue_metric('get_status', metric)

    @staticmethod
    def get_osd_stats():
        logging.info('Produced [OSD statistics] at %s' %str((datetime.datetime.now())))
        data = {
            'message': 'OK',
            'value': 1000,
        }
        metric = Metric('cephlm.ceph.osd_stats',
                        str(datetime.datetime.now()),
                        data)
        CephStatsProducers._queue_metric('get_osd_stats', metric)

    @staticmethod
    def _queue_metric(name, metric):
        q = babyapps.collector.producer_conf.producers[name]['queue']
        # If queue is not empty then move element to back before
        # producing new own and inject fresh one in the queue.
        # This can occur if producer is fast enough to generate
        # data and consumer is not able to handle.
        if not q.empty():
            q.get()
        q.put(metric)
