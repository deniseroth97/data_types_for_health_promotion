# Setup Python with Anaconda

## About Anaconda

To set up our Python session, we will use [*Anaconda*](https://www.anaconda.com/). According to Wikipedia [Wikipedia](https://en.wikipedia.org/wiki/Anaconda_(Python_distribution)), Anaconda is:

	… a distribution of the Python and R programming languages designed for scientific computing, with the goal of simplifying package management and deployment.
It includes a variety of data science packages and is compatible with Windows, Linux, and macOS.

If you ask [ask ChatGPT](https://chat.openai.com/share/958fe6cc-b411-43e5-b156-23fb6ef4fb3f) why Anaconda is particularly useful for teaching data science-related topics, you’ll find that:

	1.	Conda, Anaconda’s package manager, makes it easy to install, update, and manage various data science libraries and tools.
	2.	Anaconda is available across multiple operating systems (Windows, macOS, and Linux), making it accessible to a wide range of students.
	3.	It allows users to create isolated virtual environments, preventing dependency conflicts when working on multiple projects.
	4.	Anaconda includes Jupyter Notebook, a widely used tool for interactive coding, documentation, and visualization, making it ideal for both learning and collaboration.

## Setup instructions

To set up Anaconda for our course, follow these four steps:
	1.	Install Anaconda on your system.
	2.	Verify the installation by ensuring that both Python and Conda are ready to use.
	3.	Create a new Conda environment for the course.
	4.	Install the required packages within your Conda environment.

### 1. Install Anaconda

We recommend manual installation.
For this, you need to download the installer for your operation system (Windows or macOS), and then run the installer to configure Anaconda for use on your computer 

#### Windows


Download the Anaconda installer from: [Anaconda Download for Windows](https://www.anaconda.com/download#windows)

Once downloaded, follow the step-by-step instructions in these guides:
	•	[DataCamp: Installing Anaconda on Windows](https://www.datacamp.com/tutorial/installing-anaconda-windows) 
	•	[Anaconda Documentation: Windows Installation Guide](https://docs.anaconda.com/free/anaconda/install/windows/)

Notes:
	1.	The screenshots in the first guide may be slightly outdated, but the instructions are still accurate.
	2.	In step six of the DataCamp guide, choose the “Alternative Approach”, which automatically adds Anaconda to your PATH variable during installation.

#### Mac

Download the Installer from https://www.anaconda.com/download#macos or 
follow the instructions in ['setup_macos.md'](./setup_macos.md)

*Notes:* 

- If your computer has an M1/M2/3 chip, choose "Download for Mac (M1/M2/3)". Otherwise, choose "Download for Mac (Intel)"
- If you *don't know* whether your Mac has an M1 or M2 chip (a.k.a "Apple Silicon"), follow these instructions to find out: https://www.howtogeek.com/706226/how-to-check-if-your-mac-is-using-an-intel-or-apple-silicon-processor

With the installer downloaded, the following two links provide detailed follow-up instructions: 

- https://www.datacamp.com/tutorial/installing-anaconda-mac-os-x
- https://docs.anaconda.com/free/anaconda/install/mac-os/

**_Important note:_** When asked to select the destination of the installation (step 4 in the second link), please choose "Install for me only" (e.g., use your Application folder)

### 2. Verify your Anaconda installation

follow the instructions here: https://docs.anaconda.com/free/anaconda/install/verify-install/

### 3. Create a new conda environment

#### Using the Anaconda Navigator app

The  Anaconda Navigator app should have open when you finished your Anaconda installation.
If not, open it from your applications (see [here](https://docs.anaconda.com/free/navigator/getting-started/#navigator-starting-navigator) for instructions).

Then, follow the instructions [here](https://docs.anaconda.com/free/navigator/tutorials/create-python35-environment/),  taking into account the following notes:

- in step 4, use 'data_types_for_health_promotion' as environment name
- in step 5, use the python version that starts with '3.12'
- in step 7, choose "open Terminal" and go to the next step of our setup process 

#### Using the command line

- on Windows: Open the Anaconda Prompt
- on macOS: Open the Terminal app

To create a new conda environment, run the following lines:

**_Note:_** If you are a Mac user and your MacBook has an M1, M2, or M3 chip, put `CONDA_SUBDIR=osx-arm64` in front of `conda create` when running the code below

```shell
conda create --name data_types_for_health_promotion python=3.12 pip

conda activate data_types_for_health_promotion
```


- The part after `--name` is the name of the environment. So our new environment is called 'advanced_text_analysis'
- `python=3.11` specifies that we want to use python version 3.11 in this environment
- `pip` specifies that we want to pre-install pip

### 4. Install required pacakages

In the Anaconda Prompt (Windows)/Terminal (macOS),

```shell
# install Jupyter Notebooks
conda install -y notebook ipywidgets

# install all required packages in the correct versions
pip install -r https://raw.githubusercontent.com/deniseroth97/data_types_for_health_promotion/main/setup/requirements.txt
```

## Errors and issues

If you encounter any issues, email at denise.roth@wur.nl. 
