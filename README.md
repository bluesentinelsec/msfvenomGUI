# msfvenomGUI

msfvenomgui provides a graphical UI over Metasploit's [msfvenom tool](https://www.offsec.com/metasploit-unleashed/msfvenom/).

This tool was created to satisfy classwork for Dakota State University's CSC-842 Security Tool Development.

Demo video: [here]()

![image](media/msfvenomgui-screenshot.png)

## Prerequisites

- Python 3 Interpreter
- Pip3
- tkinter
- msfvenom

## Usage

```bash
# install msfvenomgui with pip
pip install msfvenomgui

# execute msfvenomgui
msfvenomgui
```

## Build from Source

First install [Poetry](https://python-poetry.org/docs/) for your platform.

Once Poetry is intalled, run the following commands from the msfvenom root folder:

```bash
# install needed dependencies
poetry install

# run msfvenomgui
poetry run msfvenomgui
```

## Future Work

1. Expose all payloads and executable formats
2. Automatically find the msvenom path, without blocking the program
3. Dynamically expose arguments based on the selected payload
