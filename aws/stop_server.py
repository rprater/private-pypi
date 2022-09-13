from modules.EC2 import EC2

import time


def stop_server(instance_id: str) -> None:
    ec2 = EC2()
    res = ec2.stop_instance(instance_id)

    if res["StoppingInstances"][0]["CurrentState"]["Name"] == "stopping":
        print("Waiting for server to stop")
        while ec2.get_state_of_instance(instance_id) == "stopping":
            time.sleep(1)

        if ec2.get_state_of_instance(instance_id) == "stopped":
            print("Server has stopped")
    else:
        raise ValueError("Unable to stop server")


if __name__ == "__main__":
    instance_id = "i-0cac0e1b7cd7177dc"
    stop_server(instance_id)
