set nocompatible
filetype plugin indent on

" vimtex
let g:vimtex_compiler_method='tectonic'

set mouse=v
set showcmd
set pastetoggle=<F3>
let g:netrw_sort_by='time'
let g:netrw_sort_direction='reverse'

let g:coc_node_path='/home/jing/.nvm/versions/node/v14.15.1/bin/node'

let g:mkdx#settings     = { 'highlight': { 'enable': 1 },
			\ 'enter': { 'shift': 1 },
			\ 'links': { 'external': { 'enable': 1 } },
			\ 'fold': { 'enable': 1 } }


let g:airline_theme='lucius'

" writing dairy

augroup notable
	autocmd!
	autocmd BufWritePost *otes/*.md 1,7s/\v^modified:\ "\zs.*\ze"$/\=system('date -Is | head -c -1')
augroup end

set conceallevel=2
hi Conceal NONE
let g:vimtex_view_method='zathura'

set tabstop=2
set softtabstop=2
set shiftwidth=2

" show number in sidebar

set number relativenumber

augroup numbertoggle
  autocmd!
  autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
  autocmd BufLeave,FocusLost,InsertEnter   * set norelativenumber
augroup END
