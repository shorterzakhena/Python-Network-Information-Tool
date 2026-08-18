import socket

print("=" * 50)
print("       PYTHON NETWORK TROUBLESHOOTING TOOL")
print("=" * 50)

hostname = input("\nEnter a website or IP address to test: ")

print("\nTesting network connection...")
print("-" * 50)

try:
    ip_address = socket.gethostbyname(hostname)

    print("Hostname:", hostname)
    print("IP Address:", ip_address)
    print("Status: Connection successful")
    print("The destination could be reached successfully.")

except socket.gaierror:
    print("Hostname:", hostname)
    print("Status: Connection failed")
    print("The destination could not be reached.")
    print("Check the address and try again.")

print("-" * 50)
print("Network troubleshooting test completed.")
