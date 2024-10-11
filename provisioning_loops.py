# Author: Anita Mohan (100884879)
# Date: 27-09-2024
# 1.Comment Header: The program simulates a method for allocating cloud resources. 
# Resources (CPU cores and memory) can be requested by users, and it keeps track of all resource requests—both allocated and pending—while also determining whether they are available.

# 2. Defining the two constants
availableCpuCores = 16  # Total available CPU cores
availableMemoryGB = 64.0  # Total available memory in GB

# 3. Creating the two empty lists.
allocatedResources = []  # List to store successful allocations
pendingRequests = []  # List to store requests that couldn't be fulfilled

# Initialize available resources
available_cpu_cores = availableCpuCores
available_memory_gb = availableMemoryGB

# Starting the loop to allow multiple requests
while True:
    # Gettin the UserName, requiredCpuCores, requestedMemoryGB input from the user
    userName = input("Enter userName: ")
    requiredCpuCores = int(input("Enter the required  CPU cores: "))
    requestedMemoryGB = float(input("Enter the required memory in GB: "))

    # Checking if resources are available
    if requiredCpuCores <= available_cpu_cores and requestedMemoryGB <= available_memory_gb:
        # If available, allocating the resources and storing in allocated list
        allocatedResources.append([userName, requiredCpuCores, requestedMemoryGB])
        available_cpu_cores -= requiredCpuCores
        available_memory_gb -= requestedMemoryGB
        print("Resources provisioned successfully!")
    else:
        # If not available, storing in pending requests list
        pendingRequests.append([userName, requiredCpuCores, requestedMemoryGB])
        print("Resource request exceeds available capacity. Provisioning failed.")

    # Asking the user if they want to make another request
    continueRequest = input("Do you want to make another request? (yes/no): ").lower()
    if continueRequest != 'yes':
        break

# Displaying allocated resources
print("\n Allocated Resources:")
print(f"{'userName':<15}{'CPU Cores':<15}{'Memory (GB)':<15}")
for resource in allocatedResources:
    print(f"{resource[0]:<15}{resource[1]:<15}{resource[2]:<15}")

# Displaying pending requests
print("\n Pending Requests:")
print(f"{'userName':<15}{'CPU Cores':<15}{'Memory (GB)':<15}")
for request in pendingRequests:
    print(f"{request[0]:<15}{request[1]:<15}{request[2]:<15}")
    
