# Formats Anisama concert setlists for easy posting on Discord
# by Jon Ingoglia

metadata_file = "input.txt"
showNumbers = 0

try:
    with open(metadata_file, "r", encoding="utf-8") as f:
        metadata = f.read()
except FileNotFoundError:
    print(f"Error: {metadata_file} not found in the working directory.")
    exit(1)

lines = metadata.strip().split("\n")
chapters = [0]
blocks = []
output = ''
setlist_output = ''
index = 1

for i in range(len(lines)):
    if lines[i] == (""):
        chapters.append(i + 1)

print(chapters)

for chapter in chapters:
    pretext = "**__Now Playing:__**"
    title = f":musical_note: {lines[chapter]}".strip()
    artist = f":microphone: {lines[chapter + 1]}".replace("Ã—", "x").strip()
    series = f":tv: {lines[chapter + 2]}".strip()

    if lines[chapter + 2] == "[ORIGINAL]":
        blocks.append((pretext, title, artist))
    else:
        blocks.append((pretext, title, artist, series))

# print(blocks)

for block in blocks:
    for line in block:
        output += f"{str(line)}\n"
    output += "\n"
    if (showNumbers == 1):
        setlist_output += f"{index}. {block[1]} / {block[2]}\n".replace(":musical_note: ", "").replace(":microphone: ", "")
    else:
        setlist_output += f"{block[1]} / {block[2]}\n".replace(":musical_note: ", "").replace(":microphone: ", "")
    index += 1

output_file = 'output.txt'
with open(output_file, 'w', encoding="utf-8") as o:
    o.write(output)

print(f"Content has been written to {output_file}")

output_file = 'setlist.txt'
with open(output_file, 'w', encoding="utf-8") as o:
    o.write(setlist_output)

print(f"Setlist has been written to {output_file}")