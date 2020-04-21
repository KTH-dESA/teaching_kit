# teaching_test_1
First test of website for teaching material

Visit the website at https://kth-desa.github.io/teaching_kit/

## Requirements

To use this repository the following softwares are needed:
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) follow the installation guide at the link provided
- [Python](https://www.python.org/downloads/) follow the installation guide at the link provided
- [Jekyll](https://jekyllrb.com/docs/) follow the installation guide at the link provided (you will be asked to install Ruby)

In addition, the following python packages should be added in order to run the scripts:

- pathlib typing  ```conda install pathlib``` in the terminal
- python-pptx typing ```conda install python-pptx``` in the terminal
- pyrhon-frontmatter ```conda install frontmatter```

Before installing any package in Python it is recommended to create a new environment: 
1. ```conda create -n POJECT NAME```
2. ```conda initiate PROJECT NAME```

In case of working from Windows it is useful  setting up a Linux subsystem.

## How to use

### First steps 
1. Clone repository ```git clone https://github.com/KTH-dESA/teaching_kitt```

1. Import the powerpoint presentations in ```files/ppt_presentations```
1. Tranform the presentations in modules. Run the script ```main.py``` to convert powerpoint presentations to markdown files, type ```python scripts/main.py```. The modules will be saved in presentations/modules
1. Apply tags to the modules running the script ```tags.py```
1. Create lectures combining the modules imported using the scripts ```create_lecture.py```
1. Create course pages as a combination of lectures using the script  ```create_course.py```
1. You can preview the website locally at http://127.0.0.1:4000/teaching_kit/ typing ```jekyll serve``` (the first time use ```bundle exec jekyll serve```)

### Upload changes
1. Check which files would be uploaded with ```git status```
1. Create new branch ```git checkout -b BRANCHNAME```
1. Add files ```git add . ```
1. Commit ```git commit -m "COMMIT MESSAGE```
1. Push ```git push upstream BRANCHNAME```
