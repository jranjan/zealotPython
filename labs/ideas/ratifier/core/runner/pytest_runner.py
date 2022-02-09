import subprocess
from datetime import datetime

from labs.ideas.ratifier.core.exc.unsupported import UnsupportedException
from labs.ideas.ratifier.core.runner.runner import Runner


class PytestRunner(Runner):
    def __init__(self):
        super().__init__()

    def run(self, args):
        print(args)
        suite_type = "-m {0}".format(args['test_suite_type'])
        suite_location = args['test_suite_location']
        print(suite_location)
        suite_report_name = "{0} {1}".format(datetime.now().strftime("%y:%m:%d %H:%M:%S"), args['name'])
        print(suite_report_name)
        if args['test_report_type'] == 'html':
            suite_report_fqn = "--{0}={1}/{2}.html".format('html', args['test_report_location'], suite_report_name)
            print(suite_report_fqn)
        else:
            raise UnsupportedException()

        subprocess.call(['pytest', suite_location, suite_type, suite_report_fqn])
