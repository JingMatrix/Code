set background=dark
set nocompatible

" vimtex
let g:vimtex_compiler_method='tectonic'
let g:vimtex_compiler_tectonic={'build_dir' : '/var/tmp/latex', 'executable': '~/.cargo/bin/tectonic'}

set conceallevel=2
hi Conceal NONE
let g:vimtex_view_method='zathura'

" CoC plugin
augroup coc
	autocmd!
	autocmd VimEnter *Documents/Project/* packadd coc.nvim
augroup end

" mkdx plugin
let g:mkdx#settings={ 'highlight': { 'enable': 1 },
			\ 'enter': { 'shift': 1 },
			\ 'links': { 'external': { 'enable': 1 } },
			\ 'fold': { 'enable': 1 } }


let g:airline_theme='lucius'

" writing dairy
augroup notable
	autocmd!
	autocmd BufWritePre *otes/*.md 1,7s/\v^modified:\ "\zs.*\ze"$/\=system('date -Is | head -c -1')
	autocmd InsertEnter *otes/*.md silent !ibus engine libpinyin
	autocmd InsertLeave *otes/*.md silent !ibus engine xkb:us::eng
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

set number relativenumber
augroup numbertoggle
  autocmd!
  autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
  autocmd BufLeave,FocusLost,InsertEnter   * set norelativenumber
augroup END

set undodir=/var/tmp/vim
set undofile
set textwidth=0
highlight Comment cterm=italic gui=italic
