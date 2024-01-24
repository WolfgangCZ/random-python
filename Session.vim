let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd D:/_coding/python-course
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +187 09_pong/09pingpong.py
badd +33 15_space_invaders/main.py
badd +1 term://D:/_coding/python-course/15_space_invaders//16036:C:/Windows/System32/cmd.exe
badd +9161 term://D:/_coding/python-course/15_space_invaders//10604:C:/Windows/System32/cmd.exe
badd +10024 term://D:/_coding/python-course/15_space_invaders//17616:C:/Windows/System32/cmd.exe
badd +0 term://D:/_coding/python-course/15_space_invaders//9876:C:/Windows/System32/cmd.exe
argglobal
%argdel
edit 15_space_invaders/main.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 152 + 104) / 209)
exe 'vert 2resize ' . ((&columns * 56 + 104) / 209)
argglobal
balt 09_pong/09pingpong.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 20 - ((19 * winheight(0) + 24) / 49)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 20
normal! 015|
wincmd w
argglobal
if bufexists(fnamemodify("term://D:/_coding/python-course/15_space_invaders//9876:C:/Windows/System32/cmd.exe", ":p")) | buffer term://D:/_coding/python-course/15_space_invaders//9876:C:/Windows/System32/cmd.exe | else | edit term://D:/_coding/python-course/15_space_invaders//9876:C:/Windows/System32/cmd.exe | endif
if &buftype ==# 'terminal'
  silent file term://D:/_coding/python-course/15_space_invaders//9876:C:/Windows/System32/cmd.exe
endif
balt 15_space_invaders/main.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 8886 - ((48 * winheight(0) + 24) / 49)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 8886
normal! 0
lcd D:/_coding/python-course/15_space_invaders
wincmd w
exe 'vert 1resize ' . ((&columns * 152 + 104) / 209)
exe 'vert 2resize ' . ((&columns * 56 + 104) / 209)
tabnext 1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
let &shortmess = s:shortmess_save
let &winminheight = s:save_winminheight
let &winminwidth = s:save_winminwidth
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
