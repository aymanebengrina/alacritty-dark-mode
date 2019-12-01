#! /usr/bin/env python3

import re
import os

doc = open(os.path.expanduser('~/.config/alacritty/alacritty.yml'), 'r' )
file = doc.read()
doc.close()
doc = open(os.path.expanduser('~/.config/alacritty/alacritty.yml'), 'w' )


light = re.search(r'\*light', file)
dark = re.search(r'\*dark', file)

if light:
	new_file = re.sub(r"\*light", "*dark", file, flags = re.M)
	doc.write(new_file)
	
if dark:
	new_file = re.sub(r"\*dark", "*light", file, flags = re.M)
	doc.write(new_file)
	


#config = re.search("\*dark", config)

