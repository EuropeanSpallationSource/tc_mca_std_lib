# remove LineIds
/<LineId/d
/<\/LineId/d
# Add a line after ]]
/.\]\]>/s/]]>/\r\n]]>/g
# convert tab to space
/\t/s/\t/    /g
# remove trailing space
s/[[:blank:]]*$//
s/[[:blank:]]*\r$/\r/
