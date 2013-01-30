`hub` wraps `git` with GitHub commands. You can `alias git='hub'`.

## Contributing to projects

Clone your own project.

    $ git clone notes
        -> git clone git://github.com/zenmunki/notes.git

Clone other projects.

    $ git clone defunkt/hub
        -> git clone git://github.com/defunkt/hub.git

Open the current project's issues.

    $ git browse -- issues
        -> (opens https://github.com/defunkt/hub/issues)

Open another project's wiki.

    $ git browse mojombo/jekyll wiki
        -> (opens https://github.com/mojombo/jekyll/wiki)

Example workflow for contributing to a project.

    $ git clone defunkt/hub
    $ cd hub
    $ git checkout -b lasers
    ...
    $ git commit -m "Add lasers!"
    $ git fork
        -> (forks the repo on GitHub)
        -> git remote add zenmunki git://github.com/zenmunki/hub
    $ git push -u zenmunki lasers
    $ git pull-request | xclip
        -> (opens your editor to write your pull request message)
        -> (pull request URL copied to clipboard)

## Maintaing projects

Fetch from multiple trusted forks, even if they don't yet exist as remotes.

    $ git fetch mislav,cehoffman
        -> git remote add mislav git://github.com/mislav/hub.git
        -> git remote add cehoffman git://github.com/cehoffman/hub.git
        -> git fetch --multiple mislav cehoffman

Check out a pull request for review.

    $ git checkout https://github.com/defunkt/hub/pull/134
        -> (creates a new branch with the contents of the pull request)

Directly apply all commits from a pull request to the current branch.

    $ git am -3 https://github.com/defunkt/hub/pull/134

Cherry-pick a GitHub URL.

    $ git cherry-pick http://github.com/xoebus/hub/commit/177eeb8

Although, `am` can be better than `cherry-pick` because it doesn't create a remote.

    $ git am http://github.com/xoebus/hub/commit/177eeb8

Open the GitHub compare view between two branches.

    $ git compare v0.9..v1.0

Copy the compare URL for a topic branch to the clipboard.

    $ git compare -u feature | pbcopy

Create a repo for a new project.

    $ git init world-domination
    ...
    $ git add . && git commit -m "It begins."
    $ git create -d "My plans for world domination."
        -> (creates a new project on GitHub with the name of the directory)
    $ git push -u origin master

Push to multiple remotes.

    $ git push production,staging
