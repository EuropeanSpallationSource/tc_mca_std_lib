#!/bin/sh
git grep '.\]\]>' *.Tc*
if test $? -ne 1; then
  echo >&2 "code before double square brackets found"
  exit 1
fi
