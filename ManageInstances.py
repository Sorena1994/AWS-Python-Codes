import boto3
region = 'us-east-1'
ec2 = boto3.client('ec2', region_name= region)

def describe_instance(instance_id):
    response = ec2.describe_instances(InstanceIds=[instance_id])
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print("Instance ID:", instance['InstanceId'])
            print("Instance State:", instance['State']['Name'])
            print("Instance Type:", instance['InstanceType'])
            print("---")

def run_new_instance(instance_params):
    instance_params = {ImageId: None, InstanceType: None,
                       KeyName: None, MinCount: None, 
                       MaxCount: None}
    
    try: 
        print("Enter the instance parameters: ")
        instance_params[ImageId] = input('Please enter the Image ID for the instance: ')
        instance_params[InstanceType] = input('Please specify the instance type: ')
        instance_params[KeyName] = input('Please enter the key pair (You can leave it blank)')
        instance_params[MinCount] = input('Please enter the minimum number of instances you want to launch: ')
        instance_params[MaxCount] = input('Please enter the maximum number of instances you want to launch: ')
        return instance_params
    except KeyboardInterrupt: 
        print("\nInput interrupted by user") 

def start_instance(instance_id):
    #instance_id = input("Please enter the instance ID: ")
    response = ec2.start_instances(InstanceIds=[instance_id])
    print(response)
    print(f"The instance with instance id {instance_id} is started. ")

def stop_instance(instance_id):
    #instance_id = input("Please enter the instance ID: ")
    response = ec2.stop_instances(InstanceIds= [instance_id])
    print(response)
    print(f"The instance with instance id {instance_id} is stopped. ")

def reboot_instance(instance_id):
    response = ec2.describe_instances(InstanceIds=[instance_id])
    state = response['Reservations'][0]['Instances'][0]['State']['Name']
    if state != 'stopped':
        response = ec2.reboot_instances(InstanceIds= [instance_id])
        print(response)
        print(f"The instance with instance id {instance_id} is going to reboot. ")
    else: 
        raise Exception('You cannot reboot an stopped instance!')
def terminate_instance(instance_id):
    #instance_id = input("Please enter the instance ID: ")
    response = ec2.terminate_instances(InstanceIds= [instance_id])
    print(response)
    print(f"The instance with instance id {instance_id} is going to be terminated. ")

def print_menu():
    print('\nMENU')
    print('0 = Quit')
    print('1 = Describe all instances')
    print('2 = Run new instance')
    print('3 = Describe instance')
    print('4 = Start instance')
    print('5 = Stop instance')
    print('6 = Reboot instance')
    print('7 = Terminate instance')
    return

def main():
    option = -1
    
    while option != 0:
        print_menu()
        try:
            option = int(input('\nEnter an option? '))
            if option == 0:
                print('Bye')
            elif option == 1:
                describe_instance(instance_id)
            elif option == 2:
                run_new_instance()
            elif option == 3:
                describe_instance(instance_id)
            elif option == 4:
                start_instance(instance_id)
            elif option == 5:
                stop_instance(instance_id)
            elif option == 6:
                reboot_instance(instance_id)
            elif option == 7:
                terminate_instance(instance_id)
            else:
                print('\nERROR: Enter a valid option!!')
        except ValueError:
            print('\nERROR: Enter a valid option!!')    
    return
  
if __name__ == "__main__":
    instance_id = input('Please enter the instance ID: ')
    main() 
