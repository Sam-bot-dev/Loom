# test_fetcher.py

from ingestion.fetcher import VideoFetcher

fetcher = VideoFetcher()

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
video_path = fetcher.fetch(url)

print("Downloaded:", video_path)