import argparse
import re
from pathlib import Path


DEFAULT_OUTPUT_DIR = Path(r"C:\Users\ethan\coding\anki_auto_input\text_inbox")

TIMESTAMP_LINE = re.compile(
    r"^\s*\d{1,2}:\d{2}:\d{2}[,.]\d{3}\s+-->\s+"
    r"\d{1,2}:\d{2}:\d{2}[,.]\d{3}(?:\s+.*)?\s*$"
)
CUE_NUMBER_LINE = re.compile(r"^\s*\d+\s*$")
WEBVTT_LINE = re.compile(r"^\s*WEBVTT\s*$", re.IGNORECASE)


def strip_timestamps(input_path: Path) -> str:
    transcript_lines = []

    with input_path.open("r", encoding="utf-8-sig") as transcript_file:
        for line in transcript_file:
            line = line.strip()

            if not line:
                continue
            if WEBVTT_LINE.match(line):
                continue
            if CUE_NUMBER_LINE.match(line):
                continue
            if TIMESTAMP_LINE.match(line):
                continue

            transcript_lines.append(line)

    return " ".join(transcript_lines)


def output_path_for(input_path: Path, output_dir: Path, output_name: str | None) -> Path:
    if output_name:
        filename = output_name
        if "." not in Path(filename).name:
            filename += ".md"
    else:
        filename = f"{input_path.stem}_cleaned.md"

    return output_dir / filename


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Strip subtitle cue numbers and timestamps from a txt/vtt transcript."
    )
    parser.add_argument("input_file", help="Path to the txt/vtt transcript to clean.")
    parser.add_argument(
        "-o",
        "--output-name",
        help="Optional output filename. Defaults to <input_name>_cleaned.md.",
    )
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help=f"Output folder. Defaults to {DEFAULT_OUTPUT_DIR}.",
    )
    args = parser.parse_args()

    input_path = Path(args.input_file).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()

    if not input_path.exists():
        raise FileNotFoundError(f"Input file does not exist: {input_path}")

    cleaned_text = strip_timestamps(input_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_path_for(input_path, output_dir, args.output_name)
    output_path.write_text(cleaned_text, encoding="utf-8")

    print(f"Saved cleaned transcript to {output_path}")


if __name__ == "__main__":
    main()
