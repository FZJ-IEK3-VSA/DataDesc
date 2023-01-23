source config.sh

json() {
    python3 -c "import json;print(json.loads('$1')$2)"
}

project_exists(){
    python3 -c "import json; _json=json.loads('$1'); print(next((elem['slug'] for elem in _json['results'] if elem['name']=='$2'), None))"
}


# Create Documentation
pip install sphinx sphinxcontrib-openapi
mkdir docs
cd docs

sphinx-quickstart --quiet -p "${TITLE}" -a "${CONTACT_NAME}" -v "${VERSION}" --ext-autodoc

make html

# Check if project exists
PROJECTS_JSON=$(curl -H "Authorization: Token ${RTD_AUTH}" https://readthedocs.org/api/v3/projects/)
EXISTS="$(project_exists "${PROJECTS_JSON}" "${TITLE}")"

if [ "$EXISTS" == "None" ]; then
# UPLOAD
JSON_STR='{"name":"'${TITLE}'", "repository":{ "url":"'${REPOSITORY}'", "type":"git" }, "homepage":"'https://${TITLE}.readthedocs.io'", "programming_language":"py","language":"en"}'
RES_STR=$(curl \
  -X POST \
  -H "Authorization: Token ${RTD_AUTH}" https://readthedocs.org/api/v3/projects/ \
  -H "Content-Type: application/json" \
  -d "${JSON_STR}")
echo $RES_STR
EXISTS="$(project_exists "${PROJECTS_JSON}" "${TITLE}")"

else
# UPDATE
JSON_STR='{"name":"'${TITLE}'", "repository":{ "url":"'${REPOSITORY}'", "type":"git" }, "homepage":"'https://${TITLE}.readthedocs.io'", "programming_language":"py","language":"en"}'
RES_STR=$(curl \
  -X PATCH \
  -H "Authorization: Token ${RTD_AUTH}" https://readthedocs.org/api/v3/projects/${EXISTS} \
  -H "Content-Type: application/json" \
  -d "${JSON_STR}")
echo $RES_STR
fi

# TRIGGER BUILD
RES_STR=$(curl \
  -X POST \
  -H "Authorization: Token ${RTD_AUTH}" https://readthedocs.org/api/v3/projects/${EXISTS}/versions/latest/builds)
echo $RES_STR