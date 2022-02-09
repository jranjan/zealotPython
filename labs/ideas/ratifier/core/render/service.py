from labs.ideas.ratifier.core.render.render import Render
from labs.ideas.ratifier.core.runner.pytest_runner import PytestRunner


class ServiceRender(Render):
    def __init__(self, service, test_location, test_suite_type, test_report_location):
        super(ServiceRender, self).__init__(service,
                                            test_location,
                                            test_suite_type,
                                            test_report_location)

    def render(self):
        service_attrs = dict()
        service_attrs['name'] = self.name
        service_attrs['test_suite_location'] = "{0}/service/{1}".format(self.test_suite_location,
                                                                        service_attrs['name'])
        service_attrs['test_suite_type'] = self.test_suite_type
        service_attrs['test_report_type'] = 'html'
        service_attrs['test_report_location'] = self.test_report_location

        r = PytestRunner()
        r.run(service_attrs)
