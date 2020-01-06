# {{ cookiecutter.project_name }}

  #Pre done for you
  * `pip install boto3 crhelper`
  * `pip freeze > src/requirements.txt`
  * `pip install coverage pylint pytest pytest-cov pytest-mock python-lambda-local`
  * `pip freeze -r src/requirements.txt > src/requirements-dev.txt `
  * Template yaml presetup with best practices.
  * Unit tests and __init__.py files setup for best practices

  #Getting started

  * Clone Source
  * cd into directory
  * Create virtual Directory
    * `python3 -m venv virtualdir`
  * Activate Virtual Drirectory
    * `source virtualdir/bin/activate`
  * Install dependencies for development
    * `pip install -r src/requirements-dev.txt`
    * `pip install -r src/requirements-dev.txt --upgrade`
  * Run pylint
    * `pylint src/`
    * `pylint tests/`
  * Run Unit Tests with code coverage and reporting
    * `python -m pytest  --cov-branch --cov=src/  tests/ --log-cli-level=DEBUG  --junit-xml=junit.xml  --cov-report=xml --cov-report=html:ci_coverage/`
  * Deactivate the virutal environment
    * `deactivate`
  * Run the SAM build
    * `sam build -u`
  * Test and run locally with the create/delete event json - Integration testing with SAM container environment
    * ```
        sam local invoke -e events/create_event.json
        sam local invoke -e events/delete_event.json
      ```
    

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)
