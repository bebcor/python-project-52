### Hexlet tests and linter status:
[![Actions Status](https://github.com/bebcor/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/bebcor/python-project-52/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=bebcor_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=bebcor_python-project-52)
[![Python CI](https://github.com/bebcor/python-project-52/actions/workflows/pyci.yml/badge.svg)](https://github.com/bebcor/python-project-52/actions/workflows/pyci.yml)

Project: Task Manager
Task Manager is an application designed to task tracking.

### Requirements
|     Tools      | Version |
|:--------------:|:-------:|
|     Python     | ^3.13.0 |
|     Django     |  ^5.2   |
|     gunicorn   | ^23.0.0 |


### Installation  & Launching
1. Clone the repo:
```bash
git clone https://github.com/bebcor/python-project-52.git
cd python-project-52
```
2. Install dependencies:
```bash
make install
```
3. Create `.env` file in the root directory:
```bash
SECRET_KEY=your_secret_key
DEBUG=True  # Set to False in production
DATABASE_URL=postgresql://username:password@localhost:5432/dbname
```
Replace username, password, dbname, and your_secret_key with your own values.

4. Build & Run the application:
```bash
make build
make start
```

The application will be available at: http://localhost:8000

### ❤️ Acknowledgements
Thanks for stopping by, buddy! If you find this tool helpful, don't forget to give it a ⭐ on GitHub!
