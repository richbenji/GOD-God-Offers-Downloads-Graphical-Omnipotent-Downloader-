from src.ui_main import YouTubeDownloader
from src.check_yt_dlp_update import check_yt_dlp_update

def main():
    app = YouTubeDownloader()
    app.mainloop()

if __name__ == "__main__":
    check_yt_dlp_update()
    main()
