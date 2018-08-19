import boto3

class ValueNotFound(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

def cloudformation_export(name):
    cfn = boto3.client("cloudformation")
    paginator = cfn.get_paginator("list_exports")
    page_iter = paginator.paginate()
    for page in page_iter:
        for export in page["Exports"]:
            if export["Name"] == name:
                return export["Value"]
    raise ValueNotFound("{:s} is not a cloudformation export.".format(name))
