```
pip install -r src/requirements.txt -t src/
aws cloudformation package --template-file cloudformation.yaml --s3-bucket myBucket --s3-prefix myPrefix --output-template-file cloudformation-final.yaml
aws cloudformation deploy --template-file cloudformation-final.yaml --stack-name myStackName --capabilities CAPABILITY_NAMED_IAM --parameter-overrides HipchatEndpoint=myHipchatEndpoint AuthToken=myAuthToken TopicArn=myTopicArn
```
