# YouTube Video Downloader
> **Note:** It works with Youtube videos and Shorts.
A simple Python application that allows you to download videos and audio from YouTube. It uses [Pytubefix](https://github.com/JuanBindez/pytubefix) to retrieve media streams and [FFmpeg](https://ffmpeg.org/) to merge video and audio or convert audio files to MP3.

## Features

- **Video and Audio:** Download video and audio separately and merge them into a single MP4 file.
- **Only Video:** Download a video without audio, choosing the desired resolution.
- **Only Audio:** Download audio and convert it to MP3.

## Requirements

Before running the project, make sure you have the following installed:

- Python 3.10 or higher
- FFmpeg
- Pytubefix

### Python Dependencies

The project uses the following Python library:

- [Pytubefix](https://github.com/JuanBindez/pytubefix): Used to retrieve and download video and audio streams from YouTube.

Other modules used in the project (`pathlib`, `subprocess` and `re`) are part of Python's standard library.

### FFmpeg

[FFmpeg](https://ffmpeg.org/) is required to:

- Merge separate video and audio streams into an MP4 file.
- Convert downloaded audio files into MP3 format.

> **Important:** FFmpeg is an external program, not a Python package. It must be installed separately and accessible through your system's `PATH`.
---

<p align="center">
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2JiZmR5YjFzYTBtZDd3c2I4Z28zdGt1bnpjdnJyc3Z5ZWkybWNvMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gXXFrjHFJIMoqKr8UT/giphy.gif" alt="Dancing cat GIF" width="300px" height="300px">
</p>
