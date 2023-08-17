# Chapter File Fixer

*by 42GAMI, with get_time function and other small edits by Jon Ingoglia*

This script is intended to help fix "invalid chapter file" errors when trying to load a video's chapters into MKVToolNix. This script will help format the chapter file correctly so it can be read and edited.

## To Use:

1. Move the video file into the same directory as this script
2. Install/copy ffmpeg into the same directory
3. Using ffmpeg, run this command, replacing the filename with the actual filename:
    ffmpeg -i "YOUR_VIDEO_FILE.mp4" -f ffmetadata input.txt
4. Run chapter_fixer.py
5. Drag the video file and output.xml into MKVToolNix, dismiss the message that comes up
6. Check output tab and make sure file path to output.xml is there, then multiplex them together
7. When done, you should be able to drag the video file into MKVToolNix's chapter editor with no issues

## If the audio is in ALAC format:

1. Extract the audio using MKVToolNix, rename it to audio.m4a
2. In cmd run the following: 
    ffmpeg -i audio.m4a -acodec flac audio.flac
3. Add the flac back in using MKVToolNix and multiplex