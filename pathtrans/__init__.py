import sys
import re


def convert_windows_to_unix(path):
    match = re.fullmatch(r'^([A-Za-z]):(.*)$', path)

    if not match:
        print(f"Could not parse {path}", file=sys.stderr)
        sys.exit(-1)

    drive_letter = match.group(1).lower()
    rest = match.group(2).replace("\\", "/")

    return f"/{drive_letter}{rest}"


def convert_unix_to_windows(path):
    match = re.fullmatch(r'^/([a-z])(.*)$', path)

    if not match:
        print(f"Could not parse {path}", file=sys.stderr)
        sys.exit(-1)

    drive_letter = match.group(1).upper()
    rest = match.group(2).replace("/", "\\")

    return f"{drive_letter}:{rest}"
