# ipod-music-extractor
it's not the best but it get the job done

I have not check if it does work with older ipod (tested with nano 7 gen only) but it should work if your ipod have a ipod_control folder

### library required
eyed3

`pip install eyeD3`

### Change your ipod drive letter before running the script

at line 5

`ipod_drive = "E:"` (change the "E" to match your ipod drive)

This code works by going into the ipod folder and basically copy the files and rename it fron the id3 tag

tested on windows only 

i cannot confirm it will work perfectly in my testing it works well enough
