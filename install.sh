#!/bin/sh

# Download latest version of repo to /opt/rkr-logger
cd /opt
mkdir -p rkr-logger
curl -sL https://github.com/thetimmorland/rkr-logger/tarball/master\
	| tar xz --directory rkr-logger --strip-components 1

# Additional steps go below
# modify /boot/config.txt (see https://stackoverflow.com/questions/20267910/how-to-add-a-line-in-sed-if-not-match-is-found/30736034)

# install apt dependencies
apt-get install can-utils
