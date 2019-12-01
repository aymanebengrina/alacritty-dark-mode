# alacritty-dark-mode

Un script en python pour changer les couleurs d'Alacritty.

A python script to easily switch between light and dark color schemes in Alacritty.


This scripts works simply by opening alacritty's config file (located in ~/.config/alacritty), and then, using a regex, checking if it's in light or dark mode, and inverting the color scheme using two if conditions. Maybe i'll change that to an if/else.

You have to set up your colors according to [this](https://github.com/jwilm/alacritty/wiki/Color-schemes) link for the script to work.

Tested in macOS 10.4.6 with python3 from homebrew.
