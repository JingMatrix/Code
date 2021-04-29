plugins=(git nvm npm zsh_reload vi-mode pip)
plugins+=(z.lua)
plugins+=(zsh-syntax-highlighting)
source $ZSH/oh-my-zsh.sh

function ocr {
	if [[ $(wl-paste --list-types | head -1) == image/tiff ]]; then
		wl-paste -t image/png >/tmp/clip.png
	else
		echo "No images in clipboard, try images on disk"
	fi
	if [[ -f /tmp/clip.png ]]; then
		tesseract /tmp/clip.png - -l $1 1 2>/dev/null &>/dev/tty |
			head -n -1 | wl-copy
	else
		echo "No images on disk, please take a new screenshot"
		gnome-screenshot -f /tmp/clip.png -a
	fi
}
function _ocr {
	local -a ocr_langs
	ocr_langs=('chi_sim:Chinese' 'eng:English' 'fra:French')
	_describe ocr ocr_langs
}

compdef _ocr ocr

alias zshconfig="vim $HOME/Documents/Code/Shell/.zshrc"
alias sg="TERM=xterm googler -n 5"
alias sd="TERM=xterm ddgr -n 5"
alias b="buku --suggest"
alias gcl="git clone --recursive --shallow-submodules --depth 1"
alias glols="PAGER=less git log --graph --pretty='%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --stat"
alias pd="pandoc --wrap=none"
alias w="nnn -a -T t -P n $HOME/Documents/Notes/notes"

export PATH="$PATH:$HOME/.cargo/bin"
export PATH="$PATH:$HOME/.gem/ruby/2.7.0/bin"
export GOPATH="$HOME/.local/go"
export PATH="$PATH:$GOPATH/bin"
export PATH="$PATH:$HOME/Documents/Code/Shell/scripts"
export PAGER="nvimpager"
export MUTTBOX="gmail"

# keybinding
function keep-buffer {
	xclip <<<$BUFFER
}
zle -N keep-buffer
bindkey "^Y" redo
bindkey "^Z" undo
bindkey "^F" run-help
bindkey "^K" kill-line
bindkey "^H" backward-kill-word
bindkey "^Xx" keep-buffer

fortune -e tang300 song100 chinese

# zsh-highlight

ZSH_HIGHLIGHT_HIGHLIGHTERS=(main brackets pattern cursor line)
typeset -A ZSH_HIGHLIGHT_STYLES
ZSH_HIGHLIGHT_STYLES[cursor]=bold

# texlive install
export PATH="$PATH:/usr/local/texlive/2021/bin/x86_64-linux"
