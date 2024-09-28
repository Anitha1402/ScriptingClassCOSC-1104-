# 1. Comment header
"Anitha Mohan (100884879) #27-09-2024 "
# This script simulates a cloud resource provisioning system by checking available CPU cores and memory.

# 2.Defining two constants
AvailableCpuCores = 16  # The total number of CPU cores available
AvailableMemoryGB = 64.0  # •	The total amount of memory available in gigabytes (GB).
# 3. Asking the user for the inputs
RequiredCpuCores = int(input("Please Enter the required number of CPU cores : "))
RequiredMemoryGb = float(input("Please Enter the amount of required memory(in GB): "))

# 4.checking whether the required values entered by the user are available based on the limits defined as constants
if RequiredCpuCores <= AvailableCpuCores and RequiredMemoryGb <= AvailableMemoryGB:
    print("Resources provisioned successfully!")
else:
    print("Resource request exceeds capacity. Provisioning failed!")

# Calculating the  remaining resources
remaining_cpu_cores = AvailableCpuCores - RequiredCpuCores
remaining_memory_gb = AvailableMemoryGB - RequiredMemoryGb

#5. Finally , Displaying the total remaining available CPU cores and memory after either provisioning or failing to provision the resources.
print("Remaining available CPU cores:", remaining_cpu_cores)
print("Remaining available memory (GB):", remaining_memory_gb)
