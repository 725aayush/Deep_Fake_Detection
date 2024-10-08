from flask import Flask, render_template
import imageio
import os
from datetime import datetime

app = Flask(__name__)

def get_video_metadata(video_path):
    video = imageio.get_reader(video_path, format='FFMPEG')
    metadata = video.get_meta_data()
    
    # Additional metadata
    fps = metadata['fps']
    duration = metadata['duration']
    num_frames = video.get_length()

    # File-related metadata
    file_path = os.path.abspath(video_path)
    created_time = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
    modified_time = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')


    # Camera-related metadata
    camera_model = metadata.get('camera_model', 'N/A')
    software = metadata.get('software', 'N/A')

    return {
        'fps': fps,
        'duration': duration,
        'num_frames': num_frames,
        'file_path': file_path,
        'created_time': created_time,
        'modified_time': modified_time,
        'camera_model': camera_model,
        'software': software,
        **metadata  # Include the original metadata
    }

@app.route('/')
def index():
    # Replace 'video.mp4' with the path to your video file
    video_path = r'E:\raj police hackathon\Deepfake_detection_using_deep_learning\MetaData Analysis\video_2.mp4'
    metadata = get_video_metadata(video_path)
    return render_template('index.html', metadata=metadata)

if __name__ == '__main__':
    app.run(debug=True)
