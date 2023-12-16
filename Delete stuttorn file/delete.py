# Python script to delete a specific file

import os

# Corrected path to the PDF file
# Using a raw string to handle the special characters and prefix in the path
file_path = "put your right path here"

def delete_file(path):
    try:
        # Attempt to remove the file at the specified path
        os.remove(path)
        return "File deleted successfully."
    except FileNotFoundError:
        # This error occurs if the file does not exist at the path
        return "File not found."
    except Exception as e:
        # Catch any other exceptions and return the error
        return f"An error occurred: {e}"

# Attempt to delete the file and store the result
delete_file_result = delete_file(file_path)

# Output the result of the delete operation
print(delete_file_result)
