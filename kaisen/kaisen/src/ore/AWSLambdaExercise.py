import json 
import boto3
def lambda_handler(event, context):
    s3 = boto3.client("s3")
    sns = boto3.client('sns')
    bucket_name = 'awslambdaexercise'
    object_key = 'username94.txt'
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    print(response)
    contents = response['Body'].read()
    total_words = contents.split()
    print('The word count in the file ' ,object_key, ' is ' , len(total_words))
    snsArn = 'arn:aws:s3:::awslambdaexercise/username94.txt'
    message = "The word count in the file "+object_key+" is " + str(len(total_words))
    response = sns.publish(TopicArn=snsArn,Message=message,Subject='Word Count Result')