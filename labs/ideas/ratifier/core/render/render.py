class Render(object):
    def __init__(self, service, test_location, test_suite_type, test_report_location):
        self.name = service
        self.test_suite_location = test_location
        self.test_suite_type = test_suite_type
        self.test_report_location = test_report_location

    def run(self):
        pass
