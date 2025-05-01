return {
	"akinsho/toggleterm.nvim",
	config = function()
		local toggleterm = require("toggleterm")
		toggleterm.setup({

			size = 55,
			open_mapping = [[<c-t>]],
			shade_filetypes = {},
			direction = "vertical",
		})
	end,
}
