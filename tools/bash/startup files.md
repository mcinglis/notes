# Bash invocation

## Login shell

When `bash` is invoked as an interactive login shell, it first reads and executes commands from **`/etc/profile`**.

Some distributions' default `/etc/profile` scripts will load scripts from `/etc/profile.d`.

`bash` then looks for **`~/.bash_profile`**, `~/.bash_login` and `~/.profile`, in that order, and executes the first one found.

When a login shell exits, `bash` will execute `~/.bash_logout`.

## Non-login interactive shells

When an interactive shell that is not a login shell is started (e.g. a new terminal window), `bash` will execute **`~/.bashrc`**.

## Non-interactive shells

When `bash` is started non-interactively (e.g. to run a shell script) it executes the file specified in `$BASH_ENV`.
