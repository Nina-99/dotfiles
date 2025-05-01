vim.cmd("let g:netrw_liststyle = 0")

local opt = vim.opt

opt.relativenumber = true
opt.number = true

-- tabs & indentation
opt.tabstop = 4 -- 4 spaces for tabs (prettier default)
opt.shiftwidth = 4 -- 4 spaces for indent width
opt.expandtab = true -- expand tab to spaces
opt.autoindent = true -- copy indent from current line when starting new one

opt.wrap = false

-- search settings
opt.ignorecase = true -- ignore case when searching
opt.smartcase = true -- if you include mixed case in your search, assumes you want case-sensitive

opt.cursorline = true

-- turn on termguicolors for tokyonight colorscheme to work
-- (have to use iterm2 or any other true color terminal)
opt.termguicolors = true
opt.background = "dark" -- colorschemes that can be light or dark will be made dark
opt.signcolumn = "yes" -- show sign column so that text doesn't shift

-- backspace
opt.backspace = "indent,eol,start" -- allow backspace on indent, end of line or insert mode start position

-- clipboard
-- opt.clipboard:append("unnamedplus") -- use system clipboard as default register

-- split windows
opt.splitright = true -- split vertical window to the right
opt.splitbelow = true -- split horizontal window to the bottom

-- turn off swapfile
opt.swapfile = false

opt.clipboard = "unnamedplus"

-- if vim.fn.has("wsl") == 1 then
-- 	if vim.fn.executable("wl-copy") == 0 then
-- 		print("wl-clipboard not found, clipboard integration won't work")
-- 	else
-- 		vim.g.clipboard = {
-- 			name = "wl-clipboard (wsl)",
-- 			copy = {
-- 				["+"] = "wl-copy --foreground --type text/plain",
-- 				["*"] = "wl-copy --foreground --primary --type text/plain",
-- 			},
-- 			paste = {
-- 				["+"] = function()
-- 					return vim.fn.systemlist('wl-paste --no-newline|sed -e "s/\r$//"', { "" }, 1) -- '1' keeps empty lines
-- 				end,
-- 				["*"] = function()
-- 					return vim.fn.systemlist('wl-paste --primary --no-newline|sed -e "s/\r$//"', { "" }, 1)
-- 				end,
-- 			},
-- 			cache_enabled = true,
-- 		}
-- 	end
-- end

-- curl -sLo/tmp/win32yank.zip https://github.com/equalsraf/win32yank/releases/download/v0.1.1/win32yank-x64.zip
-- unzip -p /tmp/win32yank.zip win32yank.exe > /tmp/win32yank.exe
-- chmod +x /tmp/win32yank.exe
-- sudo mv /tmp/win32yank.exe /usr/local/bin/
-- vim.g.clipboard = {
-- 	name = "win32yank-wsl",
-- 	copy = {
-- 		["+"] = "win32yank.exe -i --crlf",
-- 		["*"] = "win32yank.exe -i --crlf",
-- 	},
-- 	paste = {
-- 		["+"] = "win32yank.exe -o --lf",
-- 		["*"] = "win32yank.exe -o --lf",
-- 	},
-- 	cache_enabled = true,
-- }
