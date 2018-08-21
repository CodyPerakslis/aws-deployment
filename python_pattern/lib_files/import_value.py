import boto3
import click
from .click_tools import click_defaults

@click.option("--export-type", "-e", type=click.Choice(["cfn"]), default="cfn")
@click.argument("name")
@click_defaults
def click_import_value(export_type, name):
    if export_type == "cfn":
            print(cloudformation_export(name))

def cloudformation_export(name):
    cfn = boto3.client("cloudformation")
    paginator = cfn.get_paginator("list_exports")
    page_iter = paginator.paginate()
    for page in page_iter:
        for export in page["Exports"]:
            if export["Name"] == name:
                return export["Value"]
    raise Exception("{:s} is not a cloudformation export.".format(name))
