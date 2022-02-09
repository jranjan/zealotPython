from labs.ideas.ratifier.core.render.render import Render
from labs.ideas.ratifier.core.runner.pytest_runner import PytestRunner


class ServiceFamilyRender(Render):
    def __init__(self, test_location, test_suite_type, test_report_location):
        super(ServiceFamilyRender, self).__init__('ServiceFamily',
                                                  test_location,
                                                  test_suite_type,
                                                  test_report_location)

    def render(self):
        service_family_attrs = dict()
        service_family_attrs['name'] = 'service_family'
        service_family_attrs['test_location'] = self.test_suite_location
        service_family_attrs['test_suite_type'] = self.test_suite_type
        service_family_attrs['test_report_type'] = 'html'
        service_family_attrs['test_report_location'] = self.test_report_location

        r = PytestRunner(service_family_attrs);
        r.run(service_family_attrs)
