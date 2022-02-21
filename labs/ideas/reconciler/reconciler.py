import fnmatch
import os
import yaml
import shutil

from labs.ideas.reconciler.exc.base import ReconcilerException


class Reconciler(object):
    def __init__(self, rootd, value=False, new_key='exemptFromHealthMonitoring'):
        self.rootd = rootd
        self.key = new_key
        self.value = value
        self.metrics = ['availability', 'requestrate', 'errorrate', 'duration', 'saturation']

    def reconcile(self):
        for f in self.__find_files(self.rootd, "*.yaml"):
            self.reconcile_file(f)

    def __find_files(self, d, pattern):
        for root, dirs, files in os.walk(d):
            for basename in files:
                if fnmatch.fnmatch(basename, pattern):
                    f = os.path.join(root, basename)
                    yield f

    def reconcile_file(self, source):
        d = self.__to_json_data(source)
        data = self.__alter_key(d)
        self.__to_yaml(source, data)

    def __to_json_data(self, s):
        if os.path.isfile(s):
            with open(s, "r") as t:
                d = yaml.load(t, Loader=yaml.FullLoader)
                return d
        raise ReconcilerException()

    def __alter_key(self, d):
        for l in self.metrics:
            d[l][self.key] = self.value
        return d

    def __to_yaml(self, s, data):
        s_backup = "{0}.bak".format(s)
        shutil.copyfile(s, s_backup)
        with open(s, "w") as fh:
            yaml.dump(data, fh)


if '__main__' == __name__:
    r = Reconciler("./labs/ideas/reconciler/data/", 10000, 'downsamplingIntervalInMin')
    r.reconcile()
