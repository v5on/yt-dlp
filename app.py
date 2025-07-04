from flask import Flask, request, jsonify
from youtube_service import YouTubeService

app = Flask(__name__)
youtube_service = YouTubeService()

@app.route('/api/video-info')
def get_video_info():
    url = request.args.get('url')
    if not url:
        return jsonify({'success': False, 'error': 'Missing required parameter: url'}), 400

    if not youtube_service.is_valid_youtube_url(url):
        return jsonify({'success': False, 'error': 'Invalid YouTube URL'}), 400

    try:
        video_info = youtube_service.get_video_info(url)
        return jsonify({'success': True, 'data': video_info})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/health')
def health_check():
    return jsonify({'status': 'ok'})
