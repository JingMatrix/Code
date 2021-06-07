" vimtex
let g:vimtex_compiler_method='latexmk'
let g:vimtex_compiler_latexmk={'build_dir' : '/var/tmp/latex'}
let g:vimtex_fold_enabled=1
let g:vimtex_fold_manual=1
let g:vimtex_view_method='zathura'
let g:vimtex_view_zathura_options='--mode=fullscreen'
let g:vimtex_quickfix_method='pplatex'
let g:matchup_override_vimtex=1
let g:vimtex_quickfix_open_on_warning=0
let g:vimtex_syntax_nospell_commands=['YYCleverefInput']
let g:vimtex_syntax_nospell_comments=1
let g:vimtex_grammar_vlty={'lt_command': 'languagetool',
			\'lt_disablecategories': 'TYPOGRAPHY,TYPOS'}
let g:vimtex_quickfix_ignore_filters=[
			\'Underfull',
			\'Overfull',
			\'Fandol',
			\'multiple pdfs with page group',
			\]
let g:vimtex_fold_types={'comments' : {'enabled' : 1}}
augroup math_edit
	autocmd!
	" Fix latex log jump for project files
	autocmd FileType tex nmap <localleader>ll :exe 'lcd' b:vimtex.root <bar> VimtexCompile <cr>
	autocmd FileType tex nmap <buffer> <F9> :setl spell <bar> silent! w <bar> compiler vlty <bar> make <bar> :cw <cr><esc>
	autocmd FileType tex setl dictionary+=../.dict | setl iskeyword+=- | setl complete=.,t,k
	autocmd FileType tex setl keywordprg=texdoc
	autocmd FileType tex nmap <localleader>ld <Plug>(vimtex-doc-package)
augroup end

" startify
let g:startify_skiplist=['doc/.*\.txt$', '.*/tmp/*', 'Notes/notes/.*\.md$', 'Code/Shell/.*']
let g:startify_bookmarks=[{'z': '$HOME/Documents/Code/Shell/.zshrc'},
			\{'n': '$HOME/Notes'},
			\{'v': '$HOME/Documents/Code/Shell/init.vim'},
			\{'a': '$HOME/Documents/Code/Shell/alacritty.yml'},
			\]
let g:startify_custom_header_quotes=[
			\['Where is your improvement in five years?'],
			\['Do you feel sorry about yourself?'],
			\['Are you escaping from yourself?']]

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
let g:suda_smart_edit=1

" Add system path if not presented
if stridx($PATH, 'node')==-1
	let $PATH .=':/home/jing/.nvm/versions/node/v14.16.0/bin'
endif

" formater
augroup formatter
	autocmd!
	autocmd FileType sh,zsh,bash nmap <buffer> <localleader>f
				\ :silent %!shfmt -ln bash -filename % <cr> :w <esc> 2g;
	autocmd FileType tex,bib nmap <buffer> <localleader>f
				\	:silent %!latexindent -m -c=/tmp/ <cr> :w <esc> 2g;
	autocmd FileType javascript,html,vue,markdown,css,xhtml,scss,xml nmap <buffer> <localleader>f
				\ :silent %!prettier --stdin-filepath % <cr> :w <esc> 2g;
	autocmd FileType json,jsonc nmap <buffer> <localleader>f
				\ :silent %!jq '.' <cr> :w <esc> 2g;
augroup END

" writing dairy
augroup notable
	autocmd!
	autocmd BufWritePre *otes/*.md 1,7s/\v^modified:\ "\zs.*\ze"$/\=system('date -Is | head -c -1')
	autocmd InsertEnter *otes/*.md silent !fcitx5-remote -c &>/dev/null
	autocmd BufEnter,InsertLeave *otes/*.md silent !fcitx5-remote -o &>/dev/null
augroup END

" input Chinese
augroup chinese
	autocmd!
	" for tg
	autocmd InsertEnter /tmp/tmp*.txt silent !fcitx5-remote -c &>/dev/null
	autocmd BufEnter,InsertLeave /tmp/tmp*.txt silent !fcitx5-remote -o &>/dev/null
	" for mutt
	autocmd BufEnter,InsertLeave /var/tmp/mutt-Matrix-* silent !fcitx5-remote -o &>/dev/null
	autocmd FileType markdown setl spelllang+=cjk
augroup END

" use <Shift> key to select; see https://stackoverflow.com/a/4608387/7870953
set mouse=a
set showcmd
set inccommand=split
set scrolloff=5
set undodir=/var/tmp/vim
set backupdir=/var/tmp/vim
set undofile
augroup rmundo
	autocmd!
	autocmd VimEnter /tmp/* set noundofile
augroup END

set spelllang=en_gb
set conceallevel=2
set concealcursor=nc
hi Conceal NONE
hi Comment cterm=italic gui=italic ctermfg=gray
hi Pmenu ctermbg=NONE ctermfg=white
hi PmenuSel ctermfg=yellow

set hidden
set autowrite
set foldmethod=syntax
set fillchars=fold:\ 
set showtabline=0
set modeline

" completion
set omnifunc=v:lua.vim.lsp.omnifunc 

" lsp
lua require('lspconfig').vimls.setup{}
lua require('lspconfig').tsserver.setup{}
lua require('lspconfig').pyright.setup{}
lua require('lspconfig').texlab.setup{}
