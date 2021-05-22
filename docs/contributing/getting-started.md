# Getting Started

## Git Branches

The Thanatos project follows a branching model based on [Git-flow](https://nvie.com/posts/a-successful-git-branching-model/). As such, there are two persistent git branches:

* `release` - Serves as a snapshot of the current stable release
* `develop` - All development on the upcoming stable release occurs here

At any given time, there may additionally be zero or more long-lived branches of the form `develop-X.Y.Z`, where `X.Y.Z` is a future stable release later than the one currently being worked on in the main `develop` branch.

You will always base pull requests off of the `develop` branch, or off of `develop-X.Y.Z` if you're working on a feature targeted for a later release. **Never** target pull requests into the `main` branch, which receives merges only from the `develop` branch.

## Forking the Repo

When developing Thanatos, you'll be working on your own fork, so your first step will be to [fork the official GitHub repository](https://github.com/psmware-labs/thanatos/fork). You will then clone your GitHub fork locally for development.

!!! note
It is highly recommended that you use the CDF before proceeding.

In this guide, SSH will be used to interact with Git.

```no-highlight
> git clone git@github.com:yourusername/thanatos.git
Cloning into 'Thanatos'...
remote: Enumerating objects: 231, done.
remote: Counting objects: 100% (231/231), done.
remote: Compressing objects: 100% (147/147), done.
remote: Total 56705 (delta 134), reused 145 (delta 84), pack-reused 56474
Receiving objects: 100% (56705/56705), 27.96 MiB | 34.92 MiB/s, done.
Resolving deltas: 100% (44177/44177), done.
> ls Thanatos/
CHANGELOG.md     LICENSE    docs        poetry.lock
CONTRIBUTING.md  README.md  mkdocs.yml  pyproject.toml
```

### About Remote Repos

Git refers to remote repositories as *remotes*. When you make your initial clone of your fork, Git defaults to naming this remote `origin`. Throughout this documentation, the following remote names will be used:

* `origin` - The default remote name used to refer to *your fork of Thanatos*
* `upstream` - The main remote used to refer to the *official Thanatos repository*

### Setting up your Remotes

Remote repos are managed using the `git remote` command.

Upon cloning Thanatos for the first time, you will have only a single remote:

```no-highlight
> git remote -v
origin  git@github.com:yourusername/thanatos.git (fetch)
origin  git@github.com:yourusername/thanatos.git (push)
```

Add the official Thanatos repo as a the `upstream` remote:

```no-highlight
> git remote add upstream git@github.com:psmware-labs/thanatos.git
```

View your remotes again to confirm you've got both `origin` pointing to your fork and `upstream` pointing to the official repo:

```no-highlight
> git remote -v
origin  git@github.com:yourusername/thanatos.git (fetch)
origin  git@github.com:yourusername/thanatos.git (push)
upstream  git@github.com:psmware-labs/thanatos.git (fetch)
upstream  git@github.com:psmware-labs/thanatos.git (push)
```

You're now ready to proceed to the next steps.

!!! hint
  You will always **push** changes to `origin` (your fork) and **pull** changes from `upstream` (official repo).

### Creating a Branch

Before you make any changes, always create a new branch. In the majority of cases, you'll always want to create your branches from the `develop` branch.

Before you ever create a new branch, always  checkout the `develop` branch and make sure you you've got the latest changes from `upstream`.

```no-highlight
> git checkout develop
> git pull upstream develop
```

!!! warning
  If you do not do this, you run the risk of having merge conflicts in your branch, and that's never fun to deal with. Trust us on this one.

Now that you've got the latest upstream changes, create your branch. It's convention to always prefix your branch name with your GitHub username/JIRA Ticket, separated by hyphens. For example:

```no-highlight
> git checkout -b yourusername-myfeature

or

> git checkout -b JIRA-123/myfeature
```

## Submitting Pull Requests

Once you're happy with your work and have verified that all tests pass, commit your changes and push it upstream to your fork. Always provide descriptive (but not excessively verbose) commit messages. When working on a specific issue, be sure to reference it.

```no-highlight
> git commit -m "Closes #1234: Add IPv5 support"
or
> git commit -m "Closes JIRA-123: Add IPv5 support"
> git push origin
```

Once your fork has the new commit, submit a [pull request](https://github.com/psmware-labs/thanatos/compare) to the Thanatos repo to propose the changes. Be sure to provide a detailed accounting of the changes being made and the reasons for doing so.

Once submitted, a maintainer will review your pull request and either merge it or request changes. If changes are needed, you can make them via new commits to your fork: The pull request will update automatically.

!!! note
    Remember, pull requests are entertained only for **accepted** issues. If an issue you want to work on hasn't been approved by a maintainer yet, it's best to avoid risking your time and effort on a change that might not be accepted.
