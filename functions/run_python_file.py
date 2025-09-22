import os
import subprocess

def run_python_file(working_directory, file_path: str, args=[]):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: "{file_path}" is not in working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: "{file_path}" is not a file'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'

    try:
        final_args = ["python", file_path]
        final_args.extend(args)
        output = subprocess.run(final_args, timeout=30, cwd=abs_working_directory, capture_output=True)
        final_string = f"""
STDOUT: {output.stdout}
STDERR: {output.stderr}
    
"""
        if output.stdout == "" and output.stderr == "":
            final_string = "No Output Produced.\n"
        if output.returncode != 0:
            final_string += f"Process exited with ruturn code: {output.returncode}"
        return final_string
    except Exception as e:
        return f'Error: Executing Python File: {e}'