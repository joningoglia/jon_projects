# Add Chapter Names

This is a script meant for easily adding chapter names (supplied by the user in **chapters.txt**) to a chapter file (extracted from the video - **chapters.xml**) with the timestamps already defined. Useful for when ripping a Blu-ray or DVD with MakeMKV and the chapter file has timestamps but no chapter names.

# Instructions

1. Find a video that has chapter timestamps defined but no chapter names (chapter names are "Chapter 1", "Chapter 2", etc)
2. Drag the video into [MKVToolNix GUI](https://mkvtoolnix.download/downloads.html)'s Chapter Editor 
3. Click the **Chapter Editor** menu and select **Save as XML file** and save it as **chapters.xml**
4. Add the chapter names, in order, to a file called **chapters.txt**, one title per line, no numbers (use the line number for reference)
5. Run the script
6. A chapter file with the chapter names will be created as **output.xml**
7. Drag output.xml into [MKVToolNix GUI](https://mkvtoolnix.download/downloads.html)'s Chapter Editor and review it
8. Drag the video file into the Chapter Editor as well
9. Go back to the tab for output.xml, right click **Edition entry** at the top, and select **Copy to other tab**
10. Go to the other tab and remove the old chapter edition with the unnamed chapters
11. Click the **Chapter Editor** menu and select **Save**