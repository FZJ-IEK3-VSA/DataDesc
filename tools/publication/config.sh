#json() {
#    python3 -c "import json;print(json.safe_load(open('$1'))$2)"
#}

json() {
    python3 -c "import json;print(json.load(open('$1'))$2)"
}

## USER VARIABLES
PROJECT_URL=""
JSON_URL="${PROJECT_URL}/meta.json"

### USER NAMES
GIT_OWNER=""
PYPI_USER="__token__"   # only change if not using PyPi access token

### AUTHENTICATION TOKENS
GIT_AUTH=""
PYPI_AUTH=""
RTD_AUTH=""
PYPI_PASS="${PYPI_AUTH}"

REPO_PRIV=false
REPO_TEMP=false

########################################################################

## STATIC FIELDS: DON'T MODIFY
# INFO/CONTACT
CONTACT_EMAIL="$(json ${JSON_URL} "['info']['contact']['email']")"
CONTACT_NAME="$(json ${JSON_URL} "['info']['contact']['name']")"
CONTACT_URL="$(json ${JSON_URL} "['info']['contact']['url']")"
CONTACT_AFFILIATION="$(json ${JSON_URL} "['info']['authors']['affiliation']")"

# INFO/LICENSE
LICENSE_NAME="$(json ${JSON_URL} "['info']['license']['name']")"

DESCRIPTION="$(json ${JSON_URL} "['info']['description']")"
TITLE="$(json ${JSON_URL} "['info']['title']")"
VERSION="$(json ${JSON_URL} "['info']['version']")"

# INFO/X-...
#CATEGORY="$(json ${JSON_URL} "['info']['x-category']")"
#CI="$(json ${JSON_URL} "['info']['x-ci']")"
#CREATED="$(json ${JSON_URL} "['info']['x-created']")"
#DEV_STATUS="$(json ${JSON_URL} "['info']['x-dev-status']")"
DOWNLOAD_URL="$(json ${JSON_URL} "['info']['downloadUrl']")"
FIRST_RELEASE="$(json ${JSON_URL} "['info']['datePublished']")"
FUNDER="$(json ${JSON_URL} "['info']['funders']")"
FUNDING="$(json ${JSON_URL} "['info']['fundings']")"
ID="$(json ${JSON_URL} "['info']['identifier']")"
#ISSUE_TRACKER="$(json ${JSON_URL} "['info']['x-issue-tracker']")"
KEYWORDS="$(json ${JSON_URL} "['info']['keywords']")"
#OS="$(json ${JSON_URL} "['info']['x-os']")"
#PART_OF="$(json ${JSON_URL} "['info']['x-part-of']")"
#PLATFORM="$(json ${JSON_URL} "['info']['x-platform']")"
PROGRAMMING_LANG="$(json ${JSON_URL} "['info']['programmingLanguages']")"
REFERENCE_PUB="$(json ${JSON_URL} "['info']['referencePublication']")"
#RELATED_LINKS="$(json ${JSON_URL} "['info']['x-related-links']")"
RELEASE_NOTES="$(json ${JSON_URL} "['info']['readme']")"
REPOSITORY="$DOWNLOAD_URL"

cd ${PROJECT_URL}