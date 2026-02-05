import os
import json
import random
from datetime import datetime

# === 1. 商业配置区 (修改这里) ===
CONFIG = {
    "DOMAIN": "FreeFineAI.com",
    "TIP_JAR_URL": "https://www.paypal.com/ncp/payment/ZRQDBKWE7VBSU",
    "MEGA_BUNDLE_URL": "https://www.paypal.com/ncp/payment/AQSGVVXLW69GJ",
    "COFFEE_URL": "https://www.freefineai.com",
    "IMG_DIR": "images",
    "TEMPLATE_DIR": "templates",
    "DATA_DIR": "data"  # 新增数据目录
}

# === 2. 用户粘性功能数据 ===
DAILY_CHALLENGES = [
    {"seed": 88291, "prompt": "Cyber-organic growth on a porcelain skull", "difficulty": "Medium"},
    {"seed": 77432, "prompt": "Holographic butterfly in a crystal cave", "difficulty": "Easy"},
    {"seed": 99876, "prompt": "Steampunk lighthouse in a storm of gears", "difficulty": "Hard"},
    {"seed": 55123, "prompt": "Neon samurai in a digital bamboo forest", "difficulty": "Medium"},
    {"seed": 33445, "prompt": "Glass dragon breathing aurora flames", "difficulty": "Hard"}
]

PROMPT_TEMPLATES = [
    "Macro shot of an iridescent {subject} with {effect} wings, hyper-detailed, {lighting} lighting",
    "Architectural render of a floating {building} made of {material}, extreme minimalism, {time} lighting",
    "A transparent {creature} drifting through a neon-lit {location}, cinematic bokeh, 8k raw photo",
    "An ancient {character} covered in blooming {flowers}, weathered {texture} texture, masterpiece",
    "Surreal {landscape} with floating {objects}, {style} aesthetic, dramatic {weather}",
    "{Color} {animal} in a {environment} of pure {element}, ethereal glow, fantasy art"
]

PROMPT_VARIABLES = {
    "subject": ["insect", "flower", "crystal", "feather", "shell", "leaf"],
    "effect": ["galaxy", "rainbow", "electric", "frost", "fire", "water"],
    "lighting": ["synthwave", "golden hour", "moonlight", "neon", "candlelight", "aurora"],
    "building": ["monastery", "castle", "tower", "bridge", "temple", "palace"],
    "material": ["mercury", "glass", "crystal", "marble", "gold", "ice"],
    "time": ["sunset", "dawn", "midnight", "noon", "twilight", "storm"],
    "creature": ["jellyfish", "butterfly", "dragon", "phoenix", "unicorn", "wolf"],
    "location": ["Tokyo street", "forest path", "mountain peak", "ocean depth", "space station", "ancient ruins"],
    "character": ["mecha knight", "wizard", "samurai", "angel", "demon", "robot"],
    "flowers": ["cherry blossoms", "roses", "lotus flowers", "sunflowers", "orchids", "peonies"],
    "texture": ["metal", "stone", "wood", "fabric", "ceramic", "leather"],
    "landscape": ["desert", "ocean", "mountain", "forest", "city", "tundra"],
    "objects": ["islands", "crystals", "books", "clocks", "mirrors", "spheres"],
    "style": ["cyberpunk", "steampunk", "art deco", "minimalist", "baroque", "futuristic"],
    "weather": ["storm", "fog", "rain", "snow", "wind", "lightning"],
    "Color": ["Crimson", "Azure", "Golden", "Silver", "Emerald", "Violet"],
    "animal": ["tiger", "eagle", "whale", "fox", "lion", "deer"],
    "environment": ["maze", "garden", "library", "cathedral", "laboratory", "arena"],
    "element": ["light", "shadow", "fire", "water", "earth", "air"]
}

STYLE_PRESETS = {
    "Cinematic": ", cinematic composition, dramatic lighting, film grain, 35mm lens, depth of field",
    "Hyperrealistic": ", photorealistic, ultra-detailed, 8K resolution, professional photography",
    "Artistic": ", oil painting style, brush strokes, artistic interpretation, masterpiece",
    "Cyberpunk": ", neon lights, dark atmosphere, futuristic, cyberpunk aesthetic, synthwave",
    "Fantasy": ", magical atmosphere, ethereal lighting, fantasy art, enchanted, mystical",
    "Minimalist": ", clean composition, negative space, simple forms, minimal color palette"
}

# === 3. 自动化组件初始化 ===
def setup():
    for folder in [CONFIG["IMG_DIR"], CONFIG["TEMPLATE_DIR"], CONFIG["DATA_DIR"]]:
        if not os.path.exists(folder):
            os.makedirs(folder)
    
    # 初始化用户数据文件
    init_user_data()
    
    # 预设 Head 模板
    head_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FreeFineAI | Premium Flux.1 Digital Assets</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        body { background-color: #050505; color: #a1a1aa; font-family: 'Inter', sans-serif; margin: 0; overflow-x: hidden; }
        .masonry { column-count: 1; column-gap: 1.5rem; }
        @media (min-width: 768px) { .masonry { column-count: 2; } }
        @media (min-width: 1280px) { .masonry { column-count: 3; } }
        .nav-glass { background: rgba(0,0,0,0.85); backdrop-filter: blur(15px); border-bottom: 1px solid rgba(255,255,255,0.05); }
        #particle-canvas { position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none; }
        nav, header, main, footer { position: relative; z-index: 10; }
        .hero-title { -webkit-text-stroke: 1px rgba(255,255,255,0.1); color: transparent; transition: all 0.5s; }
        .hero-title:hover { color: white; -webkit-text-stroke: 1px transparent; }
        .notification { position: fixed; top: 100px; right: 20px; z-index: 1000; transform: translateX(400px); transition: transform 0.3s ease; }
        .notification.show { transform: translateX(0); }
        .streak-badge { animation: pulse 2s infinite; }
        @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.7; } }
    </style>
</head>
<body>
    <canvas id="particle-canvas"></canvas>
    
    <!-- 通知系统 -->
    <div id="notification" class="notification bg-gradient-to-r from-cyan-500 to-blue-600 text-white p-4 rounded-2xl shadow-2xl max-w-sm">
        <div class="flex items-center gap-3">
            <div class="w-8 h-8 bg-white/20 rounded-full flex items-center justify-center">
                <span class="text-sm">🎉</span>
            </div>
            <div>
                <div class="font-bold text-sm" id="notificationTitle">Congratulations!</div>
                <div class="text-xs opacity-90" id="notificationText">You earned a new achievement</div>
            </div>
        </div>
    </div>
    
    <script>
        // 粒子系统
        window.addEventListener('DOMContentLoaded', () => {
            const canvas = document.getElementById('particle-canvas');
            const ctx = canvas.getContext('2d');
            let particles = [];
            const resize = () => { canvas.width = window.innerWidth; canvas.height = window.innerHeight; };
            class Particle {
                constructor() { this.init(); }
                init() {
                    this.x = Math.random() * canvas.width;
                    this.y = Math.random() * canvas.height;
                    this.size = Math.random() * 1.5 + 0.5;
                    this.speedX = Math.random() * 0.4 - 0.2;
                    this.speedY = Math.random() * 0.4 - 0.2;
                    this.opacity = Math.random() * 0.5 + 0.1;
                }
                update() {
                    this.x += this.speedX; this.y += this.speedY;
                    if(this.x > canvas.width || this.x < 0) this.speedX *= -1;
                    if(this.y > canvas.height || this.y < 0) this.speedY *= -1;
                }
                draw() {
                    ctx.beginPath(); ctx.arc(this.x, this.y, this.size, 0, Math.PI*2);
                    ctx.fillStyle = `rgba(6, 182, 212, ${this.opacity})`; ctx.fill();
                }
            }
            const animate = () => {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                particles.forEach(p => { p.update(); p.draw(); });
                requestAnimationFrame(animate);
            };
            window.addEventListener('resize', resize);
            resize();
            for(let i=0; i<100; i++) particles.push(new Particle());
            animate();
        });
        
        // 用户数据管理
        class UserProgress {
            constructor() {
                this.data = JSON.parse(localStorage.getItem('freefineai_progress') || '{}');
                this.initDefaults();
            }
            
            initDefaults() {
                if (!this.data.visits) this.data.visits = 0;
                if (!this.data.downloads) this.data.downloads = 0;
                if (!this.data.promptsGenerated) this.data.promptsGenerated = 0;
                if (!this.data.lastVisit) this.data.lastVisit = null;
                if (!this.data.streak) this.data.streak = 0;
                if (!this.data.achievements) this.data.achievements = [];
                if (!this.data.favoriteImages) this.data.favoriteImages = [];
                this.save();
            }
            
            save() {
                localStorage.setItem('freefineai_progress', JSON.stringify(this.data));
            }
            
            addVisit() {
                const today = new Date().toDateString();
                if (this.data.lastVisit !== today) {
                    this.data.visits++;
                    if (this.data.lastVisit === new Date(Date.now() - 86400000).toDateString()) {
                        this.data.streak++;
                    } else {
                        this.data.streak = 1;
                    }
                    this.data.lastVisit = today;
                    this.checkAchievements();
                    this.save();
                }
            }
            
            addDownload() {
                this.data.downloads++;
                this.checkAchievements();
                this.save();
            }
            
            addPromptGeneration() {
                this.data.promptsGenerated++;
                this.checkAchievements();
                this.save();
            }
            
            checkAchievements() {
                const achievements = [
                    { id: 'first_visit', name: 'First Visit', desc: 'Welcome to FreeFineAI!', condition: () => this.data.visits >= 1 },
                    { id: 'regular_visitor', name: 'Regular Visitor', desc: 'Visit the site 5 times', condition: () => this.data.visits >= 5 },
                    { id: 'download_master', name: 'Download Master', desc: 'Download 10 images', condition: () => this.data.downloads >= 10 },
                    { id: 'prompt_creator', name: 'Prompt Creator', desc: 'Generate 20 prompts', condition: () => this.data.promptsGenerated >= 20 },
                    { id: 'streak_week', name: 'Week Streak', desc: 'Visit 7 days in a row', condition: () => this.data.streak >= 7 }
                ];
                
                achievements.forEach(achievement => {
                    if (achievement.condition() && !this.data.achievements.includes(achievement.id)) {
                        this.data.achievements.push(achievement.id);
                        this.showNotification(achievement.name, achievement.desc);
                    }
                });
            }
            
            showNotification(title, text) {
                const notification = document.getElementById('notification');
                const titleEl = document.getElementById('notificationTitle');
                const textEl = document.getElementById('notificationText');
                
                titleEl.textContent = title;
                textEl.textContent = text;
                notification.classList.add('show');
                
                setTimeout(() => {
                    notification.classList.remove('show');
                }, 4000);
            }
        }
        
        // 初始化用户进度
        const userProgress = new UserProgress();
        userProgress.addVisit();
        
        // 通知函数
        function showNotification(title, text) {
            userProgress.showNotification(title, text);
        }
    </script>
    
    <nav class="fixed top-0 w-full z-50 nav-glass px-8 py-5 flex justify-between items-center">
        <span class="text-white font-black text-xl tracking-tighter italic">FREEFINE<span class="text-cyan-500">AI</span></span>
        <div class="flex items-center gap-6">
            <!-- 用户进度显示 -->
            <div class="hidden md:flex items-center gap-4 text-xs">
                <div class="flex items-center gap-1">
                    <span class="text-cyan-400">📊</span>
                    <span class="text-zinc-400" id="userStats">Visits: 0 | Downloads: 0</span>
                </div>
                <div class="flex items-center gap-1 streak-badge" id="streakBadge" style="display: none;">
                    <span class="text-yellow-400">🔥</span>
                    <span class="text-yellow-400" id="streakCount">0</span>
                </div>
            </div>
            <a href="''' + CONFIG["TIP_JAR_URL"] + '''" target="_blank" class="hidden sm:block text-[10px] font-bold text-zinc-500 hover:text-white uppercase tracking-widest">Support</a>
            <a href="''' + CONFIG["MEGA_BUNDLE_URL"] + '''" target="_blank" class="bg-white text-black text-[10px] font-black px-6 py-2 rounded-full uppercase tracking-tighter hover:bg-cyan-400 transition">Get Bundle $9.99</a>
        </div>
    </nav>
    
    <script>
        // 更新用户统计显示
        function updateUserStats() {
            const stats = document.getElementById('userStats');
            const streakBadge = document.getElementById('streakBadge');
            const streakCount = document.getElementById('streakCount');
            
            if (stats) {
                stats.textContent = `Visits: ${userProgress.data.visits} | Downloads: ${userProgress.data.downloads}`;
            }
            
            if (userProgress.data.streak > 0) {
                streakBadge.style.display = 'flex';
                streakCount.textContent = userProgress.data.streak;
            }
        }
        
        // 页面加载完成后更新统计
        document.addEventListener('DOMContentLoaded', updateUserStats);
    </script>
'''
    with open(os.path.join(CONFIG["TEMPLATE_DIR"], "head.html"), "w", encoding="utf-8") as f: 
        f.write(head_content)

def init_user_data():
    """初始化用户数据文件"""
    data_file = os.path.join(CONFIG["DATA_DIR"], "site_data.json")
    if not os.path.exists(data_file):
        initial_data = {
            "total_visits": 0,
            "total_downloads": 0,
            "daily_challenge": get_daily_challenge(),
            "featured_prompts": [],
            "user_submissions": []
        }
        with open(data_file, "w", encoding="utf-8") as f:
            json.dump(initial_data, f, indent=2, ensure_ascii=False)

def get_daily_challenge():
    """获取今日挑战"""
    today = datetime.now().day
    return DAILY_CHALLENGES[today % len(DAILY_CHALLENGES)]

def generate_random_prompt():
    """生成随机提示词"""
    template = random.choice(PROMPT_TEMPLATES)
    variables = {}
    
    # 提取模板中的变量
    import re
    vars_in_template = re.findall(r'\{(\w+)\}', template)
    
    # 为每个变量选择随机值
    for var in vars_in_template:
        if var in PROMPT_VARIABLES:
            variables[var] = random.choice(PROMPT_VARIABLES[var])
    
    # 替换模板中的变量
    result = template
    for var, value in variables.items():
        result = result.replace(f'{{{var}}}', value)
    
    return result

# === 4. 生成增强功能组件 ===
def generate_enhanced_tools():
    """生成增强版工具箱"""
    daily_challenge = get_daily_challenge()
    
    return f'''
    <!-- 每日挑战横幅 -->
    <section class="max-w-[1400px] mx-auto px-8 mb-12">
        <div class="bg-gradient-to-r from-purple-900/40 via-blue-900/40 to-cyan-900/40 border border-purple-500/20 rounded-[2.5rem] p-8 relative overflow-hidden">
            <div class="absolute top-0 right-0 p-4">
                <div class="bg-red-500 w-3 h-3 rounded-full animate-ping"></div>
            </div>
            <div class="flex flex-col md:flex-row items-center justify-between gap-6">
                <div>
                    <h3 class="text-white font-black text-lg mb-2">🎯 Daily Challenge #{daily_challenge['seed']}</h3>
                    <p class="text-zinc-300 text-sm mb-1">"{daily_challenge['prompt']}"</p>
                    <span class="text-xs text-purple-400 font-bold">Difficulty: {daily_challenge['difficulty']}</span>
                </div>
                <div class="flex gap-3">
                    <button onclick="copyChallenge('{daily_challenge['seed']}', '{daily_challenge['prompt']}')" class="bg-purple-600 hover:bg-purple-500 text-white text-xs font-black px-6 py-3 rounded-xl uppercase tracking-widest transition">
                        Accept Challenge
                    </button>
                    <button onclick="shareChallenge()" class="bg-zinc-800 hover:bg-zinc-700 text-white px-4 py-3 rounded-xl transition">
                        📤
                    </button>
                </div>
            </div>
        </div>
    </section>

    <!-- 增强工具箱 -->
    <section class="max-w-[1400px] mx-auto px-8 mb-24">
        <div class="grid md:grid-cols-3 gap-8">
            <!-- AI Prompt 生成器 -->
            <div class="bg-zinc-900/50 border border-white/5 p-8 rounded-[2.5rem] backdrop-blur-md relative overflow-hidden group">
                <div class="flex items-center gap-3 mb-6">
                    <div class="p-2 bg-cyan-500/10 rounded-lg text-cyan-400">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                    </div>
                    <h3 class="text-white font-black text-xs uppercase tracking-[0.2em]">AI Prompt 生成器</h3>
                </div>
                <textarea id="promptInput" placeholder="Enter a simple concept (e.g. 'Cyberpunk City')..." class="w-full bg-black/40 border border-white/5 rounded-2xl p-4 text-sm text-zinc-300 h-24 mb-4 outline-none focus:border-cyan-500/50 transition"></textarea>
                
                <!-- 风格选择器 -->
                <div class="mb-4">
                    <label class="text-zinc-400 text-xs font-bold block mb-2">Choose Style:</label>
                    <select id="styleSelect" class="w-full bg-black/40 border border-white/5 rounded-xl p-3 text-sm text-zinc-300 outline-none focus:border-cyan-500/50">
                        <option value="">Default</option>
                        {generate_style_options()}
                    </select>
                </div>
                
                <div class="flex gap-2 mb-4">
                    <button onclick="expandPrompt()" class="flex-1 bg-zinc-800 hover:bg-white hover:text-black text-white text-[10px] font-black py-4 rounded-xl uppercase tracking-widest transition shadow-lg">
                        Enhance Prompt
                    </button>
                    <button onclick="generateRandomPrompt()" class="bg-purple-600 hover:bg-purple-500 text-white px-4 py-4 rounded-xl transition">
                        🎲
                    </button>
                </div>
                
                <div id="copyNotice" class="absolute top-4 right-8 text-[9px] text-cyan-500 font-bold opacity-0 transition-opacity uppercase tracking-widest">Copied to Clipboard!</div>
            </div>

            <!-- 分辨率预设 -->
            <div class="bg-zinc-900/50 border border-white/5 p-8 rounded-[2.5rem] backdrop-blur-md">
                <div class="flex items-center gap-3 mb-6">
                    <div class="p-2 bg-purple-500/10 rounded-lg text-purple-400">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4"/></svg>
                    </div>
                    <h3 class="text-white font-black text-xs uppercase tracking-[0.2em]">Flux Resolution Presets</h3>
                </div>
                <div class="grid grid-cols-1 gap-3">
                    <button onclick="copyRes('1344 x 768')" class="bg-black/40 border border-white/5 p-4 rounded-2xl hover:border-cyan-500/50 group transition text-left relative overflow-hidden">
                        <span class="block text-white font-bold text-xs">16:9 Cinematic</span>
                        <span class="text-[10px] text-zinc-600">1344 x 768 px</span>
                    </button>
                    <button onclick="copyRes('768 x 1344')" class="bg-black/40 border border-white/5 p-4 rounded-2xl hover:border-cyan-500/50 group transition text-left relative overflow-hidden">
                        <span class="block text-white font-bold text-xs">9:16 Portrait</span>
                        <span class="text-[10px] text-zinc-600">768 x 1344 px</span>
                    </button>
                    <button onclick="copyRes('1024 x 1024')" class="bg-black/40 border border-white/5 p-4 rounded-2xl hover:border-cyan-500/50 group transition text-left relative overflow-hidden">
                        <span class="block text-white font-bold text-xs">1:1 Square</span>
                        <span class="text-[10px] text-zinc-600">1024 x 1024 px</span>
                    </button>
                </div>
            </div>

            <!-- 用户成就面板 -->
            <div class="bg-zinc-900/50 border border-white/5 p-8 rounded-[2.5rem] backdrop-blur-md">
                <div class="flex items-center gap-3 mb-6">
                    <div class="p-2 bg-yellow-500/10 rounded-lg text-yellow-400">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>
                    </div>
                    <h3 class="text-white font-black text-xs uppercase tracking-[0.2em]">My Achievements</h3>
                </div>
                
                <div id="achievementsList" class="space-y-3 mb-4">
                    <!-- 成就将通过 JavaScript 动态加载 -->
                </div>
                
                <div class="text-center">
                    <button onclick="showAllAchievements()" class="text-[10px] text-zinc-500 hover:text-white font-bold uppercase tracking-widest transition">
                        View All Achievements
                    </button>
                </div>
            </div>
        </div>
    </section>

    <!-- 社区互动区 -->
    <section class="max-w-[1400px] mx-auto px-8 mb-24">
        <div class="grid md:grid-cols-2 gap-8">
            <!-- Prompt 盲盒 -->
            <div class="relative group cursor-pointer overflow-hidden rounded-[2.5rem] bg-gradient-to-br from-purple-900/40 to-black border border-white/5 p-10 flex flex-col items-center justify-center text-center transition-all hover:border-purple-500/40" onclick="getBlindBox()">
                <div class="absolute top-0 right-0 p-4 opacity-20 group-hover:opacity-100 transition-opacity">
                    <svg class="w-20 h-20 text-purple-500" fill="currentColor" viewBox="0 0 24 24"><path d="M11 15h2v2h-2v-2m0-8h2v6h-2V7m1-5C6.47 2 2 6.47 2 12s4.47 10 10 10 10-4.47 10-10S17.53 2 12 2m0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"/></svg>
                </div>
                <h3 class="text-white text-2xl font-black italic uppercase tracking-tighter mb-2">Prompt Mystery Box</h3>
                <p class="text-zinc-500 text-xs mb-6 font-bold uppercase tracking-widest">Randomly generate masterpiece seeds</p>
                <div id="blindBoxResult" class="hidden text-cyan-400 text-[10px] font-mono mb-6 bg-black/60 p-4 rounded-xl border border-cyan-500/20 w-full text-left max-h-32 overflow-y-auto"></div>
                <span class="bg-purple-600 text-white text-[10px] font-black px-8 py-3 rounded-full uppercase tracking-widest group-hover:bg-purple-400 transition">Roll the Dice</span>
            </div>

            <!-- 用户收藏夹 -->
            <div class="rounded-[2.5rem] bg-zinc-900/40 border border-white/5 p-10 flex flex-col justify-center">
                <div class="flex items-center gap-4 mb-6">
                    <span class="bg-red-500 w-3 h-3 rounded-full animate-ping"></span>
                    <h3 class="text-white font-black text-xs uppercase tracking-[0.2em]">My Favorites</h3>
                </div>
                
                <div id="favoritesList" class="space-y-3 mb-6 max-h-40 overflow-y-auto">
                    <p class="text-zinc-500 text-sm">No favorites yet</p>
                </div>
                
                <div class="flex gap-4">
                    <button onclick="clearFavorites()" class="text-[10px] font-black text-zinc-500 uppercase tracking-widest hover:text-white transition">Clear All</button>
                    <button onclick="exportFavorites()" class="text-[10px] font-black text-zinc-500 uppercase tracking-widest hover:text-white transition">Export List</button>
                </div>
            </div>
        </div>
    </section>
    '''

def generate_style_options():
    """生成风格选项"""
    options = ""
    for style_name in STYLE_PRESETS.keys():
        options += f'<option value="{style_name}">{style_name}</option>'
    return options

def generate_enhanced_scripts():
    """生成增强版 JavaScript"""
    return f'''
    <script>
        // 扩展的 Prompt 功能
        function expandPrompt() {{
            const input = document.getElementById('promptInput');
            const styleSelect = document.getElementById('styleSelect');
            const notice = document.getElementById('copyNotice');
            
            if(!input.value) return;
            
            let enhancements = ", hyper-realistic, highly detailed textures, cinematic lighting, shot on 35mm lens, f/1.8, 8k resolution, masterwork, intricate details, flux style";
            
            // 添加选择的风格
            const selectedStyle = styleSelect.value;
            if (selectedStyle) {{
                const styleEnhancements = {json.dumps(STYLE_PRESETS)};
                enhancements += styleEnhancements[selectedStyle] || "";
            }}
            
            input.value = input.value + enhancements;
            input.select();
            document.execCommand('copy');
            
            // 更新用户统计
            userProgress.addPromptGeneration();
            updateUserStats();
            
            notice.style.opacity = '1';
            setTimeout(() => notice.style.opacity = '0', 2000);
        }}
        
        // 随机生成 Prompt
        function generateRandomPrompt() {{
            const prompts = {json.dumps([generate_random_prompt() for _ in range(10)])};
            const randomPrompt = prompts[Math.floor(Math.random() * prompts.length)];
            
            document.getElementById('promptInput').value = randomPrompt;
            userProgress.addPromptGeneration();
            updateUserStats();
            showNotification('🎲 Random Prompt', 'New creative prompt generated!');
        }}
        
        // 复制分辨率
        function copyRes(val) {{
            const el = document.createElement('textarea');
            el.value = val;
            document.body.appendChild(el);
            el.select();
            document.execCommand('copy');
            document.body.removeChild(el);
            showNotification('📋 Copied', `Resolution ${{val}} copied to clipboard`);
        }}
        
        // 挑战相关功能
        function copyChallenge(seed, prompt) {{
            const challengeText = `Seed: ${{seed}}\\nPrompt: ${{prompt}}`;
            const el = document.createElement('textarea');
            el.value = challengeText;
            document.body.appendChild(el);
            el.select();
            document.execCommand('copy');
            document.body.removeChild(el);
            showNotification('🎯 Challenge Accepted', 'Seed and prompt copied!');
        }}
        
        function shareChallenge() {{
            const challengeUrl = window.location.href + '#challenge';
            if (navigator.share) {{
                navigator.share({{
                    title: 'Daily Flux Challenge',
                    text: 'Join today\\'s AI image generation challenge!',
                    url: challengeUrl
                }});
            }} else {{
                const el = document.createElement('textarea');
                el.value = challengeUrl;
                document.body.appendChild(el);
                el.select();
                document.execCommand('copy');
                document.body.removeChild(el);
                showNotification('🔗 Link Copied', 'Share link copied to clipboard');
            }}
        }}
        
        // 盲盒功能
        function getBlindBox() {{
            const prompts = {json.dumps([generate_random_prompt() for _ in range(20)])};
            const random = prompts[Math.floor(Math.random() * prompts.length)];
            const display = document.getElementById('blindBoxResult');
            
            display.innerText = random;
            display.classList.remove('hidden');
            
            // 自动复制到剪贴板
            const el = document.createElement('textarea');
            el.value = random;
            document.body.appendChild(el);
            el.select();
            document.execCommand('copy');
            document.body.removeChild(el);
            
            userProgress.addPromptGeneration();
            updateUserStats();
            showNotification('🎁 Mystery Box Opened', 'Secret prompt copied!');
        }}
        
        // 收藏功能
        function toggleFavorite(imageName) {{
            const favorites = userProgress.data.favoriteImages || [];
            const index = favorites.indexOf(imageName);
            
            if (index > -1) {{
                favorites.splice(index, 1);
                showNotification('💔 Unfavorited', 'Removed from favorites');
            }} else {{
                favorites.push(imageName);
                showNotification('❤️ Favorited', 'Added to favorites');
            }}
            
            userProgress.data.favoriteImages = favorites;
            userProgress.save();
            updateFavoritesList();
            updateFavoriteButtons();
        }}
        
        function updateFavoritesList() {{
            const favoritesList = document.getElementById('favoritesList');
            const favorites = userProgress.data.favoriteImages || [];
            
            if (favorites.length === 0) {{
                favoritesList.innerHTML = '<p class="text-zinc-500 text-sm">No favorites yet</p>';
            }} else {{
                favoritesList.innerHTML = favorites.map(img => 
                    `<div class="flex items-center justify-between bg-black/20 p-2 rounded-lg">
                        <span class="text-xs text-zinc-300 truncate">${{img}}</span>
                        <button onclick="toggleFavorite('${{img}}')" class="text-red-400 hover:text-red-300 text-xs">×</button>
                    </div>`
                ).join('');
            }}
        }}
        
        function updateFavoriteButtons() {{
            const favorites = userProgress.data.favoriteImages || [];
            document.querySelectorAll('[data-favorite-btn]').forEach(btn => {{
                const imageName = btn.getAttribute('data-image');
                const isFavorited = favorites.includes(imageName);
                btn.innerHTML = isFavorited ? '💖' : '🤍';
                btn.title = isFavorited ? 'Remove from favorites' : 'Add to favorites';
            }});
        }}
        
        function clearFavorites() {{
            if (confirm('Are you sure you want to clear all favorites?')) {{
                userProgress.data.favoriteImages = [];
                userProgress.save();
                updateFavoritesList();
                updateFavoriteButtons();
                showNotification('🗑️ Cleared', 'Favorites cleared');
            }}
        }}
        
        function exportFavorites() {{
            const favorites = userProgress.data.favoriteImages || [];
            if (favorites.length === 0) {{
                showNotification('📝 Export Failed', 'No favorites to export');
                return;
            }}
            
            const exportData = favorites.join('\\n');
            const el = document.createElement('textarea');
            el.value = exportData;
            document.body.appendChild(el);
            el.select();
            document.execCommand('copy');
            document.body.removeChild(el);
            showNotification('📋 Export Success', 'Favorites list copied to clipboard');
        }}
        
        // 成就系统
        function updateAchievementsList() {{
            const achievementsList = document.getElementById('achievementsList');
            const achievements = userProgress.data.achievements || [];
            
            const allAchievements = [
                {{ id: 'first_visit', name: 'First Visit', desc: 'Welcome to FreeFineAI!', icon: '👋' }},
                {{ id: 'regular_visitor', name: 'Regular Visitor', desc: 'Visit the site 5 times', icon: '🏠' }},
                {{ id: 'download_master', name: 'Download Master', desc: 'Download 10 images', icon: '📥' }},
                {{ id: 'prompt_creator', name: 'Prompt Creator', desc: 'Generate 20 prompts', icon: '✨' }},
                {{ id: 'streak_week', name: 'Week Streak', desc: 'Visit 7 days in a row', icon: '🔥' }}
            ];
            
            const recentAchievements = allAchievements
                .filter(a => achievements.includes(a.id))
                .slice(-3);
            
            if (recentAchievements.length === 0) {{
                achievementsList.innerHTML = '<p class="text-zinc-500 text-xs">Complete tasks to unlock achievements</p>';
            }} else {{
                achievementsList.innerHTML = recentAchievements.map(achievement => 
                    `<div class="flex items-center gap-3 bg-black/20 p-3 rounded-lg">
                        <span class="text-lg">${{achievement.icon}}</span>
                        <div>
                            <div class="text-white text-xs font-bold">${{achievement.name}}</div>
                            <div class="text-zinc-400 text-[10px]">${{achievement.desc}}</div>
                        </div>
                    </div>`
                ).join('');
            }}
        }}
        
        function showAllAchievements() {{
            // 这里可以实现一个模态框显示所有成就
            showNotification('🏆 Achievement System', 'More achievement features coming soon!');
        }}
        
        // 下载追踪
        function trackDownload(imageName) {{
            userProgress.addDownload();
            updateUserStats();
            showNotification('📥 Download Success', 'Thanks for supporting FreeFineAI!');
        }}
        
        // 页面加载完成后初始化
        document.addEventListener('DOMContentLoaded', function() {{
            updateUserStats();
            updateFavoritesList();
            updateFavoriteButtons();
            updateAchievementsList();
        }});
    </script>
    '''

# === 5. 生成主页面 ===
def generate():
    setup()
    
    with open(os.path.join(CONFIG["TEMPLATE_DIR"], "head.html"), "r", encoding="utf-8") as f: 
        head = f.read()

    images = sorted([f for f in os.listdir(CONFIG["IMG_DIR"]) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))], reverse=True)
    
    # 生成图片卡片（增强版）
    cards_html = ""
    for img in images:
        name = img.split('.')[0].replace('_', ' ').title()
        cards_html += f'''
        <div class="break-inside-avoid mb-8 relative group rounded-3xl overflow-hidden bg-zinc-900 border border-white/5 shadow-2xl transition-all duration-500 hover:border-cyan-500/50">
            <img src="images/{img}" alt="{name}" loading="lazy" class="w-full h-auto transition-transform duration-700 group-hover:scale-105">
            <div class="absolute inset-0 bg-gradient-to-t from-black via-black/60 to-transparent opacity-0 group-hover:opacity-100 transition-all duration-300 p-6 flex flex-col justify-end">
                <h3 class="text-white font-bold text-sm mb-4">{name}</h3>
                <div class="flex gap-2 text-center">
                    <a href="images/{img}" download onclick="trackDownload('{img}')" class="flex-1 bg-white text-black text-[10px] font-black py-3 rounded-xl uppercase">Download</a>
                    <button onclick="toggleFavorite('{img}')" data-favorite-btn data-image="{img}" class="bg-zinc-800 text-white px-4 py-3 rounded-xl hover:bg-pink-600 transition-all" title="添加收藏">🤍</button>
                    <a href="{CONFIG["TIP_JAR_URL"]}" target="_blank" class="bg-zinc-800 text-white px-4 py-3 rounded-xl hover:bg-blue-600 transition-all">❤</a>
                </div>
            </div>
        </div>
        '''

    # 组合页面内容
    body_content = f'''
    <header class="pt-48 pb-20 px-6 text-center">
        <div class="inline-block px-4 py-1 mb-6 border border-cyan-500/20 rounded-full bg-cyan-500/5 text-cyan-400 text-[10px] font-bold uppercase tracking-widest">Flux.1 Master Library</div>
        <h1 class="text-7xl md:text-9xl font-black mb-8 leading-none hero-title text-white">FLUX RAW.</h1>
        <p class="max-w-2xl mx-auto text-zinc-500 text-lg font-light leading-relaxed mb-12">
            Curated, high-fidelity AI assets. Free for the community, <br>designed for the visionaries.
        </p>
    </header>

    {generate_enhanced_tools()}

    <main class="max-w-[1400px] mx-auto px-6 pb-40">
        <div class="flex flex-col md:flex-row justify-between items-end mb-12 gap-4">
            <h2 class="text-white text-2xl font-black tracking-tighter uppercase italic">Recent Archive</h2>
            <p class="text-[10px] text-zinc-600 font-bold uppercase tracking-[0.3em]">Filtered by: Flux.1-Dev</p>
        </div>
        <div class="masonry">{cards_html}</div>
        
        <section class="mt-40 p-12 md:p-24 rounded-[4rem] bg-gradient-to-br from-zinc-900/80 via-zinc-900/40 to-transparent border border-white/5 relative overflow-hidden">
            <div class="absolute -top-24 -right-24 w-96 h-96 bg-cyan-500/10 blur-[120px] rounded-full"></div>
            
            <div class="relative z-10 max-w-3xl">
                <h2 class="text-4xl md:text-6xl font-black text-white mb-8 tracking-tighter leading-none">
                    Push the Boundaries <br><span class="text-cyan-500">of Flux.1</span>
                </h2>
                
                <div class="grid md:grid-cols-2 gap-8 text-left mb-12">
                    <div>
                        <p class="text-zinc-400 text-sm leading-relaxed">
                            <span class="text-white font-bold block mb-1">Standard Access</span>
                            Enjoy our curated gallery with high-quality web-ready assets. Perfect for social media, concepts, and daily inspiration. Always free, always fresh.
                        </p>
                    </div>
                    <div>
                        <p class="text-zinc-400 text-sm leading-relaxed">
                            <span class="text-white font-bold block mb-1">The Pro Vault</span>
                            For those who need every pixel. Unlock 4K uncompressed renders, complete prompt metadata (JSON), and full commercial usage rights.
                        </p>
                    </div>
                </div>

                <div class="flex flex-col sm:flex-row gap-6 items-center">
                    <a href="{CONFIG['MEGA_BUNDLE_URL']}" target="_blank" class="w-full sm:w-auto bg-white text-black font-black px-10 py-5 rounded-2xl hover:bg-cyan-400 transition-all transform hover:scale-105 uppercase tracking-widest text-xs shadow-2xl">
                        Unlock Pro Vault — $9.99
                    </a>
                    <div class="text-[10px] text-zinc-600 uppercase tracking-[0.2em] font-bold">
                        One-time support • Lifetime updates
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer class="mt-40 border-t border-white/5 bg-zinc-950/50 py-24 px-8 relative overflow-hidden">
        <div class="absolute bottom-0 left-0 w-full h-1 bg-gradient-to-r from-transparent via-cyan-500/20 to-transparent"></div>
        <div class="max-w-[1400px] mx-auto grid grid-cols-1 md:grid-cols-4 gap-12 text-left mb-20">
            <div class="md:col-span-1">
                <span class="text-white font-black text-2xl tracking-tighter italic uppercase block mb-4">FREEFINE<span class="text-cyan-500">AI</span></span>
                <p class="text-zinc-500 text-xs leading-relaxed max-w-xs">Independent archive for Flux.1-dev assets. Built for the community.</p>
            </div>
            <div>
                <h4 class="text-white text-[10px] font-black uppercase tracking-[0.2em] mb-6">Navigation</h4>
                <ul class="space-y-4 text-xs font-bold">
                    <li><a href="#" class="text-zinc-600 hover:text-cyan-400 transition uppercase tracking-widest">Gallery</a></li>
                    <li><a href="{CONFIG['MEGA_BUNDLE_URL']}" class="text-zinc-600 hover:text-cyan-400 transition uppercase tracking-widest">Pro Vault</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-white text-[10px] font-black uppercase tracking-[0.2em] mb-6">Legal</h4>
                <p class="text-[10px] text-zinc-600 font-bold uppercase">CC BY-NC 4.0 License</p>
            </div>
            <div>
                <h4 class="text-white text-[10px] font-black uppercase tracking-[0.2em] mb-6">Status</h4>
                <div class="flex items-center gap-2"><div class="w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse"></div><span class="text-[9px] text-zinc-400 uppercase font-bold">Operational</span></div>
            </div>
        </div>
        <div class="max-w-[1400px] mx-auto flex flex-col md:flex-row justify-between items-center pt-12 border-t border-white/5 gap-6">
            <p class="text-[10px] tracking-[0.5em] text-zinc-800 uppercase italic font-black">&copy; 2026 FREEFINEAI</p>
            <div class="flex gap-8">
                <a href="#" class="text-zinc-800 hover:text-white text-[9px] font-black uppercase transition">Twitter</a>
                <a href="#" class="text-zinc-800 hover:text-white text-[9px] font-black uppercase transition">GitHub</a>
            </div>
        </div>
    </footer>
    
    {generate_enhanced_scripts()}
</body>
</html>
'''

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(head + body_content)
    
    print(f"🚀 Enhanced website generated successfully!")
    print(f"📊 Includes {len(images)} images")
    print(f"✨ New features: User progress tracking, achievement system, favorites, daily challenges, AI prompt generator")
    print(f"💰 Monetization features: Enhanced user engagement, optimized donation flow, pro version promotion")

if __name__ == "__main__":
    generate()