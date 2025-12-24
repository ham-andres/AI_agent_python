import os
from config import MAX_CHARS
from google.genai import types


def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)

        file_path_dir = os.path.normpath(os.path.join(working_dir_abs,file_path))

        valid_file_path = os.path.commonpath([working_dir_abs,file_path_dir]) == working_dir_abs

        if not valid_file_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(file_path_dir):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(file_path_dir, "r") as f:
            content = f.read(MAX_CHARS)
            extra = f.read(1)
            # After reading the first MAX_CHARS...
            if extra:
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content

    except Exception as e:
        return f"Error: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read the contents of a file at the given path.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory.",
            ),
        },
    ),
)
