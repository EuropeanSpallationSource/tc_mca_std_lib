#!/bin/sh
git --no-pager grep '<Declaration><!\[CDATA\[[A-Z]'  *.Tc*
if test $? -ne 1; then
  echo >&2 "CDATA with code found. Configure and run filters"
  exit 1
fi
