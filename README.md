# Python-Network-Information-Tool

**Objective**

The objective of this project is to develop a beginner-friendly Python network troubleshooting tool that can be used to test network connectivity. The program allows a user to enter a website or IP address and uses Python to determine whether the destination can be reached. This project provides hands-on experience with Python programming, network troubleshooting, user input, error handling, and GitHub project management.

**Project Description**

I created this project to practice Python programming and apply networking concepts to a practical IT troubleshooting situation. The program allows a user to enter a website or IP address and uses Python's built-in `socket` module to attempt to resolve the destination. The program then displays the hostname, IP address, and whether the test was successful. This project demonstrates how Python can be used to create simple tools that assist with basic network troubleshooting.

**Technologies Used**

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

**Project Setup**

**Step 1: Download the Project**

Download or clone this repository from GitHub.

**Step 2: Open the Project Folder**

Open the downloaded project folder containing the Python file.

**Step 3: Open a Terminal**

Open Command Prompt, PowerShell, Terminal, or another command-line application inside the project folder.

**Step 4: Verify Python Installation**

Run:

```text
python --version
```

If Python is installed, the terminal should display the installed Python version.

**Step 5: Run the Program**

Run:

```text
python network_troubleshooter.py
```

The program will ask for a website or IP address to test.

**Step-by-Step Instructions**

**Step 1: Create the GitHub Repository**

1. Sign in to GitHub.
2. Create a new repository.
3. Name the repository `python-network-troubleshooting-tool`.
4. Set the repository visibility to Public.
5. Add a README file.

**Step 2: Create the Python File**

1. Open the GitHub repository.
2. Select **Add file**.
3. Select **Create new file**.
4. Name the file `network_troubleshooter.py`.
5. Add the Python program to the file.
6. Commit the changes to the repository.

**Step 3: Create the Network Troubleshooting Program**

1. Import Python's `socket` module.
2. Display the program title.
3. Ask the user to enter a website or IP address.
4. Use `socket.gethostbyname()` to attempt to resolve the destination.
5. Display the resolved IP address if successful.
6. Use exception handling to identify unsuccessful hostname resolution.
7. Display a troubleshooting message.
8. End the program.

**Step 4: Test the Program**

1. Open the project on the computer.
2. Open Command Prompt or Terminal.
3. Navigate to the project folder.
4. Run `python network_troubleshooter.py`.
5. Test the program using a hostname such as `google.com`.
6. Test the program using an IP address such as `8.8.8.8`.
7. Verify that the program displays the expected results.

**Step 5: Document the Project**

1. Update the README file.
2. Document the objective and purpose of the project.
3. List the technologies used.
4. Document the skills demonstrated.
5. Document the testing process.
6. Add screenshots showing the project and test results.

**Step 6: Commit the Completed Project**

Commit the completed files and documentation to the GitHub repository so the project can be viewed as part of a technical portfolio.

**How the Program Works**

The program uses Python's built-in `socket` module to perform a basic hostname resolution test.

1. The user enters a hostname or IP address.
2. Python attempts to resolve the destination.
3. If the hostname can be resolved, the program displays the hostname and corresponding IP address.
4. The program reports a successful result.
5. If the hostname cannot be resolved, the program catches the error.
6. The program reports that the destination could not be reached through hostname resolution and provides a basic troubleshooting message.

This provides a simple example of using Python to assist with network troubleshooting.

**Testing**

The program was tested using both a hostname and an IP address.

**Test 1: Hostname**

**Input:**

`google.com`

**Expected Result:**

The program should successfully resolve the hostname and display an IP address.

**Actual Result:**

*To be completed after testing.*

### Test 2: IP Address

**Input:**

`8.8.8.8`

**Expected Result:**

The program should successfully process the IP address.

**Actual Result:**

*To be completed after testing.*

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
-  Markdown documentation
