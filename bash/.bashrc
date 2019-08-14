# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
  . /etc/bashrc
fi

# terminal colors
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad

export LC_NUMERIC="en_US.UTF-8"

# Enable color support of ls and also add handy aliases
if [ "$TERM" != "dumb" ]; then
  eval "`dircolors -b`"
  alias ls='ls --color=auto'
fi

# Configure terminal prompt
if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u:\W\$ '
fi

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# git support
source ~/utils/github_utils/git/.git-completion.bash

# User specific aliases and functions
alias ..="cd .."
alias ll='ls -l'

# Prepare for environment modules
source /etc/profile.d/modules.sh