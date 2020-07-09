# Discussion - Improving the Notebook Experience for Text-based Workflows

# Contents

1. Summary
2. Proposal
3. Motivation
4. Use Cases
5. Features/Requirements of an Optional New Format
6. Compatibility with Jupyter Format Standard
7. Options Under Consideration
8. Unresolved Questions
9. Prior Art and Additional Options found Insufficient for this Proposal
10. Guide-level Explanation
11. Reference-level Explanation
12. Rationale and Alternatives


# Summary

_To Be Done_


# Proposal

_To Be Done_


# Motivation


## Project Jupyter

The goal of Project Jupyter ([Project Jupyter | Home](https://jupyter.org/)) is to provide:


### **Open Standards for Interactive Computing**


#### 
The Jupyter Notebook is based on a set of open standards for interactive computing. These open standards can be leveraged by third party developers to build customized applications with embedded interactive computing. 

Through the work of the Jupyter team, since 2006, the community has created a set of tools that enable technologists across the technological skill spectrum to simply engage with data, data science and machine learning. A subset of these tools include (below is a non-exhaustive list - for more info read ([here](https://jupyter.org/documentation))):
 - the core ([Jupyter Notebook Experience](https://jupyter-notebook.readthedocs.io/en/stable/)) (the visual experience in a browser)
 - [JupyterHub](https://jupyter.org/hub))
 - [Jupyter Console](https://jupyter-console.readthedocs.io/en/stable/))
 - [IPython](https://ipython.readthedocs.io/en/stable/))
 - [.ipynb Notebook format](https://nbformat.readthedocs.io/en/latest/format_description.html))
 - [Jupyter kernel communication protocol](https://jupyter-client.readthedocs.io/en/latest/))
 - [Binder & MyBinder.org](https://mybinder.org/))
 - [nbviewer](https://nbviewer.jupyter.org/)]
 - [nbformat](https://nbformat.readthedocs.io/en/latest/))
 - [nbconvert](https://nbviewer.jupyter.org/)]
 - [repo2docker](https://github.com/jupyter/repo2docker))

Additionally a large set of third party tools have been created to extend the usage for specific scenarios. These include:
 - [nbdime](https://github.com/jupyter/nbdime)
 - [jupytext](https://github.com/mwouts/jupytext)
 - [MyST](https://myst-parser.readthedocs.io/en/latest/)
 - [jupyter-format](https://jupyter-format.readthedocs.io/en/latest/motivation.html)
 - [reviewnb](https://github.com/ReviewNB)
 - jupyter-text ** is this different than jupytext? ** 
 - [wrattler](https://github.com/wrattler/wrattler)

The Jupyter Notebook Format is an open standard which has existed for a number of years. The 2017 ACM Software System Award recognized Jupyter for: [https://awards.acm.org/award_winners/perez_9039634#2017-acm-software-system-award](https://awards.acm.org/award_winners/perez_9039634#2017-acm-software-system-award)


For Project Jupyter, a broad collaboration that develops open-source tools for interactive computing, with a language-agnostic design. These tools, that include IPython, the Jupyter Notebook and JupyterHub, have become a de facto standard for data analysis in research, education, journalism, and industry._


## The Jupyter Notebook Format

This discussion is primarily scoped to the way Jupyter stores the notebook on disk.

The [The Jupyter Notebook Format — nbformat 5.0 documentation](https://nbformat.readthedocs.io/en/latest/index.html) defines the open standard  [format_description](https://nbformat.readthedocs.io/en/latest/format_description.html) for Jupyter notebook files, also referred to as `ipynb` files. The JSON schema for the notebook is documented in the [jupyter/nbformat · GitHub](https://github.com/jupyter/nbformat/tree/master/nbformat) repo.

The nbformat open standard notebook offers a [Python API for working with notebook files — nbformat 5.0 documentation](https://nbformat.readthedocs.io/en/latest/api.html). This Python API enables reading and writing of notebooks along with a way to programmatically create notebooks.


### Important Attributes of the Jupyter Format


*   Cells
*   Source
    *   Contains source code that a user is editing to produce outcomes. Usually what people care the most about reviewing.
    *   Can be markdown, kernel-language code, magics, or raw cells
*   Metadata
    *   Stores execution information, parameter indicators, format rendering hints, and domain/organization specific fields for jupyter extensions to reuse
    *   Stores kernel and language information
    *   Stores widget output data that’s shared across the various cells and between headless and headed execution patterns.
    *   Encodes name and authorship information
    *   Stores domain/organization specific fields for jupyter extensions to reuse
    *   Ignoring or removing metadata entirely can break workflows that are using extensions, though changes once initially set are rare for the non-runtime information attributes
    *   Exception information when error stop execution
*   Output
    *   Results of a run / execution, oriented by the source cell that triggered them.
    *   Includes logs, visuals, and data outcomes for human and machine parsing. Usually associated with a point-in time execution to capture the state of things during a notebook resolution.
    *   Typically, but not always, stripped before being included in version control.
    *   Almost always preserved when sharing outside of version control as a form or reporting.


## Motivation for Investigating a New Format

Notebooks have a broad set of uses that continue to grow every day. In order to meet the needs of these scenarios, .ipynb files contains a fair bit of complexity for capturing the inputs, outputs, and metadata from a user. Unfortunately, while the complexity is necessary for many key use cases, it can come at the expense of a user's ability to use common Unix tools. Further, the ecosystem needs the .ipynb format to be stable over time so that it does not cause massive disruption.

To give users the ability to use common Unix tools to inspect, understand, and edit the notebook's contents in a text based or line based formats, we have created this discussion document to explore potential benefits and costs.

There are a significant number of data scientists that use text-based workflows though we do not have data on exactly how many. To simplify how these individuals can interop with the Jupyter ecosystem, it is important to identify the core flows that these individuals use. Today, most of the GNU Linux/Unix ecosystem uses text-based workflows like using `diff` and `patch`. These tools are specifically called out because they are in extremely broad usage and often represent the core of both human-readable and automated tooling. If we are able to solve for using these tools, and offer an alternative, optional, file format to the ipynb file format, we would unlock level diffing, visualization, inline commenting and other common workflows more readily.


## User Groups / Communities

The IPython notebook initiative, which evolved into Jupyter notebooks, [originally provided](http://blog.fperez.org/2012/01/ipython-notebook-historical.html) an interactive notebook style user interface to the IPython environment to support interactive computation research. Since then, the user community around Jupyter notebooks has grown considerably and now includes, but is not limited to, several distinct practice areas:

*   Data Science / Machine Learning
    *   Local/offline experimentation
    *   Producing production models 
    *   Debugging existing models
    *   Machine learning research never intended to move to production
    *   Open science communication and review
    *   lecture notebooks, workshop tutorials, etc [[https://github.com/search?l=Jupyter+Notebook&q=lecture+notes&type=Repositories](https://github.com/search?l=Jupyter+Notebook&q=lecture+notes&type=Repositories)]
    *   Etc
*   Data Engineering
    *   Defining reproducible tasks for parameterized extract, transform, or load operations
    *   Recording data movement operations in a way that’s easily modified and rerun for particular parameterizations when an error occurs
    *   Localized logging associated with specific tasks
    *   Visual indicators for data trends that can indicate data quality issues
    *   Data auditing
*   Data Analytics
    *   Low-code ability to collect data (e.g. magics)
    *   Easy to share common starting places for problems
    *   Access to programmatic concepts without needing full development tool chains
    *   Easy to share results with peers and organization
    *   Productionization path is has lower friction compared to writing scripts or one-off queries
*   Systems Operations
    *   System monitoring / reaction made easy to implement and visualize (not unique to Jupyter tooling)
    *   Disaster recovery playbooks can be written in one document that’s testable and reproducible with documented instructions
    *   System probes can be captured and shared easily without screen captures
*   Teaching and learning
    *   Pipelines are used at universities who are teaching at scale especially those that are teaching data science, grading, integrating to LMS/records systems, etc.
    *   Student use and instructor use would be a separate use case
    *   E.g., [https://inferentialthinking.com](https://inferentialthinking.com), [https://data8.org](https://data8.org), [https://ds100.org](https://ds100.org) 
*   Scholarly publishing workflows
    *   E.g., [https://conp-pcno.github.io/](https://conp-pcno.github.io/)
*   Communicating data-intensive ideas
    *   Data journalists (e.g., [https://github.com/datadesk/california-coronavirus-data](https://github.com/datadesk/california-coronavirus-data))
    *   Documentation assets (e.g. [https://myst-nb.readthedocs.io/](https://myst-nb.readthedocs.io/) and [https://nbsphinx.readthedocs.io/en/0.7.1/](https://nbsphinx.readthedocs.io/en/0.7.1/))

## File Comparison

At the core of our effort is the mechanism by which most users compare files. The issues with diffing notebooks, many of which have already been identified in [JEP 08](https://github.com/jupyter/enhancement-proposals/blob/master/08-notebook-diff/notebook-diff.md) include diffing "input" content in the context of the document format (JSON) and diffing output or embedded content (cell outputs, media content embedded in markdown cells). While ``nbdime`` does provide an excellent solution for some, it unfortunately uses a non-standard mechanism for diffing that makes it difficult to integrate with most other common tools (e.g. `diff` and `patch`). Additionally, as `diff` and `patch` are included in many applications (as an embedded tool) or hosted workflows (e.g. GitLab, GitHub, Mercurial), it will be challenging to augment those solutions with an additional tool in order to unlock a better experience.

If we were able to offer an optional file format that supports line-based comparison allows users to use ``diff`` and ``patch``, we would unlock a number of new sceraios. ``diff`` and ``patch`` are available in every default server installation meaning no further installation would be required. Line level comparison is the standard in the GNU/Linux ecosystem and supporting a file format that can be diff’d in a line-level way will unlock thousands of tools and workflows. That is to say, even if someone does not use ``diff`` or ``patch``, if they need to do any sort of comparisons of files, it is likely they understand the standard ``patch`` format. Some common scenarios that would be unlocked include:

*   Shipping and visualizing patches
*   Commenting inline
*   Manually inspecting raw notebook contents
*   Any service that expects file format support of this kind

Though ``nbdime`` supports a subset of these experiences for Jupyter notebooks, there are few other tools that support the ``nbdime`` patch-format for the same use-case. 

A further challenge for comparing notebook files line by line or in a text based medium is that notebooks contain rich media contents like images, videos, animations or even small GUI applications. This content is an essential part of a notebook but showing a meaningful diff in a terminal is challenging. Solving this for the new file format is necessary before it could be accepted by the community. 

# Use Cases


## An example of an individual user

TODO: add a use-case of an individual person using jupyter notebooks locally, along with diffing / merging / etc. 

## An Example of Collaboration

**Illustrating the challenge**


*   Bao, the site reliability engineer (SRE), works at a small startup building machine learning models. She  is on-boarding a small data science team who wants to begin collaborating.
    *   To date, this team has been sharing their notebooks via network shares (e.g. SMB, DropBox) but they want to move to something better.
    *   She'd like to use commenting and patches which is how the software engineers in her organization collaborate.
    *   Bao cannot integrate notebooks into her company's existing `diff` and `merge` based infrastructure used by other software engineers and organizations because, though JSON is non-binary (and therefore can be committed), the comparisons generated are often quite complicated and non-human readible. 
    *   Further, automated tools in her corporate workflow (e.g. linting, complexity detection, etc) use `patch` files to analyze changes, and struggle with the existing files generated.
    *   Her IT department would prefer not to install new tools as adding new binaries to existing blessed images require a significant security analysis and IT analysis to add, for each incremental version.
    *   Her organization uses inline commenting, viewing diffs of her applications and notebooks together when they appear in a single commit, and patches generated by her security infrastructure to notebooks all of which cause merge conflicts when she interacts with notebooks 
        *   (e.g. her security infrastructure evaluates and generates `patch` formatted updates to python imports, and she needs to manually apply these changes where it is automatically applied in all other applications)
    *   As a result, she feels isolated. This separation has made it difficult to integrate the data science team into the rest of the software engineering toolchain making it harder to move her models, when ready, to production.
    *   If she had access to optionally saving (or converting automatically, such as via a githook) to a new format that supported these workflows, she would be much more intergrated with her colleagues and able to reuse existing tools in her organization.

**How a potential solution would look**

*   Amal, the data scientist, opens a Jupyter notebook using Jupyter. She is able to see inputs and outputs generated by her team the last time they were saved.
*   Amal goes to the first cell and enters a command saying `c.save_options = 'git-friendly'`. From this point forward, the file will be saved as a version friendly to line level diffing.
*   Adding this option does not change Amal’s experience with the notebook interface. Everything else about the file works the same - running cells, displaying rich outputs, sharing with her colleagues are all the same.
*   Her colleague, Madhuri, wants to see the changes that Amal has made.
    *   Amal saves the file to their shared SMB share. 
    *   Madhuri opens the file from the share using Jupyter > Open. Everything appears exactly as it did with the `.ipynb` format. 
    *   Madhuri has some tooling built around the existing notebook format (`.ipynb`), so she removes the configuration setting at the top of the file, and it continues to work properly. 
*   Amal is ready to contribute the file to the repo. She goes into the command line and, using standard git commands, adds and commits the notebook to her repo.
*   Amal decides to change a hyperparameter.
    *   She creates a branch locally, and  opens the notebook in that branch.
    *   She thought one variable change would be enough but it ends up being a number of different changes before she gets her model to converge.
    *   She also needs to make a change to a python file that is included with her overall project.
    *   She finally reruns all the cells, generating outputs inline, and sees that everything looks correct.
*   She goes back to the command line and decides to commit this change to the repo.
    *   When she adds and commits the file, she sees only the lines that impact inputs that are being checked-in. This is despite several large output blobs that have changed in the file.
    *   She's also able to see python changes as well - the changes feel like a unified change, rather than siloed changes - one in a notebook and one in a python file.
    *   She pushes the commit to GitHub and the diff is pushed up to site.
*   Amal goes to GitHub and executes a pull request against the core repository. She can see the line diffs in a straightforward side-by-side comparison - both python and notebook seen side by side.
*   Amal tells Madhuri via slack that she's made a change and wants feedback on her PR and wants a review.
    *   Madhuri logs in and sees the changes. She’s curious about why Amal changed the file signature to the python function and how that impacts its use in the notebook.
    *   She’s able to make an inline comment which immediately triggers Amal to come and discuss it.
    *   The two go back and forth in the flow, and agree on the final decision to add another parameter to the function.
    *   Amal goes back to her original commit, makes the changes and files a new PR.
    *   Madhuri LGTMs the PR and its merged into the main repo.
*   At this point, the automated CI/CD takes over.
    *   The workflow goes through a standard flow - stripping comments, linting, running unit tests, packaging for distributed training, and then running the distributed.
    *   Because the file only triggers this when a significant change has been made, the fact that the outputs have been removed from the core notebook file, and diffs only show line level changes, the tools are not mistakenly triggered on irrelevant content.
*   The CI/CD works great, and kicks off distributed training. Soon the project will be rolled out to production!

## Basic Use Cases

Using `diff` or `patch` comparison tools, a user or tool should be able to accomplish the following. (`.nff == ".new_file_format_extension"`)

```
diff originalfile.nff updatedfile.nff > patchfile.patch
patch originalfile.nff -i patchfile.patch -o updatedfile.nff
```
Tools to consider compatibility with as we move forward:

*   nbdime
*   nbconvert
*   jupyter-text
*   jupyter-format
*   reviewnb
*   jupytext
*   wrattler
*   nbviewer

# Features/Requirements of an Optional Format

*   Using the new notebook format is optional. A user that chooses the new format will have 100% similar functionality with the old format. When interacting with any of the core Jupyter tools, they will not experience any difference.
*   The format is 100% round-trippable to .ipynb. That’s not to say that all functionality in the new format will work in .ipynb, but 100% of .ipynb functions will work in the new format. Non-functional items will be preserved intact.
*   Supporting `diff` and `patch` so that tools that embed these tools will function
*   Users with the existing format will continue to have a first class experience and will never be forced to upgrade to the new format without their explicit consent

# Compatibility with Jupyter Format Standard

_To be done_

# Options Under Consideration

## Improve this by creating a new storage format

TODO: insert proposed path forward here

## Improve this with minor modifications to the `ipynb` storage format

Several of the issues raised with `diff` and `patch` have raised also simply boil down to JSON, as opposed to the underlying data structure itself. Another approach would be to simply try swapping out JSON for some other, more diffable structure such as YAML. This would be quite elegant, as YAML is explicitly a superset of JSON

## Improve this with minor modifications to the `ipynb` storage structure

Another option is to solve this purely at the level of the *structure* of the IPYNB JSON that is saved to disk (not the in-memory object that is loaded with `nbformat`). I can think of three big issues with diffing the current IPYNB files:

*   the outputs are incomprehensible
*   the metadata often changes in a way that isn’t relevant to the user’s diff
*   the JSON formatting requirements (e.g. special-casing characters) is cumbersome (more of a problem w/ editing than diffing per-se)

This is compounded by the fact that the notebook outputs and metadata are _interwoven _with the content (which is most likely what most users care about when they’re looking at a diff).

So, one option could be to re-work how the ipynb files are structure on-disk. They remain JSON, but the structure looks something like:

```
<for cell in cells>
    <cell input>
    <reference to cell output>
<notebook metadata>
<for output in outputs>
    <cell output>
```

That way, the incomprehensible things (the outputs) would be at the bottom of any diff, and could either be filtered out or simply ignored more easily than they currently are, allowing the user to focus on the content sections of the file.

## Improve this without changing the ipynb format or creating a new one

Changing the core ipynb format, or adding a new one, is a potentially disruptive move. These issues around diffing/merging/commenting could also be improved with better tooling, bridges, etc. See 

# Rationale and alternatives

## Unresolved Questions

*   What parts of the design do you expect to resolve through the JEP process before this gets merged?
*   What related issues do you consider out of scope for this JEP that could be addressed in the future independently of the solution that comes out of this JEP?

Below are a list of concerns that must be addressed:

*   Lossless round-tripping between .ipynb and .nff
*   100% compatibility with any tools that engage with jupyter 
    *   **QUESTION**: Possible?
*   Format must not be commercially restricted in some way
*   Format should be interactable - not a read-only and/or intermediate format
*   Format must include outputs
    *   **QUESTION**: Necessary? What use cases need outputs included?
    *   **QUESTION**: Would a separate file with pointers be acceptable?
*   Format should be compatible with being included in the default install as an option (though will not be the default for a significant amount of time)
*   Should the format be email-able?

## Answered questions

*   More performant viewing on a web page (how do we measure?) - What are the performance bottlenecks in rendering? Can we help here?
    *   A: performance (e.g. rendering, viewing, etc) is likely not a result of the underlying format, and there are several rendering tools that are highly performant for ipynb files (e.g., [GitLab](https://www.google.com/url?q=https://gitlab.com/wooheaven/Python-Study/-/tree/master/&sa=D&ust=1594233314856000&usg=AFQjCNHYO2LXEFfqcPQqO8FC2YanWpiQIQ), [nbviewer](https://nbviewer.jupyter.org/github/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/blob/master/Chapter1_Introduction/Ch1_Introduction_PyMC3.ipynb), and all of the web-based jupyter interfaces, such as jupyterlab/notebook, nteract, vscode ipynb extension, pycharm, etc)

# Prior Art

Discuss prior art, both the good and the bad, in relation to this proposal. A few examples of what this can include are:

*   Does this feature exist in other tools or ecosystems, and what experience have their community had?
*   For community proposals: Is this done by some other community and what were their experiences with it?
*   For other teams: What lessons can we learn from what other communities have done here?
*   Papers: Are there any published papers or great posts that discuss this? If you have some relevant papers to refer to, this can serve as a more detailed theoretical background.

This section is intended to encourage you as an author to think about the lessons from other languages, provide readers of your JEP with a fuller picture. If there is no prior art, that is fine - your ideas are interesting to us whether they are brand new or if it is an adaptation from other languages.

## A table of notebook formats and their features

||||||||
|--- |--- |--- |--- |--- |--- |--- |
|Project|OSS & >50% of contrib from community|Diff technique|Git ‘friendly’*?|Supports outputs in the same file?|Additional features|Rejected/Reason?|
|Jupyter Notebook|Yes|Use nbdime|No|Yes|||
|MyST Notebook|Yes||Yes|No|Works well with Sphinx & Jupyter Book (references, bibliography)||
|Jupytext Markdown|Yes||Yes|No|Well rendered by GitHub / VS Code See e.g. https://github.com/plotly/plotly.py/tree/doc-prod/doc/python||
|Percent scripts|Yes||Yes|No|Notebooks as scripts. Work well in VS Code, PyCharm Pro, Spyder, Hydrogen, and also with tools like black, etc.||
|jupyter -format|Yes||||||
|MatLab|No||||||
|R Markdown|No||Yes|No. But the .nb.html file does.|||
|Pandoc Markdown|Yes?||Yes|Yes|||
|CoLab|No||||||
|MLFlow|No||||||
|Zeppelin|Yes||||||
||||||||


* While rendering rich diffs visually is 'easy', most git workflows require things like comments, resolving conflicts, etc. This column is, ultimately, just opinions, but when described as 'git friendly' we would expect it to be reasonably possible to comment inline (in a persentent way), resolve git conflicts logically. 

## Previous discussions, JEPs, etc about text-friendly format

*   [A twitter thread/responses with lots of opinions about YAML vs. JSON](https://twitter.com/choldgraf/status/1280181444866748421)
*   [A blog post from Matthias about YAML-based notebooks](https://matthiasbussonnier.com/posts/05-YAML%20Notebook/)

# Guide-level explanation¶

Explain the proposal as if it was already implemented and you were explaining it to another community member. That generally means:

*   Adding examples for how this proposal affects people’s experience.
*   Explaining how others should _think_ about the feature, and how it should impact the experience using Jupyter tools. It should explain the impact as concretely as possible.
*   If applicable, provide sample error messages, deprecation warnings, or migration guidance.
*   If applicable, describe the differences between teaching this to existing Jupyter members and new Jupyter members.

For implementation-oriented JEPs, this section should focus on how other Jupyter developers should think about the change, and give examples of its concrete impact. For policy JEPs, this section should provide an example-driven introduction to the policy, and explain its impact in concrete terms.

**Not Yet Implemented**

# Reference-level explanation

This is the technical portion of the JEP. Explain the design in sufficient detail that:

*   Its interaction with other features is clear.
*   It is reasonably clear how the feature would be implemented.
*   Corner cases are dissected by example.

The section should return to the examples given in the previous section, and explain more fully how the detailed proposal makes those examples work.

**Not Yet Implemented**

# Rationale and alternatives

*   Why is this choice the best in the space of possible designs?
*   What other designs have been considered and what is the rationale for not choosing them?
*   What is the impact of not doing this?

**Not Yet Implemented**

Below are a few alternatives that could be explored

## Alternative approaches to changing the ipynb format

### Improve this with Jupytext + documentation

Recommend that users use Jupytext ([https://jupytext.readthedocs.io/](https://jupytext.readthedocs.io/)) to automatically keep two versions of their notebooks: one that is human-and-diff-friendly, one that is machine-friendly and   messier with more information. Outputs are in the `ipynb` format, not the text format. The text file is generally treated as the source of truth in merging conflicts.

Note: one could assume that the only time someone edits an `ipynb` file is *with a jupyter server*, and jupytext will automatically synchronize the ipynb and text file as long as the jupyter server is running. However, you could imagine many people editing the *text file* without a jupyter server (e.g. via a comment in github). That’s why the text file should always be the source of truth.

Providers that build UIs on top of git could add support in the following way

*   E.g. Two-way synchronization between a text-based notebook and an ipynb file with Jupytext.
*   Use Jupyter UI to activate this "pairing" so that it will automatically save an ipynb file to [.py/myst-markdown/pandoc markdown/etc].
*   Develop a mechanism to either move outputs to a specific section of the file (making it easier to diff/exclude) or pointers to an external file
*   Upstream recommendations to other tools (e.g. GitHub) - GitHub presents a warning that says "if you want text-based diffing for notebooks, we recommend you use jupytext to pair your ipynb files with a text-based version of them. in your PRs, make comments, edits, etc to the text-based versions." 
*   GitHub further treats a paired ipynb and text-based file in a special way. E.g.: "if in a PR, two files are detected with jupytext metadata that links them, then in the diff only show the text file, and in the "enriched view" only show the notebook file.

#### Potential challenge here
*   Scenario
    *   2 data scientists work on same notebook using git.
    *   Data scientist A uses notebook with ipynb, data scientist B uses jupytext. B changes cell and pushes both files
    *   Potential problem: A can't resolve conflict easily, has to pull B's change, resolve conflict in jupytext, export to ipynb, push.
*   One potential solution
    *   In this case, any changes to the ipynb file via a jupyter server will be automatically reflected in the text file. If we assume that the text file is always the source of truth, then DS A will merge changes into their *text file*, jupytext will automatically update the ipynb file, and then proceed.
    *   You could also imagine an extreme case (maybe a setting in jupytext or something), where jupytext stores `ipynb` files with *no content* in them, only cells with outputs. Then you rely on ipynb for all the messiness of outputs, on the text file for the content and structure of the document, and use jupytext to sync them


### Improve the tooling around ipynb diffing

There are tools out there that facilitate diffing and merging with the notebook format (most notably, [https://nbdime.readthedocs.io/](https://nbdime.readthedocs.io/)). Perhaps there are ways that this tool could improve its functionality in order to more easily integrate into git-based workflows, or into products that build on top of git-based workflows (like GitHub).

For reference, here is the output from `nbdime` and git when diffing a notebook with a single line changed:

**Git**
```
$ git diff Untitled.ipynb
diff --git a/Untitled.ipynb b/Untitled.ipynb
index e2f4c76..199ae3e 100644
--- a/Untitled.ipynb
+++ b/Untitled.ipynb
@@ -6,7 +6,7 @@
    "metadata": {},
    "outputs": [],
    "source": [
-    "print('hi')"
+    "print('there')"
    ]
   }
  ],
```


**nbdime**
```
$ nbdiff Untitled.ipynb

nbdiff Untitled.ipynb (HEAD) Untitled.ipynb
--- Untitled.ipynb (HEAD)  (no timestamp)
+++ Untitled.ipynb  2020-07-03 16:56:33.438469
## modified /cells/0/source:
-  print('hi')
+  print('there')
```

### Improve online products for diffing/merging ipynb files

As we’ve discussed in this document, many people do their diffing/merging/editing/commenting via web services and interfaces. For example, [GitHub](https://github.com) and [GitLab](https://about.gitlab.com/).

As these services have control over the interfaces that are exposed to users, and there is already some support for more “rich” interactions with certain formats (e.g., [GitHub's fancy support for images](https://docs.github.com/en/github/managing-files-in-a-repository/rendering-and-diffing-images)), the story around git-based notebook workflows could be improve at the level of these interfaces.

Some issues to track this:
*   [GitLab improvements for diffing/merging ipynb files](https://gitlab.com/gitlab-org/gitlab/-/issues/22329#note_374052932)

## Sustainability issues

The Library of Congress [Sustainability of Digital Formats](https://www.loc.gov/preservation/digital/formats/intro/intro.shtml) has a [schema for cataloguing digital document formats](https://www.loc.gov/preservation/digital/formats/fdd/fdd_explanation.shtml) as well as a set of criteria against which the sustainability of digital documents formats can be tracked.

Sustainability factors include:

*   [Disclosure](https://www.loc.gov/preservation/digital/formats/sustain/sustain.shtml#disclosure): specifications, schemata;
*   [Adoption](https://www.loc.gov/preservation/digital/formats/sustain/sustain.shtml#adoption): extent of use;
*   [Transparency](https://www.loc.gov/preservation/digital/formats/sustain/sustain.shtml#transparency): eg human readability, text format;
*   [Self-documentation](https://www.loc.gov/preservation/digital/formats/sustain/sustain.shtml#self): extent to which format is self-documenting;
*   [External dependencies](https://www.loc.gov/preservation/digital/formats/sustain/sustain.shtml#external): eg hardware, o/s;
*   [Impact of patents](https://www.loc.gov/preservation/digital/formats/sustain/sustain.shtml#patents): patent encumbered; (_"…and licensing"_ would perhaps a more useful generalisation of this field?)
*   [Technical protection mechanisms](https://www.loc.gov/preservation/digital/formats/sustain/sustain.shtml#technical): eg encryption.

There are also fields associated with [Quality and functionality factors](https://www.loc.gov/preservation/digital/formats/fdd/fdd_explanation.shtml#factors) which for text documents include: normal rendering, integrity of document structure, integrity of layout and display, support for mathematics/formulae etc., functionality beyond normal rendering.

Thet `.ipynb` format is not currently on the [list of mentioned formats](https://www.loc.gov/preservation/digital/formats/fdd/browse_list.shtml). Records for <code>[geojson](https://www.loc.gov/preservation/digital/formats/fdd/fdd000382.shtml)</code> and <code>[Rdata](https://www.loc.gov/preservation/digital/formats/fdd/fdd000470.shtml)</code> provide a steer for the sorts of thing that a such a record might initially contain.

## Downsides to creating a new format, or extending the current one

Changing the ipynb standard, or creating a different format, may have negative consequences. We should answer questions such as the following:

WIP / Outline below:

*   What are the downsides of creating a new notebook-based format?
    *   Fracturing ecosystem (e.g. “it worked in .nff why doesn’t it work in .ipynb or vice versa”)
    *   Core jupyter engineering/testing cost
    *   Confusion for users - (e.g. which one should I use)?
*   What are the downsides of changing the current ipynb format?
    *   Millions and millions of existing users
    *   This is not being considered at this time
*   Why does the current tooling ecosystem not work in a way that cannot be resolved by iterative improvements to this ecosystem?
    *   diff & patch do not work elegantly with current format
    *   Difficult for humans to interact with
    *   Difficult to comment on in standard git flows (e.g. via Reviewable, GitHub, GitLab, etc)
    *   Produces noise-y commits

# Future possibilities

Think about what the natural extension and evolution of your proposal would be and how it would affect the Jupyter community at-large. Try to use this section as a tool to more fully consider all possible interactions with the project and language in your proposal. Also consider how this all fits into the roadmap for the project and of the relevant sub-team.

This is also a good place to 'dump ideas'. if they are out of scope for the JEP you are writing but otherwise related.

If you have tried and cannot think of any future possibilities, you may simply state that you cannot think of anything.

Note that having something written down in the future-possibilities section is not a reason to accept the current or a future JEP; such notes should be in the section on motivation or rationale in this or subsequent JEPs. The section merely provides additional information.

**Not Yet Implemented**
