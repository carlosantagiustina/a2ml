import click
from a2ml.api.a2ml import A2ML
from a2ml.api.utils.context import pass_context

@click.command('import', short_help='Import data for training.')
@click.option('--provider', '-p', type=click.STRING, required=False,
    help='Cloud AutoML Provider.')
@pass_context
def cmdl(ctx, provider):
    """Import data for training."""
    ctx.setup_logger(format='')
    A2ML(ctx, provider).import_data()
