.. _DCOaccept:

=======================================
 Developer Certificate of Origin (DCO)
=======================================

Each contributor shall accept the DCO which allows VODF to use your work and to
cite you as contributor.

**If you are willing to agree to these terms, the following agreement line should be added to every commit message:**

``Signed-off-by: Random J Developer <random@developer.example.org>``

Four solutions exist:

1. You add this message by hand into each of your commit messages (not recommended)

2. You can sign each of your commits with the command:

.. code:: sh

   git commit -s

If you have authored a commit that is missing its ‘Signed-off-by’ line, you can amend your commits and push them to
GitHub:

.. code:: sh

   git commit --amend --noedit --signoff

(see also this `How To <https://github.com/src-d/guide/blob/master/developer-community/fix-DCO.md#how-to-add-sign-offs-retroactively>`_).

3. You can make an alias of the command "``git commit -s``", e.g.

.. code:: sh

   alias gcs 'git commit -s'

4. You can create a *git hook* to automatically sign all your commits
   (recommended option). This method is `described in detail here <https://github.com/src-d/guide/blob/master/developer-community/fix-DCO.md#how-to-prevent-missing-sign-offs-in-the-future>`_


For each of these solutions, it is **mandatory** to correctly set your `user.name` and `user.email` as part of your git
configuration (see `this page <https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address>`_ to configure it).
You have to use **your real name** (i.e., pseudonyms or anonymous contributions cannot be made) when using git. This is
because the DCO is a binding document, granting the Gammapy project to be an open source project.

.. _DCO:

========================================
 VODF Developer Certification of Origin
========================================

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
