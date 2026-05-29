from flask import Flask, request, render_template_string, jsonify
import requests
import re
from datetime import datetime
import random

app = Flask(__name__)

# ====================== MR USMAN ======================
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>⚡ 3D HACKING TEMPLE | SOURCE CODE EXTRACTOR PRO ⚡</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Rajdhani:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Orbitron', 'Rajdhani', monospace;
            min-height: 100vh;
            overflow-x: hidden;
            position: relative;
        }

        /* YOUR BACKGROUND IMAGE */
        body {
            background-image: url('https://i.ibb.co/SDmrqnr8/Messenger-creation-04-D4-C86-A-4-E67-4579-A896-C613435-AF568.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }

        /* Dark Overlay with Matrix Effect */
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, 
                rgba(0,0,0,0.88) 0%,
                rgba(0,20,0,0.85) 50%,
                rgba(0,0,0,0.88) 100%);
            z-index: 0;
        }

        /* Matrix Rain Canvas */
        #matrixCanvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
            opacity: 0.15;
            pointer-events: none;
        }

        /* 3D Container */
        .container-3d {
            position: relative;
            z-index: 2;
            max-width: 1600px;
            margin: 0 auto;
            padding: 20px;
            perspective: 1200px;
        }

        /* 3D Glass Card */
        .glass-3d {
            background: rgba(0, 0, 0, 0.55);
            backdrop-filter: blur(12px);
            border-radius: 40px;
            border: 1px solid rgba(0, 255, 255, 0.3);
            box-shadow: 0 0 30px rgba(0, 255, 255, 0.2),
                        0 20px 40px rgba(0,0,0,0.4),
                        inset 0 1px 2px rgba(255,255,255,0.1);
            transform-style: preserve-3d;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            animation: float3d 6s ease-in-out infinite;
        }

        @keyframes float3d {
            0%, 100% { transform: translateY(0) rotateX(0deg); }
            50% { transform: translateY(-10px) rotateX(2deg); }
        }

        .glass-3d:hover {
            transform: translateY(-5px) rotateX(3deg);
            box-shadow: 0 0 50px rgba(0, 255, 255, 0.4);
            border-color: rgba(0, 255, 255, 0.6);
        }

        /* Neon Header */
        .neon-header {
            text-align: center;
            padding: 50px 30px 40px;
            background: linear-gradient(180deg, 
                rgba(0,255,255,0.05) 0%,
                rgba(0,0,0,0) 100%);
            border-bottom: 2px solid rgba(0, 255, 255, 0.3);
            position: relative;
            overflow: hidden;
        }

        .glitch-text {
            font-size: 3.5rem;
            font-weight: 900;
            font-family: 'Orbitron', monospace;
            text-transform: uppercase;
            position: relative;
            text-shadow: 0.05em 0 0 rgba(255,0,0,0.75),
                        -0.05em -0.025em 0 rgba(0,255,0,0.75),
                        0.025em 0.05em 0 rgba(0,0,255,0.75);
            animation: glitch 3s infinite;
        }

        @keyframes glitch {
            0%, 100% { text-shadow: 0.05em 0 0 rgba(255,0,0,0.75), -0.05em -0.025em 0 rgba(0,255,0,0.75); }
            25% { text-shadow: -0.05em -0.025em 0 rgba(255,0,0,0.75), 0.025em 0.05em 0 rgba(0,255,0,0.75); }
            50% { text-shadow: 0.025em 0.05em 0 rgba(255,0,0,0.75), 0.05em 0 0 rgba(0,255,0,0.75); }
            75% { text-shadow: -0.025em -0.05em 0 rgba(255,0,0,0.75), -0.05em -0.025em 0 rgba(0,255,0,0.75); }
        }

        .neon-header h1 {
            background: linear-gradient(135deg, #0ff, #0f0, #ff0);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            font-size: 3rem;
            margin: 10px 0;
            letter-spacing: 4px;
        }

        .scan-line {
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 2px;
            background: linear-gradient(90deg, transparent, #0ff, transparent);
            animation: scan 3s linear infinite;
        }

        @keyframes scan {
            0% { left: -100%; top: 0; }
            100% { left: 100%; top: 100%; }
        }

        /* Input Section 3D */
        .input-3d-section {
            padding: 40px;
        }

        .url-group-3d {
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
        }

        .input-3d-wrapper {
            flex: 1;
            position: relative;
            transform-style: preserve-3d;
        }

        .input-3d-wrapper::before {
            content: '>';
            position: absolute;
            left: 20px;
            top: 50%;
            transform: translateY(-50%);
            color: #0f0;
            font-weight: bold;
            font-size: 1.2rem;
            z-index: 1;
            font-family: monospace;
            animation: blink 1s step-end infinite;
        }

        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0; }
        }

        .url-input-3d {
            width: 100%;
            padding: 18px 20px 18px 45px;
            font-size: 1rem;
            font-family: 'Rajdhani', monospace;
            background: rgba(0, 30, 30, 0.8);
            border: 2px solid rgba(0, 255, 255, 0.3);
            border-radius: 15px;
            color: #0ff;
            transition: all 0.3s;
        }

        .url-input-3d:focus {
            outline: none;
            border-color: #0ff;
            box-shadow: 0 0 25px rgba(0, 255, 255, 0.4);
            background: rgba(0, 20, 20, 0.9);
        }

        .extract-btn-3d {
            padding: 18px 45px;
            background: linear-gradient(135deg, #0ff, #0a0);
            border: none;
            border-radius: 15px;
            font-size: 1.1rem;
            font-weight: bold;
            color: #000;
            cursor: pointer;
            transition: all 0.3s;
            font-family: 'Orbitron', monospace;
            text-transform: uppercase;
            letter-spacing: 2px;
            position: relative;
            overflow: hidden;
        }

        .extract-btn-3d::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            background: rgba(255,255,255,0.3);
            border-radius: 50%;
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
        }

        .extract-btn-3d:hover::before {
            width: 300px;
            height: 300px;
        }

        .extract-btn-3d:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(0, 255, 255, 0.4);
        }

        /* Stats Cards 3D */
        .stats-3d {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }

        .stat-card-3d {
            background: rgba(0, 20, 20, 0.6);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            border: 1px solid rgba(0, 255, 255, 0.3);
            transform-style: preserve-3d;
            transition: all 0.3s;
            cursor: pointer;
        }

        .stat-card-3d:hover {
            transform: translateZ(20px) rotateX(5deg);
            border-color: #0ff;
            box-shadow: 0 0 30px rgba(0, 255, 255, 0.3);
        }

        .stat-number-3d {
            font-size: 2.2rem;
            font-weight: 900;
            color: #0ff;
            font-family: 'Orbitron', monospace;
            text-shadow: 0 0 10px #0ff;
        }

        /* Hacking Tabs */
        .hacking-tabs {
            display: flex;
            gap: 15px;
            margin-bottom: 25px;
            flex-wrap: wrap;
        }

        .hack-tab {
            padding: 12px 30px;
            background: rgba(0, 30, 30, 0.6);
            border: 1px solid rgba(0, 255, 255, 0.3);
            border-radius: 30px;
            color: #0ff;
            cursor: pointer;
            transition: all 0.3s;
            font-family: 'Orbitron', monospace;
            font-weight: 600;
            backdrop-filter: blur(5px);
        }

        .hack-tab.active {
            background: linear-gradient(135deg, #0ff, #0a0);
            color: #000;
            box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
            border-color: #0ff;
        }

        .hack-tab:hover {
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(0, 255, 255, 0.3);
        }

        /* Terminal Code Viewer */
        .terminal-viewer {
            background: rgba(0, 0, 0, 0.85);
            border-radius: 15px;
            overflow: hidden;
            border: 1px solid #0ff;
            box-shadow: 0 0 20px rgba(0, 255, 255, 0.2);
        }

        .terminal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 20px;
            background: linear-gradient(135deg, #0a0a0a, #000);
            border-bottom: 1px solid #0ff;
        }

        .terminal-title {
            color: #0ff;
            font-family: monospace;
            font-size: 0.85rem;
        }

        .terminal-dots {
            display: flex;
            gap: 8px;
        }

        .dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
        }

        .dot-red { background: #ff5f56; }
        .dot-yellow { background: #ffbd2e; }
        .dot-green { background: #27c93f; }

        .copy-terminal {
            background: rgba(0, 255, 255, 0.2);
            padding: 6px 15px;
            border-radius: 8px;
            border: none;
            color: #0ff;
            cursor: pointer;
            font-family: monospace;
            transition: all 0.2s;
        }

        .copy-terminal:hover {
            background: #0ff;
            color: #000;
        }

        pre {
            margin: 0;
            padding: 25px;
            overflow-x: auto;
            max-height: 500px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
            line-height: 1.5;
            color: #0f0;
            background: rgba(0, 0, 0, 0.8);
        }

        /* Owner Dialog - Premium */
        .premium-dialog {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) scale(0) rotateX(0deg);
            width: 450px;
            max-width: 90%;
            background: linear-gradient(135deg, #0a0a0a, #001a1a);
            border-radius: 30px;
            padding: 40px;
            z-index: 1000;
            text-align: center;
            border: 2px solid #0ff;
            box-shadow: 0 0 100px rgba(0, 255, 255, 0.5), 0 20px 40px rgba(0,0,0,0.5);
            transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            backdrop-filter: blur(20px);
        }

        .premium-dialog.show {
            transform: translate(-50%, -50%) scale(1) rotateX(0deg);
        }

        .hologram-icon {
            font-size: 5rem;
            color: #0ff;
            text-shadow: 0 0 20px #0ff;
            animation: pulse 1s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); text-shadow: 0 0 20px #0ff; }
            50% { transform: scale(1.1); text-shadow: 0 0 40px #0ff; }
        }

        .dialog-title {
            font-size: 2rem;
            color: #0ff;
            margin: 15px 0;
            font-family: 'Orbitron', monospace;
        }

        .owner-name-3d {
            font-size: 2rem;
            font-weight: 900;
            background: linear-gradient(135deg, #0ff, #0f0, #ff0);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            margin: 15px 0;
            font-family: 'Orbitron', monospace;
        }

        .enter-btn {
            background: linear-gradient(135deg, #0ff, #0a0);
            border: none;
            padding: 15px 40px;
            border-radius: 40px;
            font-size: 1.1rem;
            font-weight: bold;
            color: #000;
            cursor: pointer;
            margin-top: 20px;
            font-family: 'Orbitron', monospace;
            transition: all 0.3s;
        }

        .enter-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 0 30px #0ff;
        }

        /* Alerts */
        .alert-3d {
            padding: 15px 20px;
            border-radius: 15px;
            margin-bottom: 20px;
            display: none;
            animation: slideDown 0.3s;
        }

        @keyframes slideDown {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .alert-success-3d {
            background: rgba(0, 255, 0, 0.2);
            border: 1px solid #0f0;
            color: #0f0;
        }

        .alert-error-3d {
            background: rgba(255, 0, 0, 0.2);
            border: 1px solid #f00;
            color: #f66;
        }

        /* Loader 3D */
        .loader-3d {
            display: none;
            text-align: center;
            padding: 40px;
        }

        .hacking-loader {
            width: 80px;
            height: 80px;
            margin: 0 auto;
            position: relative;
        }

        .hacking-loader div {
            position: absolute;
            width: 100%;
            height: 100%;
            border: 3px solid transparent;
            border-top-color: #0ff;
            border-radius: 50%;
            animation: spin3d 1s linear infinite;
        }

        .hacking-loader div:nth-child(2) {
            border-top-color: #0f0;
            animation: spin3d 1.5s linear reverse infinite;
        }

        @keyframes spin3d {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        /* Footer */
        .hacking-footer {
            text-align: center;
            padding: 20px;
            color: rgba(0, 255, 255, 0.4);
            font-size: 0.8rem;
            border-top: 1px solid rgba(0, 255, 255, 0.2);
            margin-top: 30px;
        }

        @media (max-width: 768px) {
            .glitch-text { font-size: 1.8rem; }
            .neon-header h1 { font-size: 1.5rem; }
            .input-3d-section { padding: 25px; }
            .hack-tab { padding: 8px 15px; font-size: 0.8rem; }
        }
    </style>
</head>
<body>

    <!-- Matrix Canvas -->
    <canvas id="matrixCanvas"></canvas>

    <!-- Premium Owner Dialog -->
    <div class="premium-dialog" id="ownerDialog">
        <div class="hologram-icon">
            <i class="fas fa-robot"></i>
        </div>
        <div class="dialog-title"> SOURCE CODE EXTRACTOR ⚡</div>
        <p style="color: #0ff; margin: 10px 0;">Premium Source Code Extractor</p>
        <div class="owner-name-3d">
            <i class="fas fa-crown"></i> CREDIT: MR USMAN
        </div>
        <p style="color: rgba(0,255,255,0.7); font-size: 0.9rem;">THE SYSTEM FUCKER BOY FT USMAN</p>
        <button class="enter-btn" onclick="closeDialog()">
            <i class="fas fa-unlock-alt"></i> ENTER TOOL
        </button>
    </div>

    <div class="container-3d">
        <div class="glass-3d">
            <div class="neon-header">
                <div class="scan-line"></div>
                <div class="glitch-text">MR USMAN v3.0</div>
                <h1>
                    <i class="fas fa-skull"></i> SOURCE CODE EXTRACTOR <i class="fas fa-terminal"></i>
                </h1>
                <div style="color: #0f0; font-size: 0.85rem; margin-top: 10px;">
                    <i class="fas fa-lock"></i> ENCRYPTED MODE ACTIVATED <i class="fas fa-lock"></i>
                </div>
            </div>

            <div class="input-3d-section">
                <div class="url-group-3d">
                    <div class="input-3d-wrapper">
                        <input type="text" class="url-input-3d" id="urlInput" placeholder="https://target-website.com">
                    </div>
                    <button class="extract-btn-3d" onclick="extractSource()">
                        <i class="fas fa-bolt"></i> EXTRACT
                    </button>
                </div>

                <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 20px;">
                    <span class="hack-tab" style="padding: 5px 15px; font-size: 0.8rem;" onclick="setUrl('https://example.com')">📝 EXAMPLE</span>
                    <span class="hack-tab" style="padding: 5px 15px; font-size: 0.8rem;" onclick="setUrl('https://google.com')">🔍 GOOGLE</span>
                    <span class="hack-tab" style="padding: 5px 15px; font-size: 0.8rem;" onclick="setUrl('https://github.com')">🐙 GITHUB</span>
                    <span class="hack-tab" style="padding: 5px 15px; font-size: 0.8rem;" onclick="setUrl('https://stackoverflow.com')">📚 STACK</span>
                </div>
            </div>
        </div>

        <div class="loader-3d" id="loader">
            <div class="hacking-loader">
                <div></div>
                <div></div>
            </div>
            <p style="color: #0ff; margin-top: 15px;">HACKING INTO TARGET...</p>
        </div>

        <div id="alerts"></div>

        <div class="glass-3d" id="results" style="display: none; margin-top: 30px;">
            <div style="padding: 30px;">
                <div class="stats-3d" id="stats"></div>

                <div class="hacking-tabs">
                    <button class="hack-tab active" onclick="switchTab('html')">
                        <i class="fab fa-html5"></i> HTML
                    </button>
                    <button class="hack-tab" onclick="switchTab('css')">
                        <i class="fab fa-css3-alt"></i> CSS
                    </button>
                    <button class="hack-tab" onclick="switchTab('js')">
                        <i class="fab fa-js"></i> JAVASCRIPT
                    </button>
                    <button class="hack-tab" onclick="switchTab('full')">
                        <i class="fas fa-code"></i> FULL SOURCE
                    </button>
                </div>

                <div id="htmlPanel" class="terminal-viewer">
                    <div class="terminal-header">
                        <div class="terminal-dots">
                            <div class="dot dot-red"></div>
                            <div class="dot dot-yellow"></div>
                            <div class="dot dot-green"></div>
                        </div>
                        <div class="terminal-title">HTML_SOURCE.html</div>
                        <button class="copy-terminal" onclick="copyCode('html')">
                            <i class="fas fa-copy"></i> COPY
                        </button>
                    </div>
                    <pre><code id="htmlCode"></code></pre>
                </div>

                <div id="cssPanel" class="terminal-viewer" style="display: none;">
                    <div class="terminal-header">
                        <div class="terminal-dots">
                            <div class="dot dot-red"></div>
                            <div class="dot dot-yellow"></div>
                            <div class="dot dot-green"></div>
                        </div>
                        <div class="terminal-title">STYLE_SOURCE.css</div>
                        <button class="copy-terminal" onclick="copyCode('css')">
                            <i class="fas fa-copy"></i> COPY
                        </button>
                    </div>
                    <pre><code id="cssCode"></code></pre>
                </div>

                <div id="jsPanel" class="terminal-viewer" style="display: none;">
                    <div class="terminal-header">
                        <div class="terminal-dots">
                            <div class="dot dot-red"></div>
                            <div class="dot dot-yellow"></div>
                            <div class="dot dot-green"></div>
                        </div>
                        <div class="terminal-title">SCRIPT_SOURCE.js</div>
                        <button class="copy-terminal" onclick="copyCode('js')">
                            <i class="fas fa-copy"></i> COPY
                        </button>
                    </div>
                    <pre><code id="jsCode"></code></pre>
                </div>

                <div id="fullPanel" class="terminal-viewer" style="display: none;">
                    <div class="terminal-header">
                        <div class="terminal-dots">
                            <div class="dot dot-red"></div>
                            <div class="dot dot-yellow"></div>
                            <div class="dot dot-green"></div>
                        </div>
                        <div class="terminal-title">COMPLETE_SOURCE.html</div>
                        <button class="copy-terminal" onclick="copyCode('full')">
                            <i class="fas fa-copy"></i> COPY
                        </button>
                    </div>
                    <pre><code id="fullCode"></code></pre>
                </div>
            </div>
        </div>

        <div class="hacking-footer">
            <i class="fas fa-shield-haltered"> | ENCRYPTED MODE | <i class="fas fa-code"></i> DEVELOPED BY USMAN
        </div>
    </div>

    <script>
        // Matrix Rain Effect
        const canvas = document.getElementById('matrixCanvas');
        const ctx = canvas.getContext('2d');
        
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        
        const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()<>/\\|[]{}-=_+';
        const fontSize = 14;
        const columns = canvas.width / fontSize;
        const drops = [];
        
        for(let i = 0; i < columns; i++) {
            drops[i] = Math.random() * -100;
        }
        
        function drawMatrix() {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            ctx.fillStyle = '#0f0';
            ctx.font = fontSize + 'px monospace';
            
            for(let i = 0; i < drops.length; i++) {
                const char = chars[Math.floor(Math.random() * chars.length)];
                ctx.fillText(char, i * fontSize, drops[i] * fontSize);
                
                if(drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                    drops[i] = 0;
                }
                drops[i]++;
            }
        }
        
        setInterval(drawMatrix, 50);
        
        window.addEventListener('resize', () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        });

        // Show owner dialog on load
        window.onload = function() {
            document.getElementById('ownerDialog').classList.add('show');
        }

        function closeDialog() {
            document.getElementById('ownerDialog').classList.remove('show');
        }

        let currentData = null;

        function setUrl(url) {
            document.getElementById('urlInput').value = url;
        }

        function showAlert(type, message) {
            const alertsDiv = document.getElementById('alerts');
            const alertDiv = document.createElement('div');
            alertDiv.className = `alert-3d alert-${type}-3d`;
            alertDiv.innerHTML = `<i class="fas ${type === 'error' ? 'fa-exclamation-triangle' : 'fa-check-circle'}"></i> ${message}`;
            alertsDiv.appendChild(alertDiv);
            setTimeout(() => alertDiv.remove(), 4000);
        }

        async function extractSource() {
            const url = document.getElementById('urlInput').value;
            if(!url) {
                showAlert('error', '⚠️ TARGET URL REQUIRED!');
                return;
            }

            document.getElementById('loader').style.display = 'block';
            document.getElementById('results').style.display = 'none';
            document.getElementById('alerts').innerHTML = '';

            try {
                const response = await fetch('/extract', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({url: url})
                });

                const data = await response.json();

                if(response.ok) {
                    currentData = data;
                    displayResults(data);
                    document.getElementById('results').style.display = 'block';
                    showAlert('success', `✅ HACK SUCCESSFUL! Extracted from ${data.url}`);
                } else {
                    showAlert('error', data.error || '❌ HACK FAILED!');
                }
            } catch(err) {
                showAlert('error', '🌐 NETWORK ERROR: ' + err.message);
            } finally {
                document.getElementById('loader').style.display = 'none';
            }
        }

        function displayResults(data) {
            document.getElementById('htmlCode').textContent = data.html || '// NO HTML SOURCE FOUND';
            document.getElementById('cssCode').textContent = data.css || '/* NO CSS SOURCE FOUND */';
            document.getElementById('jsCode').textContent = data.js || '// NO JAVASCRIPT FOUND';
            document.getElementById('fullCode').textContent = data.full_source || '// NO SOURCE FOUND';

            const stats = document.getElementById('stats');
            stats.innerHTML = `
                <div class="stat-card-3d">
                    <div class="stat-number-3d">${data.html_size || 0} KB</div>
                    <div style="color: #0f0;">📄 HTML DATA</div>
                </div>
                <div class="stat-card-3d">
                    <div class="stat-number-3d">${data.css_size || 0} KB</div>
                    <div style="color: #0f0;">🎨 CSS DATA</div>
                </div>
                <div class="stat-card-3d">
                    <div class="stat-number-3d">${data.js_size || 0} KB</div>
                    <div style="color: #0f0;">⚡ JS DATA</div>
                </div>
                <div class="stat-card-3d">
                    <div class="stat-number-3d">${data.total_size || 0} KB</div>
                    <div style="color: #0f0;">📦 TOTAL SIZE</div>
                </div>
            `;
        }

        function switchTab(tab) {
            document.querySelectorAll('.hack-tab').forEach(t => t.classList.remove('active'));
            event.target.closest('.hack-tab').classList.add('active');

            document.getElementById('htmlPanel').style.display = 'none';
            document.getElementById('cssPanel').style.display = 'none';
            document.getElementById('jsPanel').style.display = 'none';
            document.getElementById('fullPanel').style.display = 'none';

            document.getElementById(tab + 'Panel').style.display = 'block';
        }

        function copyCode(type) {
            let code = '';
            if(type === 'html') code = document.getElementById('htmlCode').textContent;
            else if(type === 'css') code = document.getElementById('cssCode').textContent;
            else if(type === 'js') code = document.getElementById('jsCode').textContent;
            else code = document.getElementById('fullCode').textContent;

            navigator.clipboard.writeText(code).then(() => {
                showAlert('success', `📋 ${type.toUpperCase()} CODE COPIED!`);
            }).catch(() => {
                showAlert('error', '❌ COPY FAILED');
            });
        }
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/extract', methods=['POST'])
def extract_source():
    data = request.get_json()
    url = data.get('url')
    
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        html_content = response.text
        
        # Extract CSS
        css_pattern = r'<style[^>]*>(.*?)</style>'
        css_matches = re.findall(css_pattern, html_content, re.DOTALL | re.IGNORECASE)
        css_content = '\n\n'.join(css_matches) if css_matches else '/* No inline CSS found */'
        
        # Extract JS
        js_pattern = r'<script[^>]*>(.*?)</script>'
        js_matches = re.findall(js_pattern, html_content, re.DOTALL | re.IGNORECASE)
        js_content = '\n\n'.join(js_matches) if js_matches else '// No JavaScript found'
        
        # Sizes
        html_size = round(len(html_content) / 1024, 2)
        css_size = round(len(css_content) / 1024, 2)
        js_size = round(len(js_content) / 1024, 2)
        total_size = round(html_size + css_size + js_size, 2)
        
        return jsonify({
            'html': html_content,
            'css': css_content,
            'js': js_content,
            'full_source': html_content,
            'url': url,
            'html_size': html_size,
            'css_size': css_size,
            'js_size': js_size,
            'total_size': total_size
        })
        
    except requests.exceptions.Timeout:
        return jsonify({'error': 'Timeout - Target too slow'}), 408
    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Connection failed - Target unreachable'}), 502
    except requests.exceptions.HTTPError as e:
        return jsonify({'error': f'HTTP Error {e.response.status_code}'}), e.response.status_code
    except Exception as e:
        return jsonify({'error': f'Hack failed: {str(e)}'}), 500

if __name__ == '__main__':
    print("=" * 70)
    print("⚡ 3D HACKING TEMPLE - SOURCE CODE EXTRACTOR ULTIMATE ⚡")
    print("=" * 70)
    print("👑 DEVELOPED BY: USMAN")
    print("🔓 VERSION: ULTIMATE 3D EDITION")
    print("🚀 SERVER: http://127.0.0.1:5000")
    print("💀 HACKING MODE: ACTIVATED")
    print("=" * 70)
    app.run(debug=True, host='0.0.0.0', port=5000)
