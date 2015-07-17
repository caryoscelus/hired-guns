#! /usr/bin/env bash

# this script will update dependencies of hired-guns inside ren'py directory
# you can edit it to contain appropriate variables with paths
# should be run in ren'py core directory
# DRACYKEITON=/path/to/dracykeiton
# HIREDGUNS=/path/to/hired-guns/core

source ./env/bin/activate

pushd ${DRACYKEITON}
git pull
pip install --no-deps --no-index -U .
popd

pushd ${HIREDGUNS}
git pull
pip install --no-deps --no-index -U .
popd

