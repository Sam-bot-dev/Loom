# ingestion/fetcher.py

import yt_dlp
import os
import uuid
from datetime import datetime


class VideoFetcher:
    def __init__(self, output_dir="data/input"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def _generate_filename(self):
        """Generate unique filename"""
        unique_id = str(uuid.uuid4())[:8]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"video_{timestamp}_{unique_id}.mp4"

    def fetch(self, url: str) -> str:
        """
        Download video from URL and return file path
        """
        filename = self._generate_filename()
        output_path = os.path.join(self.output_dir, filename)

        ydl_opts = {
            'outtmpl': output_path,
            'format': 'mp4',
            'quiet': False,
            'noplaylist': True,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"[INFO] Downloading video from: {url}")
                ydl.download([url])

            print(f"[SUCCESS] Video saved to: {output_path}")
            return output_path

        except Exception as e:
            print(f"[ERROR] Failed to download video: {e}")
            return None