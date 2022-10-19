[![Build Status](https://runbot.odoo.com/runbot/badge/flat/1/master.svg)](https://runbot.odoo.com/runbot)
[![Tech Doc](https://img.shields.io/badge/master-docs-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/documentation/15.0)
[![Help](https://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/forum/help-1)
[![Nightly Builds](https://img.shields.io/badge/master-nightly-875A7B.svg?style=flat&colorA=8F8F8F)](https://nightly.odoo.com/)

Odoo
----

Odoo is a suite of web based open source business apps.

The main Odoo Apps include an <a href="https://www.odoo.com/page/crm">Open Source CRM</a>,
<a href="https://www.odoo.com/app/website">Website Builder</a>,
<a href="https://www.odoo.com/app/ecommerce">eCommerce</a>,
<a href="https://www.odoo.com/app/inventory">Warehouse Management</a>,
<a href="https://www.odoo.com/app/project">Project Management</a>,
<a href="https://www.odoo.com/app/accounting">Billing &amp; Accounting</a>,
<a href="https://www.odoo.com/app/point-of-sale-shop">Point of Sale</a>,
<a href="https://www.odoo.com/app/employees">Human Resources</a>,
<a href="https://www.odoo.com/app/social-marketing">Marketing</a>,
<a href="https://www.odoo.com/app/manufacturing">Manufacturing</a>,
<a href="https://www.odoo.com/">...</a>

Odoo Apps can be used as stand-alone applications, but they also integrate seamlessly so you get
a full-featured <a href="https://www.odoo.com">Open Source ERP</a> when you install several Apps.

Getting started with Odoo
-------------------------

For a standard installation please follow the <a href="https://www.odoo.com/documentation/15.0/administration/install.html">Setup instructions</a>
from the documentation.

To learn the software, we recommend the <a href="https://www.odoo.com/slides">Odoo eLearning</a>, or <a href="https://www.odoo.com/page/scale-up-business-game">Scale-up</a>, the <a href="https://www.odoo.com/page/scale-up-business-game">business game</a>. Developers can start with <a href="https://www.odoo.com/documentation/15.0/developer/howtos.html">the developer tutorials</a>


System workflow




Customized odoo15 project will be hosted on server (refer below)
Database will be hosted on server
Pos can be accessed on server ip address i.e 192.168.1.203 or 192.168.1.203:8069.
On port 80 i.e. 192.168.1.203 will be handled by nginx which is the proxy server of odoo server running on port 8069.
To get barcode and weights there is a separate service build on Fast api.
 Wkhtmltox-0.12.6-1.msvc2015-win32.exe will be install on server side.









Install [SOP] Customized (by Vervebot) Odoo


System Preparation


Visual c++ 14.0 or higher

Postgres (12-14)
Odoo files from project
Python 3.8 python-3.8.10-amd64.exe
Virtualenv
For Windows 
	Install wkhtmltox-0.12.6-1.msvc2015-win32.exe
	Set environment variable C:\Program Files (x86)\wkhtmltopdf\bin
	Restart system and check in cmd typing wkhtmltopdf

Installation
Backup  Demo working database in directory format and restore it in new server
Set binary path in pgadmin4 
Go to file > preference > binary path
Add path C:\Program Files\PostgreSQL\14\bin	
				Or 
Get Latest backup file from working db and user odoo interface to restore it.

		
All files from demo servers must be transfer to production server
Run by command 
python odoo-bin -d {{db name}} -r {{db username}}  -w {{db password}} -i -init
OR
python odoo-bin --db_host={{server ip}} --db_port=5432 -d {{db name}} -r {{db username}}  -w {{db password}} -i -init
Check Login And Other Functionalities


Connect all system in same network using local IP

Search Windows Defender Firewall
Click on Advance Options
Click on Inbounds rule
Enable the following rule
File and Printer Sharing (Echo Request- ICMPv4-In) Domain
File and Printer Sharing (Echo Request- ICMPv4-In) Private
File and Printer Sharing (Echo Request- ICMPv6-In) Domain
File and Printer Sharing (Echo Request- ICMPv6-In) Private
Add Inbound Rule for specific Port

Configure 5432 (Postgres port)

References:-
 HowTo Safely Open a PostgreSQL Port for Remote Access? 
Enable incoming " PING " in Windows 10 | NETVN






API For Barcode and weight scale

Open FastAPI Project 
Install required modules by running command pip install -r requirements.txt
Locate file web_server.py
Type command uvcorn web_server:app
Getting Error!
Install and double check all required modules and you are done
Connect Device
Check for response from device
Customize code in  web_server.py according to device
Create and install service in windows
Visit 127.0.0.1:8055 for response


