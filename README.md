# 🎬 YouTube Video Info & Audio Downloader API (yt-dlp-smoky)

A lightweight proxy API built with [`yt-dlp`](https://github.com/yt-dlp/yt-dlp), deployed on **Vercel**, which allows you to fetch YouTube video metadata and audio download links in structured JSON format.

---

## 📌 Features

- ✅ Get video title, description, channel info, thumbnail, views, likes
- 🎧 Extract audio-only formats (MP3/WEBM) with quality labels & direct download URLs
- ⚡ Blazing fast response (serverless deployment on Vercel)
- 🧩 Ideal for Telegram bots, preview websites, and lightweight apps

---

## 🔗 API Endpoint

```http
GET https://yt-dlp-smoky.vercel.app/?url=YOUTUBE_VIDEO_LINK
```

### 📥 Example

```http
https://yt-dlp-smoky.vercel.app/?url=https://www.youtube.com/watch?v=wac5bAJydc8
```

---

## 🧾 Sample JSON Response

```json
{
  "success": true,
  "data": {
    "title": "One Piece VS Naruto VS Bleach | Best in BIG 3 | In-Depth Analysis",
    "channel": "Daddy Vyuk",
    "channel_id": "@DaddyVyuk",
    "description": "...",
    "duration": 1176,
    "view_count": 730095,
    "like_count": 36813,
    "upload_date": "20230919",
    "video_id": "wac5bAJydc8",
    "thumbnail": "https://i.ytimg.com/vi_webp/wac5bAJydc8/maxresdefault.webp",
    "webpage_url": "https://www.youtube.com/watch?v=wac5bAJydc8",
    "formats": {
      "audio": [
        {
          "ext": "mp3",
          "quality_label": "71.18kbps",
          "filesize": 10461650,
          "type": "audio_only",
          "format_id": "250-drc",
          "url": "https://..."
        }
      ]
    }
  }
}
```

---

## 📂 Response Structure

| Field           | Description                          |
|-----------------|--------------------------------------|
| `title`         | YouTube video title                  |
| `channel`       | Channel name                         |
| `channel_id`    | YouTube handle (@username)           |
| `description`   | Full description text                |
| `duration`      | Duration in seconds                  |
| `view_count`    | Total view count                     |
| `like_count`    | Total likes                          |
| `upload_date`   | Date in `YYYYMMDD` format            |
| `thumbnail`     | Max resolution thumbnail URL         |
| `formats.audio` | List of audio formats with direct URLs |

---

## 💡 Use Cases

- Telegram bots for YouTube preview/download
- Serverless YouTube metadata fetcher
- Audio extractor for media apps
- Data enrichment from YouTube videos

---

## 🚀 Deploy Your Own (Optional)

You can clone this project and deploy on Vercel yourself:

```bash
git clone https://github.com/yourname/yt-dlp-vercel-api
cd yt-dlp-vercel-api
vercel deploy
```

---

## 🙋 Support

For support or questions, reach out via Telegram:  
📬 [@bro_bin_lagbe](https://t.me/bro_bin_lagbe)

---

## 📜 License

This project is intended for **educational and personal** use only.  
You are responsible for how you use the data fetched via this API.
