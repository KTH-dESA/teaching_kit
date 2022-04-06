# Teaching Kit and PPTX textifier

This repository contains the first prototype of a teaching kit - an online, user-updatable,
collaborative deposit of teaching material, together with some useful conversion scripts.

The online website is automatically generated from a folder of PowerPoint presentations.
By placing a new set of PowerPoint slides in the `files/ppt_presentations` folder and running
`python scripts/main.py`, you'll generate a suite of files under `_posts/modules` which can then be
rendered using a static website generator, Jekyll, and displayed online.

The files listed under the `_posts/modules` directory contain all the text and tables from the PowerPoint
presentations and are organised into files of the same name as the presentations.
Any images are stored under `assets/img/<presentation name>`.

To see the prototype in action, visit the website at https://kth-desa.github.io/teaching_kit/

## Requirements

To use this repository the following software are needed:

- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) follow the installation guide at the link provided
- [Python](https://www.python.org/downloads/) follow the installation guide at the link provided
- [Jekyll](https://jekyllrb.com/docs/) follow the installation guide at the link provided (you will be asked to install Ruby)

## Installation

Before installing any package in Python it is recommended to create a new environment using Conda:

```
conda create -n teaching_kit
conda activate teaching_kit
```

Then, install the following python packages to run the scripts:

```
conda install pathlib python-pptx
pip install frontmatter
```

In case of working from Windows it is useful setting up a Linux subsystem.

## Convert PowerPoint presentations to Markdown modules

1. Copy your PowerPoint presentations to `files/ppt_presentations`
1. Transform the presentations in modules.
   Run the script `main.py` to convert PowerPoint presentations to markdown files,
   type `python scripts/main.py`. The modules will be saved in `_posts/modules`

## Create lectures from collections of Markdown modules

To create lectures (collections of modules):

1. Apply tags to the modules running the script `python scripts/tags.py`
1. Create lectures combining the modules imported using the scripts `python scripts/create_lecture.py`
1. You can preview the website locally at http://127.0.0.1:4000/teaching_kit/ typing `jekyll serve` (the first time use `bundle exec jekyll serve`)

## Upload changes

1. Check which files would be uploaded with `git status`
1. Create new branch `git checkout -b BRANCHNAME`
1. Add files `git add . `
1. Commit `git commit -m "COMMIT MESSAGE`
1. Push `git push upstream BRANCHNAME`
