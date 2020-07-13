# Safia's notes:

* The JEP is long and repetitive. I would make some edits to:
  * Use headings and bold statements to draw the readers attention to the relevant points.
  * Leverage an appendix/endnotes to avoid repeating the same points throughout the document.
  * Include more references to prior art in the community and existing community projects.

* The JEP lacks a rigorous problem statement. The "Motivation for Investigating a New Format" section makes the case the interop with common Unix tools is a key part of the proposal but doesn't address why.
  * What about non-Unix desktop users or Jupyter notebook users who are low-code or no-code personas?
  * We would unlock level diffing, visualization, inline commenting and other common workflows more readily.
  * It's not clear how visualization and inline commenting and relevant to Unix tooling here.
  * What other motivations are there for creating a new format? Considering the scope of the proposal, identifying other motivations is key.

* The JEP lacks a lot of technical detail about the implementation. After reading the document, I'm still not clear what the problems to be solved are and what the solution is. The "Not Yet Implemented" sections should be filled in and there should be answers (collective answers or individual) to the questions in the unresolved questions sections.
  * What components in the Jupyter ecosystem need to be changed to successfully execute this change?
  * What are the performance and security ramifications of the change?
  * What is the adoption story for the proposed changes?

* While the user scenario is helpful, I'd trim it down a bit and try to think of a simple end-to-end that drives the key points.
  * The details can be moved to an appendix/endnote to keep the JEP easier to understand.

* The table at the end with prior art is helpful but I'd simplify the headings to Project/Description/Pros/Cons. This makes it easier to identify the strengths and weaknesses from an engineering perspective of existing community projects.
  * What aspects of each project make it easy to use for users and easy to maintain for the open source community?
  * What are design improvements/challenges that each open source community is undertaking?
  * At which point in the Jupyter ecosystem does the project interface?


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
 - the core ([Jupyter Notebook Experience](https://jupyter-notebook.readthedocs.io/en/stable/) (the visual experience in a browser)
 - [JupyterHub](https://jupyter.org/hub)
 - [Jupyter Console](https://jupyter-console.readthedocs.io/en/stable/)
 - [IPython](https://ipython.readthedocs.io/en/stable/)
 - [.ipynb Notebook format](https://nbformat.readthedocs.io/en/latest/format_description.html)
 - [Jupyter kernel communication protocol](https://jupyter-client.readthedocs.io/en/latest/)
 - [Binder & MyBinder.org](https://mybinder.org/)
 - [nbviewer](https://nbviewer.jupyter.org/)
 - [nbformat](https://nbformat.readthedocs.io/en/latest/)
 - [nbconvert](https://nbviewer.jupyter.org/)
 - [repo2docker](https://github.com/jupyter/repo2docker)

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


*   Notebook-Level Metadata
*   Cells
*   Source
    *   Contains source code that a user is editing to produce outcomes. Usually what people care the most about reviewing.
    *   Can be markdown, kernel-language code, magics, or raw cells
*   Metadata
    * Notebook-level Metadata
      *   Stores execution information, parameter indicators, format rendering hints, and domain/organization specific fields for jupyter extensions to reuse
      * Stores kernel and language information

    * Cell-level Metadata
      *   Stores widget output data that’s shared across the various cells and between headless and headed execution patterns.
      *   Encodes name and authorship information
      *   Stores domain/organization specific fields for jupyter extensions to reuse
      *   Ignoring or removing metadata entirely can break workflows that are using extensions, though changes once initially set are rare for the non-runtime information attributes
      *   Exception information when error stop execution
    * The `metadata` property is extendable so notebook apps, extensions, and end-users can define their own metadata.
*   Output
    *   Results of a run / execution, oriented by the source cell that triggered them.
    *   Includes logs, visuals, and data outcomes for human and machine parsing.
    *   Usually associated with a point-in time execution to capture the state of things during a notebook resolution. However, in presentational or interactive notebooks, the outputs would be the  "goal" of a notebook. For example, you might run a series of cells that in the end generate a meaningful visualization or a trained ML model. You might also have a notebook that contains interactive widgets.
    *   Typically, but not always, stripped before being included in version control.
    *   Almost always preserved when sharing outside of version control as a form or reporting.


## Motivation for Investigating a New Format

Notebooks have a broad set of uses that continue to grow every day. In order to meet the needs of these scenarios, .ipynb files captures the inputs, outputs, and metadata from a user. Unfortunately, the current structure of the .ipynb notebook makes it challenging to use common Unix tools and workflows. However, making any changes needs to be carefully considered; the ecosystem needs the .ipynb format to be stable over time so that it does not cause massive disruption.

The core of this investigate is due to the rise of a large number of new users for Jupyter. Specifically, there are a significant number of data scientists that use text-based workflows and Jupyter (though we do not have data on exactly how many). By text-based workflows we are referring to interactions (editing, sending, using in a DevOps pipeline) with files that have no higher level structure. All logic, comparison, etc must be done on a line-by-line basis. The canonical oxamplesof which in the GNU Linux/Unix ecosystem are `diff` and `patch` which are the center of most version control and comparison tools. These two tools are in extremely broad usage and often represent the core of both human-readable and automated tooling. If we are able to solve for using these tools, and offer an alternative, optional, file format to the ipynb file format, we would unlock level diffing, visualization, inline commenting and other common workflows more readily.


## User Groups / Communities

The IPython notebook initiative, which evolved into Jupyter notebooks, [originally provided](http://blog.fperez.org/2012/01/ipython-notebook-historical.html) an interactive notebook style user interface to the IPython environment to support interactive computation research. Since then, the user community around Jupyter notebooks has grown considerably and now includes, but is not limited to, several distinct practice areas:

<!--

To make this section more useful, I'd probably rephrase it in the context of the JEP. As in, here are the different types of notebook users and how they interact with the document format. As opposed to a general list of Jupyter-using communities.

-->

<!--
The pipelines are used at universities who are teaching at scale especially those that are teaching data science, grading, integrating to LMS/records systems, etc.
-->

*   Data Science / Machine Learning
    *   Local/offline experimentation
    *   Producing production models 
    *   Debugging existing models
    *   Machine learning research never intended to move to production
    *   Open science communication and review
    *   lecture notebooks, workshop tutorials, etc [[https://github.com/search?l=Jupyter+Notebook&q=lecture+notes&type=Repositories](https://github.com/search?l=Jupyter+Notebook&q=lecture+notes&type=Repositories)]
    *   Etc

<!--
I'm wary of commenting too much here because I'm not sure this is in scope for the suggested format... Maybe a thread on the discourse forum then bring back anything relevant here?

That said, by publishers, I mean eg academics who want to create and distribute:

- interactive lecture notes and tutorials; and/or
- interactive research publications.

In a sense, the aim is to produced finished works whose publication format is the rendered notebook. (This means that when viewing and editing the work you may need to install all the notebook extensions that tweak the UI so it's viewed as intended.)

Diffing and commenting are often required in several different ways:

1) during production, eg when there are multiple authors working on a publication, or when an author hands over to an edit who wants to communicate suggested edits back to the author(s);

2) during open review (eg if a paper is offered as a preprint and you are likely to want to solicit comments) or publication (promoting discussion via comments);

If used for instruction, notebooks are increasingly also used for assessment (eg using things like nbgrader or just by exchange of notebooks); for a marker/grader, they may want to diff a notebook to see what the student has done compared to the originally provided assessment notebook; the marker may then want to comment and annotate the notebook and give it back to the student, who needs to clearly see what marker has added.

-->
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

<!--
Can we dig into what it would mean to make jupytext more "core"? Also, why this is an issue for other institutions to adopt it or not? For me, it's pretty straightforward to pip-install jupytext and it integrates nicely with the jupyter interfaces etc
-->

At the core of our effort is the mechanism by which most users compare files. The issues with diffing notebooks, many of which have already been identified in [JEP 08](https://github.com/jupyter/enhancement-proposals/blob/master/08-notebook-diff/notebook-diff.md) include diffing "input" content in the context of the document format (JSON) and diffing output or embedded content (cell outputs, media content embedded in markdown cells). While ``nbdime`` does provide an excellent solution for some, it unfortunately uses a non-standard mechanism for diffing that makes it difficult to integrate with most other common tools (e.g. `diff` and `patch`). 

<!-- Need details on how nbdime diffs compare with diff/patch -->

Additionally, as `diff` and `patch` are included in many applications (as an embedded tool) or hosted workflows (e.g. GitLab, GitHub, Mercurial), it will be challenging to augment those solutions with an additional tool in order to unlock a better experience.

<!--
nbdime is indeed meant to be general tooling for improving workflows for version control, which is why it’s implemented with the standard Git API for diff extensions. What we have now is targeted at human diff viewing and not roundtripping to line-based diffs, since we figured that line-based diff tools already covered that (as well as they can for JSON in general). But if there is a reasonable case to output a different line-based diff to work with particular tooling scenarios, that would be in-scope for nbdime. One of the key use case challenges we face and try to address in nbdime is that different folks want to see diffs of different things at different times (metadata, output, etc.). That makes it hard to say what folks want to see in a diff in general because there isn’t just one answer. But if you take line-based diffs as a constraint you can do other things to accomplish similar tasks, such as group the patches differently (input first, metadata second, outputs last; I don’t think patch specifies that they must be in order). Making a new serialization format of the same information focused on line-based tooling takes a similar approach, but does so at storage/edit time instead of diff time, with the big advantage of needing no plugins. This is true whether it’s accomplished by shifting output to the end of the file as Chris has suggested, or a separate file, as can be done with jupytext.
-->

If we were able to offer an optional file format that supports line-based comparison allows users to use ``diff`` and ``patch``, we would unlock a number of new sceraios. ``diff`` and ``patch`` are available in every default server installation meaning no further installation would be required. Line level comparison is the standard in the GNU/Linux ecosystem and supporting a file format that can be diff’d in a line-level way will unlock thousands of tools and workflows. That is to say, even if someone does not use ``diff`` or ``patch``, if they need to do any sort of comparisons of files, it is likely they understand the standard ``patch`` format. Some common scenarios that would be unlocked include:

*   Shipping and visualizing patches (**NOTE** Needs example - grabbing a .patch file and sending it to another application (e.g. via pipe))
*   Commenting inline (**NOTE** Needs example of why commenting inline is challenging without line based patches)
*   Manually inspecting raw notebook (e.g. the JSON directly) contents
*   Any service that expects file format support of this kind

Though ``nbdime`` supports a subset of these experiences for Jupyter notebooks, there are few other tools that support the ``nbdime`` patch-format for the same use-case. 

<!--
Having two persist executable formats risks community fracturing. You don't have two Dockerfile formats, or two java jar formats, even though those have tooling issues that require extra command pipes to inter-operate with other standard commands. And the root reason is that the concerns and solutions will deviate over time for different formats making the overall project harder and harder to maintain and build ontop of. It doesn't matter if it's optional or not for this concern. Matter of fact I'd prefer it be more an all or nothing, moving future specs to a new base protocol format or leave the procotol as is. Have one pattern with some edge cases handled less well, not two that optimize for specific instances is a pretty common guiding principle in system design.

Additionally it feels like we're pushing Jupyter to reorient itself to native git commands when JSON's a common file format for tons of other projects. And there's lots of tooling for JSON diff / patch generically (here's the first three from googling): https://github.com/andreyvit/json-diff https://github.com/zgrossbart/jdd https://github.com/benjamine/jsondiffpatch
Yes those have their own issues concerns or problem they aren't solving, but the point is that I feel we skipped right past "make better tools to bridge ecosystems" and went to "redesign a major aspect of a mature project".

The very long thread on discourse may have given the impression that most everyone was happy with a format change, but I think the reserved concerns around what problem are we solving here, and is this the best change to make in order to solve that problem were difficult to see / express with all the noise of combined voices.

I agree - I wish that in this comment (https://discourse.jupyter.org/t/jupyter-and-github-alternative-file-format/4972/32?u=choldgraf) I had placed more emphasis on the first item, and also scoped it outside of GitHub's specific use-case. I think "improve tooling and bridges to make people's live better" is an important first step, and we should exhaust these options before we start creating new formats (or changing pre-existing ones). I think there is a lot of low-hanging fruit there that we can improve upon that would be much less-disruptive.
-->

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
*   Amal sets a configuration option in the notebook that causes Jupyter to save the file as .nff (new file format) instead of .ipynb.
*   Adding this option does not change Amal’s experience with the notebook interface. Everything else about the file works the same - running cells, displaying rich outputs, sharing with her colleagues are all the same.
*   Her colleague, Madhuri, wants to see the changes that Amal has made.
    *   Amal saves the file to their shared SMB share. 
    *   Madhuri opens the file from the share using Jupyter > Open. Everything appears exactly as it did with the `.ipynb` format. 
    *   Madhuri has some tooling built around the existing notebook format (`.ipynb`), so she removes the configuration setting at the top of the file, and it continues to work properly. 

<!--
It's not actually a part of the Jupyter spec / github, and there was no JEP (that I could find) to accept it as a standard. It's an experiment on things that can be done, not an generally accepted path forward for how to build Jupyter documents. (Correct me if I'm off base here). Which is totally fine but not a general replacement for `ipynb` files. There's also the occasional "why doesn't this work with jupytext in other project issues" and while not a huge maintenance burden it does add up and is a non-trivial risk for reliability with adding a 2nd experiment or a 2nd format. I'd like to see a Risks Section and be very clear about the implementation and tooling burden these choices would have, or you may see a split of repos that do and don't support the format change over the next year or two without maintainer inputs.

yeah I totally agree there - Jupytext is "just another project out there", it's nothing specific to Jupyter's governance processes. I see this approach as more like "don't change the underlying formats or do anything 'official', just improve the documentation around workflows that already exist, and potential build tooling that facilitates those workflows"

One thing that jupytext shows is how innovation can be applied around the open ipynb standard (is ipynb actually a standard yet?!). It extends what's possible for users who aren't necessarily interested in preserving cell outputs, and it may gain a user base of folk who use that document type as their primary document type (maybe with a paired hidden ipynb doc for rendering outputs in the notebook UI). If I don't have a jupyter server to hand, I can trivially write a markdown or py doc and know that I can later open it in a Jupyter notebook UI as a notebook. There have been a lot of attempts at jupyter-md etc over the years and Jupytext seems to be the one that has gained traction (eg positive signs based on Github fork/star/watch/used by/contributor counts).
Jupytext also provides a pragmatic attempt by a community developer to address the need for a text format. It didn't require permission and didn't try to force any changes on Jupyter standards.
-->

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

<!--
> So no DATA is lost, but no guarantees about functionality.
I agree with Chris that this sounds like it'll lead to fractured functionality and tools that can't work with one format or the other over time. I'd be more ok with 5.0 format uses .nnf and ipynb is for < 4.4. Choose one or the other based on the version of the spec being supported so the expectation would be all new tools use the new format when respecting new jupyter capabiltiies.
-->

*   Supporting `diff` and `patch` so that tools that embed these tools will function
*   Users with the existing format will continue to have a first class experience and will never be forced to upgrade to the new format without their explicit consent

# Compatibility with Jupyter Format Standard

_To be done_

# Options Under Consideration

<!--
I think another option should be considered, which is: do nothing in the Jupyter core ecosystem, and see if this problem can be improved with documentation and improvements to pre-existing tools.

I say this for two reasons:

1. IMO this should always be the first option of choice for any technical decision, and pursuing new tech should only ever happen when this option's possibilities have been fully-explored and still won't meet our needs.
2. Many of the things we've described in this JEP already exist. You can already have two-way synchronization between a text-based notebook and an ipynb file with Jupytext. There's even UI to activate this "pairing" so that it will automatically save an ipynb file to [.py/myst-markdown/pandoc markdown/etc]. The only thing that is missing there is what to do with the outputs, but that's also something that I know Jupytext would like to support as well. From the perspective of GitHub, you could imagine recommending a workflow like "if you want text-based diffing for notebooks, we recommend you use jupytext to pair your ipynb files with a text-based version of them. in your PRs, make comments, edits, etc to the text-based versions." You could even imagine GitHub treating a paired ipynb and text-based file in a special way. E.g.: "if in a PR, two files are detected with jupytext metadata that links them, then in the diff only show the text file, and in the "enriched view" only show the notebook file.


My biggest gripe with jupytext is that you need to maintain 2 files. Since Jupytext, once it handles outputs, will have all the information needed for round trip to ipynb, why do we need ipynb any more? Let's just use jupytext format for everything. That's the idea.

I think this gets to the question of trade-offs. If there is a text-based format that has all of the outputs in the format itself, is compatible with jupytext and round-trippable with ipynb, and is also much easier for humans to read, diff, etc, then sure I think this makes sense. But, I don't know if that perfect balance exists. My gut feeling is that if you try to put outputs and metadata in a text file, you'll quickly run into the same challenges we have with ipynb.

Also, I think it's worth highlighting the first bias that I mention above - we should always try to re-use pre-existing community infrastructure as much as possible before we create something new. Even if you ultimately do create something new, the experience gained from operating within the tools that the community already knows and uses will help make the end-result much better

I agree we won't get to a point when it's perfectly readable, but I do think we can get to a point when, at least code blocks and some output blocks, will be easier to handle in text manner. Problem with json is how nested it is and how poorly it handles multi-line strings. I mean, codeblocs are list of lines right now, that's hard to comprehend if you try to figure out, say, indentations. If we make it multi-line block of code, readability improves immediately. There was argument that even yaml is better than json, and that's true. Problem with yaml is that we're getting into nest-fest and distinction between python nesting and yaml nesting is next to impossible to visually determine. That's why format I'm thinking of and prototyping here https://github.com/machine-learning-apps/mystify/blob/main/examples/example_notebook.mystnb is mixture of few things:
1. inputs are as readable as I could get, so no nesting, multi line, pretty much clear python that you just need to copy-paste to run
2. blocks of output are readable when possible, but ofc things like figures will be blocks of incomprehensible gibberish. That's ok, as reviewer I simply wont even try to parse it.
3. metadata is clearly separated from input/output and stored in yaml, we may as well do it in json, but I think yaml is more readable. With json we could have 1 liner with all the metadata, which would make conflict resolution both easy and hard depending whether or not you want to understand what you're resolving.

This is obviously WIP, but I hope it shows direction I'm going for. I'll work on complex cases, including figures, next week
-->

## Improve this by creating a new storage format

TODO: insert proposed path forward here

## Improve this with minor modifications to the `ipynb` storage format

Several of the issues raised with `diff` and `patch` have raised also simply boil down to JSON, as opposed to the underlying data structure itself. Another approach would be to simply try swapping out JSON for some other, more diffable structure such as YAML. This would be quite elegant, as YAML is explicitly a superset of JSON

## Improve this with minor modifications to the `ipynb` storage structure

Another option is to solve this purely at the level of the *structure* of the IPYNB JSON that is saved to disk (not the in-memory object that is loaded with `nbformat`). I can think of three big issues with diffing the current IPYNB files:

*   the outputs are incomprehensible - e.g. images would be rendered as opaque blobs (as opposed to storing the images externally with a pointer) ** NOTE: Need additional examples here **
*   the metadata often changes in a way that isn’t relevant to the user’s diff
*   the JSON formatting requirements (e.g. special-casing characters) is cumbersome (more of a problem w/ editing than diffing per-se)

This is compounded by the fact that the notebook outputs and metadata are interwoven with the content (which is most likely what most users care about when they’re looking at a diff). This is not universally the case - for example, a diff could contain output that is relevant to the process (e.g. changes in hyperparameters from a code cell that searches the hyperparamter space for the best set).

So, one option could be to re-work how the ipynb files are structure on-disk. They remain JSON, but the structure looks something like:

```
<for cell in cells>
    <cell input>
    <reference to cell output>
<notebook metadata>
<for output in outputs>
    <cell output>
```

That way, the incomprehensible things (the outputs) would be at the bottom of any diff, and could either be filtered out or simply ignored more easily than they currently are, allowing the user to focus on the content sections of the file. This would require some form of associateion system (e.g. ID references that connect otherwise non-connected elements)

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

<!-- Restructure as pros/cons -->

* While rendering rich diffs visually is 'easy', most git workflows require things like comments, resolving conflicts, etc. This column is, ultimately, just opinions, but when described as 'git friendly' we would expect it to be reasonably possible to comment inline (in a persentent way), resolve git conflicts logically. 

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


## Previous discussions, JEPs, etc about text-friendly format

*   [A twitter thread/responses with lots of opinions about YAML vs. JSON](https://twitter.com/choldgraf/status/1280181444866748421)
*   [A blog post from Matthias about YAML-based notebooks](https://matthiasbussonnier.com/posts/05-YAML%20Notebook/)

# Guide-level explanation

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

Note: one could assume that the only time someone edits an `ipynb` file is *with a jupyter server*, and jupytext will automatically synchronize the ipynb and text file as long as the jupyter server is running. However, you could imagine many people editing the *text file* without a jupyter server (e.g. via a comment in github). That’s why the text file should always be the source of truth. (This is also the case with the nteract desktop app)

Providers that build UIs on top of git could add support in the following way

*   E.g. Two-way synchronization between a text-based notebook and an ipynb file with Jupytext.
*   Use Jupyter UI to activate this "pairing" so that it will automatically save an ipynb file to [.py/myst-markdown/pandoc markdown/etc]. (Note, this means that other clients like Lab, classic Notebook & nteract will have to implement the pairing functionality as well)
*   Develop a mechanism to either move outputs to a specific section of the file (making it easier to diff/exclude) or pointers to an external file
*   Upstream recommendations to other tools (e.g. GitHub) - GitHub presents a warning that says "if you want text-based diffing for notebooks, we recommend you use jupytext to pair your ipynb files with a text-based version of them. in your PRs, make comments, edits, etc to the text-based versions." 
*   GitHub further treats a paired ipynb and text-based file in a special way. E.g.: "if in a PR, two files are detected with jupytext metadata that links them, then in the diff only show the text file, and in the "enriched view" only show the notebook file.

<!--
For the sake of exploration. What if nbdime had a command to map the rendered outputs back to lines / opscodes? Say your text format was introduced as purely a diff format and we extended nbdime or something like it to render the proposed human readable diff that could map 1:1 back to the lines in the original file to generate opscodes. No persistence of a new format, but a schema for diff / patch friendly format. This would give the ability to choose what's important to render in a given context, while allowing for classic patch file generation for the raw source and without any tooling changes for 90% of the jupyter ecosystem. I can capture this idea in a section if we wanted to flush out what it Could be before rules it out or deciding something along those lines is workable.
-->

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

<!-- Note: What are these possible improvements? And/or what are the problems that need to be addressed in existing tools? -->

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

<!--
What about adding examples for more realistic edits? Mostly because the single line example doesn't motivate why a basic diff doesn't cut it :) I'd keep the single line diff example to give people a simple example to look at but also include one with a more complex diff to illustrate (or not) how well a line based diff works.
-->

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
