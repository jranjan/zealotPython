from labs.ideas.ratifier.core.runner.runner import Runner


class PytestRunner(Runner):
    def __init__(self):
        super().__init__()
        pass

    def run(self, service_attrs):
        print("{0} : Ran test suite={1}, published report at={2}".format(service_attrs['name'],
                                                                         service_attrs['test_suite_location'],
                                                                         service_attrs['test_report_location']))
