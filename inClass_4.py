# Author:Ankita (100941771), Anita Mohan (100884879)
# Date: November 2, 2024
""" In this program we filters AWS EC2 instances by user defined CPU and memory requirements. 
we get user input their minimum and optional maximum values, and the app loads instance details from a JSON file. 
then we identify and displays instances that meet the criteria, simplifying the search for suitable EC2 types."""

import json

# Function to load EC2 instance data from a JSON file
def load_ec2_instances(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: The specified JSON file was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Check the file formatting.")
        return []

# Function to get user input for CPU and memory requirements
def get_user_requirements():
    try:
        min_cpu = int(input("Enter minimum required CPU cores: "))
    except ValueError:
        print("Invalid input. Please enter an integer value for CPU cores.")
        return None
    
    max_cpu_input = input("Enter maximum required CPU cores (or press Enter to skip): ")
    max_cpu = int(max_cpu_input) if max_cpu_input.isdigit() else min_cpu

    try:
        min_memory = float(input("Enter minimum required memory in GiB: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value for memory.")
        return None
    
    max_memory_input = input("Enter maximum required memory in GiB (or press Enter to skip): ")
    max_memory = float(max_memory_input) if max_memory_input.replace('.', '', 1).isdigit() else min_memory

    return min_cpu, max_cpu, min_memory, max_memory

def main():
    # Use the full path to the JSON file
    ec2_instance_types = load_ec2_instances("C:\\Users\\Anitha\\Cloud\\Scripting\\Assignment\\Assignment\\ec2_instance_types.json")

    # Check if the file loaded correctly
    if not ec2_instance_types:
        print("No EC2 instance data found. Please check the file path and content.")
        return

    user_requirements = get_user_requirements()
    if not user_requirements:
        print("Invalid input for requirements. Exiting the program.")
        return

    min_cpu, max_cpu, min_memory, max_memory = user_requirements

    print("\nEC2 Instances that match your requirements:")
    found_instance = False

    for instance in ec2_instance_types:
        instance_cpu = int(instance['vcpu'].split()[0])
        instance_memory = float(instance['memory'].split()[0])

        if min_cpu <= instance_cpu <= max_cpu and min_memory <= instance_memory <= max_memory:
            print(f"Instance Name: {instance['name']}, vCPU: {instance['vcpu']}, "
                  f"Memory: {instance['memory']}, Storage: {instance['storage']}, "
                  f"Bandwidth: {instance['bandwidth']}, Availability: {instance['availability']}")
            found_instance = True

    if not found_instance:
        print("No EC2 instances found that match your requirements.")

if __name__ == "__main__":
    main()

