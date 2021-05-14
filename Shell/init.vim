" vimtex
let g:vimtex_compiler_method='latexmk'
let g:vimtex_compiler_latexmk={'build_dir' : '/var/tmp/latex'}
let g:vimtex_quickfix_autojump=1
let g:vimtex_fold_enabled=1
let g:vimtex_view_method='zathura'
let g:vimtex_quickfix_method='pplatex'
let g:matchup_override_vimtex = 1
let g:vimtex_quickfix_open_on_warning=0
let g:vimtex_quickfix_ignore_filters = [
			\ 'Underfull',
			\ 'Overfull',
			\]
let g:vimtex_fold_types={
			\ 'comments' : {'enabled' : 1},
			\ 'sections' : {
			\ 'sections' : ['section', 'subsection', 'subsubsection'],
			\ },
			\ 'envs' : {
			\ 'blacklist': ['item'],
			\ }
			\ }
augroup math_edit
	autocmd!
	autocmd FileType tex setl dictionary+=../.dict | setl iskeyword+=- | setl complete=.,t,k
	autocmd FileType tex setl keywordprg=texdoc
	autocmd FileType tex nmap <localleader>ld <Plug>(vimtex-doc-package)
augroup end

" project rooter
set autochdir
" let g:rooter_cd_cmd='lcd'
" let g:rooter_patterns=['>Latex', '.git', 'package.json']
" let g:rooter_change_directory_for_non_project_files='current'

" linter
let g:ale_linters={
			\ 'vim': ['vimls'],
			\ 'text': ['writegood', 'languagetool', 'proselint'],
			\	'tex': ['proselint', 'texlab'],
			\	'mail': ['proselint', 'languagetool']
			\}

" mkdx plugin
let g:mkdx#settings={ 'highlight': { 'enable': 1 },
			\ 'enter': {'enable': 0 },
			\ 'links': { 'external': { 'enable': 1 } },
			\ 'fold': { 'enable': 1 },
			\ 'tab': { 'enable': 0 } }


let g:airline_theme='lucius'

" Netrw 
let g:netrw_sort_by='time'
let g:netrw_sort_direction='reverse'
let g:netrw_preview=1
let g:netrw_liststyle=3
let g:netrw_winsize=30
nmap - :Explore<enter>

" fzf-vim
" Mapping selecting mappings
nmap <leader><tab> <plug>(fzf-maps-n)
xmap <leader><tab> <plug>(fzf-maps-x)
omap <leader><tab> <plug>(fzf-maps-o)


" Insert mode completion
imap <c-x><c-k> <plug>(fzf-complete-word)
imap <c-x><c-f> <plug>(fzf-complete-path)
imap <c-x><c-l> <plug>(fzf-complete-line)

" sudo edit
let g:suda_smart_edit = 1

" Add system path if not presented
if stridx($PATH, 'node') == -1
	let $PATH .= ':/home/jing/.nvm/versions/node/v14.16.0/bin'
	let $PATH .= ':/usr/local/texlive/2021/bin/x86_64-linux'
endif

" formater
augroup formatter
	autocmd!
	autocmd FileType sh,zsh,bash nmap <buffer> <localleader>f :%!shfmt -ln bash -filename %<enter>
	autocmd FileType tex,bib nmap <buffer> <localleader>f :%!latexindent -c=/tmp/<enter>
	autocmd FileType javascript,html,vue,markdown,css,xhtml,scss nmap <buffer> <localleader>f :silent %!prettier --stdin-filepath %<CR>
	autocmd FileType json,jsonc nmap <buffer> <localleader>f :%!jq '.'<enter>
augroup END

" writing dairy
augroup notable
	autocmd!
	autocmd BufWritePre *otes/*.md 1,7s/\v^modified:\ "\zs.*\ze"$/\=system('date -Is | head -c -1')
	autocmd InsertEnter *otes/*.md silent !fcitx5-remote -c &>/dev/null
	autocmd VimEnter,InsertLeave *otes/*.md silent !fcitx5-remote -o &>/dev/null
augroup END

" input Chinese
augroup chinese
	autocmd!
	" for tg
	autocmd InsertEnter /tmp/tmp*.txt silent !fcitx5-remote -c &>/dev/null
	autocmd VimEnter,InsertLeave /tmp/tmp*.txt silent !fcitx5-remote -o &>/dev/null
	" for mutt
	autocmd VimEnter,InsertLeave /var/tmp/mutt-Matrix-* silent !fcitx5-remote -o &>/dev/null
augroup END

" use <Shift> key to select; see https://stackoverflow.com/a/4608387/7870953
set mouse=a
set showcmd
set tabstop=2
set softtabstop=2
set shiftwidth=2
set inccommand=nosplit

set undodir=/var/tmp/vim
set undofile
augroup rmundo
	autocmd!
	autocmd VimEnter /tmp/* set noundofile
augroup END

set conceallevel=2
set concealcursor=nc
hi Conceal NONE
hi Comment cterm=italic gui=italic
hi Pmenu ctermbg=NONE ctermfg=white
hi PmenuSel ctermfg=yellow

set foldmethod=syntax
set fillchars=fold:\ 

set modeline

" completion
set omnifunc=syntaxcomplete#Complete
