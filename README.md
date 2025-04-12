# Trailer Movie Analysis App

A Python-based application for analyzing movie trailers using computer vision and audio processing techniques.

## Project Structure

```
.
├── data/                  # Directory to store video files
│   └── sample_trailer.mp4 # Sample trailer video (to be added)
├── outputs/               # Output directory for processed files
│   └── shots/             # Directory for extracted keyframes
├── trailer_analysis.ipynb # Jupyter notebook for analysis
├── shot_boundary_detection.ipynb # Jupyter notebook for shot detection
└── requirements.txt       # Python dependencies
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

5. Open either notebook to analyze the video:
   - `trailer_analysis.ipynb` for general video analysis
   - `shot_boundary_detection.ipynb` for shot detection and segmentation

## Features

- Video metadata extraction (duration, FPS, resolution)
- Audio extraction and waveform visualization
- Frame extraction and display
- Shot boundary detection and keyframe extraction
- Shot timeline visualization
- Modular and well-documented code structure

## Next Steps

This project can be extended to include:
- Deep learning-based shot segmentation
- Scene segmentation (grouping related shots)
- Audio emotion analysis
- Visual style classification
- Character detection
- Trailer structure analysis