# Bash shortcuts

`cd -` changes to the previous working directory.

`^foo^bar` runs previous command but replacing "foo" for "bar". Also, just `^baz` will remove all occurrences of "baz" from the previous command.

` command` (with a space prepended) will prevent the command from being saved in the history.

`>file.txt` will empty the file's contents without deleting it.

`reset` will restart the terminal.

`at` queues shell commands to be executed later. Example: `echo "ls -l" | at midnight`.

`vim -` will get Vim to read from stdin, such that commands can be piped into it.
