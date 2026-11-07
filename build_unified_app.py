# -*- coding: utf-8 -*-
import os

sl_b64_file = r'C:\Users\manpe\.gemini\antigravity\brain\bd847b5e-e3ce-4d3a-9535-c6d69caacc5a\sl_base64.txt'
world_b64_file = r'C:\Users\manpe\.gemini\antigravity\brain\bd847b5e-e3ce-4d3a-9535-c6d69caacc5a\world_base64.txt'

sl_b64 = open(sl_b64_file, 'r', encoding='utf-8').read().strip()
world_b64 = open(world_b64_file, 'r', encoding='utf-8').read().strip()

html_template = """<!DOCTYPE html>
<html lang="si">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title id="page-title-tag">SL Map Lab Pro & Social Master (Unified Edition)</title>
    
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Sinhala:wght@400;600;700;800&family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js"></script>

    <script src="https://www.gstatic.com/firebasejs/9.22.1/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.22.1/firebase-database-compat.js"></script>

    <style>
        :root {
            --primary: #4361ee; 
            --primary-dark: #3730a3;
            --secondary: #00d2d3;
            --success: #2ecc71; 
            --danger: #f72585; 
            --dark: #1a1c22; 
            --light: #f8f9fa; 
            --white: #ffffff; 
            --shadow: 0 10px 30px rgba(0,0,0,0.08);
            --share-color: #ff9f43; 
            --comment-color: #00d2d3; 
            --zip-color: #4834d4;
            --show-ans: #6c5ce7;
            --gas-color: #4285F4;
            --drive-color: #00875f;
        }

        * { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }

        body { 
            font-family: 'Inter', 'Noto Sans Sinhala', sans-serif; 
            background: #eef2f7; 
            margin: 0; 
            padding: 10px 15px 40px; 
            display: flex; 
            flex-direction: column; 
            align-items: center; 
            min-height: 100vh;
        }

        .header-section { 
            width: 100%; 
            max-width: 1160px; 
            display: flex; 
            justify-content: space-between; 
            align-items: center; 
            margin-bottom: 12px; 
            flex-wrap: wrap;
            gap: 10px;
        }

        .app-logo { 
            font-size: 1.35rem; 
            font-weight: 800; 
            color: var(--dark); 
            letter-spacing: -0.5px; 
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .app-logo span.badge {
            background: linear-gradient(135deg, #4361ee, #00d2d3);
            color: white;
            font-size: 0.72rem;
            padding: 3px 8px;
            border-radius: 20px;
            text-transform: uppercase;
            font-weight: 800;
        }

        .header-status-box {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        #page-display { 
            background: white; 
            padding: 7px 18px; 
            border-radius: 50px; 
            font-weight: 800; 
            color: var(--primary);
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
            font-size: 0.9rem;
        }

        /* Category Selection Switcher */
        .category-switcher {
            width: 100%;
            max-width: 1160px;
            display: flex;
            gap: 12px;
            margin-bottom: 12px;
            background: white;
            padding: 8px;
            border-radius: 20px;
            box-shadow: var(--shadow);
        }

        .cat-tab-btn {
            flex: 1;
            padding: 12px 18px;
            border-radius: 14px;
            border: 2px solid transparent;
            font-family: inherit;
            font-size: 1rem;
            font-weight: 800;
            cursor: pointer;
            transition: all 0.25s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            background: #f8fafc;
            color: #475569;
        }

        .cat-tab-btn:hover {
            background: #edf2f7;
            transform: translateY(-1px);
        }

        .cat-tab-btn.active {
            background: linear-gradient(135deg, #4361ee, #3a0ca3);
            color: white;
            box-shadow: 0 4px 15px rgba(67, 97, 238, 0.35);
            transform: translateY(-2px);
        }

        /* Secondary Navigation (Years / Pages Bar) */
        .sub-nav-bar { 
            width: 100%; 
            max-width: 1160px; 
            display: flex; 
            gap: 8px; 
            overflow-x: auto; 
            padding: 8px 12px; 
            margin-bottom: 15px; 
            background: #ffffff; 
            border-radius: 16px; 
            box-shadow: 0 3px 12px rgba(0,0,0,0.04); 
            scrollbar-width: thin; 
            align-items: center;
        }

        .nav-chip-btn { 
            padding: 7px 16px; 
            border-radius: 50px; 
            background: #f1f5f9; 
            font-size: 0.88rem; 
            font-weight: 700; 
            cursor: pointer; 
            border: 1.5px solid #e2e8f0; 
            white-space: nowrap; 
            transition: all 0.2s; 
            color: #475569; 
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .nav-chip-btn:hover { 
            background: #e2e8f0; 
            color: #1e293b;
        }

        .nav-chip-btn.active { 
            background: var(--primary); 
            color: white; 
            border-color: var(--primary); 
            transform: scale(1.04);
            box-shadow: 0 3px 10px rgba(67, 97, 238, 0.3);
        }

        .nav-chip-action {
            background: #dbeafe;
            color: #1d4ed8;
            border-color: #bfdbfe;
        }
        
        #step-instruction { 
            background: linear-gradient(90deg, #4361ee, #4cc9f0); 
            color: white; 
            padding: 14px 20px; 
            border-radius: 16px; 
            margin-bottom: 18px; 
            width: 100%; 
            max-width: 1160px; 
            text-align: center; 
            font-weight: 700; 
            font-size: 1rem;
            box-shadow: var(--shadow); 
            transition: 0.3s; 
            position: relative; 
            overflow: hidden; 
            min-height: 24px; 
        }

        /* Main 2-column layout */
        .main-layout { 
            display: grid; 
            grid-template-columns: 340px 1fr; 
            gap: 20px; 
            width: 100%; 
            max-width: 1160px; 
            position: relative; 
            align-items: start; 
        }

        /* Sidebar */
        .sidebar { 
            background: white; 
            padding: 20px; 
            border-radius: 22px; 
            box-shadow: var(--shadow); 
            height: fit-content; 
            width: 100%; 
        }

        .score-card { 
            background: var(--dark); 
            color: white; 
            padding: 16px; 
            border-radius: 18px; 
            text-align: center; 
            margin-bottom: 15px; 
            transition: 0.3s; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        }

        .score-card p { margin: 0; font-size: 0.8rem; opacity: 0.8; letter-spacing: 0.5px; }
        .score-card h1 { margin: 5px 0 0 0; color: #4cc9f0; font-size: 2.2rem; font-weight: 800; }

        .locations-box {
            margin-bottom: 15px; 
            background: #f8fafc; 
            border: 1px solid #e2e8f0; 
            border-radius: 16px; 
            padding: 12px; 
        }

        .locations-box-header {
            font-weight: 800; 
            font-size: 0.85rem; 
            color: var(--primary); 
            margin-bottom: 8px; 
            display: flex; 
            justify-content: space-between; 
            align-items: center;
        }

        #locations-search {
            width: 100%;
            padding: 8px 12px;
            border-radius: 10px;
            border: 1px solid #cbd5e1;
            font-size: 0.82rem;
            margin-bottom: 8px;
            font-family: inherit;
            outline: none;
        }
        #locations-search:focus { border-color: var(--primary); }

        #left-locations-list { 
            display: flex; 
            flex-direction: column; 
            gap: 6px; 
            max-height: 240px; 
            overflow-y: auto; 
            padding-right: 2px;
        }

        .loc-item {
            display: flex; 
            justify-content: space-between; 
            align-items: center; 
            background: white; 
            padding: 8px 12px; 
            border-radius: 10px; 
            font-size: 0.82rem; 
            font-weight: 700; 
            border: 1.5px solid #e2e8f0; 
            cursor: pointer; 
            transition: all 0.2s;
        }
        .loc-item:hover { border-color: #93c5fd; background: #f0f7ff; }
        .loc-item.active { border-color: var(--primary); background: #e0f2fe; color: var(--primary); }
        .loc-badge { font-size: 0.7rem; padding: 2px 7px; border-radius: 6px; }

        button { 
            font-family: inherit;
            border-radius: 12px; 
            font-weight: 700; 
            border: none; 
            cursor: pointer; 
            padding: 12px; 
            width: 100%; 
            margin-bottom: 10px; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            gap: 8px; 
            transition: all 0.2s; 
        }
        button:active { transform: scale(0.98); }
        button:disabled { opacity: 0.5; cursor: not-allowed; }
        .btn-main { background: var(--primary); color: white; font-size: 1rem; padding: 15px; box-shadow: 0 4px 12px rgba(67, 97, 238, 0.25); }
        .btn-main:hover { background: var(--primary-dark); }

        /* Canvas Wrapper & Responsive Canvas */
        .canvas-area {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
        }

        #canvas-wrapper { 
            position: relative; 
            width: 100%; 
            background: white; 
            border-radius: 20px; 
            box-shadow: var(--shadow); 
            overflow: hidden; 
            border: 6px solid white; 
            cursor: url('https://cdn-icons-png.flaticon.com/32/588/588395.png') 0 32, crosshair; 
            touch-action: none; 
            margin: 0 auto;
            transition: max-width 0.3s ease, aspect-ratio 0.3s ease;
        }

        /* Adaptive aspect ratios */
        .wrapper-srilanka {
            max-width: 460px;
            aspect-ratio: 450 / 630;
        }

        .wrapper-world {
            max-width: 720px;
            aspect-ratio: 630 / 450;
        }

        #canvas-wrapper:fullscreen {
            width: 100vw !important; 
            height: 100vh !important; 
            max-width: none !important; 
            border: none !important; 
            border-radius: 0 !important;
            display: flex; 
            align-items: center; 
            justify-content: center; 
            background: #111827;
        }
        
        #mainCanvas { 
            position: absolute; 
            top: 0; 
            left: 0; 
            z-index: 10; 
            width: 100%; 
            height: 100%; 
            transform-origin: 0 0; 
        }

        #map-img { 
            width: 100%; 
            height: 100%; 
            object-fit: contain; 
            pointer-events: none; 
            transform-origin: 0 0; 
            display: block; 
        }
        
        .zoom-controls { 
            position: absolute; 
            bottom: 16px; 
            left: 16px; 
            z-index: 100; 
            display: flex; 
            flex-direction: column; 
            gap: 8px; 
        }

        .zoom-btn {
            width: 42px; 
            height: 42px; 
            border-radius: 12px; 
            background: rgba(255,255,255,0.95);
            border: 1px solid rgba(0,0,0,0.1); 
            font-size: 20px; 
            font-weight: bold;
            cursor: pointer; 
            display: flex; 
            align-items: center; 
            justify-content: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.12); 
            color: var(--primary);
            padding: 0;
            margin: 0;
            backdrop-filter: blur(4px);
        }
        .zoom-btn:hover { background: #ffffff; color: var(--primary-dark); }

        #floating-task-list {
            position: absolute; 
            top: 10px; 
            right: 10px; 
            z-index: 100; 
            background: rgba(255, 255, 255, 0.92); 
            backdrop-filter: blur(6px);
            padding: 8px 12px; 
            border-radius: 12px; 
            border: 1px solid rgba(0,0,0,0.08); 
            max-width: 160px; 
            max-height: 180px; 
            overflow-y: auto;
            pointer-events: none; 
            box-shadow: 0 4px 12px rgba(0,0,0,0.1); 
            transition: opacity 0.3s ease;
        }
        .floating-item { font-size: 11px; font-weight: 700; color: #333; margin-bottom: 4px; display: flex; align-items: center; gap: 5px; }
        .floating-item.active { color: var(--primary); transform: scale(1.05); }

        #current-task-overlay {
            position: absolute; 
            top: 15px; 
            left: 50%; 
            transform: translateX(-50%); 
            z-index: 101; 
            background: rgba(67, 97, 238, 0.92); 
            color: white; 
            padding: 7px 18px; 
            border-radius: 50px; 
            font-weight: 800; 
            font-size: 13px; 
            pointer-events: none; 
            box-shadow: 0 5px 15px rgba(0,0,0,0.2); 
            display: none;
            backdrop-filter: blur(4px);
        }

        #action-popup { 
            position: absolute; 
            display: none; 
            z-index: 200; 
            gap: 10px; 
            background: transparent; 
            padding: 0; 
            border: none; 
            box-shadow: none; 
        }

        .pop-btn { 
            width: 42px; 
            height: 42px; 
            border-radius: 50%; 
            border: 2px solid white; 
            cursor: pointer; 
            color: white; 
            font-size: 18px; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            transition: 0.2s; 
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            margin: 0;
            padding: 0;
        }
        .pop-btn:hover { transform: scale(1.15); }
        .confirm-btn { background: #2ecc71; }
        .delete-btn { background: #f72585; }

        .confirm-pulse {
            position: absolute; 
            width: 30px; 
            height: 30px; 
            background: rgba(46, 204, 113, 0.5);
            border: 2px solid #2ecc71; 
            border-radius: 50%; 
            pointer-events: none; 
            z-index: 99;
            transform: translate(-50%, -50%); 
            animation: pulse-out 1s ease-out forwards;
        }

        @keyframes pulse-out {
            0% { transform: translate(-50%, -50%) scale(0.5); opacity: 1; }
            100% { transform: translate(-50%, -50%) scale(3); opacity: 0; }
        }

        .scroll-nav { 
            position: fixed; 
            right: 15px; 
            bottom: 80px; 
            display: flex; 
            flex-direction: column; 
            gap: 10px; 
            z-index: 9999; 
        }

        .scroll-btn { 
            width: 48px; 
            height: 48px; 
            border-radius: 50%; 
            background: var(--dark); 
            color: white; 
            border: 3px solid white; 
            font-size: 18px; 
            cursor: pointer; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.3); 
            opacity: 0.85; 
            padding: 0;
            margin: 0;
        }
        .scroll-btn:hover { opacity: 1; transform: scale(1.05); }

        #guide-hand { 
            position: fixed; 
            width: 40px; 
            height: 40px; 
            font-size: 40px; 
            z-index: 9999; 
            display: none; 
            pointer-events: none; 
            animation: hand-tap 1.5s infinite ease-in-out; 
            text-shadow: 0 2px 5px rgba(0,0,0,0.3); 
        }
        @keyframes hand-tap { 0%, 100% { transform: scale(1) translateY(0); } 50% { transform: scale(1.2) translateY(-10px); } }

        /* Admin Section */
        .admin-section { margin-top: 10px; border: 1px solid #e2e8f0; border-radius: 14px; overflow: hidden; }
        .admin-header { background: #f1f5f9; padding: 10px 14px; cursor: pointer; font-weight: 800; font-size: 0.82rem; display: flex; justify-content: space-between; }
        .admin-content { display: none; padding: 12px; background: white; }
        .admin-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 6px; }
        .tool-btn { font-size: 0.72rem; background: #fff; border: 1px solid #cbd5e1; padding: 8px 6px; margin-bottom: 0; }
        .tool-btn.active { background: var(--primary); color: white; border-color: var(--primary); }
        .slider-box { background: #f8fafc; padding: 8px 10px; border-radius: 8px; grid-column: span 2; margin-bottom: 5px; font-size: 0.8rem; font-weight: 600; }
        
        .admin-item-row { display: flex; justify-content: space-between; align-items: center; background: #f8fafc; padding: 6px 10px; border-radius: 8px; margin-bottom: 5px; font-size: 0.8rem; font-weight: 700; border: 1px solid #e2e8f0; }
        .admin-item-actions { display: flex; gap: 4px; }
        .admin-mini-btn { padding: 4px 8px; border-radius: 6px; font-size: 0.75rem; font-weight: 800; border: none; cursor: pointer; color: white; width: auto; margin: 0; }
        .btn-r { background: #f39c12; }
        .btn-m { background: #3498db; }
        .btn-d { background: #e74c3c; }

        @media (max-width: 900px) { 
            .header-section { flex-direction: column; text-align: center; }
            .category-switcher { flex-direction: column; }
            .main-layout { grid-template-columns: 1fr; width: 100%; } 
            .canvas-area { order: -1; margin-bottom: 15px; }
        }

        .success-ripple {
            position: absolute; 
            border: 4px solid var(--success); 
            border-radius: 50%;
            pointer-events: none; 
            z-index: 99; 
            animation: ripple-effect 0.8s ease-out forwards;
        }

        @keyframes ripple-effect {
            0% { transform: translate(-50%, -50%) scale(0.5); opacity: 1; border-width: 8px; }
            100% { transform: translate(-50%, -50%) scale(4); opacity: 0; border-width: 1px; }
        }
    </style>
</head>
<body>

    <div id="guide-hand">👆</div>

    <div class="scroll-nav">
        <button class="scroll-btn" onclick="window.scrollBy({top: -300, behavior: 'smooth'})" title="ඉහළට">▲</button>
        <button class="scroll-btn" onclick="window.scrollBy({top: 300, behavior: 'smooth'})" title="පහළට">▼</button>
    </div>

    <!-- Header Section -->
    <div class="header-section">
        <div class="app-logo" id="main-app-title">
            SL MAP LAB PRO <span class="badge">Unified Pro v23.0</span>
        </div>
        <div class="header-status-box">
            <div id="page-display">පිටුව: 1</div>
        </div>
    </div>

    <!-- Category Switcher: Sri Lanka Map vs World Map -->
    <div class="category-switcher">
        <button class="cat-tab-btn active" id="tab-cat-sl" onclick="switchCategory('srilanka')">
            🇱🇰 ශ්‍රී ලංකා සිතියම (Sri Lanka Map)
        </button>
        <button class="cat-tab-btn" id="tab-cat-world" onclick="switchCategory('world')">
            🌍 ලෝක සිතියම - O/L පසුගිය විභාග (World Map)
        </button>
    </div>

    <!-- Sub Navigation Bar (Years or Pages) -->
    <div class="sub-nav-bar" id="sub-nav-container"></div>

    <!-- Step Instruction Banner -->
    <div id="step-instruction">ආයුබෝවන්! වම් පසින් ස්ථානයක් තෝරා සිතියම මත ලකුණු කරන්න.</div>
    
    <!-- Main Content Layout -->
    <div class="main-layout">
        <!-- Sidebar -->
        <div class="sidebar">
            <div class="score-card" id="main-score-card">
                <p>සමස්ත ලකුණු</p>
                <h1><span id="s-val">0</span> / <span id="t-val">0</span></h1>
            </div>

            <div class="locations-box">
                <div class="locations-box-header">
                    <span>📍 ස්ථාන ලැයිස්තුව</span>
                    <button id="guide-btn" style="background:#fff3cd; color:#856404; border: 1px solid #ffeeba; padding: 4px 12px; border-radius: 20px; font-size: 0.72rem; font-weight: 700; cursor: pointer; width: auto; margin:0;" onclick="startSingleGuide()">✨ Guide</button>
                </div>
                <input type="text" id="locations-search" placeholder="ස්ථානයක් සොයන්න..." oninput="filterLocationsList(this.value)">
                <div id="left-locations-list"></div>
            </div>

            <button class="btn-main" id="check-btn" onclick="evaluateAll(); scrollToCanvas()">🔍 පරීක්ෂා කරන්න (Check)</button>
            <button style="background: #ff9f43; color: white;" onclick="showNextError(); scrollToCanvas()">🎯 වැරදි එකින් එක බලන්න</button>
            <button style="background: var(--show-ans); color: white;" id="ans-toggle" onclick="toggleCorrectAnswers(); scrollToCanvas()">👁️ නිවැරදි ස්ථාන පෙන්වන්න</button>
            <button style="background: var(--share-color); color: white;" onclick="shareMap()">📲 Share Result</button>
            
            <hr style="border:0; border-top:1px solid #e2e8f0; margin:15px 0;">
            <button onclick="resetStudent(); scrollToCanvas()" style="background:#fef2f2; color:#dc2626;">🗑️ සියල්ල මකන්න</button>
            <button onclick="exportImage()" style="background:#f5f3ff; color:#7c3aed;">📸 සිතියම Save</button>

            <div id="error-panel" style="margin-top: 15px; padding: 15px; border-radius: 15px; background: #fff5f5; border: 1px solid #feb2b2; display: none;"><div id="error-list"></div></div>
            
            <button id="admin-login-btn" style="margin-top:20px; font-size:11px; color:#94a3b8; background:none;" onclick="adminLogin()">🔐 Admin Login</button>

            <!-- Admin Panel (Password: 4112) -->
            <div id="admin-panel" style="display:none;">
                <button style="background: #2ecc71; color:white; font-weight: 800;" onclick="saveToFirebase()">☁️ Cloud Firebase Save</button>
                <button style="background: var(--gas-color); color:white; font-weight: 800;" onclick="saveToGoogleAppsScript()">📁 Google Drive (GAS) Save</button>
                <button style="background: #0f172a; color:white; font-weight: 800;" onclick="loadFromGoogleAppsScript()">📁 Google Drive (GAS) Load</button>
                <button style="background: var(--drive-color); color:white; font-weight: 800;" onclick="openGoogleDriveFolder()">📂 Open Google Drive Folder</button>
                <button style="background: #3b82f6; color:white; font-weight: 800;" onclick="importFromGoogleDriveJSON()">☁️ Google Drive JSON Import</button>
                <button style="background: var(--zip-color); color:white;" onclick="exportFullZip()">📦 ZIP Backup</button>
                
                <div class="admin-section">
                    <div class="admin-header" onclick="toggleAdminSec('sec1')">📍 මෙවලම් හා ස්ථාන කළමනාකරණය <span>▼</span></div>
                    <div id="sec1" class="admin-content" style="display:block;">
                        <div class="admin-grid">
                            <button class="tool-btn" id="point-btn" onclick="setMode('point')">📍 Point</button>
                            <button class="tool-btn" id="path-btn" onclick="setMode('path')">🌊 Path (ගංගා/මාර්ග)</button>
                            <button class="tool-btn" id="draw-shape-btn" onclick="setShapeMode()">📐 Free Shape</button>
                            <button class="tool-btn" onclick="bulkAddAll()" style="background: #10b981; color: white;">➕ Bulk Add</button>
                            <button class="tool-btn" onclick="undoPathPoint()" style="color:#e67e22">🔙 Undo Seg</button>
                            <button class="tool-btn" onclick="finishRiverPath()" style="background:#e0f2fe;">✍️ Finish Path</button>
                            <button class="tool-btn" onclick="saveFreeShape()" style="background:#dcfce7; grid-column: span 2;">✅ Save Shape</button>
                            <button class="tool-btn" onclick="undoTeacher()">↩️ Undo Item</button>
                            <button class="tool-btn" onclick="clearTeacher()" style="color:red;">🗑️ Clear All</button>
                        </div>
                        <div class="slider-box" style="margin-top:8px;">
                            <label>🎨 Shape Color:</label>
                            <input type="color" id="shape-color" value="#4361ee" style="width:100%; border:none; height:28px; cursor:pointer;">
                        </div>
                        <div id="admin-items-list" style="margin-top: 10px; max-height: 180px; overflow-y: auto;"></div>
                    </div>
                </div>

                <div class="admin-section">
                    <div class="admin-header" onclick="toggleAdminSec('sec2')">⚙️ සැකසුම් <span>▼</span></div>
                    <div id="sec2" class="admin-content">
                        <div class="slider-box"><label>🎯 හඳුනාගැනීමේ පරාසය: <span id="rad-val">25</span></label><input type="range" min="0" max="100" value="25" oninput="updateRadius(this.value)"></div>
                        <div class="slider-box"><label>📍 ලක්ෂ්‍යයේ ප්‍රමාණය: <span id="dot-val">6</span></label><input type="range" min="0" max="100" value="6" oninput="updateDotSize(this.value)"></div>
                        <div class="slider-box"><label>🎯 Path Tolerance: <span id="tol-val">35</span></label><input type="range" min="0" max="100" value="35" oninput="updateTolerance(this.value)"></div>
                        <div class="slider-box"><label>📏 Font Size: <span id="font-val">12</span></label><input type="range" min="0" max="100" value="12" oninput="updateFontSize(this.value)"></div>
                        <div class="admin-grid">
                            <button class="tool-btn" onclick="renameApp()">📛 Rename App</button>
                            <button id="global-label-toggle" class="tool-btn" onclick="toggleTeacherLabels()" style="background: #f39c12; color: white;">🏷️ Labels Hide</button>
                            <button class="tool-btn" onclick="toggleGhost()">👻 Ghost Mode</button>
                            <button class="tool-btn" onclick="document.getElementById('map-up').click()">🖼️ Change Map</button>
                            <input type="file" id="map-up" style="display:none" onchange="uploadMap(this)">
                        </div>
                    </div>
                </div>

                <div class="admin-section">
                    <div class="admin-header" onclick="toggleAdminSec('sec3')">📄 පිටු හා දත්ත කළමනාකරණය <span>▼</span></div>
                    <div id="sec3" class="admin-content">
                        <div class="admin-grid">
                            <button class="tool-btn" onclick="addNewPage()">➕ New Page</button>
                            <button class="tool-btn" onclick="renameCurrentPage()">📄 Rename Page</button>
                            <button class="tool-btn" onclick="deleteCurrentPage()" style="color:red; grid-column: span 2;">❌ Delete Page</button>
                            <button class="tool-btn" onclick="exportJSON()">📤 Export JSON</button>
                            <button class="tool-btn" onclick="importJSON()">📥 Import JSON</button>
                            <button class="tool-btn" onclick="saveToLocal()" style="background:#d1ffde; grid-column: span 2;">💾 Local Permanent Save</button>
                        </div>
                    </div>
                </div>

                <button class="tool-btn" style="margin-top:10px;" onclick="adminLogout()">🔒 Logout</button>
            </div>
        </div>

        <!-- Canvas Area -->
        <div class="canvas-area">
            <div id="canvas-wrapper" class="wrapper-srilanka">
                <div id="floating-task-list"></div>
                <div id="current-task-overlay"></div>
                
                <div class="zoom-controls">
                    <button class="zoom-btn" onclick="zoomIn()" title="විශාල කරන්න">+</button>
                    <button class="zoom-btn" onclick="zoomOut()" title="කුඩා කරන්න">-</button>
                    <button class="zoom-btn" onclick="toggleFullscreen()" title="සම්පූර්ණ තිරය (Fullscreen)">⛶</button>
                </div>

                <div id="action-popup">
                    <button class="pop-btn confirm-btn" onclick="confirmAction()" title="තහවුරු කරන්න">✅</button>
                    <button class="pop-btn delete-btn" onclick="deleteAction()" title="ඉවත් කරන්න">🗑️</button>
                </div>

                <img id="map-img" alt="Map">
                <canvas id="mainCanvas"></canvas>
            </div>
        </div>
    </div>

<script>
    // Embedded High-Resolution Base64 Map Images for 100% offline reliability
    const DEFAULT_SL_MAP = "SL_MAP_BASE64_PLACEHOLDER";
    const DEFAULT_WORLD_MAP = "WORLD_MAP_BASE64_PLACEHOLDER";
    const DRIVE_WORLD_MAP_URL = "https://lh3.googleusercontent.com/d/1Fgxo8NnrYi28x6pjoSYyapYJOWpYiL72";

    const firebaseConfig = {
        apiKey: "AIzaSyCWv8i2yxzhYCtSaEYWbCeSVtvguJs7IAE",
        authDomain: "asankasampath2026.firebaseapp.com",
        projectId: "asankasampath2026",
        storageBucket: "asankasampath2026.firebasestorage.app",
        messagingSenderId: "490777755966",
        appId: "1:490777755966:web:d7b506b8af321c9b17ac6f",
        measurementId: "G-ZV8CWD7GVL",
        databaseURL: "https://asankasampath2026-default-rtdb.asia-southeast1.firebasedatabase.app/"
    };
    firebase.initializeApp(firebaseConfig);
    const database = firebase.database();

    const canvas = document.getElementById('mainCanvas'); 
    const ctx = canvas.getContext('2d'); 
    const mapImg = document.getElementById('map-img');
    const hand = document.getElementById('guide-hand');
    const wrapper = document.getElementById('canvas-wrapper');
    const guideBtn = document.getElementById('guide-btn');
    const actionPopup = document.getElementById('action-popup');

    const defaultYears = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026];

    // Load any legacy data from App 1 or App 2 or the unified format
    let legacySL = JSON.parse(localStorage.getItem('map_lab_v22_final'));
    let legacyWorld = JSON.parse(localStorage.getItem('map_lab_v22_final_v3'));
    let unifiedStorage = JSON.parse(localStorage.getItem('map_lab_unified_v23'));

    let appState = unifiedStorage || {
        activeCategory: 'srilanka',
        appTitle: localStorage.getItem('map_lab_title') || "SL MAP LAB PRO & SOCIAL MASTER",
        srilanka: {
            curP: 0,
            pages: legacySL || [
                {
                    name: "පිටුව 1",
                    width: 450,
                    height: 630,
                    map: DEFAULT_SL_MAP,
                    teacher: [],
                    pointRadius: 25,
                    dotSize: 6,
                    fontSize: 12,
                    pathTolerance: 35,
                    labels: true
                }
            ]
        },
        world: {
            curP: 0,
            pages: legacyWorld || defaultYears.map(y => ({
                name: y.toString(),
                width: 630,
                height: 450,
                map: DEFAULT_WORLD_MAP,
                teacher: [],
                pointRadius: 25,
                dotSize: 6,
                fontSize: 12,
                pathTolerance: 35,
                labels: true
            }))
        }
    };

    // Ensure map paths are properly initialized
    appState.srilanka.pages.forEach(pg => {
        if (!pg.width) pg.width = 450;
        if (!pg.height) pg.height = 630;
        if (!pg.map || pg.map === "Slide2.JPG") pg.map = DEFAULT_SL_MAP;
    });

    appState.world.pages.forEach(pg => {
        if (!pg.width) pg.width = 630;
        if (!pg.height) pg.height = 450;
        if (!pg.map || pg.map.includes("2002 (1).jpg") || pg.map.includes("drive.google.com")) {
            pg.map = DEFAULT_WORLD_MAP;
        }
    });

    let student = [];
    let activeTask = null;
    let isAdmin = false;
    let mode = 'point';
    let showAnswers = false;
    let currentErrorPath = null;
    let draggingObj = null;
    let resizingObj = null;
    let isDrawing = false;
    let tempStroke = [];
    let currentRiverPoints = [];
    let evaluated = false;
    let isErrorReviewMode = false;
    let errorIndex = 0;
    let tutorialTimeout = null;
    let currentShapePoints = [];
    let isDrawingShape = false;
    let waitingForConfirm = false;
    let glowAlpha = 0;
    let glowDirection = 1;
    let scale = 1, lastX = 0, lastY = 0, offsetX = 0, offsetY = 0, isPinching = false, startDist = 0;

    let successMessageTimer = 0;
    let lastCorrectObjForMessage = null;
    let isTeacherLabelsVisible = true;
    let movingTargetObj = null;
    let locationFilterQuery = "";

    function switchCategory(category) {
        appState.activeCategory = category;
        
        document.getElementById('tab-cat-sl').classList.toggle('active', category === 'srilanka');
        document.getElementById('tab-cat-world').classList.toggle('active', category === 'world');

        wrapper.className = category === 'srilanka' ? 'wrapper-srilanka' : 'wrapper-world';

        saveToLocal();
        init();
    }

    function getCurrentPage() {
        const cat = appState.activeCategory;
        const curIndex = appState[cat].curP;
        if (!appState[cat].pages[curIndex]) {
            appState[cat].curP = 0;
        }
        return appState[cat].pages[appState[cat].curP];
    }

    function init() {
        clearTimeout(tutorialTimeout);
        hand.style.display = 'none';
        actionPopup.style.display = 'none';
        waitingForConfirm = false;
        isErrorReviewMode = false;
        successMessageTimer = 0;
        lastCorrectObjForMessage = null;
        movingTargetObj = null;
        resetZoom();

        document.getElementById('main-app-title').innerHTML = `${appState.appTitle} <span class="badge">Unified Pro v23.0</span>`;

        const cat = appState.activeCategory;
        const p = getCurrentPage();

        // Canvas dimensions & wrapper aspect ratio
        const targetW = p.width || (cat === 'srilanka' ? 450 : 630);
        const targetH = p.height || (cat === 'srilanka' ? 630 : 450);
        canvas.width = targetW;
        canvas.height = targetH;

        if (cat === 'srilanka') {
            wrapper.style.maxWidth = '460px';
            wrapper.style.aspectRatio = '450 / 630';
            document.getElementById('page-display').innerText = "පිටුව: " + p.name;
        } else {
            wrapper.style.maxWidth = '720px';
            wrapper.style.aspectRatio = '630 / 450';
            document.getElementById('page-display').innerText = "වර්ෂය: " + p.name;
        }

        mapImg.src = p.map;

        document.getElementById('rad-val').innerText = p.pointRadius || 25;
        document.getElementById('dot-val').innerText = p.dotSize || 6;
        document.getElementById('font-val').innerText = p.fontSize || 12;
        document.getElementById('tol-val').innerText = p.pathTolerance || 35;

        student = [];
        evaluated = false;
        activeTask = null;
        errorIndex = 0;
        currentErrorPath = null;

        document.getElementById('s-val').innerText = "0";
        document.getElementById('t-val').innerText = (p.teacher || []).length;
        document.getElementById('error-panel').style.display = 'none';
        
        const welcomeText = cat === 'srilanka' 
            ? "ආයුබෝවන්! ශ්‍රී ලංකා සිතියම සඳහා ස්ථානයක් තෝරා ආරම්භ කරන්න." 
            : "ආයුබෝවන්! වර්ෂයක් තෝරා වම් පසින් ස්ථානයක් ක්ලික් කර ආරම්භ කරන්න.";
        document.getElementById('step-instruction').innerText = welcomeText;
        document.getElementById('step-instruction').style.background = "linear-gradient(90deg, #4361ee, #4cc9f0)";
        document.getElementById('ans-toggle').innerText = "👁️ නිවැරදි ස්ථාන පෙන්වන්න";
        if (guideBtn) guideBtn.disabled = false;

        renderSubNavBar();
        renderTasks();
        renderAdminItemsList();
        redraw();
    }

    function renderSubNavBar() {
        const container = document.getElementById('sub-nav-container');
        if (!container) return;
        container.innerHTML = "";
        
        const cat = appState.activeCategory;
        const pagesList = appState[cat].pages;
        const curIndex = appState[cat].curP;

        // In Sri Lanka mode, also provide Previous / Next page arrows
        if (cat === 'srilanka') {
            const prevBtn = document.createElement('button');
            prevBtn.className = "nav-chip-btn";
            prevBtn.innerHTML = "◀ පෙර පිටුව";
            prevBtn.onclick = () => {
                if (appState.srilanka.curP > 0) {
                    appState.srilanka.curP--;
                    init();
                }
            };
            container.appendChild(prevBtn);
        }

        pagesList.forEach((pg, index) => {
            const btn = document.createElement('button');
            btn.className = `nav-chip-btn ${curIndex === index ? 'active' : ''}`;
            const prefix = cat === 'world' ? '📅 ' : '📄 ';
            btn.innerText = prefix + pg.name;
            btn.onclick = () => {
                appState[cat].curP = index;
                init();
            };
            container.appendChild(btn);
        });

        if (cat === 'srilanka') {
            const nextBtn = document.createElement('button');
            nextBtn.className = "nav-chip-btn";
            nextBtn.innerHTML = "මීළඟ පිටුව ▶";
            nextBtn.onclick = () => {
                if (appState.srilanka.curP < appState.srilanka.pages.length - 1) {
                    appState.srilanka.curP++;
                    init();
                }
            };
            container.appendChild(nextBtn);

            const addBtn = document.createElement('button');
            addBtn.className = "nav-chip-btn nav-chip-action";
            addBtn.innerHTML = "➕ නව පිටුව";
            addBtn.onclick = addNewPage;
            container.appendChild(addBtn);
        } else {
            const addYearBtn = document.createElement('button');
            addYearBtn.className = "nav-chip-btn nav-chip-action";
            addYearBtn.innerHTML = "➕ නව වර්ෂය";
            addYearBtn.onclick = addNewPage;
            container.appendChild(addYearBtn);
        }
    }

    function saveToLocal() {
        localStorage.setItem('map_lab_unified_v23', JSON.stringify(appState));
        localStorage.setItem('map_lab_v22_final', JSON.stringify(appState.srilanka.pages));
        localStorage.setItem('map_lab_v22_final_v3', JSON.stringify(appState.world.pages));
        localStorage.setItem('map_lab_title', appState.appTitle);
    }

    function renderTasks() {
        const listContainer = document.getElementById('left-locations-list');
        if (!listContainer) return;
        const p = getCurrentPage();
        const teacherData = p.teacher || [];

        let filtered = teacherData;
        if (locationFilterQuery.trim() !== "") {
            filtered = teacherData.filter(t => t.name.toLowerCase().includes(locationFilterQuery.toLowerCase()));
        }

        if (filtered.length === 0) {
            listContainer.innerHTML = "<div style='font-size:0.75rem; color:#888; text-align:center; padding:10px;'>ස්ථාන කිසිවක් සොයා ගැනීමට නොහැක.</div>";
            return;
        }

        let html = "";
        filtered.forEach((t) => {
            const originalIndex = teacherData.indexOf(t);
            const done = student.some(s => s.name === t.name);
            const isActive = activeTask === t;
            let icon = '📍';
            if (t.type === 'path') icon = '🌊';
            else if (t.type === 'shape') icon = '📐';

            html += `<div class="loc-item ${isActive ? 'active' : ''}" onclick="selectTaskByName('${t.name.replace(/'/g, "\\'")}')">
                <span>${icon} ${originalIndex + 1}. ${t.name}</span>
                <span class="loc-badge" style="background:${done ? '#dcfce7; color:#166534;' : '#f1f5f9; color:#64748b;'}">${done ? '✓ ලකුණු කර ඇත' : 'ඉතිරි'}</span>
            </div>`;
        });
        listContainer.innerHTML = html;
    }

    function filterLocationsList(q) {
        locationFilterQuery = q;
        renderTasks();
    }

    function selectTaskByName(name) {
        const p = getCurrentPage();
        const t = (p.teacher || []).find(x => x.name === name);
        if (t && !evaluated && !waitingForConfirm && !isErrorReviewMode) {
            activeTask = t;
            if (guideBtn) guideBtn.disabled = true;
            renderTasks();
            updateSteps();
            scrollToCanvas();
        }
    }

    function updateSteps() { 
        if (!evaluated) { 
            let icon = '📍';
            if (activeTask && activeTask.type === 'path') icon = '🌊';
            else if (activeTask && activeTask.type === 'shape') icon = '📐';
            document.getElementById('step-instruction').innerText = activeTask ? `${icon} ${activeTask.name} ලකුණු කරන්න.` : "ස්ථාන ලැයිස්තුවෙන් නමක් තෝරන්න."; 
        } 
    }

    function autoNext() { 
        const p = getCurrentPage(); 
        const teacherData = p.teacher || []; 
        const nextTask = teacherData.find(t => !student.some(s => s.name === t.name)); 
        activeTask = nextTask || null; 
        renderTasks(); 
        updateSteps(); 
    }

    function renderAdminItemsList() {
        const listContainer = document.getElementById('admin-items-list');
        if (!listContainer) return;
        const p = getCurrentPage();
        const teacherData = p.teacher || [];
        
        if (teacherData.length === 0) {
            listContainer.innerHTML = "<div style='font-size:0.75rem; color:#888; text-align:center;'>ස්ථාන කිසිවක් නොමැත.</div>";
            return;
        }

        let html = "";
        teacherData.forEach((t, index) => {
            html += `<div class="admin-item-row">
                <span>${index + 1}. ${t.name}</span>
                <div class="admin-item-actions">
                    <button class="admin-mini-btn btn-r" onclick="renameItem(${index})" title="නම වෙනස් කරන්න">R</button>
                    <button class="admin-mini-btn btn-m" onclick="modifyPosition(${index})" title="ස්ථානය වෙනස් කරන්න">M</button>
                    <button class="admin-mini-btn btn-d" onclick="deleteTeacherItem(${index})" title="මකන්න">✕</button>
                </div>
            </div>`;
        });
        listContainer.innerHTML = html;
    }

    function renameItem(index) {
        const p = getCurrentPage();
        const t = p.teacher[index];
        if (!t) return;
        const newName = prompt(`නව නම ඇතුළත් කරන්න (${t.name}):`, t.name);
        if (newName !== null && newName.trim() !== "") {
            t.name = newName.trim();
            saveToLocal();
            renderTasks();
            renderAdminItemsList();
            redraw();
        }
    }

    function deleteTeacherItem(index) {
        const p = getCurrentPage();
        if (confirm(`'${p.teacher[index].name}' ඉවත් කරන්නද?`)) {
            p.teacher.splice(index, 1);
            saveToLocal();
            renderTasks();
            renderAdminItemsList();
            redraw();
        }
    }

    function modifyPosition(index) {
        const p = getCurrentPage();
        const t = p.teacher[index];
        if (!t) return;
        movingTargetObj = t;
        isAdmin = true;
        alert(`'${t.name}' සඳහා නව ස්ථානය සිතියම මත ක්ලික් කරන්න.`);
        document.getElementById('step-instruction').innerText = `ස්ථානය වෙනස් කරන්න: '${t.name}' සඳහා සිතියම මත නව තැනක් ක්ලික් කරන්න.`;
    }

    function bulkAddAll() {
        const input = prompt("ස්ථාන නම් කොමා (,) මඟින් වෙන් කර ඇතුළත් කරන්න (උදා: අනුරාධපුරය, පොළොන්නරුව, සීගිරිය):");
        if (!input) return;
        const names = input.split(',').map(n => n.trim()).filter(n => n.length > 0);
        if (names.length === 0) return;

        const p = getCurrentPage();
        let startX = 80;
        let startY = 80;
        names.forEach((name, i) => {
            p.teacher.push({
                type: 'point',
                name: name,
                x: startX + ((i % 5) * 80),
                y: startY + (Math.floor(i / 5) * 60),
                angle: -45,
                length: 40
            });
        });
        saveToLocal();
        renderTasks();
        renderAdminItemsList();
        redraw();
        alert(`ස්ථාන ${names.length}ක් සාර්ථකව එකතු කර Save කරන ලදී! ✅`);
    }

    function animateGlow() {
        glowAlpha += 0.05 * glowDirection;
        if (glowAlpha > 1) { glowAlpha = 1; glowDirection = -1; }
        if (glowAlpha < 0.3) { glowAlpha = 0.3; glowDirection = 1; }
        if (successMessageTimer > 0) successMessageTimer--;
        redraw();
        requestAnimationFrame(animateGlow);
    }
    requestAnimationFrame(animateGlow);

    function scrollToCanvas() {
        wrapper.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    function redraw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height); 
        const p = getCurrentPage();
        const teacherData = p.teacher || [];

        if (isAdmin || showAnswers) {
            teacherData.forEach(t => {
                if (t.type === 'path') {
                    ctx.strokeStyle = "rgba(46, 204, 113, 0.2)"; 
                    ctx.lineWidth = (p.pathTolerance || 35) * 2; 
                    ctx.lineCap = "round"; 
                    ctx.lineJoin = "round";
                    drawPath(t.data, null, true);
                } else if (t.type === 'point') {
                    ctx.fillStyle = "rgba(46, 204, 113, 0.15)"; 
                    ctx.beginPath(); 
                    ctx.arc(t.x, t.y, p.pointRadius || 25, 0, Math.PI*2); 
                    ctx.fill();
                }
                drawElement(t, "#2ecc71", true);
            });
        }
        
        if (isErrorReviewMode && currentErrorPath) {
            const studentAttempt = student.find(s => s.name === currentErrorPath.name);
            const isCorrectInReview = studentAttempt && checkCorrectness(studentAttempt, currentErrorPath, p);

            if (studentAttempt) {
                const sx = studentAttempt.x || (studentAttempt.data ? studentAttempt.data[0].x : 0);
                const sy = studentAttempt.y || (studentAttempt.data ? studentAttempt.data[0].y : 0);
                
                ctx.save();
                ctx.textAlign = "center";
                
                if (isCorrectInReview) {
                    ctx.font = "bold 35px Arial"; ctx.fillStyle = "#2ecc71"; ctx.fillText("✔", sx, sy - 25);
                    ctx.font = "40px Arial"; ctx.globalAlpha = glowAlpha; ctx.fillText("😊", sx, sy + 35);
                } else {
                    ctx.font = "bold 35px Arial"; ctx.fillStyle = "#f72585"; ctx.fillText("✘", sx, sy - 25);
                    ctx.font = "40px Arial"; ctx.globalAlpha = glowAlpha; ctx.fillText("😟", sx, sy + 35);
                }
                ctx.restore();
            }

            ctx.save();
            const color = "#2ecc71";
            if (currentErrorPath.type === 'path') {
                ctx.strokeStyle = "rgba(46, 204, 113, 0.4)"; 
                ctx.lineWidth = (p.pathTolerance || 35) * 2; 
                ctx.lineCap = "round"; 
                ctx.lineJoin = "round";
                drawPath(currentErrorPath.data, "rgba(46, 204, 113, 0.4)");
                drawElement(currentErrorPath, color, true);
            } else if (currentErrorPath.type === 'shape') {
                renderShape(currentErrorPath, true);
            } else if (currentErrorPath.type === 'point') {
                ctx.fillStyle = "rgba(46, 204, 113, 0.3)";
                ctx.beginPath(); 
                ctx.arc(currentErrorPath.x, currentErrorPath.y, p.pointRadius || 25, 0, Math.PI*2); 
                ctx.fill();
                drawElement(currentErrorPath, color, true);
            }
            ctx.restore();
        }

        if (!showAnswers && !isErrorReviewMode) {
            student.forEach(s => {
                const t = teacherData.find(x => x.name === s.name); 
                let color = "#4361ee";
                let isGlowPointOnly = false;

                if (s.isConfirmed) {
                    isGlowPointOnly = true;
                } else if (waitingForConfirm && activeTask && s.name === activeTask.name) {
                    isGlowPointOnly = true;
                }

                if (evaluated && t) {
                    const isCorrect = checkCorrectness(s, t, p);
                    color = isCorrect ? "#2ecc71" : "#f72585";
                    const tx = s.x || (s.data ? s.data[0].x : 0);
                    const ty = s.y || (s.data ? s.data[0].y : 0);
                    ctx.font = "bold 24px Arial"; ctx.fillStyle = color; ctx.fillText(isCorrect ? "✔" : "✘", tx, ty - 45);
                }

                if (isGlowPointOnly) {
                    ctx.save();
                    ctx.shadowBlur = 15;
                    ctx.shadowColor = "rgba(67, 97, 238, " + glowAlpha + ")";
                    drawElement(s, color, true, true); 
                    ctx.restore();
                } else {
                    drawElement(s, color, false);
                }
            });
        }

        if (isErrorReviewMode && successMessageTimer > 0 && lastCorrectObjForMessage) {
            const sx = lastCorrectObjForMessage.x || (lastCorrectObjForMessage.data ? lastCorrectObjForMessage.data[0].x : 0);
            const sy = lastCorrectObjForMessage.y || (lastCorrectObjForMessage.data ? lastCorrectObjForMessage.data[0].y : 0);
            
            ctx.save();
            const msg = "ඔබ නිවැරදියි! 😊";
            ctx.font = "bold 16px 'Noto Sans Sinhala'";
            const tw = ctx.measureText(msg).width;
            
            ctx.fillStyle = "rgba(46, 204, 113, 0.9)";
            ctx.beginPath();
            ctx.roundRect(sx - (tw/2) - 10, sy - 85, tw + 20, 35, 10);
            ctx.fill();
            
            ctx.fillStyle = "white"; ctx.textAlign = "center"; ctx.fillText(msg, sx, sy - 62);
            ctx.restore();
        }
        
        if (isDrawing) drawPath(tempStroke, "#ffa500");
        if (isAdmin && currentRiverPoints.length > 0) drawPath(currentRiverPoints, "#2ecc71");
        
        drawTemporaryShape();
        updateFloatingList();
        
        if (waitingForConfirm && (draggingObj || resizingObj)) {
            const anchor = getElementAnchor(draggingObj || resizingObj);
            updatePopupPosition(anchor.x, anchor.y);
        }
    }

    function getElementAnchor(el) {
        if (!el) return {x:0, y:0};
        if (el.type === 'path' || el.type === 'shape') {
            return {x: el.data[0].x, y: el.data[0].y};
        }
        return {x: el.x, y: el.y};
    }

    function updateFloatingList() {
        const floatingList = document.getElementById('floating-task-list');
        const overlay = document.getElementById('current-task-overlay');
        const p = getCurrentPage();
        const teacherData = p.teacher || [];
        
        if (isAdmin || evaluated || showAnswers || teacherData.length === 0 || isErrorReviewMode) {
            floatingList.style.display = 'none'; overlay.style.display = 'none'; return;
        }
        floatingList.style.display = 'block';
        let html = "";
        teacherData.forEach(t => {
            const isDone = student.some(s => s.name === t.name);
            if (!isDone) html += `<div class="floating-item ${activeTask === t ? 'active' : ''}">📍 ${t.name}</div>`;
        });
        floatingList.innerHTML = html;
        if (activeTask) { 
            let prefix = '📍 ';
            if (activeTask.type === 'path') prefix = '🌊 ';
            else if (activeTask.type === 'shape') prefix = '📐 ';
            overlay.style.display = 'block'; 
            overlay.innerText = prefix + activeTask.name; 
        }
        else { overlay.style.display = 'none'; }
    }

    function checkCorrectness(studentObj, teacherObj, page) {
        if (!studentObj || !teacherObj) return false;
        const tolerance = page.pathTolerance || 35;
        if (teacherObj.type === 'point') {
            return Math.hypot(studentObj.x - teacherObj.x, studentObj.y - teacherObj.y) <= (page.pointRadius || 25);
        }
        if (teacherObj.type === 'path' || teacherObj.type === 'shape') {
            if (!studentObj.data || studentObj.data.length === 0) return false;
            return studentObj.data.some(sp => {
                return teacherObj.data.some(tp => Math.hypot(sp.x - tp.x, sp.y - tp.y) <= tolerance);
            });
        }
        return false;
    }

    function toggleTeacherLabels() {
        isTeacherLabelsVisible = !isTeacherLabelsVisible;
        const btn = document.getElementById('global-label-toggle');
        btn.innerText = isTeacherLabelsVisible ? "🏷️ Labels Hide" : "👁️ Labels Show";
        btn.style.background = isTeacherLabelsVisible ? "#f39c12" : "#27ae60";
        redraw();
    }

    function drawElement(el, col, isTeach, glowPoint = false) {
        const p = getCurrentPage(); 
        if (el.type === 'shape') { renderShape(el, isTeach); return; }
        const tx = el.x || (el.data ? el.data[0].x : 0); 
        const ty = el.y || (el.data ? el.data[0].y : 0);
        const angle = el.angle || -45; const dSize = p.dotSize || 6; const length = el.length || 40;
        
        if (el.type === 'path') drawPath(el.data, col);
        else { 
            ctx.save();
            if (glowPoint) { ctx.shadowBlur = 15; ctx.shadowColor = col; }
            ctx.fillStyle = col; ctx.beginPath(); ctx.arc(tx, ty, dSize, 0, Math.PI*2); ctx.fill(); 
            ctx.strokeStyle = "white"; ctx.lineWidth = dSize/3; ctx.stroke();
            ctx.restore();
        }

        if (isTeach && !isTeacherLabelsVisible) return;

        if (isTeach || el.isConfirmed || (p.labels && !showAnswers)) {
            const angleRad = angle * Math.PI / 180; const fx = tx - length * Math.cos(angleRad); const fy = ty - length * Math.sin(angleRad);
            drawArrowLine(tx, ty, col, angle, length); ctx.font = `bold ${p.fontSize || 12}px 'Noto Sans Sinhala'`; ctx.fillStyle = "#333";
            ctx.textAlign = (fx < tx) ? "right" : "left"; 
            ctx.fillText(el.name, fx + (fx < tx ? -10 : 10), fy + 5); ctx.textAlign = "start";
        }
    }

    function renderShape(el, isTeach) {
        if (el.type !== 'shape') return;
        const p = getCurrentPage();
        ctx.save();
        const centerX = el.data[0].x; const centerY = el.data[0].y;
        ctx.translate(centerX, centerY);
        ctx.rotate((el.rotation || 0) * Math.PI / 180);
        ctx.scale(el.scale || 1, el.scale || 1);
        ctx.translate(-centerX, -centerY);
        ctx.beginPath();
        ctx.fillStyle = (isTeach || el.isConfirmed) ? (el.color || "rgba(46, 204, 113, 0.5)") : "rgba(67, 97, 238, 0.2)";
        el.data.forEach((pt, i) => { if (i === 0) ctx.moveTo(pt.x, pt.y); else ctx.lineTo(pt.x, pt.y); });
        ctx.closePath(); ctx.fill();
        ctx.strokeStyle = (isTeach || el.isConfirmed) ? (el.color || "#2ecc71") : "#4361ee"; ctx.lineWidth = 2; ctx.stroke();
        
        if (isTeacherLabelsVisible || !isTeach) {
            if (el.showLabel !== false && (isTeach || el.isConfirmed || p.labels)) {
                ctx.fillStyle = "#000"; ctx.font = `bold ${p.fontSize || 12}px 'Inter'`;
                ctx.fillText(el.name, el.data[0].x, el.data[0].y - 10);
            }
        }
        ctx.restore();
    }

    function drawTemporaryShape() {
        if (isDrawingShape && currentShapePoints.length > 1) {
            ctx.beginPath();
            ctx.strokeStyle = document.getElementById('shape-color')?.value || "#4361ee";
            ctx.lineWidth = 2;
            currentShapePoints.forEach((pt, i) => { if (i === 0) ctx.moveTo(pt.x, pt.y); else ctx.lineTo(pt.x, pt.y); });
            ctx.stroke();
        }
    }

    function drawArrowLine(tx, ty, col, angleDegree = -45, length = 40) {
        const head = 10; const angleRad = angleDegree * Math.PI / 180;
        const fx = tx - length * Math.cos(angleRad); const fy = ty - length * Math.sin(angleRad);
        ctx.strokeStyle = col; ctx.lineWidth = 2; ctx.beginPath(); 
        ctx.moveTo(fx, fy); ctx.lineTo(tx, ty); 
        ctx.moveTo(tx, ty);
        ctx.lineTo(tx - head * Math.cos(angleRad - 0.5), ty - head * Math.sin(angleRad - 0.5));
        ctx.moveTo(tx, ty);
        ctx.lineTo(tx - head * Math.cos(angleRad + 0.5), ty - head * Math.sin(angleRad + 0.5)); 
        ctx.stroke();
    }

    function drawPath(pts, col, isBG = false) { 
        if (!pts || pts.length < 2) return; 
        if (!isBG) { ctx.strokeStyle = col; ctx.lineWidth = 4; ctx.lineCap = "round"; ctx.lineJoin = "round"; }
        ctx.beginPath(); let first = true;
        pts.forEach(p => { if (p.gap || first) { ctx.moveTo(p.x, p.y); first = false; } else { ctx.lineTo(p.x, p.y); } });
        ctx.stroke(); 
    }

    function zoomIn() { scale = Math.min(scale + 0.5, 4); updateTransform(); }
    function zoomOut() { 
        scale = Math.max(scale - 0.5, 1); 
        if (scale === 1) { offsetX = 0; offsetY = 0; } 
        updateTransform(); 
    }

    function toggleFullscreen() {
        if (!document.fullscreenElement) {
            if (wrapper.requestFullscreen) wrapper.requestFullscreen();
            else if (wrapper.webkitRequestFullscreen) wrapper.webkitRequestFullscreen();
        } else {
            if (document.exitFullscreen) document.exitFullscreen();
        }
    }

    wrapper.addEventListener('dblclick', toggleFullscreen);

    wrapper.addEventListener('touchstart', e => {
        if (e.touches.length === 2) {
            isPinching = true;
            startDist = Math.hypot(e.touches[0].pageX - e.touches[1].pageX, e.touches[0].pageY - e.touches[1].pageY);
        } else {
            lastX = e.touches[0].pageX; lastY = e.touches[0].pageY;
            handleStart(e);
        }
    }, {passive: false});

    wrapper.addEventListener('touchmove', e => {
        if (isPinching && e.touches.length === 2) {
            e.preventDefault();
            const dist = Math.hypot(e.touches[0].pageX - e.touches[1].pageX, e.touches[0].pageY - e.touches[1].pageY);
            scale *= dist / startDist;
            scale = Math.max(1, Math.min(scale, 4));
            startDist = dist;
            updateTransform();
        } else if (!isPinching) {
            if (scale > 1 && !draggingObj && !resizingObj && !isDrawing && !isDrawingShape) {
                e.preventDefault();
                offsetX += e.touches[0].pageX - lastX;
                offsetY += e.touches[0].pageY - lastY;
                lastX = e.touches[0].pageX; lastY = e.touches[0].pageY;
                updateTransform();
            } else {
                handleMove(e);
            }
        }
    }, {passive: false});

    wrapper.addEventListener('touchend', e => { isPinching = false; handleEnd(); });

    function updateTransform() {
        const transform = `translate(${offsetX}px, ${offsetY}px) scale(${scale})`;
        canvas.style.transform = transform;
        mapImg.style.transform = transform;
    }

    function resetZoom() { scale = 1; offsetX = 0; offsetY = 0; updateTransform(); }

    function getPos(e) { 
        const rect = wrapper.getBoundingClientRect(); 
        const clientX = e.clientX || (e.touches && e.touches[0].clientX); 
        const clientY = e.clientY || (e.touches && e.touches[0].clientY); 
        
        const screenX = clientX - rect.left - offsetX;
        const screenY = clientY - rect.top - offsetY;
        
        const p = getCurrentPage();
        const targetW = p.width || (appState.activeCategory === 'srilanka' ? 450 : 630);
        const targetH = p.height || (appState.activeCategory === 'srilanka' ? 630 : 450);

        const x = (screenX / scale) * (targetW / rect.width);
        const y = (screenY / scale) * (targetH / rect.height);
        return { x, y };
    }

    function updatePopupPosition(x, y) {
        const rect = wrapper.getBoundingClientRect();
        const p = getCurrentPage();
        const targetW = p.width || (appState.activeCategory === 'srilanka' ? 450 : 630);
        const targetH = p.height || (appState.activeCategory === 'srilanka' ? 630 : 450);

        const el = draggingObj || resizingObj || (activeTask ? student.find(s => s.name === activeTask.name) : null);
        let targetX = x, targetY = y;

        if (el) {
            const angleRad = (el.angle || -45) * Math.PI / 180;
            const length = el.length || 40;
            targetX = x - (length + 20) * Math.cos(angleRad);
            targetY = y - (length + 20) * Math.sin(angleRad);
        }

        let screenX = (targetX * (rect.width / targetW) * scale) + offsetX;
        let screenY = (targetY * (rect.height / targetH) * scale) + offsetY;

        if (screenX < 10) screenX = 10;
        if (screenX > rect.width - 100) screenX = rect.width - 100;
        if (screenY < 10) screenY = 10;
        if (screenY > rect.height - 50) screenY = rect.height - 50;
        
        actionPopup.style.left = screenX + 'px';
        actionPopup.style.top = screenY + 'px';
    }

    function handleStart(e) {
        if (showAnswers || isErrorReviewMode) return; 
        const pos = getPos(e); 
        const p = getCurrentPage();
        const teacherData = p.teacher || [];
        
        if (isAdmin && movingTargetObj) {
            movingTargetObj.x = pos.x;
            movingTargetObj.y = pos.y;
            movingTargetObj = null;
            saveToLocal();
            document.getElementById('step-instruction').innerText = "ස්ථානය සාර්ථකව වෙනස් කරන ලදී!";
            renderAdminItemsList();
            renderTasks();
            redraw();
            return;
        }

        if (isAdmin && mode === 'shape') {
            isDrawingShape = true; currentShapePoints = [pos]; redraw(); return;
        }

        const targetList = isAdmin ? teacherData : student;
        const resizeHit = targetList.find(t => { 
            const anchorX = t.x || (t.data ? t.data[0].x : 0); 
            const anchorY = t.y || (t.data ? t.data[0].y : 0);
            const angleRad = (t.angle || -45) * Math.PI / 180; 
            const fx = anchorX - (t.length || 40) * Math.cos(angleRad); 
            const fy = anchorY - (t.length || 40) * Math.sin(angleRad); 
            return Math.hypot(fx - pos.x, fy - pos.y) < 35; 
        });
        
        if (resizeHit) { 
            resizingObj = resizeHit; 
            if (!isAdmin) document.getElementById('step-instruction').innerText = "ඊතලය හසුරවන්න";
            return; 
        }
        
        const hitObj = targetList.find(pt => {
            const tx = pt.x || (pt.data ? pt.data[0].x : 0);
            const ty = pt.y || (pt.data ? pt.data[0].y : 0);
            return Math.hypot(tx - pos.x, ty - pos.y) < 40;
        });
        
        if (hitObj) {
            draggingObj = hitObj; 
            if (!isAdmin && !evaluated) document.getElementById('step-instruction').innerText = "ස්ථානය වෙනස් කරන්න";
            redraw();
            return;
        }
        
        if (!hitObj && !resizingObj && !evaluated && !waitingForConfirm) {
            if (isAdmin) { 
                if (mode === 'path') { isDrawing = true; tempStroke = [pos]; } 
                else if (mode === 'point') { 
                    const name = prompt("නම:"); 
                    if (name) {
                        teacherData.push({type:'point', name, x: pos.x, y: pos.y, angle: -45, length: 40});
                        saveToLocal();
                        renderAdminItemsList();
                        renderTasks();
                    }
                } 
            }
            else if (activeTask) { 
                if (activeTask.type === 'path' || activeTask.type === 'shape') { 
                    isDrawing = true; tempStroke = [pos]; 
                } else { 
                    student = student.filter(s => s.name !== activeTask.name); 
                    student.push({name: activeTask.name, type: 'point', x: pos.x, y: pos.y, angle: activeTask.angle || -45, length: activeTask.length || 40, isConfirmed: false}); 
                    showActionPopup(pos.x, pos.y);
                } 
            }
        }
        redraw();
    }

    function handleMove(e) {
        const pos = getPos(e); 
        if (resizingObj || draggingObj || isDrawing || isDrawingShape) { if (e.cancelable) e.preventDefault(); }
        
        if (isAdmin && mode === 'shape' && isDrawingShape) {
            currentShapePoints.push(pos); redraw(); return;
        }

        if (resizingObj) { 
            const anchorX = resizingObj.x || (resizingObj.data ? resizingObj.data[0].x : 0); 
            const anchorY = resizingObj.y || (resizingObj.data ? resizingObj.data[0].y : 0);
            const dx = anchorX - pos.x; const dy = anchorY - pos.y; 
            resizingObj.length = Math.hypot(dx, dy); 
            resizingObj.angle = Math.atan2(dy, dx) * (180 / Math.PI); 
            redraw();
        } 
        else if (draggingObj) { 
            if (draggingObj.type === 'path' || draggingObj.type === 'shape') { 
                const dx = pos.x - draggingObj.data[0].x; const dy = pos.y - draggingObj.data[0].y; 
                draggingObj.data.forEach(p => { p.x += dx; p.y += dy; }); 
            } else { 
                draggingObj.x = pos.x; draggingObj.y = pos.y; 
            }
            redraw();
        } 
        else if (isDrawing) { tempStroke.push(pos); redraw(); }
    }

    function handleEnd() {
        if (isAdmin && mode === 'shape') { isDrawingShape = false; redraw(); }
        if (isDrawing) { 
            if (isAdmin && mode === 'path') { 
                if (currentRiverPoints.length > 0) tempStroke[0].gap = true; 
                currentRiverPoints = currentRiverPoints.concat(tempStroke); 
            } 
            else if (activeTask && (activeTask.type === 'path' || activeTask.type === 'shape')) { 
                student = student.filter(s => s.name !== activeTask.name); 
                student.push({name: activeTask.name, type: activeTask.type, data: [...tempStroke], isConfirmed: false}); 
                showActionPopup(tempStroke[0].x, tempStroke[0].y);
            } 
        }
        
        if ((draggingObj || resizingObj) && !isAdmin) {
             const instruction = document.getElementById('step-instruction');
             instruction.style.background = "linear-gradient(90deg, #4361ee, #4cc9f0)";
             updateSteps();
        }
        draggingObj = null; resizingObj = null; isDrawing = false; tempStroke = []; redraw();
    }

    function showActionPopup(x, y) {
        waitingForConfirm = true;
        updatePopupPosition(x, y);
        actionPopup.style.display = 'flex';
        document.getElementById('step-instruction').innerText = "ලකුණු කළ ස්ථානය තහවුරු කරන්න (Confirm) හෝ ඉවත් කරන්න (Delete).";
    }

    function triggerConfirmPulse() {
        if (!activeTask) return;
        const sObj = student.find(s => s.name === activeTask.name);
        if (!sObj) return;

        const p = getCurrentPage();
        const targetW = p.width || (appState.activeCategory === 'srilanka' ? 450 : 630);
        const targetH = p.height || (appState.activeCategory === 'srilanka' ? 630 : 450);

        const x = sObj.x || (sObj.data ? sObj.data[0].x : 0);
        const y = sObj.y || (sObj.data ? sObj.data[0].y : 0);
        const rect = wrapper.getBoundingClientRect();
        const scaleX = rect.width / targetW;
        const scaleY = rect.height / targetH;

        const ripple = document.createElement('div');
        ripple.className = 'success-ripple';
        ripple.style.left = `${(x * scaleX * scale) + offsetX}px`;
        ripple.style.top = `${(y * scaleY * scale) + offsetY}px`;
        ripple.style.width = '20px'; ripple.style.height = '20px';
        wrapper.appendChild(ripple);
        setTimeout(() => ripple.remove(), 800);

        const pulse = document.createElement('div');
        pulse.className = 'confirm-pulse';
        pulse.style.left = `${(x * scaleX * scale) + offsetX}px`;
        pulse.style.top = `${(y * scaleY * scale) + offsetY}px`;
        wrapper.appendChild(pulse);
        setTimeout(() => pulse.remove(), 1000);
    }

    function confirmAction() {
        if (activeTask) {
            const sObj = student.find(s => s.name === activeTask.name);
            if (sObj) sObj.isConfirmed = true; 
        }
        triggerConfirmPulse(); 
        waitingForConfirm = false;
        actionPopup.style.display = 'none';
        resetZoom(); 
        autoNext();
        redraw();
    }

    function deleteAction() {
        if (activeTask) student = student.filter(s => s.name !== activeTask.name);
        waitingForConfirm = false;
        actionPopup.style.display = 'none';
        redraw();
    }

    canvas.addEventListener('mousedown', handleStart); 
    window.addEventListener('mousemove', handleMove); 
    window.addEventListener('mouseup', handleEnd);

    function evaluateAll() {
        if (waitingForConfirm) return;
        evaluated = true; isErrorReviewMode = false; currentErrorPath = null; 
        let score = 0; const errList = document.getElementById('error-list'); errList.innerHTML = ""; 
        const p = getCurrentPage(); const teacherData = p.teacher || [];

        teacherData.forEach(t => {
            const s = student.find(x => x.name === t.name);
            const isCorrect = checkCorrectness(s, t, p);
            if (isCorrect) score++; 
            else if (s) {
                const div = document.createElement('div'); 
                div.style.color="#b91c1c"; 
                div.style.fontWeight = "700";
                div.style.marginBottom = "4px";
                div.innerText = "❌ " + t.name; 
                errList.appendChild(div); 
            }
        });
        
        document.getElementById('s-val').innerText = score; 
        document.getElementById('t-val').innerText = teacherData.length;
        document.getElementById('error-panel').style.display = errList.children.length > 0 ? 'block' : 'none'; 
        redraw();
        if (score === teacherData.length && teacherData.length > 0) {
            document.getElementById('step-instruction').innerText = "සුභ පැතුම්! සියල්ල නිවැරදියි. 🎉";
            document.getElementById('step-instruction').style.background = "linear-gradient(90deg, #2ecc71, #27ae60)";
        }
    }

    function showNextError() {
        if (!evaluated) { alert("කරුණාකර ප්‍රථමයෙන් 'Check' බොත්තම ඔබන්න."); return; }
        const p = getCurrentPage(); const teacherData = p.teacher || [];
        const attemptedNames = student.map(s => s.name);
        const attemptedTeacherData = teacherData.filter(t => attemptedNames.includes(t.name));

        if (attemptedTeacherData.length === 0) { alert("ඔබ කිසිවක් සලකුණු කර නැත."); return; }

        isErrorReviewMode = true; 
        if (errorIndex >= attemptedTeacherData.length) errorIndex = 0;
        const currentTarget = attemptedTeacherData[errorIndex];
        currentErrorPath = currentTarget;
        
        const studentObj = student.find(s => s.name === currentTarget.name);
        const isCorrect = checkCorrectness(studentObj, currentTarget, p);

        if (isCorrect) {
            lastCorrectObjForMessage = studentObj;
            successMessageTimer = 120;
            document.getElementById('step-instruction').innerText = `${currentTarget.name}: ඔබ නිවැරදියි! 😊`;
            document.getElementById('step-instruction').style.background = "linear-gradient(90deg, #2ecc71, #27ae60)";
        } else {
            animateCorrectionArrow(studentObj, currentTarget);
        }
        errorIndex++;
    }

    function animateCorrectionArrow(studentObj, teacherObj) {
        const instruction = document.getElementById('step-instruction');
        instruction.style.background = "linear-gradient(90deg, #f72585, #ff4d4d)";
        instruction.innerText = `${teacherObj.name}: ඔබ සලකුණු කළ ස්ථානය නිවැරදි නොවේ!`;
        
        const startX = studentObj ? (studentObj.x || (studentObj.data ? studentObj.data[0].x : 0)) : 0;
        const startY = studentObj ? (studentObj.y || (studentObj.data ? studentObj.data[0].y : 0)) : 0;
        const endX = teacherObj.x || (teacherObj.data ? teacherObj.data[0].x : 0);
        const endY = teacherObj.y || (teacherObj.data ? teacherObj.data[0].y : 0);
        
        let progress = 0; const startTime = Date.now();
        function animate() {
            const elapsed = Date.now() - startTime; progress = Math.min(elapsed / 1000, 1);
            redraw();
            
            ctx.save();
            const msg = `${teacherObj.name}: නිවැරදි නොවේ 😟`;
            ctx.font = "bold 14px 'Noto Sans Sinhala'";
            const textWidth = ctx.measureText(msg).width;
            
            ctx.globalAlpha = glowAlpha; ctx.fillStyle = "rgba(247, 37, 133, 0.9)";
            ctx.beginPath();
            ctx.roundRect(startX - (textWidth/2) - 10, startY - 80, textWidth + 20, 35, 10);
            ctx.fill();
            
            ctx.fillStyle = "white"; ctx.textAlign = "center"; ctx.fillText(msg, startX, startY - 57);
            ctx.restore();
            
            const currentX = startX + (endX - startX) * progress; 
            const currentY = startY + (endY - startY) * progress;
            ctx.setLineDash([5, 5]); ctx.strokeStyle = "#4361ee"; ctx.lineWidth = 3; 
            ctx.beginPath(); ctx.moveTo(startX, startY); ctx.lineTo(currentX, currentY); ctx.stroke(); ctx.setLineDash([]);
            
            const angle = Math.atan2(endY - startY, endX - startX); 
            ctx.fillStyle = "#4361ee"; ctx.beginPath(); ctx.moveTo(currentX, currentY);
            ctx.lineTo(currentX - 15 * Math.cos(angle - Math.PI / 6), currentY - 15 * Math.sin(angle - Math.PI / 6)); 
            ctx.lineTo(currentX - 15 * Math.cos(angle + Math.PI / 6), currentY - 15 * Math.sin(angle + Math.PI / 6)); 
            ctx.fill();
            
            if (progress < 1) requestAnimationFrame(animate);
        }
        requestAnimationFrame(animate);
    }

    function setShapeMode() {
        mode = 'shape'; document.querySelectorAll('.tool-btn').forEach(b => b.classList.remove('active'));
        const btn = document.getElementById('draw-shape-btn'); if (btn) btn.classList.add('active');
        currentRiverPoints = [];
    }

    function saveFreeShape() {
        if (currentShapePoints.length < 3) { alert("කරුණාකර සිතියම මත හැඩයක් අඳින්න."); return; }
        const name = prompt("හැඩතලයේ නම:"); if (!name) return;
        const newShape = { id: "shape_" + Date.now(), name: name, type: 'shape', data: [...currentShapePoints], color: document.getElementById('shape-color')?.value || "#4361ee", opacity: 0.5, rotation: 0, scale: 1, showLabel: true };
        getCurrentPage().teacher.push(newShape); 
        saveToLocal();
        currentShapePoints = []; 
        renderTasks(); 
        renderAdminItemsList(); 
        redraw();
    }

    function finishRiverPath() { 
        if (currentRiverPoints.length < 2) { alert("කරුණාකර රේඛාවක් ඇඳ අවසන් කරන්න."); return; }
        const name = prompt("ගංගාවේ/මාර්ගයේ නම:"); 
        if (name) { 
            getCurrentPage().teacher.push({ type: 'path', name: name, data: [...currentRiverPoints], angle: -45, length: 40 }); 
            saveToLocal();
            currentRiverPoints = []; 
            renderTasks(); 
            renderAdminItemsList(); 
            redraw(); 
        }
    }

    function resetStudent() { student = []; evaluated = false; showAnswers = false; isErrorReviewMode = false; errorIndex = 0; currentErrorPath = null; init(); }
    function toggleCorrectAnswers() { showAnswers = !showAnswers; isErrorReviewMode = false; document.getElementById('ans-toggle').innerText = showAnswers ? "🔙 ආපසු හැරෙන්න" : "👁️ නිවැරදි ස්ථාන පෙන්වන්න"; redraw(); }
    
    function adminLogin() { 
        if (prompt("Pass:") === "4112") { 
            isAdmin = true; 
            document.getElementById('admin-panel').style.display='block'; 
            renderAdminItemsList(); 
            redraw(); 
        } 
    }
    function adminLogout() { isAdmin = false; document.getElementById('admin-panel').style.display='none'; redraw(); }
    function setMode(m) { mode = m; currentRiverPoints = []; currentShapePoints = []; document.querySelectorAll('.tool-btn').forEach(b => b.classList.remove('active')); if (document.getElementById(m+'-btn')) document.getElementById(m+'-btn').classList.add('active'); redraw(); }
    
    function toggleAdminSec(id) { const el = document.getElementById(id); el.style.display = el.style.display === "block" ? "none" : "block"; }
    
    function updateRadius(v) { getCurrentPage().pointRadius = parseInt(v); document.getElementById('rad-val').innerText = v; saveToLocal(); redraw(); }
    function updateDotSize(v) { getCurrentPage().dotSize = parseInt(v); document.getElementById('dot-val').innerText = v; saveToLocal(); redraw(); }
    function updateFontSize(v) { getCurrentPage().fontSize = parseInt(v); document.getElementById('font-val').innerText = v; saveToLocal(); redraw(); }
    function updateTolerance(v) { getCurrentPage().pathTolerance = parseInt(v); document.getElementById('tol-val').innerText = v; saveToLocal(); redraw(); }
    
    function exportImage() { 
        html2canvas(document.getElementById('canvas-wrapper')).then(cvs => { 
            const a = document.createElement('a'); 
            a.href = cvs.toDataURL(); 
            a.download = `${appState.activeCategory}_map.png`; 
            a.click(); 
        }); 
    }

    async function shareMap() { 
        const score = document.getElementById('s-val').innerText; 
        const total = document.getElementById('t-val').innerText; 
        const canvasSnap = await html2canvas(document.getElementById('canvas-wrapper')); 
        canvasSnap.toBlob(async (blob) => { 
            const file = new File([blob], "result.png", { type: "image/png" }); 
            if (navigator.share) {
                try {
                    await navigator.share({ title: appState.appTitle, text: `ලකුණු: ${score}/${total}`, files: [file] }); 
                } catch(e) {}
            } else {
                alert(`ලකුණු: ${score} / ${total}`);
            }
        }); 
    }

    async function exportFullZip() { 
        const zip = new JSZip(); 
        zip.file("map_data_backup.json", JSON.stringify(appState, null, 2)); 
        zip.generateAsync({type:"blob"}).then(c => { 
            const a = document.createElement('a'); 
            a.href = URL.createObjectURL(c); 
            a.download = "MapLab_Pro_Backup.zip"; 
            a.click(); 
        }); 
    }

    function exportJSON() { 
        const blob = new Blob([JSON.stringify(appState, null, 2)], {type:'application/json'}); 
        const a = document.createElement('a'); 
        a.href = URL.createObjectURL(blob); 
        a.download = `MapData_${appState.activeCategory}.json`; 
        a.click(); 
    }
    
    function importJSON() {
        const i = document.createElement('input');
        i.type = 'file';
        i.accept = '.json';
        i.onchange = e => {
            const r = new FileReader();
            r.onload = ev => {
                try {
                    const parsed = JSON.parse(ev.target.result);
                    if (parsed.srilanka && parsed.world) {
                        appState = parsed;
                    } else if (Array.isArray(parsed)) {
                        // Imported pages array into active category
                        const cat = appState.activeCategory;
                        appState[cat].pages = parsed;
                    }
                    saveToLocal();
                    init();
                    alert("JSON දත්ත සාර්ථකව ඇතුළත් කරන ලදී! ✅");
                } catch (err) {
                    alert("JSON ගොනුව විග්‍රහ කිරීමේ දෝෂයකි: " + err.message);
                }
            };
            r.readAsText(e.target.files[0]);
        };
        i.click();
    }

    function undoTeacher() { getCurrentPage().teacher.pop(); saveToLocal(); renderTasks(); renderAdminItemsList(); redraw(); }
    function clearTeacher() { 
        if (confirm("මෙම පිටුවේ සියලු ස්ථාන මකන්නද?")) { 
            getCurrentPage().teacher = []; 
            saveToLocal(); 
            renderTasks(); 
            renderAdminItemsList(); 
            redraw(); 
        }
    }
    function undoPathPoint() { 
        if (currentRiverPoints.length > 0) { 
            let lastGapIndex = -1; 
            for (let i = currentRiverPoints.length - 1; i >= 0; i--) { 
                if (currentRiverPoints[i].gap) { lastGapIndex = i; break; } 
            } 
            if (lastGapIndex === -1) currentRiverPoints = []; 
            else currentRiverPoints.splice(lastGapIndex); 
            redraw(); 
        } 
    }

    function toggleGhost() { mapImg.style.opacity = mapImg.style.opacity == "0.3" ? "1" : "0.3"; }
    function renameApp() { 
        const newTitle = prompt("යෙදුමේ නම:", appState.appTitle); 
        if (newTitle) { appState.appTitle = newTitle; saveToLocal(); init(); } 
    }
    
    function uploadMap(el) { 
        if (el.files[0]) { 
            const r = new FileReader(); 
            r.onload = e => { 
                getCurrentPage().map = e.target.result; 
                saveToLocal(); 
                init(); 
            }; 
            r.readAsDataURL(el.files[0]); 
        }
    }

    function addNewPage() {
        const cat = appState.activeCategory;
        const defaultName = cat === 'world' ? `${2026 + appState[cat].pages.length}` : `පිටුව ${appState[cat].pages.length + 1}`;
        const name = prompt("නව පිටුවේ / වර්ෂයේ නම:", defaultName);
        if (!name) return;

        const newP = {
            name: name,
            width: cat === 'srilanka' ? 450 : 630,
            height: cat === 'srilanka' ? 630 : 450,
            map: cat === 'srilanka' ? DEFAULT_SL_MAP : DEFAULT_WORLD_MAP,
            teacher: [],
            pointRadius: 25,
            dotSize: 6,
            fontSize: 12,
            pathTolerance: 35,
            labels: true
        };
        appState[cat].pages.push(newP);
        appState[cat].curP = appState[cat].pages.length - 1;
        saveToLocal();
        init();
    }

    function renameCurrentPage() {
        const cat = appState.activeCategory;
        const curIndex = appState[cat].curP;
        const currentName = appState[cat].pages[curIndex].name;
        const newName = prompt("පිටුවේ නව නම:", currentName);
        if (newName && newName.trim() !== "") {
            appState[cat].pages[curIndex].name = newName.trim();
            saveToLocal();
            init();
        }
    }

    function deleteCurrentPage() {
        const cat = appState.activeCategory;
        if (appState[cat].pages.length <= 1) {
            alert("අවම වශයෙන් එක් පිටුවක්වත් පැවතිය යුතුය.");
            return;
        }
        if (confirm(`'${appState[cat].pages[appState[cat].curP].name}' මකා දැමීමට අවශ්‍යද?`)) {
            appState[cat].pages.splice(appState[cat].curP, 1);
            appState[cat].curP = 0;
            saveToLocal();
            init();
        }
    }

    // Cloud Firebase Integration
    function connectFirebase() {
        database.ref('mapDataUnified').on('value', (snapshot) => {
            const data = snapshot.val();
            if (data) {
                if (data.srilanka && data.world) {
                    appState = data;
                } else if (data.pages) {
                    appState.world.pages = data.pages;
                }
                init();
            }
        });
    }

    function saveToFirebase() {
        database.ref('mapDataUnified').set(appState)
        .then(() => alert("Cloud Firebase වෙත සාර්ථකව සුරැකිණි! ✅"))
        .catch(e => alert("දෝෂයකි: " + e.message));
    }

    // Google Apps Script Integration
    async function saveToGoogleAppsScript() {
        const gasUrl = prompt("Google Apps Script Web App එකේ URL එක ඇතුළත් කරන්න:");
        if (!gasUrl) return;

        try {
            alert("Google Drive වෙත දත්ත යවමින් පවතී... රැඳී සිටින්න.");
            await fetch(gasUrl, {
                method: "POST",
                mode: "no-cors",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(appState)
            });
            alert("Google Drive වෙත දත්ත සාර්ථකව යවන ලදී! ✅");
        } catch (e) {
            alert("දෝෂයකි: " + e.message);
        }
    }

    async function loadFromGoogleAppsScript() {
        const gasUrl = prompt("Google Apps Script Web App එකේ URL එක ඇතුළත් කරන්න:");
        if (!gasUrl) return;

        try {
            alert("Google Drive එකෙන් දත්ත ලබාගනිමින් පවතී... රැඳී සිටින්න.");
            const response = await fetch(gasUrl);
            const data = await response.json();
            
            if (data) {
                if (data.srilanka && data.world) appState = data;
                else if (data.pages) appState.world.pages = data.pages;
                saveToLocal();
                init();
                alert("Google Drive එකෙන් දත්ත සාර්ථකව සිතියමට ලබාගන්නා ලදී! ✅");
            } else {
                alert("දත්ත සොයා ගැනීමට නොහැකි විය!");
            }
        } catch (e) {
            alert("දෝෂයකි: " + e.message);
        }
    }

    function openGoogleDriveFolder() {
        const folderUrl = "https://drive.google.com/drive/folders/1PB1s6J6gWtBBk3Qqfo8-iWc7xJtLRZFj?usp=sharing";
        window.open(folderUrl, '_blank');
    }

    async function autoLoadFromDrive() {
        const fileId = "1Xzxu7w86zdA0LDm3ZVWG7-4pMS9tTuYk";
        const driveUrl = `https://drive.google.com/uc?export=download&id=${fileId}`;
        const proxyUrl = `https://api.allorigins.win/raw?url=${encodeURIComponent(driveUrl)}`;

        try {
            const response = await fetch(proxyUrl);
            const data = await response.json();
            if (data && data.pages) {
                appState.world.pages = data.pages;
                appState.world.pages.forEach(pg => {
                    if (!pg.map || pg.map.includes("drive.google.com")) pg.map = DEFAULT_WORLD_MAP;
                });
                saveToLocal();
                init();
            }
        } catch (e) {
            console.log("Drive load notice:", e);
        }
    }

    async function importFromGoogleDriveJSON() {
        await autoLoadFromDrive();
        alert("Google Drive JSON දත්ත සාර්ථකව යාවත්කාලීන විය! ✅");
    }

    // Step-by-Step Interactive Guide Hand
    function startSingleGuide() {
        const p = getCurrentPage(); 
        const teacherData = p.teacher || [];
        if (!p || teacherData.length === 0) {
            alert("මෙම පිටුව සඳහා තවමත් ගුරු ලක්ෂ්‍ය ඇතුළත් කර නැත.");
            return;
        }
        if (guideBtn) guideBtn.disabled = true;
        resetStudent();
        const firstTask = teacherData[0];
        const instruction = document.getElementById('step-instruction');
        const checkBtn = document.getElementById('check-btn');
        const scoreCard = document.getElementById('main-score-card');
        
        instruction.innerText = `පියවර 1: '${firstTask.name}' තෝරා ලකුණු කරන ආකාරය බලමු.`;
        
        const rectWrapper = wrapper.getBoundingClientRect();
        const midX = rectWrapper.left + rectWrapper.width / 2;
        const midY = rectWrapper.top + rectWrapper.height / 2 + window.pageYOffset;
        
        setTimeout(() => {
            moveHandToCoords(midX, midY, () => {
                const listContainer = document.getElementById('left-locations-list');
                const firstItem = listContainer.querySelector('.loc-item');
                moveHandTo(firstItem, () => {
                    activeTask = firstTask; 
                    renderTasks();
                    instruction.innerText = `පියවර 2: සිතියම මත නිවැරදි ස්ථානය ලකුණු කරයි.`;
                    window.scrollTo({ top: wrapper.offsetTop - 100, behavior: 'smooth' });
                    
                    const targetW = p.width || (appState.activeCategory === 'srilanka' ? 450 : 630);
                    const targetH = p.height || (appState.activeCategory === 'srilanka' ? 630 : 450);

                    setTimeout(() => {
                        const rect = canvas.getBoundingClientRect();
                        const tx = rect.left + (firstTask.x || (firstTask.data ? firstTask.data[0].x : 0)) * (rect.width / targetW) + window.pageXOffset;
                        const ty = rect.top + (firstTask.y || (firstTask.data ? firstTask.data[0].y : 0)) * (rect.height / targetH) + window.pageYOffset;
                        
                        moveHandToCoords(tx, ty, () => {
                            if (firstTask.type === 'path' || firstTask.type === 'shape') { 
                                student.push({name: firstTask.name, type: firstTask.type, data: firstTask.data, isConfirmed: false}); 
                            } else { 
                                student.push({name: firstTask.name, type:'point', x: firstTask.x, y: firstTask.y, isConfirmed: false}); 
                            }
                            
                            waitingForConfirm = true;
                            actionPopup.style.display = 'flex';
                            updatePopupPosition(firstTask.x || firstTask.data[0].x, firstTask.y || firstTask.data[0].y);

                            redraw();
                            instruction.innerText = `පියවර 3: තහවුරු කර 'Check' බොත්තම ඔබා පරීක්ෂා කරයි.`;
                            
                            setTimeout(() => {
                                const confirmBtn = actionPopup.querySelector('.confirm-btn');
                                moveHandTo(confirmBtn, () => {
                                    confirmAction();
                                    window.scrollTo({ top: checkBtn.offsetTop - 200, behavior: 'smooth' });
                                    setTimeout(() => {
                                        moveHandTo(checkBtn, () => {
                                            evaluateAll();
                                            instruction.innerText = `ලකුණු ලැබී ඇත. දැන් ඔබ උත්සාහ කරන්න!`;
                                            scoreCard.style.border = "4px solid #2ecc71";
                                            scoreCard.style.transform = "scale(1.05)";
                                            
                                            setTimeout(() => { 
                                                scoreCard.style.border = "none"; 
                                                scoreCard.style.transform = "scale(1)"; 
                                                hand.style.display = 'none'; 
                                                resetStudent(); 
                                                window.scrollTo({ top: 0, behavior: 'smooth' }); 
                                            }, 4000); 
                                        });
                                    }, 2000);
                                });
                            }, 2000);
                        });
                    }, 2500);
                });
            });
        }, 1500);
    }

    function moveHandTo(el, callback) { 
        if (!el) return; 
        const rect = el.getBoundingClientRect(); 
        const scrollY = window.pageYOffset; 
        hand.style.display = 'block'; 
        hand.style.left = (rect.left + rect.width/2 - 20) + 'px'; 
        hand.style.top = (rect.top + rect.height/2 - 20 + scrollY) + 'px'; 
        setTimeout(callback, 2500); 
    }

    function moveHandToCoords(x, y, callback) { 
        hand.style.display = 'block'; 
        hand.style.left = (x - 20) + 'px'; 
        hand.style.top = (y - 20) + 'px'; 
        setTimeout(callback, 2500); 
    }

    connectFirebase();
    autoLoadFromDrive();
    init();
</script>
</body>
</html>
"""

# Replace base64 placeholders
final_html = html_template.replace("SL_MAP_BASE64_PLACEHOLDER", sl_b64)
final_html = final_html.replace("WORLD_MAP_BASE64_PLACEHOLDER", world_b64)

out_path = r'C:\Users\manpe\.gemini\antigravity\scratch\sl_map_lab_pro\index.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Unified HTML successfully created at:", out_path)
print("File size:", len(final_html), "bytes")
