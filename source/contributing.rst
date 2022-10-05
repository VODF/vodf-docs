.. Licensed under a 3-clause BSD style license - see LICENSE.rst

============
Contributing
============

Note: This text is freely inspired by the
`Contribution.md <https://raw.githubusercontent.com/astropy/astropy/main/CONTRIBUTING.md>`_
file of the `Astropy <https://www.astropy.org/>`_ project.

**Anyone is welcome to contribute to VODF !**

Meetings
========

All the meeting notes can be found on `these GitHub pages <https://github.com/VODF/vodf-meetings>`_.

Contributing Changes to VODF
============================

Reporting Issues
----------------
When opening an issue to report a problem, please try to provide a minimal example
that describes the issue along with details of the used data and `VODF` version you
are using.

How to make a change?
---------------------
Changes to the VODF documentation are made by GitHub Pull Request (PR).  Each PR is reviewed, 
and upon acceptance will be merged into the main branch and included in the next release.

There are two ways to do this: 

1. to edit a single file and make a change, simply click the "*edit this page*" link in the right-hand sidebar of the documentation.  This will open an editor on GitHub where you can make changes and create a PR. 
2. For many changes, use git with the procedure as follows:

Checkout the git repo (get the URL in the GitHub page - you can use https or ssh, depending on your needs):

.. code:: sh

  git clone https://github.com/VODF/vodf-docs.git
  cd vodf-docs
  conda env create -f environment.yaml   # if not already done
  conda activate vodf-docs
  make html   # check that it builds
 
Then to make your change, first make a branch (in this example, we will call it 
`my changes` but you should choose a descriptive name), edit the source, 
push your branch and open a PR:
 
.. code:: sh

  git switch main             # start on the main branch
  git pull origin             # make sure you have the latest changes
  git switch -c my_changes    # creates a new branch and switches to it
  
Edit the source, make sure it builds ok with `make html`, and if so, create the PR:

.. code:: sh
 
  git add [all files you changed]          # add files to the change set
  git commit -s -m "[Change description]"  # commit changes
  
  git push -u origin my_changes  # push your branch to GitHub
  
And open the URL mentioned in the message displayed to open the PR. In the PR,
please describe the changes. 
  
Promoting contributions
=======================
Even in the Open Source landscape, promoting the work of any is not only **natural** but
also a duty for the VODF leading parties. We are taking care that
*each contribution are correctly awarded for each product of the VODF project*.

An *Authorship Policy* will be settled of each type of products (releases, papers,
conferences). Note that each VODF release will be published with an official DOI
(though the `Zenodo deposit <https://zenodo.org/>`_) that you can use as an Open
Science publication. This publication will associated with a list of *authors* stored
into our metada files (``CITATION.cff`` and ``codemeta.json``).

In order to properly build the authors list with you as contributor, VODF is using the
so-called **Developer Certificate of Origin** (DCO). This is a lightweight way for
contributors to certify that they wrote or otherwise have the right to submit the
code they are contributing to the project. The used DCO is from the Linux Foundation
and can be found [below](#markdown-header-gammapy-developer-certification-of-origin). The practical acceptation of our DCO
can be found here: :ref:`DCO`.

.. _DCOaccept:

Acceptation of the Developer Certificate of Origin (DCO)
--------------------------------------------------------
Each contributor shall accept the DCO which allows VODF to use your work and to cite
you as contributor.

**If you are willing to agree to these terms, the following agreement line should be added to every commit message:**

``Signed-off-by: Random J Developer <random@developer.example.org>``

Four solutions exist:

1. You add this message by hand into each of your commit messages (not recommended)

2. You can sign each of your commits with the command: "``git commit -s``".

If you have authored a commit that is missing its ‘Signed-off-by’ line, you can amend your commits and push them to
GitHub: "``git commit --amend --noedit --signoff``"
(see also this `How To <https://github.com/src-d/guide/blob/master/developer-community/fix-DCO.md#how-to-add-sign-offs-retroactively>`_).

3. You can make an alias of the command "``git commit -s``", e.g.

``alias gcs 'git commit -s'``

4. You can create a so-called `git hooks` allowing to automatically sign all your commits (recommended option). This
method is described in detail `here <https://github.com/src-d/guide/blob/master/developer-community/fix-DCO.md#how-to-prevent-missing-sign-offs-in-the-future>`_.

For each of these solutions, it is **mandatory** to correctly set your `user.name` and `user.email` as part of your git
configuration (see `this page <https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address>`_ to configure it).
You have to use **your real name** (i.e., pseudonyms or anonymous contributions cannot be made) when using git. This is
because the DCO is a binding document, granting the Gammapy project to be an open source project.

.. _DCO:

VODF Developer Certification of Origin
--------------------------------------

..  code-block:: text
    :name: "DCO"

    Developer Certificate of Origin
    Version 1.1

    Copyright (C) 2004, 2006 The Linux Foundation and its contributors.

    Everyone is permitted to copy and distribute verbatim copies of this
    license document, but changing it is not allowed.


    Developer's Certificate of Origin 1.1

    By making a contribution to this project, I certify that:

    (a) The contribution was created in whole or in part by me and I
        have the right to submit it under the open source license
        indicated in the file; or

    (b) The contribution is based upon previous work that, to the best
        of my knowledge, is covered under an appropriate open source
        license and I have the right under that license to submit that
        work with modifications, whether created in whole or in part
        by me, under the same open source license (unless I am
        permitted to submit under a different license), as indicated
        in the file; or

    (c) The contribution was provided directly to me by some other
        person who certified (a), (b) or (c) and I have not modified
        it.

    (d) I understand and agree that this project and the contribution
        are public and that a record of the contribution (including all
        personal information I submit with it, including my sign-off) is
        maintained indefinitely and may be redistributed consistent with
        this project or the open source license(s) involved.


