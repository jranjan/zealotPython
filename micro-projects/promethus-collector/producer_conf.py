from babyapps.collector.ceph.ceph_producers import CephStatsProducers
import Queue

producers = {
    'get_status' :{
        'scanner': CephStatsProducers.get_status,
        'queue': Queue.Queue(1),
        'queue_backup': Queue.Queue(1),
        'frequency': 6
    },
    'get_osd_stats': {
        'scanner': CephStatsProducers.get_osd_stats,
        'queue': Queue.Queue(1),
        'queue_backup': Queue.Queue(1),
        'frequency': 60
    },
}