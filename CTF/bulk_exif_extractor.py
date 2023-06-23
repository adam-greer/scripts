import subprocess
import os 
# Folder path containing the files
folder_path = '/tmp/path/to/pics'

# Output file path
output_file = '/tmp/output.txt'

# exiftool command to extract description tag
exiftool_cmd = 'exiftool -s -s -s -Description "{}"'

# Iterate over files in the folder
with open(output_file, 'w') as f:
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        # Run exiftool command
        cmd = exiftool_cmd.format(file_path)
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        # Get description value
        description = result.stdout.strip()
        
        # Write to output file
        f.write(f'{file_name}: {description}\n')

print('Exiftool command executed successfully. Output saved to', output_file)
