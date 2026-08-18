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


**Project Requirements**

To run this project, you will need:

- A Windows, macOS, or Linux computer
- Python 3 installed
- An internet connection
- A GitHub account if downloading the project directly from GitHub
- A command-line terminal such as Command Prompt, PowerShell, Terminal, or Git Bash


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

**How the Program Works**

The program uses Python's built-in `socket` module to perform a basic network troubleshooting test.

1. The program asks the user to enter a website or IP address.
2. The program attempts to resolve the entered hostname or IP address.
3. If the destination can be resolved successfully, the program displays the hostname, IP address, and a successful connection message.
4. If the destination cannot be resolved, the program uses error handling to display a connection failure message.
5. The program displays a message when the troubleshooting test is completed.

The program demonstrates how Python can be used to perform a basic network-related troubleshooting task.

**Testing Results**

### Test 1 — Successful IP Address Test

**Input:**

`8.8.8.8`

**Result:**

The program successfully processed the IP address and displayed:

- IP Address: 8.8.8.8
- Status: Connection successful
- The destination could be reached successfully.

### Test 2 — Invalid Hostname Test

**Input:**

`not-a-real-website-12345.com`

**Result:**

The program correctly identified that the hostname could not be reached and displayed:

- Status: Connection failed
- The destination could not be reached.
- The program instructed the user to check the address and try again.

**Testing Conclusion**

Both tests worked as expected. The successful test demonstrated that the program could process a valid IP address, while the failed test demonstrated that the program could handle an invalid hostname without crashing.

**What I Learned**

Through this project, I gained hands-on experience using Python to create a basic network troubleshooting tool.

**What I Learned**

I learned how to create and run a basic Python program.

I learned how to:

- Use the socket module.
- Get information from the user.
- Use variables.
- Use try and except.
- Test my program using Command Prompt.
- Fix problems when my program would not run.
- Use GitHub to store my Python project.
- Add screenshots and information to my GitHub project.

This project gave me more practice with Python and basic networking.

**Challenges and Solutions**

One of my biggest challenges was getting my Python file to run from Command Prompt. I had some problems with the file location and the Python command. I was able to fix it by finding the correct location of my Python file and running it using the full file path.

I also had to learn how to organize my project on GitHub and add my screenshots.

After working through these problems, I was able to get my program running and complete both of my tests successfully.

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

Author: Zakhena K.Shorter IT Professional | Recent IT Graduate
