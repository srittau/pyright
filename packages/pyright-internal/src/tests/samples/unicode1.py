# This sample tests a variety of unicode characters including those that
# require two-code (surrogate) forms.

# Old Italic
𐌎𐌘𐌟𐌁 = 42

# Egyptian hieroglyphs
𓃘𓐭𓇀𓅨𓆙 = 2

# Linear B Ideograms
𐂂𐃪𐃯 = ""

# Cuneiform
𒀟𒀕𒀰𒁜𒂐𒄊 = ""

# Old Persian
𐎠𐏊𐏏 = 3

# Lydian
𐤢𐤷𐤬𐤮 = 4

# Phoenician
𐤔𐤑𐤇 = 4

# Nabataean
𐢖𐢊ﬗ = 0

# This should generate an error because "𐢭" is outside the range of
# characters supported by the Python standard.
𐢭 = 0


