#!/bin/sh
qemu-system-hppa -m 512 -machine hppa -drive if=scsi,bus=0,index=6,file=HP-UX_hdd0.qcow2 -cdrom /Users/jesse/Downloads/HP-UX\ 10.20\ \[HP9000\ S700\]/hpux-10.20_os_700.iso -net nic,model=tulip -net user
