from __future__ import print_function

import argparse
import pkg_resources
import json
import sys
import traceback


def display_json(metrics, pretty):
    kwargs = {}
    if pretty:
        kwargs = {
            'sort_keys': True,
            'indent': 2,
        }

    print(json.dumps(metrics, **kwargs))


FORMATS = {
    'json': display_json
}


def construct_parser(plugins):
    parser = argparse.ArgumentParser(description='Parser sample')
    # Create a flag for each plugin that adds the matching function to the
    # selected list if it appears on the command line.
    selection_group = parser.add_argument_group(
        'Available Checks',
        'Select one or more of the available checks to run as a subset.'
    )
    for name, unloaded_func in plugins.items():
        func = unloaded_func.load()
        help_string = func.__doc__ or 'Reserved for future use.'

        selection_group.add_argument(
            '--' + name,
            dest='selected',
            action='append_const',
            const=func,
            help=help_string
        )

    parser.add_argument(
        '--format',
        choices=FORMATS.keys(),
        default='json',
        help='Format output (default: %(default)s).'
    )
    parser.add_argument(
        '-p', '--pretty',
        action='store_true',
        help='Format output in a more easy to read way.'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='count'
    )

    return parser


def parse_args():
    ps = pkg_resources.get_entry_map('cephlm', 'cephlm.plugins')
    p = construct_parser(ps)
    args = p.parse_args()

    # we make the common case easy, No selected flags indicate that we should
    # run all diagnostics.
    if args.selected is None:
        args.selected = [f.load() for f in ps.values()]

    return args


def main():
    args = parse_args()
    metrics = []

    for func in args.selected:
        try:
            r = func()
            if isinstance(r, list) and r and isinstance(r[0], MetricData):
                metrics.extend([result.metric() for result in r])
            elif isinstance(r, MetricData):
                metrics.append(r.metric())
        except:   # noqa
            t, v, tb = sys.exc_info()
            backtrace = ' '.join(traceback.format_exception(t, v, tb))
            r = MetricData.single('check.failure', Severity.fail,
                                  '{error} failed with: {check}',
                                  dimensions={'component': 'cephlm-probe',
                                              'service': 'ceph-storage'},
                                  msgkeys={'check': func.__module__,
                                           'error':
                                               backtrace.replace('\n', ' ')})
            metrics.append(r.metric())

    # There is no point in reporting multiple measurements of
    # cephlm.check.failure metric in same cycle.
    check_failures_found = []
    for metric in metrics:
        if metric.get('metric') == 'cephlm.check.failure':
            check_failures_found.append(metric)
    if check_failures_found:
        # Remove all except one instance
        for metric in check_failures_found[:-1]:
            metrics.remove(metric)
    else:
        r = MetricData.single('check.failure', Severity.ok, 'ok',
                              dimensions={'component': 'cephlm-probe',
                                          'service': 'ceph-storage'})
        metrics.append(r.metric())

    FORMATS[args.format](metrics, args.pretty)


if __name__ == '__main__':
    main()
