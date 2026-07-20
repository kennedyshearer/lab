# For Loops

instance_ids = ["i-123456abcd", "i-23456", "i-abcde1234"]

for instance_id in instance_ids:
    print(f"Checking status of instance {instance_id}...")
    # Code to check instance status
    print(f"Instance {instance_id} status check complete.")

print("All instances have been checked.")