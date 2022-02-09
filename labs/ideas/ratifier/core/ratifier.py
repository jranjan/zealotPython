from labs.ideas.ratifier.core.render.service import ServiceRender


class Ratifier(object):
    def __init__(self, test_root_location, test_report_root_location):
        self.test_location = test_root_location
        self.test_report_location = test_report_root_location

    def run(self, suite_attrs=dict()):
        self.display_suite_info(suite_attrs)
        if suite_attrs:
            self.__run_service()
        else:
            self.__run_all()

    def display_suite_info(self, suite_attrs=dict()):
        if suite_attrs:
            self.__display_suite_info(suite_attrs)
        else:
            self.__display_suite_info_all()

    def __run_service(self, suite_attrs):
        service_attrs = dict()
        service_attrs['name'] = suite_attrs['name']
        service_attrs['test_suite_type'] = suite_attrs['type']
        service_attrs['test_location'] = "{0}//{1}".format(self.root, service_attrs['name'])
        service_attrs['test_report_name'] = "{0}.html".format(service_attrs['name'])
        service_attrs['test_report_location'] = "{0}//{1}".format(self.test_report_location,
                                                                  service_attrs['test_report_name'])
        render = ServiceRender(service_attrs)
        render.run()

    def __run_all(self, suite_attrs):
        service_family_attrs = dict()
        service_family_attrs['name'] = 'service-family'
        service_family_attrs['test_suite_type'] = suite_attrs['type']
        service_family_attrs['test_location'] = self.root
        service_family_attrs['test_report_name'] = "{0}.html".format('service-family.html')
        service_family_attrs['test_report_location'] = self.test_report_location + '/' + \
                                                            service_family_attrs['test_report_name']
        render = ServiceRender(service_family_attrs)
        render.run()

    def __display_suite_info(self, suite_attrs):
        print("Discovered test details at location={0} for service={1}".format(self.root), suite_attrs['service'])

    def __display_suite_info_all(self):
        print("Discovered test details at location={0}".format(self.root))
