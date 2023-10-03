# Add Chapter Names

This is a script meant for easily adding chapter names (supplied by the user in **chapters.txt**) to a chapter file (extracted from the video - **chapters.xml**) with the timestamps already defined. Useful for when ripping a Blu-ray or DVD with MakeMKV and the chapter file has timestamps but no chapter names.

# Instructions

1. Find a video that has chapter timestamps defined but no chapter names (chapter names are "Chapter 1", "Chapter 2", etc)
2. Add those chapter names, in order, to a file called **chapters.txt**, one title per line
3. Use [gMKVExtract GUI](https://sourceforge.net/projects/gmkvextractgui/) or ffmpeg to extract the chapter file and save it to the same directory as **chapters.xml**
4. Run the script
5. Chapter file with chapter name will be created as **output.xml**
6. Use [MKVToolNix GUI](https://mkvtoolnix.download/downloads.html) or ffmpeg to add the new chapter file in
7. Remove the old chapter file with the unnamed chapters