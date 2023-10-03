# Creates a chapter file from a list of chapters and 
# an XML file with the timestamps already in it.
# by Jon Ingoglia

import math

chapter_file = "chapters.txt"
xml_file = "chapters.xml"
start = []
end = []
timestamps = []

try:
    with open(chapter_file, "r", encoding="utf-8") as f:
        metadata = f.read()
except FileNotFoundError:
    print(f"Error: {chapter_file} not found in the working directory.")
    exit(1)

chapter_names = metadata.strip().split("\n")

try:
    with open(xml_file, "r", encoding="utf-8") as f:
        metadata = f.read()
except FileNotFoundError:
    print(f"Error: {xml_file} not found in the working directory.")
    exit(1)

xml_lines = metadata.strip().split("\n")

for i, line in enumerate(xml_lines):
    if ("<ChapterTimeStart>" in line):
        start.append(line.replace('<ChapterTimeStart>', '').replace('</ChapterTimeStart>', '').strip())

for i, line in enumerate(xml_lines):
    if ("<ChapterTimeEnd>" in line):
        end.append(line.replace('<ChapterTimeEnd>', '').replace('</ChapterTimeEnd>', '').strip())

for i, chapter_name in enumerate(chapter_names):
    timestamps.append((start[i], end[i], chapter_name))

xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml_content += '<Chapters>\n'
xml_content += '    <EditionEntry>\n'

for (start, end, chapter_name) in timestamps:
    print(f"{start}-{end} {chapter_name}")
    xml_content += f'        <ChapterAtom>\n'
    xml_content += f'            <ChapterTimeStart>{start}</ChapterTimeStart>\n'
    xml_content += f'            <ChapterTimeEnd>{end}</ChapterTimeEnd>\n'
    xml_content += f'            <ChapterDisplay>\n'
    xml_content += f'                <ChapterString>{chapter_name}</ChapterString>\n'
    xml_content += f'                <ChapterLanguage>eng</ChapterLanguage>\n'
    xml_content += f'            </ChapterDisplay>\n'
    xml_content += f'        </ChapterAtom>\n'

xml_content += '    </EditionEntry>\n'
xml_content += '</Chapters>\n'

output_file = 'output.xml'
with open(output_file, 'w', encoding="utf-8") as xml_file:
    xml_file.write(xml_content)