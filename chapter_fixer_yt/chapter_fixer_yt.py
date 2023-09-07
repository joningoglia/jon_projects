# Generate a chapter file from timestamps in video comments
# by Jon Ingoglia

import re

metadata_file = "input.txt"

try:
    with open(metadata_file, "r", encoding="utf-8") as f:
        metadata = f.read()
except FileNotFoundError:
    print(f"Error: {metadata_file} not found in the working directory.")
    exit(1)

lines = metadata.strip().split("\n")
chapters = []

for i in range(len(lines)):
  if (re.split('\s', lines[i], 1)[1] != '[END]'):
    start = re.split('\s', lines[i], 1)[0]
    end = re.split('\s', lines[i + 1], 1)[0]
    title = re.split('\s', lines[i], 1)[1].strip()
    chapters.append((start, end, title))

xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml_content += '<Chapters>\n'
xml_content += '    <EditionEntry>\n'

for i, (start, end, title) in enumerate(chapters):
    print(f"{start}-{end}: {title}")
    xml_content += f'        <ChapterAtom>\n'
    xml_content += f'            <ChapterTimeStart>{start}</ChapterTimeStart>\n'
    xml_content += f'            <ChapterTimeEnd>{end}</ChapterTimeEnd>\n'
    xml_content += f'            <ChapterDisplay>\n'
    xml_content += f'                <ChapterString>{title}</ChapterString>\n'
    xml_content += f'                <ChapterLanguage>eng</ChapterLanguage>\n'
    xml_content += f'            </ChapterDisplay>\n'
    xml_content += f'        </ChapterAtom>\n'

xml_content += '    </EditionEntry>\n'
xml_content += '</Chapters>\n'

output_file = 'output.xml'
with open(output_file, 'w', encoding="utf-8") as xml_file:
    xml_file.write(xml_content)

print(f"XML content has been written to {output_file}")
