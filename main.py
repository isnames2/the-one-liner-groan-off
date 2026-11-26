"""Write the one-line dad joke entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Gate: UTF-8 text of 1 to 140 characters, one line.
"""

import os
from pathlib import Path

ENTRY = "I told my wife she should embrace her mistakes. She gave me a hug."
# Gate: 1-140 characters; this line is 66. The punchline ("She gave me a
# hug") is the twist on "embrace her mistakes" — a dad joke in one breath.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
