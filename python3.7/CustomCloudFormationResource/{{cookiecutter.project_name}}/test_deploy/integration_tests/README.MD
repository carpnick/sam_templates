To deploy your custom resource, go to your last succesful build page.

It will have something like the following listed in an information section:
```
Information:
MASTER Location: us-east-1: https://s3.us-east-1.amazonaws.com/com.elizacloud.us-east-1.cfresources/CustomCFResources/Production/Repositories/Eliza-eliza_cf_test/latest/template.yaml
MASTER Location: ap-southeast-2: https://s3.ap-southeast-2.amazonaws.com/com.elizacloud.ap-southeast-2.cfresources/CustomCFResources/Production/Repositories/Eliza-eliza_cf_test/latest/template.yaml
us-east-1 - feature/test: https://s3.us-east-1.amazonaws.com/com.elizacloud.us-east-1.cfresources/CustomCFResources/Development/Repositories/Eliza-eliza_cf_test/feature/test/template.yaml
ap-southeast-2 - feature/test: https://s3.ap-southeast-2.amazonaws.com/com.elizacloud.ap-southeast-2.cfresources/CustomCFResources/Development/Repositories/Eliza-eliza_cf_test/feature/test/template.yaml

```

Login to a CFR account and deploy you custom resource based on what region you are in.  Typically you are deploying your feature branch.  There are 2 use cases you need to handle when deploying:
1. When the Custom Resource already exists and is deployed across all accounts
    - You must find the nested stack within AUT-CustomResources stack.  This file from Eliza-AWSAccountManagement can help you: `CloudFormation/infrastructure/custom_resources/latest/custom_resources.yml`.  Once you find the nested stack, you can update the nested stack and paste in the appropriate S3 URL from the build.  This allows you to update the stack with what has been deployed to the local account, typically one of the CFR accounts.
    - After it is deployed you can then use test_use_of_cf_resource.yml to use the custom resource within a CF stack.
2. Net new resource
    - When it is a net new resource you will create a new stack.  It needs to be named something like  'AUT-*' due to our SCP policies.  You also must use tags of Team DICE due to tagging policies.
    - After it is deployed you can then use test_use_of_cf_resource.yml to use the custom resource within a CF stack.