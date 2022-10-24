.. _HowToMakeAChange:

How to make a change?
---------------------

Changes to the VODF documentation are made by GitHub Pull Request (PR). Each PR
is reviewed, and upon acceptance will be merged into the main branch and
included in the next release.

There are two ways to do this:

1. to edit a single file and make a change, simply click the "*edit this page*"
   link in the right-hand sidebar of the documentation. This will open an editor
   on GitHub where you can make changes and create a PR.
2. For many changes, use git with the procedure as follows:

Checkout the git repo (get the URL in the GitHub page - you can use https or
ssh, depending on your needs):

.. code:: sh

  git clone https://github.com/VODF/vodf-docs.git
  cd vodf-docs
  conda env create -f environment.yaml   # if not already done
  conda activate vodf-docs
  make html   # check that it builds

Then to make your change, first make a branch (in this example, we will call it
`my changes` but you should choose a descriptive name), edit the source, push
your branch and open a PR:

.. code:: sh

  git switch main             # start on the main branch
  git pull origin             # make sure you have the latest changes
  git switch -c my_changes    # creates a new branch and switches to it

Edit the source, make sure it builds ok with `make html`, and if so, create the
PR:

.. code:: sh

  git add [all files you changed]   # add files to the change set
  git commit                        # commit changes

  git push -u origin my_changes  # push your branch to GitHub

And open the URL mentioned in the message displayed to open the PR. In the PR,
please describe the changes.
