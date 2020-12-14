set nocompatible 
filetype plugin indent on

" vimtex
let g:vimtex_compiler_method='tectonic'

set mouse=v
set showcmd
set pastetoggle=<F3>
let g:netrw_sort_by='time'
let g:netrw_sort_direction='reverse'

let g:mkdx#settings     = { 'highlight': { 'enable': 1 },
			\ 'enter': { 'shift': 1 },
			\ 'links': { 'external': { 'enable': 1 } },
			\ 'fold': { 'enable': 1 } }


let g:airline_theme='luna'

augroup notable
	autocmd!
	autocmd BufWritePost /home/jing/Notes/*.md 1,7s/\v^modified:\ "\zs.*\ze"$/\=system('date -Is | head -c -1')
augroup end

set conceallevel=2
hi clear conceal
