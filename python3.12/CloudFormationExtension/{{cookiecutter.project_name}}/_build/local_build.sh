set -e

echo "Installing Dependencies"
pip3 install -r requirements_dev.txt


echo "Running cfn validate: cfn validate"
cfn validate

# E3006: The validation is done against a pre-compiled spec of resources that AWS manages. We can either ignore the check, or provide our own custom spec.
# - https://github.com/aws-cloudformation/cfn-lint/blob/74847b145d63e7038752db93efd5ef5d4f9bd75e/src/cfnlint/rules/resources/ResourceType.py#L14
# - https://github.com/aws-cloudformation/cfn-lint/blob/v1.18.1/src/cfnlint/schema/manager.py#L274
# - Override Spec examaple: https://github.com/aws-cloudformation/cfn-lint/issues/445
echo "Running cfn-lint: cfn-lint -t test_deploy/**/*.yaml"
cfn-lint -t test_deploy/**/*.yaml

echo "Running cfn-lint: cfn-lint -t template_deploy_regional_extension.yaml"
cfn-lint -t template_deploy_regional_extension.yaml

echo "Running cfn generate: cfn generate.  Also determining if files are out of date in git"
cfn generate
set +e
git diff --compact-summary --exit-code
if [ $? -ne 0  ]; then
  echo "---"
  echo "'cfn generate' generated some changes. Run it locally and commit changes."
  exit 1
fi
set -e

echo "Running mypy: mypy "
mypy

echo "Running black:  black -l 120 --check --extend-exclude \".*models\.py\" src/ tests/"
black -l 120 --check --extend-exclude ".*models\.py" src/ tests/

echo "\nRunning flake8: flake8 --max-line-length 120 --per-file-ignores='src/**/models.py:F401,W391' src/ tests/"
flake8 --max-line-length 120 --per-file-ignores='src/**/models.py:F401,W391' src/ tests/

echo "\nRunning Unit Tests: pytest --cov --cov-report html --cov-report xml --log-cli-level=DEBUG --junit-xml=junit.xml tests/unit"
pytest --cov --cov-report html --cov-report xml --log-cli-level=DEBUG --junit-xml=junit.xml tests/unit

echo "\n Running cfn submit for build verification: cfn submit --dry-run"
cfn submit --dry-run

#For local contract testing - Not run as part of the CI processes
echo "\nRunning sam build to build a local copy: sam build -u -m requirements.txt"
sam build -u -m requirements.txt

echo "Build is completed"