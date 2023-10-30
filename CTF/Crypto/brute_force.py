import subprocess
import time

# Read the input list from a file
with open("rockyou.txt", "r", encoding="latin1") as file:
    input_list = [line.strip() for line in file.readlines()]

# Iterate through the inputs
for user_input in input_list:
    # Run the executable using subprocess
    command = "./Decrypt.exe"  # Replace with the actual path to your executable
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

    # Provide user input to the executable
    time.sleep(1)  # Add a short delay (adjust as needed)
    process.stdin.write(user_input + "\n")
    process.stdin.flush()

    # Get the output from the executable
    output = process.stdout.read()

    # Close the subprocess
    process.stdin.close()
    process.stdout.close()

    # Print the output (if needed)
    print(output)

    # Read the contents of output.txt
    with open("./output.txt", "r") as output_file:
        output_content = output_file.read()

    # Print the contents of output.txt
    print(output_content)
