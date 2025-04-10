import json
import os

# Define the notebook content
notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Movie Trailer Analysis Notebook\n",
                "\n",
                "This notebook performs basic analysis of movie trailers, extracting and visualizing key information such as:\n",
                "- Video duration, FPS, and resolution\n",
                "- Audio tracks\n",
                "- Video frames\n",
                "\n",
                "This provides a foundation for more advanced AI-based movie analysis."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 1. Setup and Dependencies\n",
                "\n",
                "First, we'll import the necessary libraries for video and audio processing."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Import libraries\n",
                "import os\n",
                "import numpy as np\n",
                "import matplotlib.pyplot as plt\n",
                "from moviepy.editor import VideoFileClip\n",
                "import librosa\n",
                "import librosa.display\n",
                "import cv2\n",
                "\n",
                "# Configure matplotlib for better display in notebook\n",
                "%matplotlib inline\n",
                "plt.rcParams['figure.figsize'] = (12, 6)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Load Video File\n",
                "\n",
                "Using MoviePy to load the sample trailer video file."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# File paths\n",
                "video_path = 'data/sample_trailer.mp4'\n",
                "audio_output_path = 'outputs/sample_audio.wav'\n",
                "\n",
                "# Check if video file exists\n",
                "if not os.path.exists(video_path):\n",
                "    print(f\"Error: Video file '{video_path}' not found.\")\n",
                "    print(\"Please place a sample trailer video in the data directory.\")\n",
                "else:\n",
                "    # Load the video file\n",
                "    video_clip = VideoFileClip(video_path)\n",
                "    print(f\"Successfully loaded video: {video_path}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3. Video Metadata Analysis\n",
                "\n",
                "Extracting and displaying key metadata from the video."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "try:\n",
                "    # Extract video metadata\n",
                "    duration = video_clip.duration\n",
                "    fps = video_clip.fps\n",
                "    width, height = video_clip.size\n",
                "    \n",
                "    # Display the metadata\n",
                "    print(\"Video Metadata:\")\n",
                "    print(f\"Duration: {duration:.2f} seconds\")\n",
                "    print(f\"FPS: {fps:.2f}\")\n",
                "    print(f\"Resolution: {width} × {height} pixels\")\n",
                "except Exception as e:\n",
                "    print(f\"Error extracting video metadata: {e}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 4. Extract and Save Audio\n",
                "\n",
                "Extracting the audio track from the video and saving it as a WAV file."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "try:\n",
                "    # Extract audio from video\n",
                "    audio_clip = video_clip.audio\n",
                "    \n",
                "    # Save audio to WAV file\n",
                "    audio_clip.write_audiofile(audio_output_path)\n",
                "    \n",
                "    print(f\"Audio successfully extracted and saved to: {audio_output_path}\")\n",
                "except Exception as e:\n",
                "    print(f\"Error extracting audio: {e}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 5. Visualize Audio Waveform\n",
                "\n",
                "Loading the extracted audio and visualizing its waveform using Librosa."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "try:\n",
                "    # Load the audio file using librosa\n",
                "    y, sr = librosa.load(audio_output_path, sr=None)\n",
                "    \n",
                "    # Get audio duration\n",
                "    audio_duration = librosa.get_duration(y=y, sr=sr)\n",
                "    \n",
                "    print(f\"Audio loaded: {len(y)} samples, sample rate: {sr} Hz\")\n",
                "    print(f\"Audio duration: {audio_duration:.2f} seconds\")\n",
                "    \n",
                "    # Plot the waveform\n",
                "    plt.figure(figsize=(14, 5))\n",
                "    librosa.display.waveshow(y, sr=sr)\n",
                "    plt.title('Audio Waveform')\n",
                "    plt.xlabel('Time (s)')\n",
                "    plt.ylabel('Amplitude')\n",
                "    plt.tight_layout()\n",
                "    plt.show()\n",
                "except Exception as e:\n",
                "    print(f\"Error visualizing audio: {e}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 6. Extract and Display Video Frame\n",
                "\n",
                "Extracting and displaying the first frame of the video."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Extract frame using MoviePy\n",
                "try:\n",
                "    # Get the first frame (at time t=0)\n",
                "    first_frame = video_clip.get_frame(0)\n",
                "    \n",
                "    # Display the frame\n",
                "    plt.figure(figsize=(10, 8))\n",
                "    plt.imshow(first_frame)\n",
                "    plt.title('First Frame of Video')\n",
                "    plt.axis('off')\n",
                "    plt.tight_layout()\n",
                "    plt.show()\n",
                "    \n",
                "    # Save the frame as an image\n",
                "    plt.imsave('outputs/first_frame.jpg', first_frame)\n",
                "    print(\"First frame saved as 'outputs/first_frame.jpg'\")\n",
                "except Exception as e:\n",
                "    print(f\"Error extracting frame: {e}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 7. Clean Up Resources\n",
                "\n",
                "Properly close and release all resources."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Close the video clip to release resources\n",
                "try:\n",
                "    video_clip.close()\n",
                "    print(\"Video clip resources released.\")\n",
                "except Exception as e:\n",
                "    print(f\"Error closing video clip: {e}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 8. Conclusion\n",
                "\n",
                "This notebook demonstrates basic movie trailer analysis techniques including:\n",
                "- Extracting video metadata (duration, FPS, resolution)\n",
                "- Separating and analyzing audio tracks\n",
                "- Extracting video frames\n",
                "\n",
                "These foundational techniques can be expanded for more advanced AI-based movie analysis, such as:\n",
                "- Scene detection and segmentation\n",
                "- Visual style analysis\n",
                "- Audio emotion detection\n",
                "- Character recognition\n",
                "- Pattern identification across different trailers"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.8.10"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# Write the notebook to file
with open('trailer_analysis.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=2)

print("Jupyter notebook 'trailer_analysis.ipynb' created successfully.") 