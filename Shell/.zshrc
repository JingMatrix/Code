plugins=(git nvm zsh_reload vi-mode pip)
plugins+=(yarn-autocompletions tldr nnn)
plugins+=(z.lua)
plugins+=(zsh-syntax-highlighting)
source $ZSH/oh-my-zsh.sh

export LANG=fr_FR.UTF-8

alias zshconfig="vim $HOME/Documents/Code/Shell/.zshrc"
alias pasteimg="xclip -selection clipboard -t image/png -o > /tmp/clip.png"
alias ocrchi="pasteimg && tesseract  /tmp/clip.png - -l chi_sim 2> /dev/null"
alias ocren="pasteimg && tesseract  /tmp/clip.png - -l eng 2> /dev/null"
alias ocrfr="pasteimg && tesseract  /tmp/clip.png - -l fra &> /dev/null"
alias ocrmath="app_id=$app_id app_key=$app_key ~/Documents/Code/Shell/mathpix"
alias vim="vim --servername VIM"
alias sg="googler -n 5"
alias sd="ddgr -n 5"
alias b="buku --suggest"
alias gcl="git clone --recursive --shallow-submodules --depth 1"
alias pd="pandoc --wrap=none"
alias w="nnn -T t -P n $HOME/Documents/Notes/notes"

export MUTTBOX=gmail
export BROWSER=w3m
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

if [[ -z $POEM ]]; then
	fortune -e tang300 song100 chinese
	export POEM=1
fi

# nnn config

export NNN_ARCHIVE="\\.(7z|a|ace|alz|arc|arj|bz|bz2|cab|cpio|deb|epub|gz|jar|lha|lz|lzh|lzma|lzo|rar|rpm|rz|t7z|tar|tbz|tbz2|tgz|tlz|txz|tZ|tzo|war|xpi|xz|Z|zip)$"
export NNN_BMS="m:~/Mathematics;a:~/Mathematics/Textbook_Archive;c:~/Documents/Code;p:~/Documents/Project;"
export NNN_FIFO="/tmp/nnn.fifo"
export NNN_PLUG="n:preview-note;f:fzcd;j:autojump"
source "$HOME/Documents/Project/nnn/misc/quitcd/quitcd.bash_zsh"
export FZF_DEFAULT_COMMAND='fd --type file --follow --hidden --exclude .git'
export FZF_DEFAULT_OPTS="--ansi"

# zsh-highlight

ZSH_HIGHLIGHT_HIGHLIGHTERS=(main brackets pattern cursor line)
