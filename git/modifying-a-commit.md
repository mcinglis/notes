# How to modify a previous commit.

* http://stackoverflow.com/questions/1186535/how-to-modify-a-specified-commit

To change the most-recent commit, just use `git commit --amend`.

To change older commits, you can use `git rebase`.

For example, to modify back to commit `bbc643`, do:

``` sh
$ git rebase -i bbc643^
# Change 'pick' to 'edit' for the commit you want to change.
# Save and close the rebase file.
# Make your changes to the commit, and stage them:
$ git add <files>
# Modify the commit.
$ git commit --amend
# Continue with the rebase.
$ git rebase --continue
```
