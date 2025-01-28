extentions.
	selenium IDE https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd?hl=en
	chrome driver https://googlechromelabs.github.io/chrome-for-testing/
	
Conventions.
    A. Indentation
	    # Aligned with opening delimiter.
	    foo = long_function_name(var_one, var_two,
	                             var_three, var_four)

	B. Imports
		from subprocess import Popen, PIPE

	C. Whitespace in Expressions and Statements
		spam(ham[1], {eggs: 2})
		foo = (0,)
		ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
		spam(1)
		dct['key'] = lst[index]
		x = 1
		x = x*2 - 1
		def munge(sep: AnyStr = None) -> PosInt:
		def complex(real, imag=0.0):
		if foo == 'blah':
		    do_blah_thing()
		
	D. Naming Conventions
		* 	Non-public method begin with a single underscore
		** 	with words separated by underscores

		Packages
			lowercase

		Module
			lower case

		Class 
			UpperCaseCamelCase
		
		Functions 
			lowercase

		Variable
			lowercase

		Bool Variable
			is_ + lowercase

		Arguments
			lowercase

		Global
			should be all lowercase

		Constant
			fully capitalized

Class Structure
	a. standard Functions
		1. __new__
			deploy Singltone pattern
			add attributte of providers from base classes

		2. __init__
			add field to classes

		3. setup
			place of eager loading

		4. __call__
			call dev-methods and extra methods

		5. prepare
			prepare Attributes

		6. __teardown
			!!!shutdown test in class and create report!!!! I am not sure about it

		7. decorators
			waitfor
				waiting for element visibility in base class (element_for_waiting_until_visible, type_of_element)


Create venv
        python -m venv C:\Users\mpaarmann\MyProjects\rdc_automat\.venv
        Create pth file in C:\Users\mpaarmann\Projects\rdc_automat\.venv\Lib\site-packages\rdc_automat.pth contain(C:\Users\mpaarmann\MyProjects\rdc_automat)
        cd C:\Users\mpaarmann\projects\rdc_automat\.venv\Scripts

		run activate.bat
		pip3 install --upgrade pip


Usefull Commands
		pip3 freeze > requirements.txt
		pip3 uninstall -r requirements.txt

		pip install --force-reinstall  -r requirements.txt
		pip3 install -r requirements.txt

		pip list	
		if get error with no module then 
			1. ctrl+shift+p
			2. venv
			3. add venv


Execute file
		pyinstaller -d all --clean  C:\Users\mpaarmann\Projects\rdc_automat\test_applications\md_365\controler\userstory_pytest.py

install Package
	altgraph==0.17.4
	appdirs==1.4.4
	Appium-Python-Client==3.1.0
	attrs==23.1.0
	auto-py-to-exe==2.44.1
	beautifulsoup4==4.12.3
	blinker==1.7.0
	bottle==0.13.1
	bottle-websocket==0.2.9
	bs4==0.0.2
	certifi==2023.7.22
	cffi==1.16.0
	charset-normalizer==3.3.2
	click==8.1.7
	colorama==0.4.6
	comtypes==1.2.0
	cssselect==1.2.0
	de==0.1
	dict2xml==1.7.3
	Eel==0.17.0
	et-xmlfile==1.1.0
	execnet==2.0.2
	fake-useragent==1.5.1
	ffmpeg-python==0.2.0
	Flask==3.0.3
	future==1.0.0
	gevent==24.2.1
	gevent-websocket==0.10.1
	greenlet==3.1.1
	h11==0.14.0
	idna==3.4
	importlib_metadata==7.1.0
	importlib_resources==6.4.5
	iniconfig==2.0.0
	itsdangerous==2.1.2
	Jinja2==3.1.2
	jsonschema==4.19.1
	jsonschema-specifications==2023.7.1
	lxml==5.2.1
	lxml_html_clean==0.1.1
	MarkupSafe==2.1.3
	MouseInfo==0.1.3
	multithreading==0.2.0
	numpy==1.26.4
	onetimepass==1.0.1
	opencv-python==4.9.0.80
	openpyxl==3.1.2
	outcome==1.3.0
	packaging==23.2
	parse==1.20.1
	pefile==2024.8.26
	pillow==10.3.0
	pluggy==1.3.0
	PyAutoGUI==0.9.54
	pycparser==2.21
	pyee==11.1.0
	PyExecJS==1.5.1
	PyGetWindow==0.0.9
	pyinstaller==6.10.0
	pyinstaller-hooks-contrib==2024.8
	PyMsgBox==1.0.9
	pyodbc==5.0.1
	pyotp==2.9.0
	pyparsing==3.1.4
	pyperclip==1.8.2
	pyppeteer==2.0.0
	pyproject-toml==0.0.10
	PyQt5==5.15.10
	PyQt5-Qt5==5.15.2
	PyQt5-sip==12.13.0
	pyquery==2.0.0
	PyRect==0.2.0
	PyScreeze==0.1.30
	PySocks==1.7.1
	pytest==7.4.2
	pytest-asyncio==0.23.6
	pytest-azurepipelines==1.0.5
	pytest-html==4.0.2
	pytest-metadata==3.0.0
	pytest-nunit==1.0.7
	pytest-xdist==3.3.1
	pytweening==1.2.0
	pywin32==306
	pywin32-ctypes==0.2.3
	pywinauto==0.6.8
	PyYAML==6.0.1
	referencing==0.30.2
	requests==2.31.0
	requests-html==0.10.0
	rpds-py==0.10.6
	selenium==4.14.0
	setuptools==68.2.2
	six==1.16.0
	sniffio==1.3.0
	sortedcontainers==2.4.0
	soupsieve==2.5
	toml==0.10.2
	totp==1.3.0
	tqdm==4.66.2
	trio==0.22.2
	trio-websocket==0.11.1
	typing_extensions==4.11.0
	urllib3==1.26.18
	utils==1.0.2
	w3lib==2.1.2
	websockets==10.4
	Werkzeug==3.0.2
	wheel==0.41.2
	whichcraft==0.6.1
	wsproto==1.2.0
	XlsxWriter==3.2.0
	xlwings==0.31.2
	xmltodict==0.13.0
	zipp==3.18.1
	zope.event==5.0
	zope.interface==7.0.3