#!/bin/sh
brew install postgres
#To reload postgresql after an upgrade:
#    launchctl unload ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist
#    launchctl load ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist
#Or, if you don't want/need launchctl, you can just run:
#    postgres -D /usr/local/var/postgres
#==> Summary
createdb
psql

