import os
import warnings
warnings.filterwarnings("ignore")

from helper import load_env
load_env()

from crewai import Agent, Task, Crew

os.environ['OPENAI_MODEL_NAME'] = 'gpt-4o-mini'