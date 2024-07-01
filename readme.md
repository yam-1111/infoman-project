<h1 align="center"> CSC Personal Data Sheet Management System </h1>

Created and developed by the BSCS 2-1 Group 1 for Information Management. The CSC Personal Data Sheet Management System is a web-based application designed to streamline the collection and management of personal data sheets for the CSC (Civil Service Commission). This system offers functionalities for both administrators and applicants:

## 💼 Project Functionality

* Applicants: Applicants can conveniently register and submit their personal data sheets electronically. They also have the ability to edit and update their submitted information for accuracy.

* Administrators: Administrators have full CRUD (Create, Read, Update, Delete) capabilities for managing applicant data sheets. This includes adding new admins, viewing submitted forms, editing existing information, and deleting records as needed.

## 💻 Technology Used

* Python and Flask (Backend API of the website)
* HTML, CSS and JS (Frontend of the website)
* Daisy Ui, Bootstrap 5 and FontAwesome Icons (Frontend framework)
* HTMX


<p align="left">
 <!---Python--->
  <a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg" width="40" height="40"/> </a> <a><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg" width="40" height="40"/></a> <a> <img src="https://img.daisyui.com/images/daisyui-logo/daisyui-logomark-1024-1024.png" width="40" height="40"> <a><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flask/flask-original.svg" width="40" height="40"/><a><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/figma/figma-original.svg" width="40" height="40"/></a>

</p>

## 🛠️ Usage

### If the virtual environment is not set up, run the following command:
```
python3 -m venv .venv
```

### Entering the virtual environment

#### Windows

```
.\venv\Scripts\activate
```

#### Linux / Unix / Mac

```
source .venv/bin/activate
```

### Installing pre-requisties library

```
pip install -r requirements.txt
```
### setting up the database

Create a `.env` file on your root directory, not in the `/src`
please follow the format on `.env.example`

```
SECRET_KEY=<any_secret_key>
ADMIN_EMAIL=<admin_email>
ADMIN_PASSWORD=<admin_password>

DB_PORT=3306
DB_HOST=localhost
DB_NAME=<awesome_db_name>
DB_USERNAME=<username>
DB_PASSWORD=<password>
```


## 👨 👩 Members

* [Anthony John Hinay](https://github.com/yam-1111)

* Aira Jayoma

* Kristina Amor Marzan

* Joanna Salvador