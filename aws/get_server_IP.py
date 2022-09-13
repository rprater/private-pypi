from modules.EC2 import EC2


def get_server_IP(instance_id: str) -> None:
    ec2 = EC2()
    return ec2.get_IP_of_instance(instance_id)


if __name__ == "__main__":
    instance_id = "i-0cac0e1b7cd7177dc"
    print(get_server_IP(instance_id))
