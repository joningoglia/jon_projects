# Fixes bad chapter files in videos
# by 42GAMI and Jon I

# TO USE: first use ffmpeg to extract the chapter file
# example: ffmpeg -i "file.mp4" -f ffmetadata file.txt
# then run this script in same dir

import math

metadata_file = "file.txt"

try:
    with open(metadata_file, "r") as f:
        metadata = f.read()
except FileNotFoundError:
    print(f"Error: {metadata_file} not found in the working directory.")
    exit(1)

lines = metadata.strip().split("\n")
chapters = []

def get_time(ts):
    sec = ts/10000000
    h = math.floor(sec/3600)
    m = math.floor((sec/60)-(h*60))
    s = math.floor(sec % 60)
    d = str((sec % 60) % 1).replace('0.', '')
    return f"{h:02d}:{m:02d}:{s:02d}.{d[:9]}"

for i in range(len(lines)):
    if lines[i].startswith("[CHAPTER]"):
        start = int(lines[i + 2].split("=")[1])
        start_full = get_time(start)
        end = int(lines[i + 3].split("=")[1])
        end_full = get_time(end)
        title = lines[i + 4].split("=")[1].strip()
        if not title:
            title = f"Chapter {len(chapters) + 1}"
        chapters.append((start_full, end_full, title))

xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml_content += '<Chapters>\n'
xml_content += '    <EditionEntry>\n'

for i, (start, end, title) in enumerate(chapters):
    print(f"{title}: {start}-{end}")
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
with open(output_file, 'w') as xml_file:
    xml_file.write(xml_content)

print(f"XML content has been written to {output_file}")
