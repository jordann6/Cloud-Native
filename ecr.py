import boto3
from botocore.exceptions import ClientError

# Initialize the ECR client
ecr_client = boto3.client('ecr')

repository_name = "my_monitoring_app_image"

try:
    # Attempt to create the repository
    response = ecr_client.create_repository(repositoryName=repository_name)

    # Extract the repository URI from the response
    repository_uri = response['repository']['repositoryUri']

    # Print the repository URI
    print(f"Repository created successfully: {repository_uri}")

except ClientError as e:
    # Handle any exceptions that occur during the repository creation
    print(f"Error occurred: {e}")
