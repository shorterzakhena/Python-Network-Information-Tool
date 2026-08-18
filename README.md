# Python-Network-Information-Tool

**Objective**

The objective of this project is to develop a beginner-friendly Python network troubleshooting tool that can be used to test network connectivity. The program allows a user to enter a website or IP address and uses Python to determine whether the destination can be reached. This project provides hands-on experience with Python programming, network troubleshooting, user input, error handling, and GitHub project management.

**Project Description**

I created this project to practice Python programming and apply networking concepts to a practical IT troubleshooting situation. The program allows a user to enter a website or IP address and uses Python's built-in `socket` module to attempt to resolve the destination. The program then displays the hostname, IP address, and whether the test was successful. This project demonstrates how Python can be used to create simple tools that assist with basic network troubleshooting.

**Tools Used**

- Python 3
- GitHub
- Windows Command Prompt / Terminal
- Python `socket` module
- Markdown

**Project Requirements**

To run this project, you will need:

- A Windows, macOS, or Linux computer
- Python 3 installed
- An internet connection
- A GitHub account if downloading the project directly from GitHub
- A command-line terminal such as Command Prompt, PowerShell, Terminal, or Git Bash
-  Markdown documentation

**Python Program Directions**

**Step 1: Import the Socket Module**

Start the program by importing Python's built-in `socket` module.

```python
import socket
```

The `socket` module provides networking functions that allow the program to work with hostnames and IP addresses.

**Step 2: Create the Program Title**

Add a title that identifies the program when it runs.

```python
print("=" * 50)
print("       PYTHON NETWORK TROUBLESHOOTING TOOL")
print("=" * 50)
```

**Step 3: Ask the User for a Hostname or IP Address**

Use the `input()` function to ask the user what website or IP address they want to test.

```python
hostname = input("\nEnter a website or IP address to test: ")
```

The user's response is stored in the `hostname` variable.

**Step 4: Display a Testing Message**

Tell the user that the network test is beginning.

```python
print("\nTesting network connection...")
print("-" * 50)
```

**Step 5: Attempt to Resolve the Hostname**

Use `socket.gethostbyname()` to attempt to find the IP address associated with the hostname.

```python
ip_address = socket.gethostbyname(hostname)
```

**Step 6: Display the Successful Result**

If the hostname is successfully resolved, display the hostname, IP address, and connection status.

```python
print("Hostname:", hostname)
print("IP Address:", ip_address)
print("Status: Connection successful")
print("The destination could be reached successfully.")
```

**Step 7: Add Error Handling**

Use `try` and `except` to handle situations where the hostname cannot be resolved.

```python
except socket.gaierror:
    print("Hostname:", hostname)
    print("Status: Connection failed")
    print("The destination could not be reached.")
    print("Check the address and try again.")
```

**Step 8: Add a Completion Message**

Add a message indicating that the troubleshooting test has finished.

```python
print("-" * 50)
print("Network troubleshooting test completed.")
```

**Step 9: Combine the Code**

After completing each step, the complete Python program should look like this:

```python
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
```

**Step 10: Run the Program**

Run the Python program and enter a website or IP address when prompted.

Example:

```text
google.com
```

The program should attempt to resolve the hostname and display the result.

Test the program again using an IP address such as:

```text
8.8.8.8
```

Finally, test an invalid hostname to verify that the error-handling section works correctly.

**Skills Demonstrated**

- Python programming
- Network troubleshooting
- DNS and hostname resolution
- User input
- Variables
- Exception handling
- Command-line execution
- Program testing
- Problem-solving
- Technical documentation
- GitHub repository management
