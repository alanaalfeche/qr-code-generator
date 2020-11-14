## QR Code Generator
### The purpose of this project is two-fold:
1. To create QR codes for blue apron recipes. User can opt out from receiving physical copy of recipes and instead they receive a list of QR codes that they can scan with their iphone camera, which will redirect them to the digital recipes. 
2. To create QT codes for tips and tricks. If a user needs guidance on how to properly slice an onion, they can scan the QR code on the physical copy of recipe, which will redirect them to a video of a chef showcasing how to properly slice an onion. 

### Installation
1a. Create virtual environment
```
python3 -m venv .env
source .env/bin/activate
```
1b. If using vscode, a prompt will displayed to allow you to select it for the workspace. Then run command+shift+p > select interpreter > select .env

2. Install dependencies
```
pip install -r requirements.txt
```

### Running the program
1. To create the QR codes for blue apron recipes.
```
python qr_generator.py
```
2. To create the QR codes attached to physical copy.
```
python 
```

### Resources:
https://note.nkmk.me/en/python-pillow-qrcode/
https://pypi.org/project/qrcode/