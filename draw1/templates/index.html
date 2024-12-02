<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>關鍵字繪畫</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
        input, button { padding: 10px; margin: 10px; }
        img { margin-top: 20px; max-width: 400px; height: auto; }
    </style>
</head>
<body>
    <h1>輸入關鍵字生成圖片</h1>
    <form id="generateForm" method="POST" action="/generate">
        <input type="text" name="keyword" placeholder="輸入關鍵字" required>
        <button type="submit">生成圖片</button>
    </form>
    <div id="result">
        <img id="generatedImage" style="display: none;" />
    </div>
    <script>
        const form = document.getElementById('generateForm');
        const resultDiv = document.getElementById('result');
        const image = document.getElementById('generatedImage');

        form.onsubmit = async (e) => {
            e.preventDefault();
            const formData = new FormData(form);
            const response = await fetch('/generate', { method: 'POST', body: formData });
            const imagePath = await response.text();
            image.src = imagePath;
            image.style.display = 'block';
        };
    </script>
</body>
</html>
