# WordPress Salts

[![The MIT License](https://flat.badgen.net/badge/license/MIT/blue)](https://opensource.org/licenses/MIT)
[![GitHub](https://flat.badgen.net/github/release/idleberg/sublime-wordpress-salts)](https://github.com/idleberg/sublime-wordpress-salts/releases)
[![CircleCI](https://flat.badgen.net/circleci/github/idleberg/generator-atom-package-coffeescript)](https://circleci.com/gh/idleberg/sublime-wordpress-salts)

Context-aware WordPress salts insertion for PHP, YAML and DotEnv files

## Installation

### Package Control

1. Make sure you have [Package Control](https://packagecontrol.io/) installed
2. Add our repository `https://idleberg.github.io/sublime-wordpress-salts/repository.json`
3. Choose *“Install Package”* from the Command Palette (<kbd>Super</kbd>+<kbd>Shift</kbd>+<kbd>p</kbd>)
4. Type *“WordPress Salts”* and press <kbd>Enter</kbd>

With the [`auto_upgrade`](https://packagecontrol.io/docs/settings#setting-auto_upgrade) setting enabled, Package Control will keep all installed packages up-to-date!

### Using Git

1. Change to your Sublime Text `Packages` directory
2. Clone repository `git clone https://github.com/idleberg/sublime-wordpress-salts.git WordPress Salts`

## Usage

This package exposes the *WordPress Salts: Insert* command in your [Command Palette](http://docs.sublimetext.info/en/latest/reference/command_palette.html), but can also be triggered using shortcuts.

Command                 | Operating System | Shortcut
------------------------|------------------|-----------------------------------------------------------------------------------------
WordPress Salts: Insert | Linux, Windows   | <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>W</kbd>, <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>P</kbd>
WordPress Salts: Insert | macOS            | <kbd>Ctrl</kbd>+<kbd>W</kbd>, <kbd>Ctrl</kbd>+<kbd>P</kbd>

Also take note of the available package settings to tweak the behaviour.

## Related

- [atom-wordpress-salts](https://atom.io/packages/wordpress-salts)
- [vscode-wordpress-salts](https://marketplace.visualstudio.com/items?itemName=idleberg.wordpress-salts)

## License

This work is licensed under the [The MIT License](LICENSE)
