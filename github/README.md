# GitHub files & Helpers
This is a brief collection of GitHub files, templates, and configurations.

### Configuring a GitHub project

## Template for Issues
The template ```ISSUE_TEMPLATE.md``` populates a new issue with default text to guide developers on how to file an issue. 
I recommend putting it into the directory ```.github``` to hide it from the user.

## Template for Pull Requests
The template ```PULL_REQUEST_TEMPLATE.md``` populates a new pull request with default text to guide developers on how to file a pull request. 
I recommend putting it into the directory ```.github``` to hide it from the user.

## Enforcing pull requests
To increase software qualitity and to spread knowledge among all developers, it is recommended to 
- block ```push``` operations to the main branch
- establish a Fork/Branch/Pull-Request workflow for contributing to the code.

The concept of _Code Owners_ is very useful in that regard.

## Code Owners
Defining _code owners_ allos to enforce reviews by the maintainers or main developers of certain files or modules of the code.
Details can be found [here](https://help.github.com/articles/about-codeowners/).
