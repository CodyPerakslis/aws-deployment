import csv
import subprocess
import os.path
from os import remove as os_remove
import click
from .click_tools import click_defaults

@click.argument("credentials-file")
@click.option("--profile", "-p", default="default")
@click.option("--region-value", "-r", default=None)
@click.option("--format-type", "-f", default=None)
@click.option("--rm", is_flag=True)
@click_defaults
def click_set_config(credentials_file, profile, region_value, format_type, rm):
    kwargs = {}
    if region_value:
        kwargs["region"] = region_value
    if format_type:
        kwargs["format"] = format_type
    from_credentials_file(credentials_file, profile, rm, **kwargs)


def from_credentials_file(cred, profile, remove, **kwargs):
    while cred.startswith("/"):
        cred = cred[1:]
    if os.path.isfile(os.path.join("./local", cred)):
        path = os.path.join("./local", cred)
    elif os.path.isfile(os.path.join("./absolute", cred)):
        path = os.path.join("./absolute", cred)
    else:
        raise Exception("File not found")
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        row = list(reader)[0]
        update_config("aws_access_key_id", row["Access key ID"], profile)
        update_config("aws_secret_access_key", row["Secret access key"], profile)
        for k in kwargs:
            update_config(k, kwargs[k], profile)
    if remove:
        os_remove(path)

def update_config(name, value, profile):
    command = "aws configure set {:s} {:s} --profile {:s}".format(name, value, profile)
    res = subprocess.run(command.split(' '), capture_output=True)
    if res.returncode != 0:
        raise Exception(x.stderr.decode("utf-8"))
