# Eclipse

## Import ```C++``` project from existing ```git``` repository

We assume that the ```git``` repository has been cloned locally to the path ```PATH_TO_GIT_REPO```.
To import this repository as a ```C++``` project into Eclipse, follow these steps:

1. Open Eclipse
2. File --> New --> C++ Project.
3. Type a project name, uncheck 'Use default location' and select path ```PATH_TO_GIT_REPO```.
4. Select 'Project type' to be 'Makefile project --> Empty Project'.
5. Click 'Finish'.

## Code style

To use a code style formatter pre-defined in a ```xml```-file, follow these steps:

1. Go to Window --> Preferences.
2. Expand the C/C++ branch and select 'Code Style', then select 'Formatter'.
3. Click on 'Import'.
4. Select ```xml```-file with code style definition and accept.
5. Click on 'Apply' and then 'OK'.

Now eclipse will automatically format the code in accordance to the recommended style. 
This feature not only works for new code you are writing, 
but also you can select a block of code and have it reformatted with "Ctrl + Shift + f". 

A nice ```C++``` code style is defined [here](https://github.com/mayrmt/utils/blob/master/eclipse/baci_eclipse_style.xml).
