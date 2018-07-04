### Set-up of virtual environment
Adapt uses libraries which should be isolated from main python installation using a virtual environment as follows.

Traverse to the folder where you want to install the adapt.
Then follow these steps to set up the virtual env and install adapt libraries.
```
virtualenv myvirtualenv
. myvirtualenv/bin/activate
pip install -e git+https://github.com/mycroftai/adapt#egg=adapt-parser
```
*.(dot) command is similar to `source` command to execute a source code file within the same shell. Here, it starts the python virtual environment.*

### Chatbot setup
1. Copy `mycroft_chatbot_demo.py` to your local machine.
2. Execute while inside the python virtual env: `(myvirtualenv)` shows in shell prompt.
3. Run using:
```
python mycroft_chatbot_demo.py
```
