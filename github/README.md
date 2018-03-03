# GitHub files & Helpers
This is a brief collection of GitHub files, templates, and configurations.

## Configuring a GitHub project

### Template for Issues
The template ```ISSUE_TEMPLATE.md``` populates a new issue with default text to guide developers on how to file an issue. 
I recommend putting it into the directory ```.github``` to hide it from the user.

### Template for Pull Requests
The template ```PULL_REQUEST_TEMPLATE.md``` populates a new pull request with default text to guide developers on how to file a pull request. 
I recommend putting it into the directory ```.github``` to hide it from the user.

### Enforcing pull requests
To increase software qualitity and to spread knowledge among all developers, it is recommended to 
- block ```push``` operations to the main branch
- establish a Fork/Branch/Pull-Request workflow for contributing to the code.

The concept of _Code Owners_ is very useful in that regard.

### Code Owners
Defining _code owners_ allos to enforce reviews by the maintainers or main developers of certain files or modules of the code.
Details can be found [here](https://help.github.com/articles/about-codeowners/).

## Issue Tracking via Kanban Board
A _Kanban_ board can help to keep the progress and status of issues (and pull requests) organized. 
Automation features help to assign issues (and pull requests) to columns in the Kanban board.

### Setup
To add a Kanban board with Automation, select _Projects_, add a _New Project_, 
give a project name and a brief description, and choose the template _Kanban (Automated)_.

### Workflow
During its lifetime, an issue moves through the Kanban board form left to right. It passes thruogh several columns.

These columns have proven to be useful:
- **Backlog**: This is the default location for new issues. Issues begin their life in the Backlog. New issues can be added to **Backlog** via automation.
- **Blocked**: If at any point in an issue's life it becomes blocked by something (either another issue, or perhaps something external), move the issue card into the **Blocked** column to indicate that work can't proceed until something else is dealt with.
- **Ready**: When enough information has been gathered and work is ready to begin on an issue, drag it to the **Ready** column.
- **In Progress**: When work commences on an issue, move the issue card to the **In Progress** column.
- **Under Review**: When your changes are ready to be integrated into the main branch, move the issue card from **In Progress** to **Under Review**.
- **Done**: Closed issues are collected in **Done**. Adding closed issues to **Done** can be done via automation. 

>Note: If your pull request description has some form of "closes #<issueNumber>" in it somewhere, merging the PR will automatically close the associated issue, which will move the issue card from **Under Review** to **Done** on the Kanban board. If not, you'll need to make this move manually.
