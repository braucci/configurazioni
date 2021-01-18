set encoding=utf-8
set number relativenumber
syntax enable
set noswapfile
set scrolloff=7
set backspace=indent,eol,start
set guifont=Monaco\ 16

set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab
set autoindent
set fileformat=unix
set laststatus=2
set nocompatible              " required
filetype off                  " required
                                                 

map <F6> {!}par jw72 <%

" set number
" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" add all your plugins here (note older versions of Vundle
" used Bundle instead of Plugin)
Plugin 'preservim/nerdtree'
Plugin 'jaredgorski/spacecamp'
Plugin 'jiangmiao/auto-pairs'
Plugin 'artanikin/vim-synthwave84'
Plugin 'xuhdev/vim-latex-live-preview'
Plugin 'itchyny/lightline.vim'
Plugin 'ap/vim-css-color'
" ...

" All of your Plugins must be added before the following line
call vundle#end()            " required

filetype plugin indent on    " required
nnoremap <silent> <F2> :NERDTreeToggle<CR>


let g:lightline = {
      \ 'colorscheme': 'wombat',
      \ }



let g:NERDTreeNodeDelimiter = "\u00a0"
syntax on
set backspace=indent,eol,start
"split navigations
autocmd FileType python map <buffer> <C-B> :w<CR>:exec '!python3' shellescape(@%, 1)<CR>
autocmd FileType python imap <buffer> <C-B> <esc>:w<CR>:exec '!python3' shellescape(@%, 1)<CR>

nnoremap <C-J> <C-W><C-J> "Ctr-J --> Move to the bottom
nnoremap <C-K> <C-W><C-K> "Ctr-K --> Move to the top
nnoremap <C-L> <C-W><C-L> "Ctr-L --> Move to the right
nnoremap <C-H> <C-W><C-H> "Ctr-H --> Move to the left
" colorscheme spacecamp
" colorscheme synthwave84
autocmd Filetype tex setl updatetime=1
let g:livepreview_previewer = 'evince'
