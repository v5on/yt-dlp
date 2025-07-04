from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/video-info")
def proxy_video_info():
    youtube_url = request.args.get("url")
    if not youtube_url:
        return jsonify({"error": "Missing 'url' query parameter"}), 400

    main_api_url = "https://youtube-api-production-e07a.up.railway.app/api/video-info"
    try:
        response = requests.get(main_api_url, params={"url": youtube_url})
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500
