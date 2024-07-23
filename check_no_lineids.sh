#!/bin/sh
git grep '<LineIds' *.Tc*
if test $? -ne 1; then
  echo >&2 "LineIds found"
  exit 1
fi
