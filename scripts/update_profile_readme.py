from datetime import datetime, timezone
from pathlib import Path


README_PATH = Path(__file__).resolve().parents[1] / "README.md"
START = "<!--AUTO_REFRESH-->"
END = "<!--/AUTO_REFRESH-->"


def main() -> None:
    text = README_PATH.read_text(encoding="utf-8")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    replacement = f"{START}{now}{END}"

    start_idx = text.find(START)
    end_idx = text.find(END)
    if start_idx == -1 or end_idx == -1 or end_idx < start_idx:
        raise RuntimeError("AUTO_REFRESH markers not found in README.md")

    updated = text[:start_idx] + replacement + text[end_idx + len(END):]
    README_PATH.write_text(updated, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
