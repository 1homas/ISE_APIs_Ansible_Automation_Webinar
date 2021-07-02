# Python Virtual Environment and Ansible Installation

## Clone This Repository

```bash
git clone https://github.com/1homas/APIs_Ansible_Automation_ISE_Webinar 
```

## Installation

1. Install Python 3.9 (tested with 3.9.5)

```bash
sudo apt install python3.9.5
```

1. Use the latest version of PIP

```bash
pip3 install --upgrade pip
```

1. Use a virtual environment for Python

```bash
pipenv install --python 3.9
pipenv shell
python --version        # Python 3.9.5+
```

1. Install the ciscoisesdk Python package

```bash
pipenv install ciscoisesdk
```

1. Install Ansible Python package

```bash
pipenv install ansible
```

1. Install cisco.ise Ansible collection

```bash
ansible-galaxy collection install cisco.ise
```


## Environment

Source the `source_me.sh` file to set the prompt and a few environment variables to ignore some warnings.


