---
layout: lesson
root: ../..
title: The Git Development Workflow
level: intermediate
---

An important best practice for scientific software developers is to
focus on making *incremental changes*.  In this section, we'll focus
on the basic techniques for saving your work using Git.  In this
lesson, you'll learn a third use for the checkout command, how to work
with development branches, and then how to save revisions in the
staging area.

## Objectives

After this lesson, students should be able to:

* Create and manipulate development branches using `git checkout` and
  `git branch`.
* Inspect the changes they have made to their files using `git status`
  and `git diff`.
* Add and remove changes from the staging area using `git add`, `git
  reset`, and `git rm`.
* Save versions of their work using `git commit`.

## Development Branches

In the last lesson we cloned a repository and explored its history.
We also learned about HEAD, a special *pointer* to the revision of our
project that we most recently checked out.  We call lightweight
pointers to revisions in Git *branches*.  This is confusing at
first, because many newcomers to Git think of branches as part of the
repository's history.

The best way to think of branches is to first imagine your repository as a
notebook shared by several collaborators in your laboratory, with
bookmarks (the *branches*) on the page of their most recent experiment.
Every time somebody performs an experiment, they move their bookmark
to the page of the newest experiment.  Any time somebody wants to keep
track of one of their collaborators, they just need to look up their
bookmarks.  Since bookmarks are cheap, some of the scientists track
multiple experiments, even risky ones that might not pan out, with
their bookmarks.  The bookmarks are not the entries in the notebook,
but they are a handy way to keep track of active work.

In Git, a branch is a reference that follows your development.  When
you create new revisions, your current branch will automatically move
to new commits you make.  Branches are also primary tools for sharing
and collaboration, as they allow you to refer others to work-in-progress (and
scientific software development is always work-in-progress).

When a repository is created, Git creates a branch called `master`.
Unlike HEAD, the only thing special about `master` is that it's the
default name given to this branch.  It's generally not a great idea to
work directly on `master`, so we'll start this lesson by creating a new
branch from it for development.  

By default, Git creates branches that point to the currently
checked-out revision.  We would like to start our development at the
most up-to-date version of the repository, so we check out our local
copy of the `master` branch first.

~~~
$ git checkout master
Switched to branch 'master'
~~~

We can create and checkout a branch in the same step by adding the
`-b` flag to `git checkout`.  Since later we'll be fixing an error
in the  file `python_pipeline.ipy`, we'll name the branch
`fix_pipeline`.

~~~
$ git checkout -b pipeline_fix
Switched to a new branch 'pipeline_fix'
~~~

We can see the current branches available with `git branch`, but this
command is much more useful if we add the `-v` flag (for verbose).

~~~
$ git branch -v
  master       61fd2bc Made fixes to Python pipeline
* pipeline_fix 61fd2bc Made fixes to Python pipeline
~~~

Now that we've created our development branch, let's start preparing
some changes to our repository.

## Seeing Changes

## Staging Changes

## Committing Changes

## Review
