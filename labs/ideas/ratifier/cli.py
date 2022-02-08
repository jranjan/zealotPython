import click

from labs.ideas.ratifier.core.sdk.render.service import ServiceRender
from labs.ideas.ratifier.core.sdk.render.composite import ServiceFamilyRender


@click.group()
def cli():
    pass


class HelpCmd(click.Command):
    def format_usage(self, ctx, formatter):
        formatter.write_usage("")


@click.command(no_args_is_help=True, cls=HelpCmd)
@click.option('--service', '-s', help='Service name', required=True)
@click.argument('name')
def show(service):
    try:
        print("Show testsuite detail for service={0}".format(service))
    except Exception:
        print("Command execution error")


@click.command(no_args_is_help=True, cls=HelpCmd)
def showall():
    try:
        print("Show testsuite detail for service={0}".format())
    except Exception:
        print("Command execution error")


@click.command(no_args_is_help=True, cls=HelpCmd)
@click.option('--service', '-s', help='Service name', required=True)
def run(service):
    try:
        s = ServiceRender(service, "1", "2", "3", "4")
        s.render()
    except Exception:
        print("Command execution error")


@click.command(no_args_is_help=True, cls=HelpCmd)
def runall():
    try:
        attrs = dict()
        r = ServiceFamilyRender(attrs)
        r.render()
    except Exception:
        print("Command execution error")


cli.add_command(show)
cli.add_command(showall)
cli.add_command(run)
cli.add_command(runall)


if __name__ == '__main__':
    cli()
