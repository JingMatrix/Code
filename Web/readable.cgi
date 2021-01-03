#!/bin/zsh
# enable read mode in w3m
# dependencies: zsh, readability-cli (node.js module)
# place to this file in /urs/lib/w3m/cgi-bin with sudo
# then assign a keymap in .w3m/keymap, for example, write following to this file: 
# keymap r GOTO /urs/lib/w3m/cgi-bin/readable.cgi
#
echo "Content-type: text/html\n"
if [[ $W3M_SOURCEFILE:e == "gz" ]]
then
	tmp_html=/tmp/html
	gzip -cd $W3M_SOURCEFILE | readable -q -
else
	readable -q $W3M_SOURCEFILE
fi
