# 🎓 Tutorial – GOD (God Offers Downloads)

## 🚀 Introduction

Welcome to the application tutorial! This app allows you to download YouTube videos and playlists in video or audio format, with support for private playlists.

The application offers two main modes:

- 📥 **Simple Download**: to manage videos one by one (or playlists)
- 📋 **Batch Download**: to download multiple URLs at once

------

## 📥 Simple Download

1. **Copy the URL** of the YouTube video 🔗

2. **Paste it** into the URL field

3. **Click** on the "➕ Check" button

4. **Wait** for the video information to load (thumbnail, duration, size)

   **Select** your options:

   - 🎥 **Video**: choose the resolution (Best, 2160p, 1440p, 1080p, 720p, 480p, 360p, 240p, 144p)
   - 🎵 **Audio only**: choose the bitrate (Best, 320, 256, 192, 128, 96, 64, 32 kbps) and format (M4A or MP3)

   **Click** on "⬇️ Download"

   **Select** the destination folder

### Tips 💡

- You can **add multiple videos** to the queue before starting the download
- The **total size** and number of videos are displayed on the download button
- Use the **🗑️ Clear queue** button to remove all pending videos
- Click the **ℹ️** button next to each video to see detailed information (available formats, description, etc.)
- Click **❌** to remove a video from the queue

------

## 📚 Playlists

### Public playlists

Simply copy the playlist URL into the "Simple Download" tab, the application will automatically detect all videos! You can modify the video/audio options before starting the download.

The application:

- ✅ Automatically loads all playlist videos
- ✅ Displays a thumbnail and information for each video
- ✅ Allows you to customize options for each video individually
- ✅ Downloads everything in a single operation

### 🍪 Private playlists

#### Method 1: Automatic browser connection (Recommended ⭐)

**The application automatically uses your Firefox cookies if you're logged into YouTube!**

1. **Log in** to your YouTube account in Firefox
2. **Copy** your private playlist URL
3. **Paste it** into the application
4. ✅ **It works automatically!** The application accesses your Firefox cookies

> 💡 **Tip**: Stay logged into YouTube in Firefox so the application can always access your private playlists without additional steps.

#### Method 2: Manual cookie export (Alternative)

If the automatic method doesn't work or if you use another browser, you must provide your **YouTube cookies**:

1. Install a browser extension:
   - **Firefox**: [cookies.txt](https://addons.mozilla.org/en/firefox/addon/cookies-txt/) or [get cookies](https://addons.mozilla.org/en/firefox/addon/get_cookies/)
   - **Chrome**: [Get cookies.txt LOCALLY](https://chrome.google.com/webstore)
2. Log in to YouTube
3. **Export** your cookies in Netscape format (`.txt` file)
4. **Click** on the "🍪 ⬆️ cookies.txt" button at the top left of the application
5. **Select** your `cookies.txt` file
6. **Test** with your private playlist

> ⚠️ **Warning**: Never share your cookies.txt file, it contains your login credentials!

### ⚠️ Tips

- Don't delete the cookies.txt file
- If an error appears, reload the cookies

------

## 📦 Batch Download

The "Batch Download" tab allows you to download multiple videos with the **same settings** for all.

### Usage

1. **Open** the "Batch Download" tab
2. **Enter** video URLs (one per line) in the text area
   - OR click "⬆️ Load from file" to import a `.txt` file containing your URLs
3. **Select** the type:
   - 🎥 **Video**: with common resolution for all
   - 🎵 **Audio only**: with common bitrate for all
4. **Choose** the resolution (if video) and audio bitrate
5. **Click** on "⬇️ Download"
6. **Select** the destination folder

### Difference with simple download

| Simple Download                       | Batch Download                |
| ------------------------------------- | ----------------------------- |
| **Customized** options per video      | **Identical** options for all |
| Displays thumbnails and detailed info | Simplified interface          |
| Ideal for a few varied videos         | Ideal for many similar videos |

------

## ⚙️ Advanced Options

### Video resolution

| Resolution          | Recommended usage                 | Approximate size (1h) |
| ------------------- | --------------------------------- | --------------------- |
| **Best**            | Best available quality            | Variable              |
| **2160p (4K)**      | 4K screens, archiving             | ~4-8 GB               |
| **1440p (2K)**      | High definition monitors          | ~2-4 GB               |
| **1080p (Full HD)** | Standard usage, best compromise ⭐ | ~1-2 GB               |
| **720p (HD)**       | Mobile devices, space saving      | ~500 MB-1 GB          |
| **480p**            | Slow connection, limited storage  | ~300-500 MB           |
| **360p**            | Very slow connection              | ~200-300 MB           |

> 💡 **Tip**: For daily use, **1080p** offers the best quality/size compromise.

### Audio bitrate

| Bitrate      | Quality           | Recommended usage        | Size (1h) |
| ------------ | ----------------- | ------------------------ | --------- |
| **Best**     | Maximum available | Archiving, audiophiles ⭐ | Variable  |
| **320 kbps** | Excellent         | High quality music       | ~140 MB   |
| **256 kbps** | Very good         | Standard usage           | ~115 MB   |
| **192 kbps** | Good              | Quality/size compromise  | ~85 MB    |
| **128 kbps** | Decent            | Podcasts, conferences    | ~60 MB    |
| **96 kbps**  | Acceptable        | Voice only               | ~45 MB    |
| **64 kbps**  | Low               | Very slow connection     | ~30 MB    |

### Audio format

- **M4A**:
  - ✅ Better quality for same size
  - ✅ Lighter files
  - ✅ YouTube native format (no conversion)
  - ❌ Less compatible with old players
- **MP3**:
  - ✅ Compatible with all devices
  - ✅ Widely supported
  - ✅ Customizable (bitrate of choice)
  - ❌ Requires conversion (FFmpeg required)

------

## Customization

### 🌍 Change language

Click on the language selector 🌐 at the top left to choose from available languages.

### 🌓 Dark / Light mode

Use the **🌙 / ☀️** switch to toggle between themes.

------

## ❓ Common Issues

### "The playlist does not exist"

**Possible causes:**

1. The playlist is **private** → Make sure you're logged into YouTube in Firefox, or provide a `cookies.txt` file
2. The URL is incorrect → Check that you've copied the complete playlist URL
3. The playlist was deleted → Verify it still exists on YouTube

### "ERROR: unable to download video data"

**Possible causes:**

1. Unstable internet connection
2. Deleted or private video
3. YouTube changed its format → Update yt-dlp: `pip install -U yt-dlp`

### Slow download

- **Solutions:**
  - ✅ Check your internet connection 📶
  - ✅ YouTube sometimes limits speed based on your location
  - ✅ Try downloading at a different time
  - ✅ Download a lower resolution (720p instead of 1080p)

### MP3 conversion error

**Error**: `ERROR: ffmpeg not found`

**Solution**: MP3 conversion requires **FFmpeg** installed on your system.

**Installing FFmpeg:**

```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# Fedora
sudo dnf install ffmpeg

# Arch Linux
sudo pacman -S ffmpeg

# macOS (Homebrew)
brew install ffmpeg

# Windows (Chocolatey)
choco install ffmpeg
```

**Verify installation:**

```bash
ffmpeg -version
```

### Download stops at 99%

This is normal! The application is **merging** video and audio (or converting to MP3). This step can take from a few seconds to a few minutes depending on:

- File size
- Your computer's power
- Chosen resolution

> 💡 **Tip**: Don't close the application while the progress bar is at 99%!

### "Permission denied" during download

**Possible causes:**

1. The destination folder is write-protected
2. A file with the same name is already open
3. Your antivirus is blocking writes

**Solutions:**

- ✅ Choose a folder in your home directory (Documents, Downloads)
- ✅ Close any open video files
- ✅ Add an exception in your antivirus

## 📞 Support

### Getting help

For any questions or issues:

- 🐛 Report a bug on [GitHub](https://github.com/richbenji/Ultimate-GUI-YouTube-Downloader-yt-dlp-Ctk)
- 💬 **Question**: Check this tutorial first, then open an issue on GitHub
- ⭐ **Like the app?**: Star it on GitHub!

### Contributing

The project is open-source! Contributions are welcome:

- 🔧 Bug fixes
- ✨ New features
- 🌍 Additional translations
- 📖 Documentation improvements

------

## 📜 Legal Notice

### Responsible use

This application is a download tool. **You are responsible** for how you use it:

- ✅ **Allowed**: Download your own videos, free license content, or content you have permission for
- ❌ **Forbidden**: Download copyrighted content without permission, redistribute downloaded content

> ⚠️ **Important**: Always respect YouTube's terms of service and your country's copyright laws.

------

**Happy downloading! 🎉**