from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "ok", "message": "YouTube Preview API working."})

@app.route("/api/preview", methods=["GET"])
def preview():
    video_url = request.args.get("url")
    if not video_url:
        return jsonify({"error": "Missing YouTube URL"}), 400

    ydl_opts = {
        'quiet': True,
        'format': 'best[ext=mp4][vcodec!=none][acodec!=none]/best',
        'skip_download': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            result = {
                "title": info.get("title"),
                "thumbnail": info.get("thumbnail"),
                "duration": info.get("duration"),
                "preview_url": info.get("url"),
                "format": info.get("format_note"),
            }
            return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
