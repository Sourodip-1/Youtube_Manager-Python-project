# 📺 YouTube Manager

A simple command-line Python application to manage a list of YouTube videos.  
You can **add, update, delete, and view videos** with their durations.  
All data is stored in a local JSON file (`youtube.txt`), making it lightweight and easy to use.

---

## 🚀 Features
- ✅ List all saved YouTube videos  
- ➕ Add a new video with name and duration  
- ✏️ Update details of an existing video  
- ❌ Delete a video from the list  
- 💾 Persistent storage using JSON  

---

## 🛠️ How It Works
The app uses a text file (`youtube.txt`) to store video data in JSON format.  
Each video is represented as a dictionary:

```json
{
  "name": "Video Title",
  "time": "Duration (e.g., 48min, 1hr 30min)"
}
```

#FILE STRUCTURE
```python
youtube_manager.py     # Main application script
youtube.txt            # JSON file storing video data
```

```bash
Youtube Manager | Choose An Option
1. List all YouTube Videos
2. Add a YouTube Video
3. Update a YouTube Video Details
4. Delete a YouTube Video
5. Exit The App
Enter Your Choice: 2

enter video name: Python Tutorial
enter video time: 1hr 10min
```
