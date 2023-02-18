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

You will see a final.exe executable in dist folder in your current working directory (CWD)

Make it's shortcut by right-cliking and selecting 'create shortcut'

Press Win+R to prompt the Run window; and type 'shell:startup' and paste the shortcut in the window which you see opened (containing the Startup Programs)

All's done! Enjoy!
