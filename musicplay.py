#-*- cording: utf-8 -*-
import subprocess

def musicplay(filename):
    subprocess.call(["mpc","stop"])
    subprocess.call(["mpc","clear"])
    subprocess.call(["mpc","update"])
    subprocess.call(["mpc","add",filename])
    subprocess.call(["mpc","play"])
