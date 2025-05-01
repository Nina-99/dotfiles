return {
	"CRAG666/code_runner.nvim",
	dependencies = {
		"nvim-lua/plenary.nvim",
	},
	config = function()
		local code_runner = require("code_runner")

		code_runner.setup({
			-- put here the commands by filetype
			filetype = {
				java = "cd $dir && javac $fileName && java $fileNameWithoutExt",
				python = "python3 -u",
				cpp = "cd $dir && g++ $fileName -o $fileNameWithoutExt && $dir/$fileNameWithoutExt",
				typescript = "deno run",
				rust = "cd $dir && rustc $fileName && $dir/$fileNameWithoutExt",
			},
		})
		local keymap = vim.keymap
		keymap.set("n", "<leader>qe", ":RunCode<CR>", { noremap = true, silent = false }, { desc = "RunCode" })
		keymap.set("n", "<leader>qf", ":RunFile<CR>", { noremap = true, silent = false }, { desc = "RunFile" })
		keymap.set("n", "<leader>qft", ":RunFile tab<CR>", { noremap = true, silent = false }, { desc = "RunFile tab" })
		keymap.set("n", "<leader>qp", ":RunProject<CR>", { noremap = true, silent = false }, { desc = "RunProject" })
		keymap.set("n", "q", ":RunClose<CR>", { noremap = true, silent = false }, { desc = "RunClose" })
	end,
}
