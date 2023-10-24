# Instructions

- Find and download a video with timestamps in the comments (such as a concert video with a setlist in the comments)
- Copy and paste that comment into input.txt and manually remove anything irregular. It should be just timestamps and chapter names (no "EN" for encore, for example).
- Last line must be the length of the entire video followed by `[END]`
- Run this script, it will output an XML file
- Use MKVToolNix GUI to add the XML file to the video

# Regex to move timestamps from end of line to start

**Find:**

`(.+) ([0-9][0-9]?:[0-9][0-9]:?[0-9]?[0-9]?)`

**Replace:**

`$2 $1`