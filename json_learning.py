import json

def get_input(prompt, is_float=False):
    """Gets input from the user as either integer or float."""
    user_input = input(prompt).strip()
    return float(user_input) if is_float else int(user_input) if user_input else None

def filter_instances(instances, min_cpu=None, max_cpu=None, min_memory=None, max_memory=None):
    """Filters instances based on provided CPU and memory requirements."""
    filtered = []
    for instance in instances:
        # Extract numeric CPU and memory values
        cpu_cores = int(instance['vcpu'].split()[0])
        memory_gib = float(instance['memory'].split()[0])

        # Check if instance meets CPU and memory conditions
        if ((min_cpu is None or cpu_cores >= min_cpu) and
            (max_cpu is None or cpu_cores <= max_cpu) and
            (min_memory is None or memory_gib >= min_memory) and
            (max_memory is None or memory_gib <= max_memory)):
            filtered.append(instance)

    return filtered

def main():
    # Step 1 & 2: Get user input for minimum and maximum CPU and memory requirements
    min_cpu = get_input("Enter minimum CPU cores required (or press Enter to skip): ")
    max_cpu = get_input("Enter maximum CPU cores allowed (or press Enter to skip): ")
    min_memory = get_input("Enter minimum memory in GiB required (or press Enter to skip): ", is_float=True)
    max_memory = get_input("Enter maximum memory in GiB allowed (or press Enter to skip): ", is_float=True)

    # Step 3: Load EC2 instance data from JSON file
    with open("ec2_instance_types.json", "r") as file:
        instances = json.load(file)

    # Step 4: Filter instances based on user input
    filtered_instances = filter_instances(instances, min_cpu, max_cpu, min_memory, max_memory)

    # Step 5: Display the filtered instances
    if filtered_instances:
        print("\nMatching EC2 Instances:")
        for instance in filtered_instances:
            print(f"- Name: {instance['name']}, CPU: {instance['vcpu']}, Memory: {instance['memory']}")
    else:
        print("No EC2 instances match your criteria.")

if __name__ == "__main__":
    main()
