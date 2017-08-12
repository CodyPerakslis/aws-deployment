#!/bin/bash

echo "Setting-up bash pattern (only needs to happen once) ..."
echo "Re-initialize after any changes to aws_container image"

docker build -t aws_container .
chmod +x myAws
ln -s `pwd`/myAws /usr/local/bin/myAws

echo "Complete. Run myAws to open."
