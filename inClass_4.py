# Author: Anita Mohan (100884879)
# Date: 1-11-2024
# EC2 Instance Specification Validatating in JSON file

import json  

# Function to load EC2 instance data from a JSON file
def load_ec2_instances(filename):
    with open(filename, 'r') as file: 
        return json.load(file)  

# Function to get user input for CPU and memory requirements
def get_user_requirements():
    min_cpu = int(input("Enter minimum required CPU cores: "))
    max_cpu_input = input("Enter maximum required CPU cores (or press Enter to skip): ")
    max_cpu = int(max_cpu_input) if max_cpu_input else min_cpu

    min_memory = float(input("Enter minimum required memory in GiB: "))
    max_memory_input = input("Enter maximum required memory in GiB (or press Enter to skip): ")
    max_memory = float(max_memory_input) if max_memory_input else min_memory

    return min_cpu, max_cpu, min_memory, max_memory  


def main():
    ec2_instance_types = load_ec2_instances('ec2_instance_types.json')

    min_cpu, max_cpu, min_memory, max_memory = get_user_requirements()

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
