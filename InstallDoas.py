import subprocess

pkg = (input("Whats your package manager?(type search for the supported ones you can skip with skip):"))

if pkg == "emerge":
 subprocess.run(["emerge", "--ask doas"])


elif pkg == "apt":
 subprocess.run(["apt", "install doas"])

elif pkg == "pacman":
 subprocess.run(["pacman", "-S opendoas"])

elif pkg == "dnf":
    subprocess.run(["dnf", "install opendoas"])

elif pkg == "search":
 print("Supported package managers:emerge, apt, pacman and dnf")
 exit()

elif pkg == "skip":
 print("You skipped!")

else:
 print("Package manager not supported!Install it yourself and continue!")



nopass = (input("Do you want nopass?"))

if nopass == "yes":
 print("Using nopass")

elif nopass == "no":
 print("not using nopass")

else:
 print("yes or no")
 exit()

user = (input("Whats your user named?"))

if nopass == "yes":
 file = open("test", "w")
 file.write("permit nopass " + user + " as root")
 file.close()

elif nopass == "no":
 file = open("test", "w")
 file.write("permit persist " + user + " as root")
 file.close()





