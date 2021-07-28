import subprocess

interface = input("Network Interface : ")
new_mac = input("Enter new MacAddress : ")


def mac_changer(inferface,new_mac):
    print("+======================================================+")
    print("Current Interface Info")
    subprocess.call("ifconfig",shell=True)
    print("+--------------------------------------------------------+")
    subprocess.call("ifconfig " + interface + " down" , shell=True)
    #mac_address_change
    subprocess.call("ifconfig " + interface + " hw ether " + new_mac,shell=True)

    subprocess.call("ifconfig eth0 up",shell=True)
    print("+=============================================================+")
    subprocess.call("ifconfig",shell = True)

mac_changer(interface,new_mac)
