source config.sh

RES_STR=$(curl \
  -X POST "https://api.swaggerhub.com/apis/${SWAGGER_USER}/${TITLE}" \
  -H "Authorization: ${SWAGGER_AUTH}" \
  -H "Content-Type: application/yaml" \
  --data-binary ${YAML_URL} \
  --ssl-no-revoke)
echo $RES_STR
