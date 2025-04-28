# cluedo

## Instructions for running Cluedo:
* ### Prerequisites:
	* Clone the repo with git command `$ git clone https://github.com/t-d-o-g/cluedo.git` and change directory into the repo with command `$ cd cluedo`. You will be on the main branch.
	* It is recommended to activate a Python Virtual Environment with Python version 3.9.0 or higher to install dependencies locally. Run the command `$ python -m venv venv` followed by `$ source venv/bin/activate` on mac or `$ venv\Scripts\activate` on windows. For further reference see the [docs](https://docs.python.org/3/library/venv.html).

* Step 1: Install the requirements:
	* Update pip with `$ pip install -U pip` 
	* Install the requirements with `$ pip install -r requirements.txt`
* Step 2: Run the application with `$ python3 cluedo.py`. You will see a Tkinter GUI interface displayed.
* Step 3: Play the game:
	* You are Miss Scarlett.
	* Pick a room to visit by clicking on a room in the Tkinter graphical gameboard.
	* Then make a suggestion by entering a numerical value corresponding the room, weapon, and suspect in the terminal
	* Finally, your answer will be compared with the contents of the case file to determine whether or not you are correct.