from pathlib import Path
from pytubefix import YouTube
import subprocess
import re

video_dir = Path('Video')
video_dir.mkdir(parents=True,exist_ok=True)
audio_dir = Path('Audio')
audio_dir.mkdir(parents=True,exist_ok=True)

def download_video_with_audio(link):
    video = YouTube(link)
    
    #Get only video
    video_streams = video.streams.filter(
        only_video=True,
        file_extension='mp4'
    ).order_by('resolution').desc()

    if not video_streams:
        print("Compatible video and audio format not found")
        return

    #Get audio streams
    audio_streams = video.streams.filter(
        only_audio=True
    ).order_by('abr').desc()

    if not audio_streams:
        print("Compatible audio not found")
        return

    print(f"--- Available Video Options for: {video.title}")

    for index,stream in enumerate(video_streams):
        size = stream.filesize / (1024 * 1024)

        print(
            f"{index} - {stream.resolution} "
            f"| {stream.fps} FPS "
            f"| {size:.2f}"
        )
    try:
        option = int(input("Select a video option --> "))
        if not 0 <= option < len(video_streams):
            print("Invalid option")
            return

        selected_video = video_streams[option]
        selected_audio = audio_streams[0]
        
        print("[1 / 2] Downloading video ...")
        download_video = selected_video.download(
            output_path = str(video_dir)
        )
        video_path = Path(download_video)

        print("[2 / 2] Downloading audio ...")
        download_audio = selected_audio.download(
            output_path = str(audio_dir)
        )
        audio_path = Path(download_audio)

        #Final Mp4 path
        final_video_path = video_path.with_name(f"{video.title}_video.mp4")

        #Merge video and audio with FFmpeg
        print("Merging video and audio ...")

        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-i", str(video_path),
                "-i", str(audio_path),
                "-c:v", "copy",
                "-c:a", "aac",
                str(final_video_path)
            ],
            check=True
        )
        video_path.unlink()
        audio_path.unlink()
        print(f"Download Completed: {final_video_path}")
        
    except ValueError as e:
        print(f"ValueError: {e}")
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg error: {e}")
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}")

def download_video(link):
   video = YouTube(link)
   video_stream = video.streams.filter(
        only_video=True,
        file_extension='mp4'
    ).order_by('resolution').desc()

   if video_stream:
       print("Video found")
   else:
       print("Compatible format not found")

   print("Available Resolutions") 
   for index,stream in enumerate(video_stream):
       print(f"{index} - {stream.resolution} | {stream.fps} FPS")

   option = int(input("Select the video option --> "))

   if 0 <= option < len(video_stream):
        selected_stream = video_stream[option]
        print("Downloading video ...")
        selected_stream = selected_stream.download(
            output_path = str(video_dir)
        )
        print("Download Completed")
   else:
       print("Invalid Option")


def download_audio(link):
    video = YouTube(link)

    audio_streams = video.streams.filter(
        only_audio=True).order_by('abr').desc()

    if not audio_streams:
        print("Compatible audio format not found")
        return
    print(f"\nAvailable Audio Options for: {video.title}")
    for index,stream in enumerate(audio_streams):
        size = stream.filesize / (1024 * 1024)

        print(
            f"{index} - {stream.abr} | {stream.mime_type} | {size:.2f} MB"
        )
    try:
        option = int(input("\nSelect an audio option -->"))

        if not 0 <= option < len(audio_streams):
            print("Invalid option")
            return

        selected_stream = audio_streams[option]

        print("\n Downloading Audio ...")

        # Downloaded original Audio
        downloaded_audio = selected_stream.download(
            output_path = str(audio_dir)
        )
        audio_path = Path(downloaded_audio)

        #Convert to mp3
        mp3_path = audio_path.with_suffix(".mp3")
        print("Converting audio to MP3 ...")

        #Convert using FFmpeg
        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-i", str(audio_path),
                "-vn",
                "-codec:a","libmp3lame",
                "-q:a", "2",
                str(mp3_path)
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        audio_path.unlink()
        print(f"Download Completed: {mp3_path}")
        
    except ValueError:
        print("Please Enter a valid number")    
    except FileNotFoundError:
        print("FFmpeg was not found")
    except subprocess.CalledProcessError:
        print("Error converting audio to mp3")
    

##Main Menu

while True:
    print("----------")
    print("Menu")
    print("1 - Video and audio")
    print("2 - ONLY video")
    print("3 - ONLY audio")
    print("0 - Exit")

    try:
        menu_option = int(input("---- Select an Option -->"))
    except ValueError:
        print("Invalid input. Please enter a number")
        continue
    if menu_option == 0:
        print("Exiting ... Goodbye! :D")
        break

    if menu_option not in (1,2,3):
        print("Wrong option, try again")
        break

    link = input("Place the video URL here --> ")

    match menu_option:
        case 1:
            print("--- Video and Audio ---")
            download_video_with_audio(link)
        case 2:
            print("--- Only Video ---")
            download_video(link)
        case 3:
            print("--- Only Audio ---")
            download_audio(link)
