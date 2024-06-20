import boto3
import os

client = boto3.client('sns')

def lambda_handler(event, context):
   response = client.publish(TopicArn=os.environ['SNSTopicARN'], Message="Object uploaded in bucket!")
   print("Message published")
   return(response)