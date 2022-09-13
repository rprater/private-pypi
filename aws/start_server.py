from modules.EC2 import EC2

import time


def start_server(instance_id: str) -> None:
    ec2 = EC2()
    res = ec2.start_instance(instance_id)

    if res["StartingInstances"][0]["CurrentState"]["Name"] == "pending":
        print("Waiting for server to start")
        while ec2.get_state_of_instance(instance_id) == "pending":
            time.sleep(1)

        if ec2.get_state_of_instance(instance_id) == "running":
            print("Server has started")
    else:
        raise ValueError("Unable to start server")


if __name__ == "__main__":
    instance_id = "i-0cac0e1b7cd7177dc"
    start_server(instance_id)
