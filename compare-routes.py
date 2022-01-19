# diff_tool.py
# credits: https://florian-dahlitz.de/articles/create-your-own-diff-tool-using-python

from pathlib import Path
from datetime import date
import argparse
import difflib
import sys
import mmap
import re

def create_diff(old_file: Path, new_file: Path, output_file: Path = None):
    file_1 = open(old_file).readlines()
    file_2 = open(new_file).readlines()
    if output_file:
        delta = difflib.HtmlDiff().make_file(
            file_1, file_2, old_file.name, new_file.name
        )
        with open(output_file, "w") as f:
            f.write(delta)
    else:
        delta = difflib.unified_diff(file_1, file_2, old_file.name, new_file.name)
        sys.stdout.writelines(delta)

def find_route(old_file: Path, new_file: Path, route: str = None, hostname :str = None):
	with open('example.txt', 'rb', 0) as file, mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
		if s.find(b'blabla') != -1:
			print('true')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("old_file_version")
    parser.add_argument("new_file_version")
    # parser.add_argument("--html", help="specify html file to write to")
    parser.add_argument("--dst", help="specify destination ip")
    parser.add_argument("--hostname", help="(optional) specify hostname")
    args = parser.parse_args()

    old_file = Path(args.old_file_version)
    new_file = Path(args.new_file_version)

    if args.html:
        output_file = Path(args.html)
    else:
        output_file = None

    create_diff(old_file, new_file, output_file)


if __name__ == "__main__":
    main()