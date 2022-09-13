import boto3


class EC2:
    def __init__(self) -> None:
        self.client = boto3.client("ec2")

    def start_instance(self, instance_id: str):
        return self.client.start_instances(
            InstanceIds=[
                instance_id,
            ]
        )

    def stop_instance(self, instance_id: str):
        return self.client.stop_instances(
            InstanceIds=[
                instance_id,
            ]
        )

    def get_state_of_instance(self, instance_id: str):
        return self.client.describe_instances(
            Filters=[
                {
                    "Name": "instance-id",
                    "Values": [
                        instance_id,
                    ],
                },
            ]
        )["Reservations"][0]["Instances"][0]["State"]["Name"]

    def get_IP_of_instance(self, instance_id: str):
        return self.client.describe_instances(
            Filters=[
                {
                    "Name": "instance-id",
                    "Values": [
                        instance_id,
                    ],
                },
            ]
        )["Reservations"][0]["Instances"][0]["PublicIpAddress"]


if __name__ == "__main__":
    ec2 = EC2()
    instance_id = "i-0cac0e1b7cd7177dc"
    print(ec2.get_IP_of_instance(instance_id))
