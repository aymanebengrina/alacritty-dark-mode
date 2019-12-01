#! /usr/bin/env python3
# alacritty-dark-mode.py: A script to switch between dark and light color schemes in alacritty

import re
import os

# Opens alacritty's config file in read only mode, and save its contents into a variable
doc = open(os.path.expanduser('~/.config/alacritty/alacritty.yml'), 'r' )
file = doc.read()
# Closing the document and opening it again in write mode
doc.close()
doc = open(os.path.expanduser('~/.config/alacritty/alacritty.yml'), 'w' )

# The two regular expressions to detect if Alacritty is in dark or light mode
light = re.search(r'\*light', file)
dark = re.search(r'\*dark', file)

# If alacritty is in light mode, switch to dark mode
if light:
	new_file = re.sub(r"\*light", "*dark", file, flags = re.M)
	doc.write(new_file)
# If alacritty is in dark mode, switch to light mode	
if dark:
	new_file = re.sub(r"\*dark", "*light", file, flags = re.M)
	doc.write(new_file)
