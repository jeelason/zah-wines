# Zah Wines

## Project description
Minimalistc wine brand website displaying splash page, wine descriptions, consultant and contact inquiries. 
Admin access allows for creating new wines to be view in wine list page with ability to edit and delete present wines.
Admin access also can view submissions and mark them as complete.


login by clicking the Fried Chicken icon in the bottom right footer.

## Technologies Used

- Setup and Configuration: \
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![PyPI](https://img.shields.io/badge/PYPI-%231572B6.svg?style=for-the-badge&logo=pypi&logoColor=white)
<!--[NPM](https://img.shields.io/badge/NPM-%23000000.svg?style=for-the-badge&logo=npm&logoColor=white)-->


- Front End Development : \
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

- Back End Development: \
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Sqlite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

- Deployment: \
![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)

## Setup

In your terminal, clone down repository and in root directory run create new python environment.<br />
`python -m venv .venv`

activate the environment<br />
`source .venv/bin/activate`

update pip<br />
`python -m pip install --upgrade pip`

install requirements<br />
`pip install -r requirements.txt`

Run migrations<br />
`python manage.py migrate`

runserver<br />
`python manage.py runserver`

create super user<br />
`python manage.py createsuperuser`

in browser link <br />
`http://localhost:8000`

## App Overview

<div align="center"><br />
    <h3 align="center">Homepage & wine detail list page</h3>
  <img src="https://raw.githubusercontent.com/jeelason/zah-wines/main/ss/z-1.png" alt="homepage" width='40%'/>
  <img src="https://raw.githubusercontent.com/jeelason/zah-wines/main/ss/z-2.png" alt="wine list" width='40%'/><br />
    <h3 align="center">submit new wine while admin, guest submissions</h3>
  <img src="https://raw.githubusercontent.com/jeelason/zah-wines/main/ss/z-3.png" alt="wine form" width='40%' />
    <img src="https://raw.githubusercontent.com/jeelason/zah-wines/main/ss/z-4.png" alt="admin-tasks" width='40%' /><br />
    <h3 align="center">Admin functionality to view and mark inquiries as complete</h3>
    <img src="https://raw.githubusercontent.com/jeelason/zah-wines/main/ss/z-5.png" alt="admin-tasks" width='40%' /><br />
  </div>
