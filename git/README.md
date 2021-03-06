# Git

A collection of git helpers...

## Resources
A vast amount of resources covers various aspects of ```git```. Here is just a brief list of useful resources:
- [Git website](www.git-scm.org)
- [ProGit](https://git-scm.com/book/en/v2)

There are many others out there. Just search the internet.


## Tools, Utils, and Configuration

### Tab Completion of git commands
The script ```.git-completion.sh``` provides tab completion capabilites for git commands, git branch names, and other git stuff. To enable tab completion, add
```
source <path_to_this_folder>/.git-completion.bash
``` 
to your ```~/.bashrc``` file.

### Git Prompts
The script ```.git-prompt.sh``` enhances the terminal prompt when your inside a Git repository. To enable the enhanced prompt, add
```
source ~/.git-prompt.sh
```
to your ```~/.bashrc``` file.

### Git Config
A generic ```.gitconfig``` is provided. To use it, copy it into your ```/home/``` directory as ```~/.gitconfig```.

### Ignoring and Excluding Files from Version Control
To maintain a _clean_ repository and history, certain file types should not be included into a ```git``` repository.
Examples are:
- temporary backup files that have been auto-generated by the operating system
- binary files generated from the source code of this particular git repository

There are two mechanisms to exclude files from indexing and tracking in ```git```, namely ```.gitignore``` and ```git/info/exclude```.
- The file ```.gitignore``` is part of the ```git``` tree and is to be shared among project members (i.e. everybody working on the project should consider the paths that match the ignore pattern in there as cruft).
- Personal ignore patterns that are not to be shared with other project members are listed in ```.git/info/exclude```. 

Full details can be found [here](https://git-scm.com/docs/gitignore).

### Pre-commit hook to prevent commits on `master` branch

The script `pre-commit` implements a pre-commit hook to
- reject commits on `master`
- allow commits only on a feature branch.

To use it, copy the file `pre-commit` hook into a repository's `.git/hooks/` directory.