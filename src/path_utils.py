'''
Get input folder path and clean

'''
def clean_input(input_path: str) -> str:
    cleaned = input_path.strip().strip('"')

    if not cleaned:
        raise ValueError("Folder path cannot be empty")

    return cleaned


