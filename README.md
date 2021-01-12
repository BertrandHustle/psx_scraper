### psx_scraper

Psx eboot folders are frequently named by part number instead of game name, which makes it difficult to know
which games you have.
  
psx_scraper aims to fix that.
 
Just run the script on any system where Python is installed.
Run the script in a directory with your eboot.pbp files in individual folders (as you would on your PSP/PS3), 
or specify a directory with the -d flag (see below). 

###### Command Line Options:

-d/--dir: specify a directory to scrape

-l/--log: produces a log (psx_scraper.log) in the directory where the script is run, this log details any 
pbp files that the scraper was unable to find information for

-p/--print: dry run option, print out game names but make no changes to directory names