import yt_dlp
import os

def download_video(url, format_choice):
    output_folder = os.path.join(os.getcwd(), "videos")
    os.makedirs(output_folder, exist_ok=True)

    if format_choice == 'mp3':
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    elif format_choice == 'mp4':
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
        }
    else:
        print("Invalid format! Please choose either mp3 or mp4.")
        return

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print(f"\n✅ Download complete! Your file is saved in: {output_folder}")

if __name__ == "__main__":
    print("=== YouTube Downloader by Khoa ===")
    url = input("Enter YouTube video URL: ").strip()
    print("Choose download format:")
    print("1. mp4 (video)")
    print("2. mp3 (audio)")
    choice = input("Enter your choice (1/2): ").strip()

    format_choice = 'mp4' if choice == '1' else 'mp3'
    download_video(url, format_choice)

    input("\nPress Enter to exit...")
