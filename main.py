Last login: Mon May  1 09:26:01 on ttys000
[oh-my-zsh] Would you like to update? [Y/n] y
Updating Oh My Zsh
master

BREAKING CHANGES:

 - 673b9fc [aws]

   This commit removes compatibility for `aws` cli v1. Now only v2 is supported.

Features:

 - 9139d30 [aws]               Allow more customisation in prompt function (#11619)
 - 673b9fc [aws]               Improve `aws_change_access_key` (#11378)
 - 5d3e86e [dbt]               Create plugin (#11635)
 - 91c7ed4 [npm]               Add `npmrd` alias (#11627)
 - bd5ebba [pipenv]            Add pupd alias (#11616)
 - 0745402 [starship]          Create plugin (#10947)
 - 2e7a247 [z]                 Update to latest upstream version

Bug fixes:

 - 343c78a [aws]               Set properly set divider to space
 - 6569991 [azure]             Recognize properly linuxbrew
 - d889eca [check_for_upgrade] Update properly `LAST_EPOCH`
 - 5b11e70 [cli]               Execute as expected if `ksh_arrays` is set (#11629)
 - 18c837b [dirhistory]        Run properly if `ksh_arrays` is set (#11630)

You can see the changelog with `omz changelog`
         __                                     __
  ____  / /_     ____ ___  __  __   ____  _____/ /_
 / __ \/ __ \   / __ `__ \/ / / /  /_  / / ___/ __ \
/ /_/ / / / /  / / / / / / /_/ /    / /_(__  ) / / /
\____/_/ /_/  /_/ /_/ /_/\__, /    /___/____/_/ /_/
                        /____/

Hooray! Oh My Zsh has been updated!

To keep up with the latest news and updates, follow us on Twitter: @ohmyzsh
Want to get involved in the community? Join our Discord: Discord server
Get your Oh My Zsh swag at: Planet Argon Shop
(base)  a06@a06ui-iMac  ~  ls
Desktop                          Pictures
# Let's leanrn Vim
Documents                        Public
Downloads                        [파이썬] 2일차 과제.ipynb
Google Drive                     cse101
Library                          miniforge3
Movies                           zsh-syntax-highlighting
Music                            무제 폴더
(base)  a06@a06ui-iMac  ~  ls -a
.                                .zprofile
..                               .zsh_history
.CFUserTextEncoding              .zsh_sessions
.DS_Store                        .zshrc
.Trash                           .zshrc.pre-oh-my-zsh
.cache                           Desktop
.conda                           Documents
.config                          Downloads
.hammerspoon                     Google Drive
.ipynb_checkpoints               Library
.ipython                         Movies
.jupyter                         Music
.lesshst                         Pictures
.local                           Public
.matplotlib                      [파이썬] 2일차 과제.ipynb
.mysql_history                   cse101
.oh-my-zsh                       miniforge3
.vscode                          zsh-syntax-highlighting
.zcompdump-a06의 iMac-5.8.1      무제 폴더
.zcompdump-a06의 iMac-5.9
(base)  a06@a06ui-iMac  ~  ls -l
total 48
drwx------@ 22 a06  staff    704  4 28 11:19 Desktop
drwx------+  4 a06  staff    128  4 21 10:31 Documents
drwx------+ 99 a06  staff   3168  4 28 11:16 Downloads
lrwx------   1 a06  staff     62  4 28 13:56 Google Drive -> /Users/a06/Library/CloudStorage/GoogleDrive-kangjs92@gmail.com
drwx------@ 89 a06  staff   2848  5  1 01:04 Library
drwx------   4 a06  staff    128  3 27 09:12 Movies
drwx------+  4 a06  staff    128  3 17 12:48 Music
drwx------+  4 a06  staff    128  3 17 12:12 Pictures
drwxr-xr-x+  4 a06  staff    128  3 17 11:01 Public
-rw-r--r--   1 a06  staff  23837  4 19 09:01 [파이썬] 2일차 과제.ipynb
drwxr-xr-x   6 a06  staff    192  3 29 17:38 cse101
drwxr-xr-x  16 a06  staff    512  4 24 08:58 miniforge3
drwxr-xr-x  22 a06  staff    704  3 31 17:00 zsh-syntax-highlighting
drwxr-xr-x   2 a06  staff     64  4 12 09:50 무제 폴더
(base)  a06@a06ui-iMac  ~  cd Documents/
(base)  a06@a06ui-iMac  ~/Documents  ls
Zoom
(base)  a06@a06ui-iMac  ~/Documents  mkdir dev
(base)  a06@a06ui-iMac  ~/Documents  ls
Zoom dev
(base)  a06@a06ui-iMac  ~/Documents  cd dev
(base)  a06@a06ui-iMac  ~/Documents/dev  ls
(base)  a06@a06ui-iMac  ~/Documents/dev  touch main.py
(base)  a06@a06ui-iMac  ~/Documents/dev  ls
main.py
(base)  a06@a06ui-iMac  ~/Documents/dev  touch learn-vim.md
(base)  a06@a06ui-iMac  ~/Documents/dev  ls
learn-vim.md main.py
(base)  a06@a06ui-iMac  ~/Documents/dev  vi learn-vim.md
(base)  a06@a06ui-iMac  ~/Documents/dev  cat learn-vim.md
# Let's leanrn Vim

## Mode

- Normal mode: press 'esc' on any mode.
- Insert mode: press 'i' on Normal mode.
- Visual mode: press 'v' on Normal mode.
- Command mode: press ':' on Normal mode.

## Command flow

```shell
$ vi learn-vim.md
i
(type something)
`esc` -> return to Normal mode
`:wq + enter`
(base)  a06@a06ui-iMac  ~/Documents/dev  clear
# git-practice
credential.helper=osxkeychain
init.defaultbranch=main
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
remote.origin.url=https://github.com/jun-suk/git-practice.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.main.remote=origin
branch.main.merge=refs/heads/main
...skipping...
(base)  a06@a06ui-iMac  ~/Documents/dev  ls
learn-vim.md main.py
(base)  a06@a06ui-iMac  ~/Documents/dev  git clone https://github.com/jun-suk/git-practice.git
Cloning into 'git-practice'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), done.
(base)  a06@a06ui-iMac  ~/Documents/dev  ls
git-practice learn-vim.md main.py
(base)  a06@a06ui-iMac  ~/Documents/dev  cd git-practice/
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice   main  ls
LICENSE   README.md
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice   main  vi README.md
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice   main ±  cat README.md

# git-practice

docs: Edit README.md
abstract: This project is to pratice git
[See demo](https://www.google.com/)

## Vim modes

- Noraml mode: press `esc` on ANY mode
- Insert mode: press `i` on Normal mode
- Visual mode: press `v` on Normal mode
- Command mode: press `:` on Normal mode

## Installation

```shell
$ git clone {repo address}
$ cd {repo name}
$ vi README.md
```


## How to start

```python
def hello(name):
    print(f'hello, {name}')

hello('John Doe')
```

## Features

(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice   main ±  git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice   main ±  git add README.md
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice   main ✚  git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   README.md

(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice   main ✚  git config --list
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice   main ✚  git config --global user.name "jun-suk"
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice   main ✚  git congig --global user.email "kangjs92@gmail.com"
git: 'congig' is not a git command. See 'git --help'.

The most similar command is
	config
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice   main ✚  git config --global user.email "kangjs92@gmail.com"
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice   main ✚  git config --global core.editor "vim"
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice   main ✚  git config --global core.pager "cat"
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice   main ✚  git config --list
credential.helper=osxkeychain
init.defaultbranch=main
user.name=jun-suk
user.email=kangjs92@gmail.com
core.editor=vim
core.pager=cat
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
remote.origin.url=https://github.com/jun-suk/git-practice.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.main.remote=origin
branch.main.merge=refs/heads/main
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice   main ✚  git commit
Aborting commit due to empty commit message.
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice   main ✚  git commit
[main 8b3db5f] docs: Edit README.md
 1 file changed, 32 insertions(+), 1 deletion(-)
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git log
commit 8b3db5f26e237516725c9ed6984d361d0828ac27 (HEAD -> main)
Author: jun-suk <kangjs92@gmail.com>
Date:   Mon May 1 10:31:37 2023 +0900

    docs: Edit README.md

    I wrote README.md to describe what this project is.

commit 5ac1ac7669324f01d8a9392b43292db04eec9c3c (origin/main, origin/HEAD)
Author: jun-suk <73885257+jun-suk@users.noreply.github.com>
Date:   Mon May 1 10:04:34 2023 +0900

    Initial commit
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git push 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
fatal: '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' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git push orgin main
fatal: 'orgin' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git push 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
fatal: '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' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git push 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
fatal: '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' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git push orgin main 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
error: src refspec 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 does not match any
error: failed to push some refs to 'orgin'
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git push orginmain
fatal: 'orginmain' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git log
commit 8b3db5f26e237516725c9ed6984d361d0828ac27 (HEAD -> main)
Author: jun-suk <kangjs92@gmail.com>
Date:   Mon May 1 10:31:37 2023 +0900

    docs: Edit README.md

    I wrote README.md to describe what this project is.

commit 5ac1ac7669324f01d8a9392b43292db04eec9c3c (origin/main, origin/HEAD)
Author: jun-suk <73885257+jun-suk@users.noreply.github.com>
Date:   Mon May 1 10:04:34 2023 +0900

    Initial commit
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git push origin main
Username for 'https://github.com': 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
Password for 'https://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@github.com':
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/jun-suk/git-practice.git/'
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git commit
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git log
commit 8b3db5f26e237516725c9ed6984d361d0828ac27 (HEAD -> main)
Author: jun-suk <kangjs92@gmail.com>
Date:   Mon May 1 10:31:37 2023 +0900

    docs: Edit README.md

    I wrote README.md to describe what this project is.

commit 5ac1ac7669324f01d8a9392b43292db04eec9c3c (origin/main, origin/HEAD)
Author: jun-suk <73885257+jun-suk@users.noreply.github.com>
Date:   Mon May 1 10:04:34 2023 +0900

    Initial commit
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  ›››git push orgin main
zsh: command not found: ›››git
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git log
commit 8b3db5f26e237516725c9ed6984d361d0828ac27 (HEAD -> main)
Author: jun-suk <kangjs92@gmail.com>
Date:   Mon May 1 10:31:37 2023 +0900

    docs: Edit README.md

    I wrote README.md to describe what this project is.

commit 5ac1ac7669324f01d8a9392b43292db04eec9c3c (origin/main, origin/HEAD)
Author: jun-suk <73885257+jun-suk@users.noreply.github.com>
Date:   Mon May 1 10:04:34 2023 +0900

    Initial commit
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git orgin main
git: 'orgin' is not a git command. See 'git --help'.
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git push origin main
Username for 'https://github.com': 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
Password for 'https://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@github.com':
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/jun-suk/git-practice.git/'
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git log
commit 8b3db5f26e237516725c9ed6984d361d0828ac27 (HEAD -> main)
Author: jun-suk <kangjs92@gmail.com>
Date:   Mon May 1 10:31:37 2023 +0900

    docs: Edit README.md

    I wrote README.md to describe what this project is.

commit 5ac1ac7669324f01d8a9392b43292db04eec9c3c (origin/main, origin/HEAD)
Author: jun-suk <73885257+jun-suk@users.noreply.github.com>
Date:   Mon May 1 10:04:34 2023 +0900

    Initial commit
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git push orgin main
fatal: 'orgin' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git log
commit 8b3db5f26e237516725c9ed6984d361d0828ac27 (HEAD -> main)
Author: jun-suk <kangjs92@gmail.com>
Date:   Mon May 1 10:31:37 2023 +0900

    docs: Edit README.md

    I wrote README.md to describe what this project is.

commit 5ac1ac7669324f01d8a9392b43292db04eec9c3c (origin/main, origin/HEAD)
Author: jun-suk <73885257+jun-suk@users.noreply.github.com>
Date:   Mon May 1 10:04:34 2023 +0900

    Initial commit
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git push origin main
Username for 'https://github.com': kangjs92@gamil.com
Password for 'https://kangjs92@gamil.com@github.com':
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/jun-suk/git-practice.git/'
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git log
commit 8b3db5f26e237516725c9ed6984d361d0828ac27 (HEAD -> main)
Author: jun-suk <kangjs92@gmail.com>
Date:   Mon May 1 10:31:37 2023 +0900

    docs: Edit README.md

    I wrote README.md to describe what this project is.

commit 5ac1ac7669324f01d8a9392b43292db04eec9c3c (origin/main, origin/HEAD)
Author: jun-suk <73885257+jun-suk@users.noreply.github.com>
Date:   Mon May 1 10:04:34 2023 +0900

    Initial commit
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git push orgin main
fatal: 'orgin' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git log
commit 8b3db5f26e237516725c9ed6984d361d0828ac27 (HEAD -> main)
Author: jun-suk <kangjs92@gmail.com>
Date:   Mon May 1 10:31:37 2023 +0900

    docs: Edit README.md

    I wrote README.md to describe what this project is.

commit 5ac1ac7669324f01d8a9392b43292db04eec9c3c (origin/main, origin/HEAD)
Author: jun-suk <73885257+jun-suk@users.noreply.github.com>
Date:   Mon May 1 10:04:34 2023 +0900

    Initial commit
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git push origin main
Username for 'https://github.com': kangjs92@gmail.com
Password for 'https://kangjs92@gmail.com@github.com':
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/jun-suk/git-practice.git/'
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git push orgin main
fatal: 'orgin' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git log
commit 8b3db5f26e237516725c9ed6984d361d0828ac27 (HEAD -> main)
Author: jun-suk <kangjs92@gmail.com>
Date:   Mon May 1 10:31:37 2023 +0900

    docs: Edit README.md

    I wrote README.md to describe what this project is.

commit 5ac1ac7669324f01d8a9392b43292db04eec9c3c (origin/main, origin/HEAD)
Author: jun-suk <73885257+jun-suk@users.noreply.github.com>
Date:   Mon May 1 10:04:34 2023 +0900

    Initial commit
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git push origin main
Username for 'https://github.com': jun-suk
Password for 'https://jun-suk@github.com':
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/jun-suk/git-practice.git/'
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git log
commit 8b3db5f26e237516725c9ed6984d361d0828ac27 (HEAD -> main)
Author: jun-suk <kangjs92@gmail.com>
Date:   Mon May 1 10:31:37 2023 +0900

    docs: Edit README.md

    I wrote README.md to describe what this project is.

commit 5ac1ac7669324f01d8a9392b43292db04eec9c3c (origin/main, origin/HEAD)
Author: jun-suk <73885257+jun-suk@users.noreply.github.com>
Date:   Mon May 1 10:04:34 2023 +0900

    Initial commit
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git orgin main
git: 'orgin' is not a git command. See 'git --help'.
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git log
commit 8b3db5f26e237516725c9ed6984d361d0828ac27 (HEAD -> main)
Author: jun-suk <kangjs92@gmail.com>
Date:   Mon May 1 10:31:37 2023 +0900

    docs: Edit README.md

    I wrote README.md to describe what this project is.

commit 5ac1ac7669324f01d8a9392b43292db04eec9c3c (origin/main, origin/HEAD)
Author: jun-suk <73885257+jun-suk@users.noreply.github.com>
Date:   Mon May 1 10:04:34 2023 +0900

    Initial commit
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git origin main
git: 'origin' is not a git command. See 'git --help'.
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git push orgin main
fatal: 'orgin' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git log
commit 8b3db5f26e237516725c9ed6984d361d0828ac27 (HEAD -> main)
Author: jun-suk <kangjs92@gmail.com>
Date:   Mon May 1 10:31:37 2023 +0900

    docs: Edit README.md

    I wrote README.md to describe what this project is.

commit 5ac1ac7669324f01d8a9392b43292db04eec9c3c (origin/main, origin/HEAD)
Author: jun-suk <73885257+jun-suk@users.noreply.github.com>
Date:   Mon May 1 10:04:34 2023 +0900

    Initial commit
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git push orgin main
fatal: 'orgin' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git config --global use.password
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git config
usage: git config [<options>]

Config file location
    --global              use global config file
    --system              use system config file
    --local               use repository config file
    --worktree            use per-worktree config file
    -f, --file <file>     use given config file
    --blob <blob-id>      read config from given blob object

Action
    --get                 get value: name [value-pattern]
    --get-all             get all values: key [value-pattern]
    --get-regexp          get values for regexp: name-regex [value-pattern]
    --get-urlmatch        get value specific for the URL: section[.var] URL
    --replace-all         replace all matching variables: name value [value-pattern]
    --add                 add a new variable: name value
    --unset               remove a variable: name [value-pattern]
    --unset-all           remove all matches: name [value-pattern]
    --rename-section      rename section: old-name new-name
    --remove-section      remove a section: name
    -l, --list            list all
    --fixed-value         use string equality when comparing values to 'value-pattern'
    -e, --edit            open an editor
    --get-color           find the color configured: slot [default]
    --get-colorbool       find the color setting: slot [stdout-is-tty]

Type
    -t, --type <type>     value is given this type
    --bool                value is "true" or "false"
    --int                 value is decimal number
    --bool-or-int         value is --bool or --int
    --bool-or-str         value is --bool or string
    --path                value is a path (file or directory name)
    --expiry-date         value is an expiry date

Other
    -z, --null            terminate values with NUL byte
    --name-only           show variable names only
    --includes            respect include directives on lookup
    --show-origin         show origin of config (file, standard input, blob, command line)
    --show-scope          show scope of config (worktree, local, global, system, command)
    --default <value>     with --get, use default value when missing entry

(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git commit
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git log
commit 8b3db5f26e237516725c9ed6984d361d0828ac27 (HEAD -> main)
Author: jun-suk <kangjs92@gmail.com>
Date:   Mon May 1 10:31:37 2023 +0900

    docs: Edit README.md

    I wrote README.md to describe what this project is.
# it is python

# it is pytho
commit 5ac1ac7669324f01d8a9392b43292db04eec9c3c (origin/main, origin/HEAD)
Author: jun-suk <73885257+jun-suk@users.noreply.github.com>
Date:   Mon May 1 10:04:34 2023 +0900

    Initial commit
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git push orgin main
# it is pytho
fatal: 'orgin' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git log
commit 8b3db5f26e237516725c9ed6984d361d0828ac27 (HEAD -> main)
Author: jun-suk <kangjs92@gmail.com>
Date:   Mon May 1 10:31:37 2023 +0900

    docs: Edit README.md

    I wrote README.md to describe what this project is.

commit 5ac1ac7669324f01d8a9392b43292db04eec9c3c (origin/main, origin/HEAD)
Author: jun-suk <73885257+jun-suk@users.noreply.github.com>
Date:   Mon May 1 10:04:34 2023 +0900

    Initial commit
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  ls
LICENSE   README.md
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git log
commit 8b3db5f26e237516725c9ed6984d361d0828ac27 (HEAD -> main)
Author: jun-suk <kangjs92@gmail.com>
Date:   Mon May 1 10:31:37 2023 +0900

    docs: Edit README.md

    I wrote README.md to describe what this project is.

commit 5ac1ac7669324f01d8a9392b43292db04eec9c3c (origin/main, origin/HEAD)
Author: jun-suk <73885257+jun-suk@users.noreply.github.com>
Date:   Mon May 1 10:04:34 2023 +0900

    Initial commit
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git commit
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

# ddd
nothing to commit, working tree clean
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git push orgin main
fatal: 'orgin' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  ls
LICENSE   README.md
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  touch main.py
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  ls
LICENSE   README.md main.py
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	main.py

nothing added to commit but untracked files present (use "git add" to track)
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  touch main.py
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  main.py
zsh: command not found: main.py
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  vi main.py
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  vi main.py
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  python main.py
  File "/Users/a06/Documents/dev/git-practice/main.py", line 2
    print("hello")n
                  ^
sdas
~

SyntaxError: invalid syntax
# Test python env
(base)  ✘ a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  vi main.py
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  python main.py
hello
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  ls
LICENSE   README.md main.py
(base)  a06@a06ui-iMac  ~/Documents/dev/git-practice  ↱ main  git status
# Test python env
def pring_hello():
    animals = ['dog', 'cat', 'hamster']
    foods = [
        'pizza',
        'spagetti'
 ]
        # w/o trailing comma
    names = [
        "John,
         'Jane',
         'Gil-dong',
]
        #w/ trailing comma
for f_name in names:
    print('f'hello, {f_name}')

if __name__ == '__main__':
    print_hello()
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
NSERT -# Test python env
def pring_hello():
    animals = ['dog', 'cat', 'hamster']
    foods = [
	'pizza',
	'spagetti'
 ]
	# w/o trailing comma
    names = [
	"John,
	 'Jane',
	 'Gil-dong',
]
	#w/ trailing comma
for f_name in names:
    print('f'hello, {f_name}')

if __name__ == '__main__':
    print_hello()
