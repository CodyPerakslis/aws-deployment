import click
from functools import wraps

def click_defaults(f):
    names = filter((lambda x: x != "click"), (f.__name__.split("_")))
    @wraps(f)
    @click.command("-".join(names))
    def output(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except Exception as e:
            raise click.ClickException(str(e))
    return output
