#!/bin/sh
ckan -c /srv/app/production.ini harvester initdb
ckan -c /srv/app/production.ini ldap initdb
