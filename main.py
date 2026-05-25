import subprocess

# Retrieve the list of saved Wi-Fi profiles
profiles = subprocess.check_output("netsh wlan show profiles", shell=True).decode()

# Extract only the Wi-Fi network names from the command output
names = [line.split(":")[1].strip() 
         for line in profiles.split("\n") if "All User Profile" in line]

# Display the found Wi-Fi networks with a number index
for i, n in enumerate(names, 1):
    print(f"[{i}] {n}")

# Prompt the user to select a network number
ch = int(input("\nChoose WiFi number: "))
wifi = names[ch - 1]

# Retrieve and print the details (including the password) for the chosen network
result = subprocess.check_output(
    f'netsh wlan show profile "{wifi}" key=clear', 
    shell=True).decode()

print("\n" + result)

# ADD THIS LINE TO KEEP THE WINDOW OPEN:
input("\nPress Enter to exit...")