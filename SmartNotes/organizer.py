def detect_headings(text):
    lines = text.splitlines()
    headings = []
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        if line.endswith(":"):
            headings.append(line)
        elif len(line.split()) <= 3 and not line.endswith("."):
            headings.append(line)

    return headings


def detect_definitions(text):
    lines = text.splitlines()
    definitions = []
    for line in lines:
        line = line.strip()
        if "is" in line or "are" in line:
            definitions.append(line)
    return definitions


def detect_bullet_points(text):
    lines = text.splitlines()
    bullet_points = []
    for line in lines:
        line = line.strip()
        if line.startswith("-") or line.startswith("*"):
            bullet_points.append(line)
        elif "." in line:
            parts = line.split(".", 1)
            if parts[0].isdigit():
                bullet_points.append(line)
    return bullet_points


def detect_examples(text):
    lines = text.splitlines()
    examples = []
    inside_example = False
    for line in lines:
        line = line.strip()
        lower_line = line.lower()

        if lower_line.startswith("example") or lower_line.startswith("for example"):
            inside_example = True
            continue
        if line == "":
            inside_example = False
            continue
        if inside_example:
            examples.append(line)

    return examples


def detect_advantages(text):
    lines = text.splitlines()
    advantages = []
    inside_advantages = False
    for line in lines:
        line = line.strip()
        lower_line = line.lower()
        if lower_line.startswith("advantages") or lower_line.startswith("pros"):
            inside_advantages = True
            continue
        if lower_line.startswith("disadvantages") or lower_line.startswith("cons"):
            inside_advantages = False
            continue
        if line == "":
            inside_advantages = False
            continue
        if inside_advantages:
            advantages.append(line)
    return advantages


def detect_disadvantages(text):
    lines = text.splitlines()
    disadvantages = []
    inside_disadvantages = False
    for line in lines:
        line = line.strip()
        lower_line = line.lower()
        if lower_line.startswith("disadvantages") or lower_line.startswith("cons"):
            inside_disadvantages = True
            continue
        if lower_line.startswith("advantages") or lower_line.startswith("pros"):
            inside_disadvantages = False
            continue
        if line == "":
            inside_disadvantages = False
            continue
        if inside_disadvantages:
            disadvantages.append(line)
    return disadvantages
