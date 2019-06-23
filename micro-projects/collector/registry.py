from babyapps.collector.ceph import ceph


class CheckRegistry:
    def __init__(self):
        self.db = dict()

    def register(self, name, check_fn):
        self.db[name] = check_fn

    def get_checks(self):
        return self.db


def setup_check_plugin():
    registry = CheckRegistry()
    registry.register('cephlm.prob.status', ceph.CephStats.get_status)
    registry.register('cephlm.prob.osd_stats', ceph.CephStats.get_osd_stats)
    return registry.get_checks()
