from typing import Optional, Tuple


def parse_command(content: str) -> Tuple[Optional[str], Optional[str]]:
    """Return a command and its argument only when exactly one argument is present."""
    parts = content.split()
    if not parts:
        return None, None

    command = parts[0]
    if len(parts) != 2:
        return command, None

    return command, parts[1]
