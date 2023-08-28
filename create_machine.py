import os
import config

def editConfig(_vmname, is_independent = True):
    if (is_independent):
        focus(_vmname)

    os.system(config.favorite_editor() +" start.sh")

    if (is_independent):
        unfocus()

def runMachine(_vmname):
    focus(_vmname)
    os.system("./start.sh")
    unfocus()

def focus(_vmname):
    if (os.path.exists(os.getcwd() + "/start.sh") == False):
        if (os.path.exists(os.getcwd() + "/"+ _vmname) == False):
            os.mkdir(_vmname)
        os.chdir(_vmname)

def unfocus():
    if (os.path.exists(os.getcwd() + "/start.sh") == True):
        os.chdir("..")

def create_hdd(_vmname, is_independent = True):
    if (is_independent):
        focus(_vmname)
    hddcounter = 0
    for file in os.listdir(os.getcwd()):
        if (file.endswith(".qcow2")):
            hddcounter = hddcounter + 1

    hddname = _vmname + "_hdd" + str(hddcounter) + ".qcow2"

    print("Enter size of HDD: ")
    hddsize = input()
    hdd_create_cmd = "qemu-img create -f qcow2 " + hddname + " " + hddsize
    print("Creating Hard Drive")
    os.system(hdd_create_cmd)
    if (is_independent):
        unfocus()
    return hddname

def create_vm(_vmname):
    vmname = _vmname
    if (vmname == ""):
        print("Enter new name: ")
        vmname = input()

    focus (vmname)

    print ("Enter System Architecture: ")
    print ("Common CPU Types")
    print ("x86_64 - Intel Based (Windows Vista+ / Most Linux Systems)")
    print ("i386 - Intel Based (Windows XP and below)")
    print ("aarch64 - ARM Based")
    print ("riscv64 - RISC-V Based")
    print ("ppc - PowerPC Based (Mac OS 9 / Early Mac OS X)")
    arch = input()


    print ("Arch-Specific Machine Types")
    if (arch == "x86_64" or arch == "i386"):
        print ("pc - i440vx Based (Recommended for XP)")
        print ("q35 - Q35 Based (Recommended for Windows 11 and Modern Linux Distros)")
        print ("isapc - ISA Only PC (Use this for systems like Windows NT 3.X and 4.0 and OS/2)")
        print ("microvm - MicroVM")
    elif (arch == "aarch64"):
        print ("virt - Generic ARM Virtual Machine (Linux Distros)")
        print ("There are a ton of supported machines, so please consult https://www.qemu.org/docs/master/system/target-arm.html")
    elif (arch == "riscv64" or arch == "riscv32"):
        print ("virt - Generic ARM Virtual Machine (Linux Distros)")
        print ("microchip-icicle-kit")
        print ("shakti_c")
        print ("sifive_u")
    elif (arch == "ppc"):
        print ("mac99 - Mac99 based PowerMac (Recommended for OS X)")
        print ("g3beige - Heathrow based PowerMac")
        print ("Consult https://www.qemu.org/docs/master/system/target-ppc.html for Non-Macintosh Applicances")

    print ("Enter Machine Type: ")
    machine = input()

    print ("Enter RAM in MB: ")
    mem = input()

    hda = create_hdd(vmname, False)

    vm_run_cmd = "qemu-system-" + arch + " -m " + mem + " -machine " + machine + " -hda " + hda

    startfile = open("start.sh", "w")
    startfile.write("#!/bin/sh\n" + vm_run_cmd)
    startfile.close()

    os.system("chmod +x start.sh")

    editConfig(vmname, False)

    unfocus()