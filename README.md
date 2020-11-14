## QR Code Generator
### The purpose of this project is two-fold:
1. Create QR codes for blue apron recipe cards. User can opt out from receiving physical copy of recipe cards and instead they receive a list of QR codes that they can scan with their iphone camera, which will redirect them to digital recipe cards. This helps the environment, and it's cost saving for BA. Win - win! 
2. Create QR codes for tips and tricks to include in physical recipe cards. If a user needs guidance on how to properly chop scallions, they can scan the QR code found on the right-bottom corner of the recipe card, which will redirect them to a help-video. This provides an illusion to customer that we are with them, helping them in real-time. Moreover, the BA Youtube Channel can gain viewers. Win - win! 

### Other ideas with QR Codes:
1. Create traceability of where ingredients come from. Customers can hover over the produce QR codes, which can link them to the produce history -- where it came from, when it was harvested, etc. This can greatly showcase the `farm-to-table` feel that BA currently offers.

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
1. To create the QR codes for digital recipe cards, 
- Add recipe_name:recipe_hyperlink to recipes_links.py
- Then run:
```
python3 digital_recipes_qr_generator.py
```
- This generates the QR codes for digital recipes in the digital_recipes_qr_code/ folder. 
- Go to digital_recipes_qr_code/, select any png file, open the camera app in your phone, and hover over the QR code. 
- For example, hover over the two qr codes below to take you to general tso chicken digital recipe card:
![alt text](digital_recipes_qr_code/general_tso_chicken_qr_code_inverted.png)
![alt text](digital_recipes_qr_code/general_tso_chicken_qr_code.png)

2. To attach tips and tricks QR codes to a physical recipe card,
- Add tips_and_tricks_name:tips_and_tricks_hyperlink to tips_and_tricks_links.py
- Then run:
```
python3 physical_recipes_qr_generator.py
```
- This generates the tips and tricks QR codes for physical recipes in the physical_recipes_qr_code/folder.
- Go to physical_recipes_qr_code/, select any file with `_qr_code`, open the camera app in your phone, and hover over the QR code in the right-bottom corner.
- For example, hover over the QR code located in the right-botoom corner of the cheesy chipotle beef recipe below, and the link should take you to 'How To: Chop Scallions' Youtube link:
![alt text](physical_recipes_qr_code/cheesy_chipotle_beef_qr_code.jpg)

### Resources:
- https://note.nkmk.me/en/python-pillow-qrcode/
- https://pypi.org/project/qrcode/