# Function
import random

def generate_bucket_name(project_name):
    random_suffix = random.randint(1000, 9999)
    bucket_name = f"{project_name}-bucket-{random_suffix}"
    return bucket_name

# Using the function
user_project_name = input("Enter your project name: ")
new_bucket = generate_bucket_name(user_project_name)
print(f"Created new S3 bucket: {new_bucket}")