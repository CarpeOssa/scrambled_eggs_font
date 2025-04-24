from fontTools.ttLib import TTFont

# Load the original egg (font)
egg_carton = TTFont("original.ttf")

# Get the scramble tray (Windows Unicode cmap)
scramble_tray = egg_carton['cmap'].getcmap(3, 1)

# Make a scrambled eggmap (Caesar-style remap)
eggmap = {}
for shell in scramble_tray.cmap:
    yolk = scramble_tray.cmap[shell]
    if 65 <= shell <= 90 or 97 <= shell <= 122:  # A-Z, a-z
        scrambled = shell + 3
        if (shell <= 90 and scrambled > 90) or (shell >= 97 and scrambled > 122):
            scrambled -= 26
        eggmap[shell] = scramble_tray.cmap.get(scrambled, yolk)
    else:
        eggmap[shell] = yolk

# Apply the scramble
scramble_tray.cmap = eggmap

# Save our delicious scrambled font
egg_carton.save("scrambled.ttf")
print("Scrambled font cooked and saved as scrambled.ttf")
