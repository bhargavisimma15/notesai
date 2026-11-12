def clean_text(text):
    text = text.strip()
    lines = text.splitlines()
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if line != "":
            cleaned_lines.append(line)
        elif cleaned_lines and cleaned_lines[-1] != "":
            cleaned_lines.append("")
    return "\n".join(cleaned_lines)
