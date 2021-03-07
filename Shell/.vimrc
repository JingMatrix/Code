set background=dark
set nocompatible

" vimtex
let g:vimtex_compiler_method='latexmk'
let g:vimtex_compiler_latexmk={'build_dir' : '/var/tmp/latex'}
let g:vimtex_quickfix_autojump=1
let g:vimtex_quickfix_method='pplatex'


set conceallevel=2
hi Conceal NONE
let g:vimtex_view_method='zathura'

" mkdx plugin
let g:mkdx#settings={ 'highlight': { 'enable': 1 },
			\ 'enter': {'enable': 0 },
			\ 'links': { 'external': { 'enable': 1 } },
			\ 'fold': { 'enable': 1 },
			\ 'tab': { 'enable': 0 } }


let g:airline_theme='lucius'
let g:UltiSnipsExpandTrigger="<m-tab>"
let g:coc_node_path='/home/jing/.nvm/versions/node/v14.15.1/bin/node'

" formater
augroup formatter
	autocmd!
	autocmd FileType sh,zsh,bash nmap <leader>p :Shfmt<enter>
	autocmd FileType tex,bib nmap <leader>p :silent !latexindent -w -s -c=/tmp/ %<enter>:redraw!<enter>
augroup END

" writing dairy
augroup notable
	autocmd!
	autocmd BufWritePre *otes/*.md 1,7s/\v^modified:\ "\zs.*\ze"$/\=system('date -Is | head -c -1')
	autocmd InsertEnter *otes/*.md silent !ibus engine libpinyin &>/dev/null
	autocmd InsertLeave *otes/*.md silent !ibus engine xkb:us::eng &>/dev/null
	" we can achieve this by press shift
	" autocmd InsertEnter,InsertLeave *otes/*.md silent !xdotool key shift &
augroup end

" native function

"" use <Shift> key to select; see https://stackoverflow.com/a/4608387/7870953
set mouse=a
set showcmd
set pastetoggle=<F3>
let g:netrw_sort_by='time'
let g:netrw_sort_direction='reverse'
set tabstop=2
set softtabstop=2
set shiftwidth=2

set relativenumber
augroup numbertoggle
	autocmd!
	autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
	autocmd BufLeave,FocusLost,InsertEnter   * set norelativenumber
augroup END

set undodir=/var/tmp/vim
set undofile
set directory=/var/tmp/vim/swap//
augroup rmundo
	autocmd!
	autocmd VimEnter /tmp/* set noundofile
augroup END
set textwidth=0
highlight Comment cterm=italic gui=italic

set path+=..
hi Pmenu ctermbg=NONE ctermfg=white
hi PmenuSel ctermfg=yellow

let g:netrw_preview=1
let g:netrw_liststyle = 3
let g:netrw_winsize   = 30
nmap - :Explore<enter>

set autochdir
