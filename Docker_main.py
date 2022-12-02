#### MENU ####

import os
import docker
import time
client = docker.from_env()
#### module ####

#### module ####



###########################   function for each service   ##################################


def handle_list_menu_choice(choid_id):
    if choid_id == "1":
        #print("[1] List all EC2 instances")
        for container in client.containers.list():
            print(container.id)
        
#------------------------------------------------------------------------------------------

    elif choid_id == "2":
        #print("[2] Start a specific instance")
        ec2_handle.print_ec2_instance_start() 

#------------------------------------------------------------------------------------------

    elif choid_id == "3":
        #print("[3] Stop a specific instance")
        ec2_handle.print_ec2_instance_stop()

# #==============================================================================================================

def handle_run_menu_choice(choid_id):
    if choid_id == "1":
        #print("[1] List all volumes")
        ebs_handle.print_ebs_all_volumes()

#------------------------------------------------------------------------------------------

def handle_execute_menu_choice(choid_id):
    if choid_id == "1":
        #print("[1] List all objects in a bucket")
        s3_handle.print_list_object_bucket()

#------------------------------------------------------------------------------------------

def handle_stop_menu_choice(choid_id):
    if choid_id == "1":
        #print("[1] Display the CPUUtilization for an EC2 instance")
        cloudwatch_handle.print_display_cpu()

#======================================================================

def handle_remove_menu_choice(choid_id):
    if choid_id == "1":
        #print("[1] Create an RDS instance")
        rds_handle.print_create_rds_instance()

#--------------------------------------------------------------------------------------


####################### Menu ###############################

def print_remove_menu():
    print("[1] Remove a container")
    print("[0] Exit to the main menu")

def print_stop_menu():
    print("[1] Stop a container")
    print("[0] Exit to the main menu")

def print_execute_menu():
    print("[1] Execute a command on a container")
    print("[0] Exit to the main menu")

def print_run_menu():
    print("[1] Run a container")
    print("[0] Exit to the main menu")


def print_list_menu():
    print("[1] List all containers")
    print("[2] List all stopped containers")
    print("[3] List all exited containers")
    print("[0] Exit to the main menu")

def print_main_menu():
    print("-" * 20)
    print("[1] List containers")
    print("[2] Run containers")
    print("[3] Execute a command")
    print("[4] Stop containers")
    print("[5] Remove containers")
    print("[0] Exit the program")

######################## loop menu ###############################

def run_cli_menu():
    try:
        LOOP_CONTINUE = True
        while LOOP_CONTINUE:
            print_main_menu()  

            menu_id = input(f"Menu choice: ")
            print(f"Your choice: {menu_id}")

            if menu_id == "0":
                LOOP_CONTINUE = False
                break  # Exit from Main Loop
            elif menu_id == "1":
                print_list_menu()

                sub_menu_id = input(f"Menu choice: ")
                if sub_menu_id in ["1", "2", "3"]:
                    handle_list_menu_choice(sub_menu_id)
                elif sub_menu_id == 0:
                    pass # loop again

            elif menu_id == "2":
                print_run_menu()

                sub_menu_id = input(f"Menu choice: ")
                if sub_menu_id in ["1"]:
                    handle_run_menu_choice(sub_menu_id)
                elif sub_menu_id == 0:
                    pass # loop again

            elif menu_id == "3":
                print_execute_menu()

                sub_menu_id = input(f"Menu choice: ")
                if sub_menu_id in ["1"]:
                    handle_execute_menu_choice(sub_menu_id)
                elif sub_menu_id == 0:
                    pass # loop again
            
            elif menu_id == "4":
                print_stop_menu()

                sub_menu_id = input(f"Menu choice: ")
                if sub_menu_id in ["1"]:
                    handle_stop_menu_choice(sub_menu_id)
                elif sub_menu_id == 0:
                    pass # loop again

            elif menu_id == "5":
                print_remove_menu()

                sub_menu_id = input(f"Menu choice: ")
                if sub_menu_id in ["1"]:
                    handle_remove_menu_choice(sub_menu_id)
                elif sub_menu_id == 0:
                    pass # loop again


            # Wait for response text before requesting next input
            time.sleep(1)


        print("Exit Menu CLI. Good Bye~")
    except KeyboardInterrupt as kie:
        print(f"Exit by : {kie}")
    except Exception as e:
        print(e)
    

######################################################################

def main():
    run_cli_menu()

if __name__ == "__main__":
    main()





