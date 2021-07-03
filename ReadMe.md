# ISE APIs Ansible Automation Webinar

These examples were created for the Cisco Identity Services Engine (ISE) Webinar: **ISE 3.1 APIs, Ansible, and Automation** delivered on July 6, 2021. 

## Cisco DevNet Sandbox

If you are looking for a lab environment to try Ansible with ISE, you may use the Cisco DevNet Sandbox [ISE with Ansible Automation](https://devnetsandbox.cisco.com/RM/Diagram/Index/ad4bb2ae-bb67-4d93-9f0d-2a6a04792e2e?diagramType=Topology) for free!

## Quick Start

Clone this repository to your local lab or sandbox environment.
```bash
git clone https://github.com/1homas/APIs_Ansible_Automation_ISE_Webinar 
```

Install Python 3.9 (tested with 3.9.5)

```bash
sudo apt install python3.9.5
```

Use the latest version of PIP

```bash
pip3 install --upgrade pip
```

Use a virtual environment for Python

```bash
pipenv install --python 3.9
pipenv shell
python --version        # Python 3.9.5+
```

Install the ciscoisesdk Python package

```bash
pipenv install ciscoisesdk
```

Install Ansible Python package

```bash
pipenv install ansible
```

Install cisco.ise Ansible collection

```bash
ansible-galaxy collection install cisco.ise
```


## Environment

Source the `source_me.sh` file to set the prompt and a few environment variables to ignore some warnings.

```bash
source source_me.sh
```

## License

The examples in this repository are licensed under the [Cisco Sample Code License](https://developer.cisco.com/site/license/cisco-sample-code-license/).


