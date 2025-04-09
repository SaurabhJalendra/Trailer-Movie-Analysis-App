import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import VideoFileClip
import librosa
import librosa.display
import pandas as pd

print("All imports successful!")
print(f"NumPy version: {np.__version__}")
print(f"Matplotlib version: {plt.__version__}")
print(f"MoviePy version: {VideoFileClip.__module__.split('.')[0]}")
print(f"Librosa version: {librosa.__version__}")
print(f"Pandas version: {pd.__version__}") 