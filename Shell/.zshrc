plugins=(git nvm npm zsh_reload vi-mode pip)
plugins+=(z.lua)
plugins+=(zsh-syntax-highlighting)
source $ZSH/oh-my-zsh.sh

function ocr {
	if [[ $(wl-paste --list-types | head -1) =~ ^image ]]; then
		wl-paste -t image/png >/tmp/clip.png
	else
		echo "No images in clipboard, try images on disk"
	fi
	if [[ -f /tmp/clip.png ]]; then
		tesseract /tmp/clip.png - -l $1 quiet | head -n -1 | wl-copy
		wl-paste
	else
		echo "No images on disk, please take a new screenshot"
		gnome-screenshot -f /tmp/clip.png -a
	fi
}

function _ocr {
	local -a ocr_langs
	ocr_langs=('chi_sim:Simplified Chinese'
		'chi_tra:Traditional Chinese'
		'eng:English'
		'fra:French')
	_describe ocr ocr_langs
}

compdef _ocr ocr

alias sg="TERM=xterm googler -n 5"
alias sd="TERM=xterm ddgr -n 5"
alias gcl="git clone --recursive --shallow-submodules --depth 1"

export PATH="$PATH:$HOME/.cargo/bin"
export PATH="$PATH:$HOME/.gem/ruby/2.7.0/bin"
export GOPATH="$HOME/.local/go"
export PATH="$PATH:$GOPATH/bin"
export PATH="$PATH:$HOME/Documents/Code/Shell/scripts"
export MANPAGER='nvim +Man!'
export MUTTBOX="gmail"

# keybinding
function keep-buffer {
	wl-copy -p $BUFFER
	BUFFER=''
}
zle -N keep-buffer
bindkey "^Y" redo
bindkey "^Z" undo
bindkey "^F" run-help
bindkey "^K" keep-buffer
bindkey "^H" backward-kill-word

# zsh-highlight

ZSH_HIGHLIGHT_HIGHLIGHTERS=(main brackets pattern cursor line)
typeset -A ZSH_HIGHLIGHT_STYLES
ZSH_HIGHLIGHT_STYLES[cursor]=bold
