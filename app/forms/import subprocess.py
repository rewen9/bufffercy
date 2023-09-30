import subprocess



def install_xclip():
    try:
        # Try running the xclip command
        subprocess.run(['xclip', '-version'], check=True)
    except FileNotFoundError:
        # xclip command not found, install it using apt-get
        subprocess.run(['sudo', 'apt-get', 'update'])
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'xclip'])


install_xclip()
import subprocess
command = ['xclip', '-selection', 'clipboard', '-o']
process = subprocess.run(command, capture_output=True, text=True)
print(process.stdout.strip())