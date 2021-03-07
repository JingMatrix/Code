plugins=(git nvm zsh_reload vi-mode pip)
plugins+=(z.lua)
plugins+=(zsh-syntax-highlighting)
source $ZSH/oh-my-zsh.sh

alias zshconfig="vim $HOME/Documents/Code/Shell/.zshrc"
alias pasteimg="xclip -selection clipboard -t image/png -o > /tmp/clip.png"
alias ocrchi="pasteimg && tesseract  /tmp/clip.png - -l chi_sim 2> /dev/null"
alias ocren="pasteimg && tesseract  /tmp/clip.png - -l eng 2> /dev/null"
alias ocrfr="pasteimg && tesseract  /tmp/clip.png - -l fra &> /dev/null"
alias ocrmath="app_id=$app_id app_key=$app_key ~/Documents/Code/Shell/mathpix"
alias sg="TERM=xterm googler -n 5"
alias sd="TERM=xterm ddgr -n 5"
alias b="buku --suggest"
alias gcl="git clone --recursive --shallow-submodules --depth 1"
alias pd="pandoc --wrap=none"
alias w="nnn -a -T t -P n $HOME/Documents/Notes/notes"

function v {
	vim --servername $RANDOM $@
}

export PATH="$PATH:$HOME/.cargo/bin"
export PATH="$PATH:$HOME/.gem/ruby/2.7.0/bin"
export GOPATH="$HOME/.local/go"
export PATH="$PATH:$GOPATH/bin"
export PATH="$PATH:$HOME/Documents/Code/Shell/scripts"
export LESSOPEN="| /usr/share/source-highlight/src-hilite-lesspipe.sh %s"

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
