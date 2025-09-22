import os 
from google.genai import types


def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: "{file_path}" is not in working directory'
    
    parent_dir = os.path.dirname(abs_file_path)
    if not os.path.isdir(parent_dir):
        try:
            os.makedirs(parent_dir)
        except Exception as e:
            return f'Error creating directories: {parent_dir} = {e}'
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to file: "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Failed writing to file: {file_path}, {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites an existing file or writes a new file if it doesn't exists (and creates parent dirs safely) constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file as a string.",
            ),
        },
    ),
)