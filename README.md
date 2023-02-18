# QALMS
A repo for the QALMS project, made with Flask for 1st semester project, BSCS NUST.

This is scrapper for lms course contents; runs periodically as exe file upon startup; downloads only new content

Clone the repo and put your credentials in the 'data.json' file and run the bash script

Necessary libraries to be installed:
- python 
- selenium-wire
- json
- pyinstaller
- socket

Once all these lib are installed; open cmd in the same directory and type the following:
```pyinstaller --onefile --add-data "data.json;." final.py```
