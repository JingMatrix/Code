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
let g:vimtex_grammar_vlty={'lt_command': 'languagetool'}
let g:vimtex_quickfix_ignore_filters=[
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
let g:startify_change_to_dir=1
let g:startify_skiplist=['doc/.*\.txt$', '.*/tmp/*', 'Notes/notes/.*\.md$', 'Code/Shell/.*']
let g:startify_files_number=5
let g:startify_bookmarks=[
			\{'z': '$HOME/Documents/Code/Shell/.zshrc'},
			\{'n': '$HOME/Notes'},
			\{'v': '$HOME/Documents/Code/Shell/init.vim'},
			\{'a': '$HOME/Documents/Code/Shell/alacritty.yml'},
			\]
let g:startify_lists=[
			\{ 'type': 'dir',       'header': ['   MRU '. getcwd()] },
			\{ 'type': 'sessions',  'header': ['   Sessions']       },
			\{ 'type': 'bookmarks', 'header': ['   Bookmarks']      },
			\]
let g:startify_custom_header_quotes=[
			\['Where is your improvement in five years?'],
			\['Do you feel sorry about yourself?'],
			\['Are you escaping from yourself?']]
nnoremap <c-h> :Startify<cr><esc>

" Airline
let g:airline_theme='apprentice'
let g:airline#extensions#whitespace#skip_indent_check_ft={'tex': ['indent']}
let g:airline_powerline_fonts=1
let g:airline#extensions#tabline#enabled=1
let g:airline#extensions#tabline#buffer_min_count=2

" Netrw
let g:netrw_sort_by='time'
let g:netrw_sort_direction='reverse'
let g:netrw_preview=1
let g:netrw_liststyle=3
let g:netrw_winsize=30

" mkdx
let g:mkdx#settings={'highlight': {'enable': 1},
			\'enter': {'enable': 0},
			\'fold': {'enable': 1}}

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
	let $PATH .=':/home/jing/.nvm/versions/node/v16.3.0/bin'
endif

" formater
augroup formatter
	autocmd!
	autocmd FileType sh,zsh,bash setl formatprg=shfmt\ -ln\ bash\ -filename\ %
	"% <cr> :w <esc> 2g;
	autocmd FileType tex,bib setl formatprg=latexindent\ -m\ -c=/tmp/
	autocmd FileType javascript,html,vue,markdown,css,xhtml,scss,xml setl formatprg=prettier\ --stdin-filepath\ %
	autocmd FileType json,jsonc setl formatprg=jq\ '.'
augroup END


" input Chinese
function ToggleChineseInput()
	if !exists('#chinese#InsertEnter')
		augroup chinese
			autocmd! * <buffer>
			autocmd InsertEnter <buffer> silent !fcitx5-remote -c &>/dev/null
			autocmd InsertLeave <buffer> silent !fcitx5-remote -o &>/dev/null
		augroup END
	else
		augroup chinese
			autocmd! * <buffer>
		augroup END
	endif
endfunction
nmap yoz :call ToggleChineseInput()<cr>
augroup toggles
	autocmd!
	autocmd BufEnter /tmp/tmp*.txt,*otes/*.md normal yoz
augroup END

" writing dairy
augroup notable
	autocmd!
	autocmd BufWritePre *otes/*.md 1,7s/\v^modified:\ "\zs.*\ze"$/\=system('date -Is | head -c -1')
	autocmd FileType markdown setl spelllang+=cjk
augroup END

" custom mapping
nnoremap <c-t> :vsplit \| terminal<cr>i

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

set spelllang=en_us
set conceallevel=2
set concealcursor=nc
hi Conceal NONE
hi Comment cterm=italic ctermfg=gray
hi Pmenu ctermbg=NONE ctermfg=white
hi PmenuSel ctermfg=yellow

set hidden
set autowrite
set autochdir
set foldmethod=syntax
set fillchars=fold:\ ,
set modeline

" completion
set omnifunc=syntaxcomplete#Complete

" tree-sitter
lua require('nvim-treesitter.configs').setup{ highlight = { enable = true, } }
