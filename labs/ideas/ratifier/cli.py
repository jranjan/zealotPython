import click

from labs.ideas.ratifier.config import RatifierConfig
from labs.ideas.ratifier.core.exc.config import ConfigException
from labs.ideas.ratifier.core.render.service import ServiceRender
from labs.ideas.ratifier.core.render.service_family import ServiceFamilyRender


class HelpCmd(click.Command):
    def format_usage(self, ctx, formatter):
        formatter.write_usage("")


@click.group()
def cli():
    pass


@click.command(no_args_is_help=True, cls=HelpCmd)
@click.option('--service', '-s', help='Service name', required=True)
@click.pass_context
def show(ctx, service):
    try:
        print("Show testsuite detail for service={0}".format(service))
    except Exception:
        print("Command execution error")


@click.command(no_args_is_help=True, cls=HelpCmd)
@click.pass_context
def showall(ctx):
    try:
        print("Show testsuite detail for service={0}".format())
    except Exception:
        print("Command execution error")


@click.command(no_args_is_help=True, cls=HelpCmd)
@click.option('--service', '-s', help='Service name', required=True)
@click.option('--suite', '-t', help='Bucket type', required=True)
@click.pass_context
def run(ctx, service, suite):
    try:
        config = RatifierConfig()
        s = ServiceRender(service, config.get_test_rootd(), suite, config.get_test_reportd())
        print('ServiceRender(service')
        s.render()
    except ConfigException as re:
        print(re.get_msg)
    except Exception as e:
        print("!!! Fatal error !!!")


@click.command(no_args_is_help=True, cls=HelpCmd)
@click.pass_context
def runall(ctx):
    try:
        attrs = dict()
        r = ServiceFamilyRender(attrs)
        r.render()
    except ConfigException as re:
        print(re.get_msg)
    except Exception as e:
        print("!!! Fatal error !!!")


cli.add_command(show)
cli.add_command(showall)
cli.add_command(run)
cli.add_command(runall)


if __name__ == '__main__':
   cli()
