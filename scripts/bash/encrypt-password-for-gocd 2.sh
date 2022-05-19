#!/bin/bash

PASSWORD=$1

encrypted=$(python -c "import sha; from base64 import b64encode; print b64encode(sha.new('${PASSWORD}').digest())")

echo $encrypted