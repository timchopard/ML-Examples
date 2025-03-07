# Machine Learning Examples

## Getting Started

### Set up a Virtual Environment

> Note: The instructions below are for using the python venv package and pip.
> There are other package managers available, such as conda.

Using a virtual environment keeps the packages for separate projects separate.
This way, specific version requirements can be met for projects without
interference.

#### Create a new virtual environment

```bash 
python3 -m venv .venv 
```

This will create a ```.venv``` directory containing the virtual environment 
within the current directory.

#### Activate the virtual environment

Run the following command to activate the virtual environment 

```bash
./.venv/bin/activate
```

#### Deactivate the virtual environment 

Run the following command to deactivate the virtual environment 

```bash 
deactivate 
```

### Bash aliases 

In order to speed up creating and activating environments, the following lines 
may be added to ```.bashrc```

```bash
alias newvenv='python3 -m venv .venv && source .venv/bin/activate'
alias actvenv='source .venv/bin/activate'
```
With these two added to your ```.bashrc```, and bash reloaded by running 
```source ~/.bashrc``` you will now be able to create an environment with the
```newvenv``` command and activate the environment within a directory with
```actvenv```.

#### Install packages 

If you have a ```requirements.txt``` file, the packages may be installed with 

```bash
pip install -r requirements.txt 
```

Otherwise they may be installed as normal with ```pip```

# K-Means Clustering

This algorithm clusters data together into $K$ discrete groups with means 


