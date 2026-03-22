import boto3
import logging
import botocore
import sys
from botocore.exceptions import ClientError

# ---------------- LOGGING ----------------
logging.basicConfig(
    filename='ec2-scheduler.log',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- INPUT ----------------
if len(sys.argv) != 2:
    print("Usage: python3 script.py start|stop")
    sys.exit(1)

action = sys.argv[1].lower()

if action not in ["start", "stop"]:
    print("Invalid action. Use 'start' or 'stop'")
    sys.exit(1)

# ---------------- AWS SETUP ----------------
region_name = 'us-east-1'

try:
    ec2 = boto3.client('ec2', region_name=region_name)

    response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Environment', 'Values': ['Dev']}
        ]
    )

    # ---------------- MAIN LOGIC ----------------
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:

            instance_id = instance['InstanceId']
            state = instance['State']['Name']

            # -------- STOP --------
            if action == "stop" and state == "running":
                logging.info(f"Stopping {instance_id}")

                try:
                    ec2.stop_instances(InstanceIds=[instance_id])

                    waiter = ec2.get_waiter('instance_stopped')
                    waiter.wait(InstanceIds=[instance_id])

                    logging.info(f"Instance stopped: {instance_id}")

                except botocore.exceptions.WaiterError as e:
                    logging.error(f"Failed to stop {instance_id}: {str(e)}")

            # -------- START --------
            elif action == "start" and state == "stopped":
                logging.info(f"Starting {instance_id}")

                try:
                    ec2.start_instances(InstanceIds=[instance_id])

                    waiter = ec2.get_waiter('instance_running')
                    waiter.wait(InstanceIds=[instance_id])

                    logging.info(f"Instance started: {instance_id}")

                except botocore.exceptions.WaiterError as e:
                    logging.error(f"Failed to start {instance_id}: {str(e)}")

            # -------- NO ACTION --------
            else:
                logging.info(
                    f"No action needed for {instance_id} (state: {state})")

except ClientError as e:
    logging.error(f"AWS error: {e}")

except Exception as e:
    logging.error(f"Unexpected error: {e}")
