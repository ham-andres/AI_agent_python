import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        # turn working directory into absolute path
        working_dir_abs = os.path.abspath(working_directory)    
        # build the full path
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        # check the target dir is in inside working directory abs
        valid_target = os.path.commonpath([working_dir_abs,target_dir]) ==  working_dir_abs


        if not valid_target:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory' 
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        items = os.listdir(target_dir)

        lines = []

        for name in items:
            full_path = os.path.join(target_dir,name)
            size = os.path.getsize(full_path)
            is_dir = os.path.isdir(full_path)
            line = f"- {name}: file_size={size} bytes, is_dir={is_dir}"
            lines.append(line)
        result = "\n".join(lines)
        return result

    except Exception as e:
        return f"Error: {e}"




schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)





