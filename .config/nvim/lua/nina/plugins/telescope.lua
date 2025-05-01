return {
	"nvim-telescope/telescope.nvim",
	-- branch = "0.1.x",
	event = "VeryLazy",
	dependencies = {
		"nvim-lua/plenary.nvim",
		"nvim-telescope/telescope-file-browser.nvim",
		{ "nvim-telescope/telescope-fzf-native.nvim", build = "make" },
		"nvim-tree/nvim-web-devicons",
	},
	opts = {
		extensions = {
			fzf = {
				fuzzy = true,
				override_generic_sorter = true,
				override_file_sorter = true,
				case_mode = "smart_case",
			},
		},
	},
	config = function(opts)
		require("telescope").setup(opts)
		require("telescope").load_extension("fzf")
		local telescope = require("telescope")
		local actions = require("telescope.actions")

		telescope.setup({
			defaults = {
				path_display = { "smart" },
				mappings = {
					i = {
						["<C-k>"] = actions.move_selection_previous, -- move to prev result
						["<C-j>"] = actions.move_selection_next, -- move to next result
						["<C-q>"] = actions.send_selected_to_qflist + actions.open_qflist,
					},
				},
			},
		})

		--telescope.load_extension("fzf")

		-- set keymaps
		local keymap = vim.keymap -- for conciseness

		keymap.set("n", "<leader>ff", "<cmd>Telescope find_files<cr>", { desc = "Fuzzy find files in cwd" })
		keymap.set("n", "<leader>fr", "<cmd>Telescope oldfiles<cr>", { desc = "Fuzzy find recent files" })
		keymap.set("n", "<leader>fs", "<cmd>Telescope<cr>", { desc = "Find string in cwd" })
		keymap.set("n", "<leader>fc", "<cmd>Telescope grep_string<cr>", { desc = "Find string under cursor in cwd" })
		keymap.set("n", "<leader>ft", "<cmd>TodoTelescope<cr>", { desc = "Find todos" })
		keymap.set("n", "<leader>gf", "<cmd>Telescope git_file<cr>", { desc = "Telescope Git Files" })
		keymap.set("n", "<leader>gs", "<cmd>Telescope git_status<cr>", { desc = "Telescope Git status" })
		keymap.set("n", "<leader>gc", "<cmd>Telescope git_bcomits<cr>", { desc = "Telescope Git status" })
		keymap.set("n", "<leader>gb", "<cmd>Telescope git_branches<cr>", { desc = "Telescope Git branches" })
		keymap.set("n", "<leader>fb", "<cmd>Telescope buffers<cr>", { desc = "Telescope buffers" })
	end,
}
