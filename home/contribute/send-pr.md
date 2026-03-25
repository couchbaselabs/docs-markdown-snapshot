---
title: Send Your Changes for Review
editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/contribute/pages/send-pr.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:home:contribute:send-pr.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/contribute/send-pr.html)

# Send Your Changes for Review

After you have [edited documentation](edit-pages.md), [added any new pages](add-pages.md), and [tested your changes with a local build](test-site.md), you should:

* [Commit and push your changes](#commit).
* [Open a pull request (PR)](#pr) to merge your changes into the live documentation.

## [](#commit)Commit and Push Your Changes

Committing your files means that you’re ready for those changes to go to the remote version of your branch in the GitHub repository. Commits group related changes together on a branch. You can group similar changes together in a commit to make it easier to undo changes.

Pushing actually sends your changes to the remote version of your branch in the GitHub repository. Pushing ensures that the changes are safely stored on GitHub, and not just your computer.

It’s a good idea to commit and push regularly to avoid losing your work.

You can commit and push using VS Code, GitHub Desktop, or the command line.

### [](#commit-and-push-with-vs-code)Commit and Push With VS Code

> [!TIP]
> You can view more details in the [VS Code Documentation](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git).

To commit changes and push them to your remote branch from VS Code:

1. Click ![The Source Control icon from the VS Code editor. It shows a forked line.](_images/source-control.png) **Source Control**.  
VS Code should list all of the changes you have made to files in the repository. Click a change entry to view more details.
2. Do one of the following:

  1. To prepare to commit a single change, point to the change entry and click **\+ (Stage Changes)**.
  2. To prepare to commit all of your listed changes, point to the **Changes** heading and click **\+ (Stage All Changes)**.  
  > [!TIP]  
  > If you want to discard any changes, point to the change and click ![The Discard Changes button. It shows an arrow pointing back on itself.](_images/discard-changes.png) **Discard Changes**.
3. In the text field, write a descriptive commit message. Start your commit message with the ticket number for your changes, surrounded in square brackets. For example, `[AV-000001]`.  
Try to be descriptive about what you changed so other contributors know what changes were made in your commit. For example, `Changed "server" to "Server" in add-pages.adoc`.
4. Click **Commit**.
5. Click **Sync Changes**.

### [](#commit-and-push-with-github-desktop)Commit and Push with GitHub Desktop

See the documentation on [Committing and reviewing changes to your project in GitHub Desktop](https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop).

When you’re writing your commit message, start with the ticket number for your changes, surrounded in square brackets. For example, `[AV-000001]`.

Try to be descriptive about what you changed so other contributors know what changes were made in your commit. For example, `Changed "server" to "Server" in add-pages.adoc`.

### [](#commit-and-push-with-the-command-line)Commit and Push with the Command Line

To commit changes and push them to your remote branch from the command line:

1. Open a terminal window.
2. Check the changes on your local branch:  
```console  
$ git status  
```
3. For each file you want to add to your commit, run the following command, filling in the filepath and filename:  
```console  
$ git add <file-path>/<file-name>  
```
4. Run the following command to add a commit message and commit your changes, filling in a descriptive commit message:  
```console  
$ git commit -m "<Your-commit-message>"  
```  
Start your commit message with the ticket number for your changes, surrounded in square brackets. For example, `[AV-000001]`.  
Try to be descriptive about what you changed so other contributors know what changes were made in your commit. For example, `Changed "server" to "Server" in add-pages.adoc`.
5. Push your changes to the remote version of your branch by running the following command:  
```console  
$ git push origin <branch-name>  
```

## [](#pr)Open a Pull Request for Your Branch

After you have committed and pushed all of the changes you need to make to the documentation files to GitHub, you need to open a pull request (PR).

PRs let other writers review your changes before they get added to the live documentation. They merge the changes from your working branch into a release branch or the main branch in a Documentation repository.

To open a PR for your working branch:

1. Go to the GitHub page for the repository you were working on.
2. In the branch list, select your branch:  
![The GitHub branches list on the docs-site repository. It shows a list of the branches in the repository, with a text box where you can find or create a new branch and the option to view all branches.](_images/github-branches-list.png)
3. Go to **Contribute** **Open Pull Request**.
4. In the **base** list, select the branch you selected as your base branch when you [created your working branch](create-branches.md).
5. In the **Add a title** field, enter a descriptive title for your changes.  
Start with the ticket number for your changes, surrounded in square brackets. For example, `[AV-000001]`. The rest of your title can be similar to the name of your branch.
6. In the **Add a description** field, enter a more detailed description of the changes you made with your commit or commits.  
Make sure to provide enough context that your reviewers know why you made the changes. If you’re making a substantial enough change, make sure to also include a link to your preview site.
7. In the **Reviewers** section, click the gear icon and add any specific reviewers you need for your PR.  
You might need to know their GitHub username.
8. If you’re ready to send a notification to your chosen reviewers, click **Create Pull Request**.  
If you still need more time to make additional changes, but just wanted a quick check on the start of a project, expand **Create Pull Request** and click **Create draft pull request**, instead.

Your PR should be reviewed by your chosen reviewers or someone else on the Documentation team within a couple of working days. We greatly appreciate community contributions and do our best to review them promptly.

If you’re a member of the Documentation team, do not forget to share a link to your PR in our review channel on Slack.

## [](#review-an-existing-pull-request)Review an Existing Pull Request

To review an existing pull request, use GitHub’s Pull Request Review features:

1. [Starting a Review](https://help.github.com/en/articles/reviewing-proposed-changes-in-a-pull-request#starting-a-review)
2. [Marking a File as Viewed](https://help.github.com/en/articles/reviewing-proposed-changes-in-a-pull-request#marking-a-file-as-viewed)
3. [Submitting your Review](https://help.github.com/en/articles/reviewing-proposed-changes-in-a-pull-request#submitting-your-review)

## [](#incorporate-feedback-from-a-review)Incorporate Feedback from a Review

To incorporate feedback from a review of an existing pull request, use GitHub’s [Applying Suggested Changes](https://help.github.com/en/articles/incorporating-feedback-in-your-pull-request#applying-suggested-changes) instruction page.

## [](#next-step)Next Step

After your PR has been reviewed, you can click **Merge pull request** to merge your changes into your chosen branch.

If you’re a member of the Documentation team, you can choose to build the Couchbase Documentation site to get your changes live right away, or wait for the daily build to publish your changes the next day.

> [!NOTE]
> Make sure you delete your branch after you have merged your pull request. This keeps our repositories tidy.