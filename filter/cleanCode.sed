# remove LineIds
/<LineId/d
/<\/LineId/d
# enforce empty first line
/CDATA\[[^\r]/s/\[CDATA\[/\[CDATA\[\r\n/g
# enforce empty last line
/.\]\]>/s/]]>/\r\n]]>/g
# convert tab to space
/\t/s/\t/    /g
# remove trailing space
s/[[:blank:]]*$//
s/[[:blank:]]*\r$/\r/

# add trailing line
$s/>/>\r\n/
