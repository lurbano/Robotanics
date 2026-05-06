create virtual environment
> python3 -m venv .venv
> source .venv/bin/activate

install plantcv 
> pip install plantcv


Testing: test.py
https://plantcv.org/tutorials/simple-rgb-workflow
 

With Anaconda
get anaconda
> curl -O https://repo.anaconda.com/archive/Anaconda3-2025.12-2-Linux-x86_64.sh
install
> bash ~/Anaconda3-2025.12-2-Linux-x86_64.sh

Manual fix for Bash: Add this line to your ~/.bashrc file:
export PATH="~/anaconda3/bin:$PATH".
then
> source ~/.bashrc


Install conda environment for plantcv
> conda create -n plantcv -c conda-forge plantcv jupyterlab ipympl nodejs

Stop auto activitating conda base
> conda config --set auto_activate_base false

Activate plantcv
> conda activate plantcv


To Do
- Lights
- Turntable to rotate plant for photographs
