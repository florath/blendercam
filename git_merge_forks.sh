#!/bin/bash
#
# This script sets the different origins to be able
# to pick up changes from other forks easily.

# The upstream of the original author.
git remote add upstream  https://github.com/vilemduha/blendercam.git

# jeffmd
git remote add jeffmd https://github.com/jeffmd/blendercam-1.git

# RusticSignDesign is not added: no patches

# feler404
git remote add feler404 https://github.com/feler404/blendercam.git

# pltsi
git remote add pltsi https://github.com/pltsi/blendercam.git

# TurBoss
git remote add TurBoss https://github.com/TurBoss/blendercam.git


### Merge it:
git fetch jeffmd
