#!/bin/sh

# To adding and commiting files in git

git add .
read -p 'Commit Message: ' comMsg
git commit -m "$comMsg"		
