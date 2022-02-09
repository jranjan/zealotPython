from labs.ideas.ratifier.core.runner.pytest_runner import PytestRunner
from labs.ideas.ratifier.core.render import Render


class ServiceFamilyRender(Render):
    def __init__(self, test_location, test_suite_type, test_report_name, test_report_location):
        super(ServiceFamilyRender, self).__init__('ServiceFamily',
                                                  test_location,
                                                  test_suite_type,
                                                  test_report_name,
                                                  test_report_location)

    def render(self):
        service_attrs = dict()
        service_attrs['name'] = self.name
        service_attrs['test_location'] = self.test_suite_location
        service_attrs['test_suite_type'] = self.test_suite_type
        service_attrs['test_report_name'] = self.test_report_name
        service_attrs['test_report_location'] = self.test_report_location

        r = PytestRunner(service_attrs);
        r.run(service_attrs)
