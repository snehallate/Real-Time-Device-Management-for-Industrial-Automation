# Real-Time-Device-Management-for-Industrial-Automation
Repository Link: https://github.com/snehallate/Real-Time-Device-Management-for-Industrial-Automation

# Introduction
In an industrial environment, various devices like sensors and actuators play crucial roles in monitoring and controlling processes. To ensure the smooth operation of these devices, a system must be in place to track their status (whether they are online or offline) and monitor their performance. This project focuses on creating a system that updates device statuses in real time and tracks their reliability over time. The system allows for quick and efficient management of devices, which is essential for industrial automation.

# Related Study
1)Existing Device Management Solutions: 
* Mobile Device Management (MDM) systems
* Enterprise Mobility Management (EMM) platforms
* Unified Endpoint Management (UEM) solutions
* Internet of Things (IoT) device management platforms
2) Key Features of Modern Device Management: 
* Remote device configuration and control
* Real-time monitoring and reporting
* Automated software updates and patch management
* Security policy enforcement
* Asset tracking and inventory management
3) Challenges in Device Management: 
* iversity of device types and operating systems
* Scalability issues in large-scale deployments
* Security concerns and data privacy
* Network connectivity and bandwidth constraints
* User experience and productivity considerations

# Flowchat
<img width="429" height="709" alt="image" src="https://github.com/user-attachments/assets/de93daec-d134-40ba-a292-984cbb14a63a" />

# Algorithm
1)  Initialize Device
* Input: device_id, name, status="offline", reliability_score=0
Process:
* Create an object of the class Device.
* Assign input values to device_id, name, status, and reliability_score.
* Output: New device object with the given attributes.
2)  Add Device to Device Manager
* Input: Device object
Process:
* Add the device to the devices dictionary in DeviceManager, using device_id as the key.
* Output: Confirmation of device added.
3) Update Device Status
* Input: device_id, new_status
Process:
* Search for the device using device_id in the devices dictionary.
If found:
1.Start the timer to measure the response time.
2.Update the device's status to new_status.
3.Stop the timer and calculate the response time.
4.Print the updated status and the response time.
* Else: Print "Device not found".
* Output: The response time taken to update the device status.
4) Update Device Reliability
* Input: device_id, score
Process:
* Search for the device using device_id in the devices dictionary.
If found:
* Update the reliability_score to the new score.
* Print the updated reliability score.
* Else: Print "Device not found".
* Output: Confirmation of the updated reliability score.
5) Get Device Status
* Input: device_id
Process:
* Search for the device using device_id in the devices dictionary.
If found:
* Retrieve the current status of the device.
* Else: Return "Device not found".
* Output: Device status.
6) Check Device Reliability
* Input: device_id
Process:
* Search for the device using device_id in the devices dictionary.
If found:
* Retrieve the current reliability_score of the device.
* Else: Return "Device not found".
* Output: Device reliability score.

# Project Design- Architecture block diagram with description
# 1. Class Diagram
The class diagram depicts the structure of the system, showing the Device and DeviceManager classes and their interactions.
Device Class:
* Attributes: device_id, name, status, reliability_score
* Methods: update_status(), update_reliability()
DeviceManager Class:
* Attributes: devices (a dictionary of devices)
* Methods: add_device(), update_device_status(), get_device_status(), check_device_reliability()
# 2. Sequence Diagram
The sequence diagram outlines the interactions between the DeviceManager and Device objects when updating device status and checking reliability.
Add Device Sequence:
The DeviceManager sends a request to add_device(), which adds the device to the internal collection.
Update Device Status Sequence:
The DeviceManager invokes the update_status() method on the Device object, triggering a status update.
Reliability Check Sequence:
The DeviceManager calls check_device_reliability(), which retrieves the reliability score of a device.

# Class Diagram:

<img width="530" height="412" alt="image" src="https://github.com/user-attachments/assets/66bd1ed5-d20e-49d1-bb80-1a68e019c6e7" />

# Sequence Diagram:
<img width="610" height="554" alt="image" src="https://github.com/user-attachments/assets/a813a75f-3a23-44fe-91b4-74884da9df6c" />

# Description
# 1)Device Manager Class: 
Manages all the devices in the system and handles operations such as adding new devices, updating their status, and checking their reliability scores. It interacts with one or more Device objects, storing them in a dictionary for easy lookup.
# 2)Device Class:
Represents an individual device such as a sensor or actuator. Each device has a unique ID, a name, a status (e.g., online/offline), and a reliability score. The class provides methods to update the device’s status and reliability.
# 3)Sequence Explanation:
* The DeviceManager first adds devices to its collection using add_device().
* When a device's status needs to be updated, the manager calls update_device_status() on the corresponding device.
* The system measures the response time of this update.
* The reliability of the device is periodically checked using check_device_reliability().

# Features
* Add and manage devices
* Update device status in real time
* Monitor device reliability
* Measure response time
* Simulate industrial automation management

# Technologies Used
* Python
* Operating System Concepts
* Industrial Automation Simulation

# Project Structure
Real-Time-Device-Management/
* │── main.py
* │── README.md
* │── report.pdf

# How to Run
Install Python and run:
python main.py

# Sample Output
The program displays:
* Device status updates
* Response times
* Reliability scores

# Project Objectives
* Understand real-time device management
* Learn industrial automation concepts
* Implement responsiveness and reliability tracking
* Simulate device monitoring systems

