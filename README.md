# Chess Workshop
UCI AI Club Chess  

## Download

Press the green "Code" button and click "Download ZIP".

Save the folder to your computer, and extract the contents.

Open a Terminal (OSX/LINUX) or CMD (WINDOWS) and follow the below instructions.

## Prerequisites

We have provided a requirements.txt for you to setup your python environment.

Python Latest Version Download:
https://www.python.org/downloads/


Change directories to chess folder.
```
cd /path/to/chess/folder/
```

First off, create your virtual environment by entering the commands below...

### Mac OSX / Linux

Install virtual environment tool:
```
pip3 install virtualenv
```

Create and activate virtual environment:
```
python3 -m venv chessenv

source chessenv/bin/activate

pip3 install -r requirements.txt
```

### Windows

Install virtual environment tool:
```
pip3 install --user virtualenv
```

Create and activate virtual environment:
```
py -m venv chessenv

chessenv\Scripts\activate.bat

pip3 install -r requirements.txt
```
### RUN

Once you have got your venv activated, run the following command:

#### Mac OSX / Linux
```
python3 chess.py
```

#### Windows
```
chess.py
```

Note: The Minimax AI will not work until you complete the code outlined in the video. But, you should try playing against the random AI to make sure that everything works.

### Playing on a Powerful PC?

If you have a powerful computer, try upping the depth parameter of the minimax algorithm. To do this, navigate to the "chess.py" file in the project directory, and locate the function named determine_move. Once there, you can increase the number to be greater than 3. I started getting recursion errors when I went past 100, so I would recommend that you stay below that threshold.
