#! /bin/zsh

for d in ~/.vim/pack/*/*/* ~/.oh-my-zsh/custom/plugins/* ~/Documents/Project/*; do
	(
		cd "$d"
		echo $d && [[ -d .git ]] && git pull --rebase
	)
done
