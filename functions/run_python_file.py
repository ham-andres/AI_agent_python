import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        if args is None:
            args = []

        working_dir_abs = os.path.abspath(working_directory)

        file_path_abs = os.path.normpath(os.path.join(working_dir_abs,file_path))

        valid_file_path = os.path.commonpath([working_dir_abs,file_path_abs]) == working_dir_abs

        if not valid_file_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(file_path_abs):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not os.path.basename(file_path_abs).endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", file_path_abs]
        command.extend(args)

        result = subprocess.run(command, cwd=working_dir_abs,capture_output=True,text=True,timeout=30)

        output = []

        if result.returncode != 0:
            output.append(f'Process exited with code {result.returncode}')
        

        if result.stdout:
            output.append(f'STDOUT:\n{result.stdout}')
        if result.stderr:
            output.append(f'STDERR:\n{result.stderr}')

        if not output:
            output.append(f'No output produced')

        return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute the Python file at the given path.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type = types.Type.STRING,
                description="The path to the Python file, relative to the working directory.",
            ),
        },
    ),
)