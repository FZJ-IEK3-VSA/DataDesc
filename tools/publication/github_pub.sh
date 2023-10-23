source config.sh

JSON_STR='{"name":"'${TITLE}'","description":"'${DESCRIPTION}'","homepage":"https://github.com","private":'${REPO_PRIV}',"is_template":'${REPO_TEMP}'}'
echo $JSON_STR

# CREATE A REPO
curl \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer ${GIT_AUTH}"\
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/user/repos \
  -d "${JSON_STR}"

# ADD README TO REPO
printf '# '"${TITLE}"'
'"${DESCRIPTION}"'

## Features
'"${RELEASE_NOTES}"'

## Installation
...

## Example
...

## License
'"${LICENSE_NAME}"'

Copyright (C) '"${CONTACT_NAME}"'

## Acknowledgements
This work is supported by '"${FUNDER}"' with a grant for the project '"${FUNDING}"'.' > README.md

# INITIALIZE 
git init
git config user.name "$GIT_OWNER@DataDesc"
git config user.email "<>"
git add .
git commit -m "Initial commit"

# LINK
git remote add origin https://$GIT_OWNER:$GIT_AUTH@github.com/$GIT_OWNER/$TITLE.git
git push -u origin master