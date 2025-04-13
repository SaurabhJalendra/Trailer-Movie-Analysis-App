# Trailer Movie Analysis App

A Python-based application for analyzing movie trailers using computer vision, audio processing, and emotion detection techniques.

## Overview

This project provides a suite of analysis tools to understand the emotional and structural components of movie trailers. It uses computer vision to detect shot boundaries and facial emotions, audio processing to analyze music and sound, and combines these signals into a comprehensive emotional timeline.

## Project Structure

```
.
├── data/                      # Directory to store video files
│   └── sample_trailer.mp4     # Sample trailer video (to be added)
├── outputs/                   # Output directory for processed files
│   ├── shots/                 # Directory for extracted keyframes
│   ├── shot_emotions.csv      # Facial emotions data
│   ├── audio_analysis.csv     # Audio features data
│   ├── emotion_timeline.csv   # Combined emotion timeline
│   └── feedback_summary.txt   # Generated trailer feedback
├── 01_input_explorer.ipynb    # Basic video/audio extraction
├── 02_shot_detection.ipynb    # Shot boundary detection
├── 03_emotion_detection.ipynb # Facial emotion analysis
├── 04_audio_analysis.ipynb    # Audio feature extraction
├── 05_emotion_timeline.ipynb  # Combined emotional analysis
├── 06_feedback_generator.ipynb # Trailer feedback generation
└── requirements.txt           # Python dependencies
```

## Setup Instructions

1. Create a Python virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Place a sample trailer video file in the `data` directory and name it `sample_trailer.mp4`

4. Launch Jupyter Notebook:
   ```
   jupyter notebook
   ```

5. Run the notebooks in sequence (1-6) for a complete analysis pipeline

## Analysis Pipeline

The trailer analysis is divided into six sequential notebooks, each building on the outputs of the previous ones:

1. **Input Explorer** (`01_input_explorer.ipynb`): 
   - Extracts basic metadata from the trailer (duration, FPS, resolution)
   - Extracts and saves the audio track
   - Displays sample video frames

2. **Shot Detection** (`02_shot_detection.ipynb`):
   - Detects shot boundaries using histogram differencing
   - Saves keyframes from each detected shot
   - Visualizes the shot structure of the trailer

3. **Emotion Detection** (`03_emotion_detection.ipynb`):
   - Uses DeepFace to detect faces in keyframes
   - Classifies facial emotions (happy, sad, etc.)
   - Links emotions to shots and timestamps

4. **Audio Analysis** (`04_audio_analysis.ipynb`):
   - Splits audio into small chunks (2s windows)
   - Analyzes tempo, energy, and silence 
   - Simulates audio emotion classification

5. **Emotion Timeline** (`05_emotion_timeline.ipynb`):
   - Merges facial and audio emotion data
   - Creates a unified emotional timeline
   - Visualizes the emotional journey of the trailer

6. **Feedback Generator** (`06_feedback_generator.ipynb`):
   - Analyzes the emotional arc and structure
   - Scores the trailer on multiple dimensions
   - Generates actionable feedback for improvement
   - Creates a feedback summary report

## Features

- Video metadata extraction (duration, FPS, resolution)
- Audio extraction and waveform visualization
- Shot boundary detection and keyframe extraction
- Facial emotion detection and classification
- Audio feature extraction (tempo, energy, silence)
- Emotional timeline generation
- Comprehensive visualizations:
  - Shot timeline
  - Emotion progression
  - Audio characteristics
  - Correlation between features
- Trailer evaluation and feedback:
  - Narrative flow scoring
  - Emotional engagement assessment
  - Pacing and energy analysis
  - Predictability measurement
  - Specific improvement suggestions

## Applications

This analysis pipeline can be used for:
- Trailer editing and optimization
- Emotional impact assessment
- Audience engagement prediction
- Genre and style analysis
- Comparative analysis between trailers
- Marketing strategy development
- Automated feedback generation

## Dependencies

Key libraries used:
- OpenCV (video processing)
- MoviePy (video/audio manipulation)
- DeepFace (facial emotion detection)
- Librosa (audio analysis)
- Pandas/NumPy (data processing)
- Matplotlib/Seaborn (visualization)
- scikit-learn (data normalization and analysis)