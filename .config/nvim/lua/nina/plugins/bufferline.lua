return {
	"akinsho/bufferline.nvim",
	keys = {
		{ "[B", "<cmd>BufferLineMovePrev<cr>", desc = "Swap with prev buffer" },
		{ "]B", "<cmd>BufferLineMoveNext<cr>", desc = "Swap with next buffer" },
	},
	---@param opts bufferline.UserConfig
	opts = function(_, opts)
		opts.options.show_close_icon = true
		-- opts.options.separator_style = "slant"
		opts.options.offsets = {
			{
				filetype = "neo-tree",
				text = "Neo-tree",
				highlight = "Directory",
				text_align = "left",
			},
			{
				filetype = "Outline",
				text = "Symbols Outline",
				highlight = "TSType",
				text_align = "left",
			},
		}
		opts.options.hover = {
			enabled = true,
			delay = 200,
			reveal = { "close" },
		}
		opts.highlights = function(config) ---@param config bufferline.Config
			local hl = {}

			for name, tbl in pairs(config.highlights) do
				local tbl_copy = {}
				for k, v in pairs(tbl) do
					-- Modify gui to remove italic
					if k == "gui" then
						local parts = vim.split(v, ",")
						for _, part in pairs(parts) do
							if part ~= "italic" then
								tbl_copy["gui"] = part
							end
						end
					else
						tbl_copy[k] = v
					end
				end
				hl[name] = tbl_copy
			end

			return hl
		end
	end,
}
-- return {
-- 	"akinsho/bufferline.nvim",
-- 	dependencies = { "nvim-tree/nvim-web-devicons" },
-- 	version = "*",
-- 	opts = {
-- 		options = {
-- 			mode = "tabs",
-- 		},
-- 	},
-- }
