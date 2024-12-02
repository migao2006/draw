from flask import Flask, render_template, request, send_from_directory
from datetime import datetime
import os
import random

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 確保上傳資料夾存在
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    keyword = request.form.get('keyword', 'default')
    # 模擬生成圖像（實際上可使用 AI 圖像生成 API 或自製生成工具）
    filename = f"{keyword}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # 暫時生成隨機顏色背景圖片
    from PIL import Image, ImageDraw
    img = Image.new('RGB', (400, 400), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    draw = ImageDraw.Draw(img)
    draw.text((50, 180), keyword, fill="white")
    img.save(filepath)

    return filepath

@app.route('/uploads/<filename>')
def uploads(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
