from labs.ideas.ratifier.core.common.system import System
from labs.ideas.ratifier.core.exc.config import ConfigException
from labs.ideas.ratifier.core.exc.unsupported import UnsupportedException


class RatifierConfig(object):
    def __init__(self, conf=None):
        self.load(conf)

    def get_test_rootd(self):
        return self.test_rootd

    def get_test_reportd(self):
        return self.test_reportd

    def load(self, conf):
        if conf is None:
            self.test_rootd = "./labs/ideas/ratifier/tests"
            if not System.is_directory_exist(self.test_rootd):
                raise ConfigException()
            self.test_reportd = "./labs/ideas/ratifier/.ratifier_reports"
            if not System.is_directory_exist(self.test_reportd):
                self.__create_test_reportd(self.test_reportd)
        else:
            raise UnsupportedException()

    def __create_test_reportd(self, d):
        if not System.is_directory_exist(self.test_reportd):
            System.create_dir(self.test_reportd)
