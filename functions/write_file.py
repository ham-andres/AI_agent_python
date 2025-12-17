import os


def write_file(working_directory, file_path, content):
    try:
        working_dir_abs_write = os.path.abspath(working_directory)

        file_path_dir_write = os.path.normpath(os.path.join(working_dir_abs_write,file_path))

        valid_file_path_write = os.path.commonpath([working_dir_abs_write,file_path_dir_write]) == working_dir_abs_write

        if not valid_file_path_write:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(file_path_dir_write):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        parent_dir = os.path.dirname(file_path_dir_write)
        os.makedirs(parent_dir, exist_ok=True)

        with open(file_path_dir_write,"w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {e}'



