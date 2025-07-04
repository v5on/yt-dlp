import yt_dlp
import re
import logging

class YouTubeService:
    def is_valid_youtube_url(self, url):
        pattern = re.compile(
            r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'
            r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
        )
        return pattern.match(url) is not None

    def get_video_info(self, url):
        try:
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
                'extract_flat': False,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)

            return {
                'title': info.get('title'),
                'channel': info.get('uploader'),
                'channel_id': info.get('uploader_id'),
                'duration': info.get('duration'),
                'view_count': info.get('view_count'),
                'like_count': info.get('like_count'),
                'upload_date': info.get('upload_date'),
                'description': info.get('description'),
                'thumbnail': info.get('thumbnail'),
                'webpage_url': info.get('webpage_url'),
                'video_id': info.get('id')
            }

        except Exception as e:
            logging.error(f"Error getting video info: {e}")
            raise Exception(f"Could not extract video info: {str(e)}")
