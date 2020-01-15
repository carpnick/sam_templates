# Summary

TODO: Replace with the summary.  See [Boto3 docs](https://google.com).

## Syntax

```
Type: Custom::{{cookiecutter.project_name}}
Properties: 
  ServiceToken: !Ref ARNOfResource         #Required for all Custom Resources
  Param1: ParamValue                       #TODO: Replace with all parameters for resource
```

# Properties
### Param1
 TODO: Add summary of parameter

*Required: No/Yes*

*Type: String*


# Return Values
### Ref
When the logical ID of this resource is provided to the Ref intrinsic function, Ref returns the resource name.

### Fn::GetAtt
The `Fn::GetAtt` or `!GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.
* RandomAttribute - TODO: Fill this section out

# Examples

```
  TestResource:
    Type: 'Custom::{{cookiecutter.project_name}}'
    Properties:
      ServiceToken: !Ref ARNParam
      Param1: Awesome String
```
