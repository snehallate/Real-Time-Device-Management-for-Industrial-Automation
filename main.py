import time

class Device:
    def __init__(self, device_id, name, status="offline", reliability_score=0):
        self.device_id = device_id
        self.name = name
        self.status = status
        self.reliability_score = reliability_score

    def update_status(self, new_status):
        start_time = time.time()  # Start the timer
        self.status = new_status
        end_time = time.time()  # End the timer
        response_time = end_time - start_time
        print(f"Device {self.name} status updated to {self.status} in {response_time:.4f} seconds")
        return response_time

    def update_reliability(self, score):
        self.reliability_score = score
        print(f"Device {self.name} reliability score updated to {self.reliability_score}")


class DeviceManager:
    def __init__(self):
        self.devices = {}

    def add_device(self, device):
        self.devices[device.device_id] = device
        print(f"Added device: {device.name}")

    def get_device_status(self, device_id):
        device = self.devices.get(device_id)
        if device:
            return device.status
        else:
            return "Device not found"

    def update_device_status(self, device_id, status):
        device = self.devices.get(device_id)
        if device:
            response_time = device.update_status(status)
            return response_time
        else:
            print("Device not found")
            return None

    def check_device_reliability(self, device_id):
        device = self.devices.get(device_id)
        if device:
            return device.reliability_score
        else:
            return "Device not found"


# Example Usage
if __name__ == "__main__":
    manager = DeviceManager()

    # Create devices
    device1 = Device(device_id=1, name="Sensor A", reliability_score=98)
    device2 = Device(device_id=2, name="Actuator B", reliability_score=92)

    # Add devices to the manager
    manager.add_device(device1)
    manager.add_device(device2)

    # Update device status and measure response time
    response_time = manager.update_device_status(1, "online")
    print(f"Response time for updating Device 1: {response_time:.4f} seconds")

    # Check device reliability
    reliability = manager.check_device_reliability(1)
    print(f"Device 1 reliability: {reliability}")

    # Get device status
    status = manager.get_device_status(2)
    print(f"Device 2 status: {status}")
