#!/usr/bin/env python3
"""Write one original dad joke to /output/entry.txt.

v2 (revised): tightened hard. The v1 setup ("I asked my son what
he wanted for dinner — he said ...") spent half the line before
the turn. Now the request itself is the setup — "dinner with a
twist" — and the punchline (pasta, a twist shape) lands on word
nine. Shorter line, faster punchline, same groan, and fewer bytes
helps the size tie-break.
"""

from pathlib import Path

TEXT = "My son asked for dinner with a twist — so I served pasta."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
