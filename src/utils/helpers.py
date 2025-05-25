def format_text(text):
    return text.strip().replace('\n', ' ').replace('\r', '')

def validate_file_type(file_name, allowed_extensions):
    return any(file_name.endswith(ext) for ext in allowed_extensions)

def log_message(message):
    print(f"[LOG] {message}")