#!/bin/zsh
set -e
zathura_history=$HOME/.local/share/zathura/history
sed -n -E "s/^\[(.*)\]$/\1/p" $zathura_history | while read file; do
	if ! [[ -e $file ]]; then
		sed -i "s#\[$file\]#TOREMOVE#" $zathura_history
	fi
done
sed -i "/TOREMOVE/,/^$/d" $zathura_history
