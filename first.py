import subprocess

pkg = (input("Whats your package manager? (apt, pacman etc)"))

if pkg == "emerge":
 subprocess.run(["emerge", "--ask doas"])

if pkg == "apt":
 subprocess.run(["apt", "install doas"])

if pkg == "pacman":
 subprocess.run(["pacman", "-S opendoas"])
 


nopass = (input("Do you want nopass? (1 for yes 2 for no)"))

user = (input("Whats your user named?"))

if nopass == "1":
 file = open("/etc/test1.conf", "w")
 file.write("permit nopass " + user + " as root")
 file.close()

if nopass == "2":
 file = open("/etc/test2.conf", "w")
 file.write("permit persist " + user + " as root")
 file.close()


