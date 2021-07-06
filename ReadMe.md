# ISE APIs, Ansible, and Automation Webinar

These examples were created for the Cisco Identity Services Engine (ISE) Webinar: **ISE 3.1 APIs, Ansible, and Automation** delivered on July 6, 2021. 

## Cisco DevNet Sandbox

If you are looking for a lab environment to try Ansible with ISE, you may use the Cisco DevNet Sandbox [ISE with Ansible Automation](https://devnetsandbox.cisco.com/RM/Diagram/Index/ad4bb2ae-bb67-4d93-9f0d-2a6a04792e2e?diagramType=Topology) for free!

## Quick Start

Clone this repository to your local lab or sandbox environment :  
```bash
git clone https://github.com/1homas/APIs_Ansible_Automation_ISE_Webinar.git
```

Install Python 3.9 (tested with 3.9.5) :  

```bash
sudo apt install python3.9.5
```

Use the latest version of PIP :  

```bash
pip3 install --upgrade pip
```

Use a virtual environment for Python :  

```bash
pipenv install --python 3.9
pipenv shell
python --version        # Python 3.9.5+
```

Install the `ciscoisesdk`, `ansible`, and `jmespath` Python packages :  

```bash
pipenv install ciscoisesdk
pipenv install ansible
pipenv install jmespath
```

Install the `cisco.ise` Ansible collection:  

```bash
ansible-galaxy collection install cisco.ise
```

Install the `community.general` Ansible collection to take advantage of `json_query` and other filters :  

```bash
ansible-galaxy collection install community.general
```

To install a specific version of the `cisco.ise` collection, use `:` followed by range identifiers (`*` (latest/default), `!=`, `==`, `>=`, `>`, `<=`, `<`)

```bash
ansible-galaxy collection install cisco.ise:==0.0.7
```

To check for upgrades to the `cisco.ise` Ansible collection, use :  

```bash
ansible-galaxy collection install cisco.ise --upgrade
```

View the list of installed Ansible modules and versions :  

```bash
ansible-galaxy collection list
```

## Environment

Source the `source_me.sh` file to set the prompt and a few environment variables to ignore some warnings.

```bash
source source_me.sh
```

## License

The examples in this repository are licensed under the [Cisco Sample Code License](https://developer.cisco.com/site/license/cisco-sample-code-license/).


