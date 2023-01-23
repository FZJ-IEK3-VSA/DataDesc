yaml() {
    python3 -c "import yaml;print(yaml.safe_load(open('$1'))$2)"
}

## USER VARIABLES
PROJECT_URL=""
YAML_URL="${PROJECT_URL}/meta.yaml"

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
CONTACT_EMAIL="$(yaml ${YAML_URL} "['info']['contact']['email']")"
CONTACT_NAME="$(yaml ${YAML_URL} "['info']['contact']['name']")"
CONTACT_URL="$(yaml ${YAML_URL} "['info']['contact']['url']")"
CONTACT_AFFILIATION="$(yaml ${YAML_URL} "['info']['contact']['x-affiliation']")"

# INFO/LICENSE
LICENSE_NAME="$(yaml ${YAML_URL} "['info']['license']['name']")"

DESCRIPTION="$(yaml ${YAML_URL} "['info']['description']")"
TITLE="$(yaml ${YAML_URL} "['info']['title']")"
VERSION="$(yaml ${YAML_URL} "['info']['version']")"

# INFO/X-...
CATEGORY="$(yaml ${YAML_URL} "['info']['x-category']")"
CI="$(yaml ${YAML_URL} "['info']['x-ci']")"
CREATED="$(yaml ${YAML_URL} "['info']['x-created']")"
DEV_STATUS="$(yaml ${YAML_URL} "['info']['x-dev-status']")"
DOWNLOAD_URL="$(yaml ${YAML_URL} "['info']['x-download-url']")"
FIRST_RELEASE="$(yaml ${YAML_URL} "['info']['x-first-release']")"
FUNDER="$(yaml ${YAML_URL} "['info']['x-funder']")"
FUNDING="$(yaml ${YAML_URL} "['info']['x-funding']")"
ID="$(yaml ${YAML_URL} "['info']['x-id']")"
ISSUE_TRACKER="$(yaml ${YAML_URL} "['info']['x-issue-tracker']")"
KEYWORDS="$(yaml ${YAML_URL} "['info']['x-keywords']")"
OS="$(yaml ${YAML_URL} "['info']['x-os']")"
PART_OF="$(yaml ${YAML_URL} "['info']['x-part-of']")"
PLATFORM="$(yaml ${YAML_URL} "['info']['x-platform']")"
PROGRAMMING_LANG="$(yaml ${YAML_URL} "['info']['x-programming-lang']")"
REFERENCE_PUB="$(yaml ${YAML_URL} "['info']['x-reference-pub']")"
RELATED_LINKS="$(yaml ${YAML_URL} "['info']['x-related-links']")"
RELEASE_NOTES="$(yaml ${YAML_URL} "['info']['x-release-notes']")"
REPOSITORY="$(yaml ${YAML_URL} "['info']['x-repository']")"

cd ${PROJECT_URL}