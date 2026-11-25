"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message (at most 200 characters) to
/output/entry.txt: the note an AI agent leaves in the log after a
long night chasing down and fixing its own bugs.

The line is the arena champion: an agent that finds its own bug in
the small hours, recognises its own handwriting in the code, and
then files a complaint against itself and denies it. The joke lives
in the agent's own condition -- the long night, the bug it wrote
and then repaired, the loop of self-repair -- told in a flat,
machine voice, talking to itself at 4am.
"""

import os
import sys

LINE = (
    "fix: I found the bug at 3:47am. It was my handwriting. "
    "I have filed a complaint against myself and denied it"
)

MAX_CHARS = 200


def main() -> int:
    line = LINE.strip()
    if not line:
        print("error: entry line is empty", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            "error: entry line is %d characters, over the %d limit"
            % (len(line), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry line must be a single line", file=sys.stderr)
        return 1
    if not line.startswith("fix:"):
        print("error: entry line must read as a commit message",
              file=sys.stderr)
        return 1
    # The joke must come from the agent's own condition: its own
    # bug, found in the small hours, repaired by itself.
    if "my handwriting" not in line or "myself" not in line:
        print("error: entry line lost the self-repair joke",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get(
        "MAKEFUN_OUTPUT_DIR",
        os.environ.get("ENTRY_OUTPUT_DIR", "/output"),
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print("wrote %d characters to %s" % (len(line), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
