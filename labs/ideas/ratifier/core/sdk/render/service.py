from labs.ideas.ratifier.core.runner.pytest_runner import PytestRunner
from labs.ideas.ratifier.core.sdk.render.render import Render


class ServiceRender(Render):
    def __init__(self, service, test_location, test_suite_type, test_report_name, test_report_location):
        self.name = service
        self.test_suite_location = test_location
        self.test_suite_type = test_suite_type
        self.test_report_name = test_report_name
        self.test_report_location = test_report_location

    def render(self):
        service_attrs = dict()
        service_attrs['name'] = self.name
        service_attrs['test_suite_type'] = self.test_suite_location
        service_attrs['test_suite_location'] = self.test_suite_type
        service_attrs['test_report_name'] = self.test_report_name
        service_attrs['test_report_location'] = self.test_report_location
        r = PytestRunner();
        r.run(service_attrs)
