import os
import json
import random
import configparser
from datetime import datetime

class ConfigManager:
    """配置文件管理器"""
    def __init__(self, config_file="settings.config"):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.load_config()
    
    def load_config(self):
        """加载配置文件"""
        if os.path.exists(self.config_file):
            self.config.read(self.config_file, encoding='utf-8')
        else:
            self.create_default_config()
    
    def create_default_config(self):
        """创建默认配置文件"""
        default_config = """# FreeFineAI 网站配置文件
# 修改这个文件来自定义你的网站

[BASIC]
DOMAIN = FreeFineAI.com
SITE_TITLE = FreeFineAI | Premium Flux.1 Digital Assets
SITE_DESCRIPTION = 精选高保真 AI 资源。为社区免费提供，为远见者而设计。

[PAYMENT]
TIP_JAR_URL = https://www.paypal.com/ncp/payment/ZRQDBKWE7VBSU
MEGA_BUNDLE_URL = https://www.paypal.com/ncp/payment/AQSGVVXLW69GJ
BUNDLE_PRICE = ¥68
COFFEE_URL = https://www.freefineai.com

[DIRECTORIES]
IMG_DIR = images
TEMPLATE_DIR = templates
DATA_DIR = data

[FEATURES]
ENABLE_ACHIEVEMENTS = true
ENABLE_DAILY_CHALLENGE = true
ENABLE_FAVORITES = true
ENABLE_USER_STATS = true
ENABLE_NOTIFICATIONS = true
ENABLE_PWA = false

[SOCIAL]
TWITTER_URL = #
GITHUB_URL = #
DISCORD_URL = #

[ANALYTICS]
GOOGLE_ANALYTICS_ID = 
ENABLE_TRACKING = false

[CUSTOMIZATION]
PRIMARY_COLOR = cyan
ACCENT_COLOR = purple
THEME = dark
LANGUAGE = zh-CN

[CONTENT]
MAX_IMAGES_PER_PAGE = 50
ENABLE_LAZY_LOADING = true
IMAGE_QUALITY = high
ENABLE_WATERMARK = false

[ADVANCED]
ENABLE_SERVICE_WORKER = false
CACHE_DURATION = 7
DEBUG_MODE = false"""
        
        with open(self.config_file, 'w', encoding='utf-8') as f:
            f.write(default_config)
        self.config.read(self.config_file, encoding='utf-8')
    
    def get(self, section, key, fallback=None):
        """获取配置值"""
        try:
            return self.config.get(section, key)
        except:
            return fallback
    
    def getboolean(self, section, key, fallback=False):
        """获取布尔配置值"""
        try:
            return self.config.getboolean(section, key)
        except:
            return fallback
    
    def getint(self, section, key, fallback=0):
        """获取整数配置值"""
        try:
            return self.config.getint(section, key)
        except:
            return fallback

# 初始化配置管理器
config = ConfigManager()

# === 1. 从配置文件读取设置 ===
CONFIG = {
    "DOMAIN": config.get("BASIC", "DOMAIN", "FreeFineAI.com"),
    "SITE_TITLE": config.get("BASIC", "SITE_TITLE", "FreeFineAI | Premium Flux.1 Digital Assets"),
    "SITE_DESCRIPTION": config.get("BASIC", "SITE_DESCRIPTION", "精选高保真 AI 资源"),
    "TIP_JAR_URL": config.get("PAYMENT", "TIP_JAR_URL", "https://www.paypal.com/ncp/payment/ZRQDBKWE7VBSU"),
    "MEGA_BUNDLE_URL": config.get("PAYMENT", "MEGA_BUNDLE_URL", "https://www.paypal.com/ncp/payment/AQSGVVXLW69GJ"),
    "BUNDLE_PRICE": config.get("PAYMENT", "BUNDLE_PRICE", "¥68"),
    "COFFEE_URL": config.get("PAYMENT", "COFFEE_URL", "https://www.freefineai.com"),
    "IMG_DIR": config.get("DIRECTORIES", "IMG_DIR", "images"),
    "TEMPLATE_DIR": config.get("DIRECTORIES", "TEMPLATE_DIR", "templates"),
    "DATA_DIR": config.get("DIRECTORIES", "DATA_DIR", "data"),
    
    # 功能开关
    "ENABLE_ACHIEVEMENTS": config.getboolean("FEATURES", "ENABLE_ACHIEVEMENTS", True),
    "ENABLE_DAILY_CHALLENGE": config.getboolean("FEATURES", "ENABLE_DAILY_CHALLENGE", True),
    "ENABLE_FAVORITES": config.getboolean("FEATURES", "ENABLE_FAVORITES", True),
    "ENABLE_USER_STATS": config.getboolean("FEATURES", "ENABLE_USER_STATS", True),
    "ENABLE_NOTIFICATIONS": config.getboolean("FEATURES", "ENABLE_NOTIFICATIONS", True),
    "ENABLE_PWA": config.getboolean("FEATURES", "ENABLE_PWA", False),
    
    # 社交链接
    "TWITTER_URL": config.get("SOCIAL", "TWITTER_URL", "#"),
    "GITHUB_URL": config.get("SOCIAL", "GITHUB_URL", "#"),
    "DISCORD_URL": config.get("SOCIAL", "DISCORD_URL", "#"),
    
    # 分析
    "GOOGLE_ANALYTICS_ID": config.get("ANALYTICS", "GOOGLE_ANALYTICS_ID", ""),
    "ENABLE_TRACKING": config.getboolean("ANALYTICS", "ENABLE_TRACKING", False),
    
    # 自定义
    "PRIMARY_COLOR": config.get("CUSTOMIZATION", "PRIMARY_COLOR", "cyan"),
    "ACCENT_COLOR": config.get("CUSTOMIZATION", "ACCENT_COLOR", "purple"),
    "THEME": config.get("CUSTOMIZATION", "THEME", "dark"),
    "LANGUAGE": config.get("CUSTOMIZATION", "LANGUAGE", "zh-CN"),
    
    # 内容
    "MAX_IMAGES_PER_PAGE": config.getint("CONTENT", "MAX_IMAGES_PER_PAGE", 50),
    "ENABLE_LAZY_LOADING": config.getboolean("CONTENT", "ENABLE_LAZY_LOADING", True),
    "IMAGE_QUALITY": config.get("CONTENT", "IMAGE_QUALITY", "high"),
    "ENABLE_WATERMARK": config.getboolean("CONTENT", "ENABLE_WATERMARK", False),
    
    # 高级
    "ENABLE_SERVICE_WORKER": config.getboolean("ADVANCED", "ENABLE_SERVICE_WORKER", False),
    "CACHE_DURATION": config.getint("ADVANCED", "CACHE_DURATION", 7),
    "DEBUG_MODE": config.getboolean("ADVANCED", "DEBUG_MODE", False)
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

def print_config_info():
    """打印配置信息"""
    print("📋 当前配置:")
    print(f"   网站标题: {CONFIG['SITE_TITLE']}")
    print(f"   域名: {CONFIG['DOMAIN']}")
    print(f"   Bundle价格: {CONFIG['BUNDLE_PRICE']}")
    print(f"   主色调: {CONFIG['PRIMARY_COLOR']}")
    print(f"   语言: {CONFIG['LANGUAGE']}")
    print(f"   成就系统: {'✅' if CONFIG['ENABLE_ACHIEVEMENTS'] else '❌'}")
    print(f"   每日挑战: {'✅' if CONFIG['ENABLE_DAILY_CHALLENGE'] else '❌'}")
    print(f"   收藏功能: {'✅' if CONFIG['ENABLE_FAVORITES'] else '❌'}")
    print(f"   PWA支持: {'✅' if CONFIG['ENABLE_PWA'] else '❌'}")
    print(f"   调试模式: {'✅' if CONFIG['DEBUG_MODE'] else '❌'}")

# === 3. 自动化组件初始化 ===
def setup():
    for folder in [CONFIG["IMG_DIR"], CONFIG["TEMPLATE_DIR"], CONFIG["DATA_DIR"]]:
        if not os.path.exists(folder):
            os.makedirs(folder)
    
    # 初始化用户数据文件
    init_user_data()
    
    # 生成 Head 模板
    generate_head_template()

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

def generate_head_template():
    """生成 Head 模板"""
    # 根据配置生成不同的颜色主题
    primary_color = CONFIG["PRIMARY_COLOR"]
    accent_color = CONFIG["ACCENT_COLOR"]
    
    # 颜色映射
    color_map = {
        "cyan": "6, 182, 212",
        "blue": "59, 130, 246", 
        "purple": "147, 51, 234",
        "pink": "236, 72, 153",
        "green": "34, 197, 94",
        "yellow": "234, 179, 8",
        "red": "239, 68, 68"
    }
    
    primary_rgb = color_map.get(primary_color, "6, 182, 212")
    accent_rgb = color_map.get(accent_color, "147, 51, 234")
    
    # Google Analytics 代码
    analytics_code = ""
    if CONFIG["ENABLE_TRACKING"] and CONFIG["GOOGLE_ANALYTICS_ID"]:
        analytics_code = f'''
    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={CONFIG["GOOGLE_ANALYTICS_ID"]}"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', '{CONFIG["GOOGLE_ANALYTICS_ID"]}');
    </script>
    '''
    
    # PWA 支持
    pwa_code = ""
    if CONFIG["ENABLE_PWA"]:
        pwa_code = '''
    <link rel="manifest" href="manifest.json">
    <meta name="theme-color" content="#050505">
    <link rel="apple-touch-icon" href="icon-192.png">
    '''
    
    head_content = f'''<!DOCTYPE html>
<html lang="{CONFIG["LANGUAGE"]}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{CONFIG["SITE_TITLE"]}</title>
    <meta name="description" content="{CONFIG["SITE_DESCRIPTION"]}">
    {analytics_code}
    {pwa_code}
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary-color: {primary_rgb};
            --accent-color: {accent_rgb};
        }}
        body {{ background-color: #050505; color: #a1a1aa; font-family: 'Inter', sans-serif; margin: 0; overflow-x: hidden; }}
        .masonry {{ column-count: 1; column-gap: 1.5rem; }}
        @media (min-width: 768px) {{ .masonry {{ column-count: 2; }} }}
        @media (min-width: 1280px) {{ .masonry {{ column-count: 3; }} }}
        .nav-glass {{ background: rgba(0,0,0,0.85); backdrop-filter: blur(15px); border-bottom: 1px solid rgba(255,255,255,0.05); }}
        #particle-canvas {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none; }}
        nav, header, main, footer {{ position: relative; z-index: 10; }}
        .hero-title {{ -webkit-text-stroke: 1px rgba(255,255,255,0.1); color: transparent; transition: all 0.5s; }}
        .hero-title:hover {{ color: white; -webkit-text-stroke: 1px transparent; }}
        .notification {{ position: fixed; top: 100px; right: 20px; z-index: 1000; transform: translateX(400px); transition: transform 0.3s ease; }}
        .notification.show {{ transform: translateX(0); }}
        .streak-badge {{ animation: pulse 2s infinite; }}
        @keyframes pulse {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.7; }} }}
        .primary-color {{ color: rgb(var(--primary-color)); }}
        .accent-color {{ color: rgb(var(--accent-color)); }}
        .bg-primary {{ background-color: rgb(var(--primary-color)); }}
        .bg-accent {{ background-color: rgb(var(--accent-color)); }}
        .border-primary {{ border-color: rgb(var(--primary-color)); }}
        .border-accent {{ border-color: rgb(var(--accent-color)); }}
    </style>
</head>
<body>
    <canvas id="particle-canvas"></canvas>
    
    <!-- 通知系统 -->
    {generate_notification_html() if CONFIG["ENABLE_NOTIFICATIONS"] else ""}
    
    <script>
        // 配置对象
        window.SITE_CONFIG = {json.dumps({
            "ENABLE_ACHIEVEMENTS": CONFIG["ENABLE_ACHIEVEMENTS"],
            "ENABLE_DAILY_CHALLENGE": CONFIG["ENABLE_DAILY_CHALLENGE"], 
            "ENABLE_FAVORITES": CONFIG["ENABLE_FAVORITES"],
            "ENABLE_USER_STATS": CONFIG["ENABLE_USER_STATS"],
            "ENABLE_NOTIFICATIONS": CONFIG["ENABLE_NOTIFICATIONS"],
            "PRIMARY_COLOR": CONFIG["PRIMARY_COLOR"],
            "ACCENT_COLOR": CONFIG["ACCENT_COLOR"],
            "DEBUG_MODE": CONFIG["DEBUG_MODE"]
        })};
        
        // 粒子系统
        window.addEventListener('DOMContentLoaded', () => {{
            const canvas = document.getElementById('particle-canvas');
            if (!canvas) return;
            
            const ctx = canvas.getContext('2d');
            let particles = [];
            const resize = () => {{ canvas.width = window.innerWidth; canvas.height = window.innerHeight; }};
            
            class Particle {{
                constructor() {{ this.init(); }}
                init() {{
                    this.x = Math.random() * canvas.width;
                    this.y = Math.random() * canvas.height;
                    this.size = Math.random() * 1.5 + 0.5;
                    this.speedX = Math.random() * 0.4 - 0.2;
                    this.speedY = Math.random() * 0.4 - 0.2;
                    this.opacity = Math.random() * 0.5 + 0.1;
                }}
                update() {{
                    this.x += this.speedX; this.y += this.speedY;
                    if(this.x > canvas.width || this.x < 0) this.speedX *= -1;
                    if(this.y > canvas.height || this.y < 0) this.speedY *= -1;
                }}
                draw() {{
                    ctx.beginPath(); ctx.arc(this.x, this.y, this.size, 0, Math.PI*2);
                    ctx.fillStyle = `rgba({primary_rgb}, ${{this.opacity}})`; ctx.fill();
                }}
            }}
            
            const animate = () => {{
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                particles.forEach(p => {{ p.update(); p.draw(); }});
                requestAnimationFrame(animate);
            }};
            
            window.addEventListener('resize', resize);
            resize();
            for(let i=0; i<100; i++) particles.push(new Particle());
            animate();
        }});
        
        {generate_user_progress_js() if CONFIG["ENABLE_USER_STATS"] else ""}
    </script>
    
    <nav class="fixed top-0 w-full z-50 nav-glass px-8 py-5 flex justify-between items-center">
        <span class="text-white font-black text-xl tracking-tighter italic">FREEFINE<span class="primary-color">AI</span></span>
        <div class="flex items-center gap-6">
            {generate_user_stats_html() if CONFIG["ENABLE_USER_STATS"] else ""}
            <a href="{CONFIG["TIP_JAR_URL"]}" target="_blank" class="hidden sm:block text-[10px] font-bold text-zinc-500 hover:text-white uppercase tracking-widest">Support</a>
            <a href="{CONFIG["MEGA_BUNDLE_URL"]}" target="_blank" class="bg-white text-black text-[10px] font-black px-6 py-2 rounded-full uppercase tracking-tighter hover:bg-primary transition">Get Bundle {CONFIG["BUNDLE_PRICE"]}</a>
        </div>
    </nav>
'''
    
    with open(os.path.join(CONFIG["TEMPLATE_DIR"], "head.html"), "w", encoding="utf-8") as f: 
        f.write(head_content)

def generate_notification_html():
    """生成通知HTML"""
    return '''<div id="notification" class="notification bg-gradient-to-r from-primary to-accent text-white p-4 rounded-2xl shadow-2xl max-w-sm">
        <div class="flex items-center gap-3">
            <div class="w-8 h-8 bg-white/20 rounded-full flex items-center justify-center">
                <span class="text-sm">🎉</span>
            </div>
            <div>
                <div class="font-bold text-sm" id="notificationTitle">恭喜！</div>
                <div class="text-xs opacity-90" id="notificationText">你获得了新成就</div>
            </div>
        </div>
    </div>'''

def generate_user_stats_html():
    """生成用户统计HTML"""
    return '''<!-- 用户进度显示 -->
            <div class="hidden md:flex items-center gap-4 text-xs">
                <div class="flex items-center gap-1">
                    <span class="primary-color">📊</span>
                    <span class="text-zinc-400" id="userStats">访问: 0 | 下载: 0</span>
                </div>
                <div class="flex items-center gap-1 streak-badge" id="streakBadge" style="display: none;">
                    <span class="text-yellow-400">🔥</span>
                    <span class="text-yellow-400" id="streakCount">0</span>
                </div>
            </div>'''

def generate_user_progress_js():
    """生成用户进度JavaScript"""
    return '''
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
                if (window.SITE_CONFIG.DEBUG_MODE) {
                    console.log('用户数据已保存:', this.data);
                }
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
                    if (window.SITE_CONFIG.ENABLE_ACHIEVEMENTS) this.checkAchievements();
                    this.save();
                }
            }
            
            addDownload() {
                this.data.downloads++;
                if (window.SITE_CONFIG.ENABLE_ACHIEVEMENTS) this.checkAchievements();
                this.save();
            }
            
            addPromptGeneration() {
                this.data.promptsGenerated++;
                if (window.SITE_CONFIG.ENABLE_ACHIEVEMENTS) this.checkAchievements();
                this.save();
            }
            
            checkAchievements() {
                const achievements = [
                    { id: 'first_visit', name: '初次访问', desc: '欢迎来到 FreeFineAI！', condition: () => this.data.visits >= 1 },
                    { id: 'regular_visitor', name: '常客', desc: '访问网站 5 次', condition: () => this.data.visits >= 5 },
                    { id: 'download_master', name: '下载达人', desc: '下载 10 张图片', condition: () => this.data.downloads >= 10 },
                    { id: 'prompt_creator', name: 'Prompt 创作者', desc: '生成 20 个提示词', condition: () => this.data.promptsGenerated >= 20 },
                    { id: 'streak_week', name: '连续一周', desc: '连续访问 7 天', condition: () => this.data.streak >= 7 }
                ];
                
                achievements.forEach(achievement => {
                    if (achievement.condition() && !this.data.achievements.includes(achievement.id)) {
                        this.data.achievements.push(achievement.id);
                        if (window.SITE_CONFIG.ENABLE_NOTIFICATIONS) {
                            this.showNotification(achievement.name, achievement.desc);
                        }
                    }
                });
            }
            
            showNotification(title, text) {
                if (!window.SITE_CONFIG.ENABLE_NOTIFICATIONS) return;
                
                const notification = document.getElementById('notification');
                const titleEl = document.getElementById('notificationTitle');
                const textEl = document.getElementById('notificationText');
                
                if (notification && titleEl && textEl) {
                    titleEl.textContent = title;
                    textEl.textContent = text;
                    notification.classList.add('show');
                    
                    setTimeout(() => {
                        notification.classList.remove('show');
                    }, 4000);
                }
            }
        }
        
        // 初始化用户进度
        const userProgress = new UserProgress();
        userProgress.addVisit();
        
        // 通知函数
        function showNotification(title, text) {
            if (window.userProgress) {
                userProgress.showNotification(title, text);
            }
        }
        
        // 更新用户统计显示
        function updateUserStats() {
            const stats = document.getElementById('userStats');
            const streakBadge = document.getElementById('streakBadge');
            const streakCount = document.getElementById('streakCount');
            
            if (stats) {
                stats.textContent = `访问: ${userProgress.data.visits} | 下载: ${userProgress.data.downloads}`;
            }
            
            if (userProgress.data.streak > 0 && streakBadge && streakCount) {
                streakBadge.style.display = 'flex';
                streakCount.textContent = userProgress.data.streak;
            }
        }
        
        // 页面加载完成后更新统计
        document.addEventListener('DOMContentLoaded', updateUserStats);
    '''# ==
= 4. 生成增强功能组件 ===
def generate_enhanced_tools():
    """生成增强版工具箱"""
    daily_challenge = get_daily_challenge()
    
    return f'''
    <!-- 每日挑战横幅 -->
    <section class="max-w-[1400px] mx-auto px-8 mb-8">
        <div class="bg-gradient-to-r from-purple-900/40 via-blue-900/40 to-cyan-900/40 border border-purple-500/20 rounded-3xl p-6 relative overflow-hidden">
            <div class="absolute top-0 right-0 p-4">
                <div class="bg-red-500 w-2 h-2 rounded-full animate-ping"></div>
            </div>
            <div class="flex flex-col md:flex-row items-center justify-between gap-4">
                <div>
                    <h3 class="text-white font-black text-base mb-1">🎯 今日挑战 #{daily_challenge['seed']}</h3>
                    <p class="text-zinc-300 text-sm mb-1">"{daily_challenge['prompt']}"</p>
                    <span class="text-xs text-purple-400 font-bold">难度: {daily_challenge['difficulty']}</span>
                </div>
                <div class="flex gap-2">
                    <button onclick="copyChallenge('{daily_challenge['seed']}', '{daily_challenge['prompt']}')" class="bg-purple-600 hover:bg-purple-500 text-white text-xs font-black px-4 py-2 rounded-xl uppercase tracking-widest transition">
                        接受挑战
                    </button>
                    <button onclick="shareChallenge()" class="bg-zinc-800 hover:bg-zinc-700 text-white px-3 py-2 rounded-xl transition">
                        📤
                    </button>
                </div>
            </div>
        </div>
    </section>

    <!-- 增强工具箱 -->
    <section class="max-w-[1400px] mx-auto px-8 mb-12">
        <div class="grid md:grid-cols-3 gap-6">
            <!-- AI Prompt 生成器 -->
            <div class="bg-zinc-900/50 border border-white/5 p-6 rounded-3xl backdrop-blur-md relative overflow-hidden group">
                <div class="flex items-center gap-3 mb-4">
                    <div class="p-2 bg-cyan-500/10 rounded-lg text-cyan-400">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                    </div>
                    <h3 class="text-white font-black text-xs uppercase tracking-[0.2em]">AI Prompt 生成器</h3>
                </div>
                <textarea id="promptInput" placeholder="输入简单概念 (例如: '赛博朋克城市')..." class="w-full bg-black/40 border border-white/5 rounded-xl p-3 text-sm text-zinc-300 h-20 mb-3 outline-none focus:border-cyan-500/50 transition resize-none"></textarea>
                
                <!-- 风格选择器 -->
                <div class="mb-3">
                    <select id="styleSelect" class="w-full bg-black/40 border border-white/5 rounded-xl p-2 text-xs text-zinc-300 outline-none focus:border-cyan-500/50">
                        <option value="">选择风格</option>
                        {generate_style_options()}
                    </select>
                </div>
                
                <div class="flex gap-2">
                    <button onclick="expandPrompt()" class="flex-1 bg-zinc-800 hover:bg-white hover:text-black text-white text-[10px] font-black py-3 rounded-xl uppercase tracking-widest transition shadow-lg">
                        增强提示词
                    </button>
                    <button onclick="generateRandomPrompt()" class="bg-purple-600 hover:bg-purple-500 text-white px-3 py-3 rounded-xl transition">
                        🎲
                    </button>
                </div>
                
                <div id="copyNotice" class="absolute top-3 right-6 text-[9px] text-cyan-500 font-bold opacity-0 transition-opacity uppercase tracking-widest">已复制!</div>
            </div>

            <!-- 分辨率预设 -->
            <div class="bg-zinc-900/50 border border-white/5 p-6 rounded-3xl backdrop-blur-md">
                <div class="flex items-center gap-3 mb-4">
                    <div class="p-2 bg-purple-500/10 rounded-lg text-purple-400">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4"/></svg>
                    </div>
                    <h3 class="text-white font-black text-xs uppercase tracking-[0.2em]">分辨率预设</h3>
                </div>
                <div class="grid grid-cols-1 gap-2">
                    <button onclick="copyRes('1344 x 768')" class="bg-black/40 border border-white/5 p-3 rounded-xl hover:border-cyan-500/50 group transition text-left">
                        <span class="block text-white font-bold text-xs">16:9 电影级</span>
                        <span class="text-[10px] text-zinc-600">1344 x 768 px</span>
                    </button>
                    <button onclick="copyRes('768 x 1344')" class="bg-black/40 border border-white/5 p-3 rounded-xl hover:border-cyan-500/50 group transition text-left">
                        <span class="block text-white font-bold text-xs">9:16 竖屏</span>
                        <span class="text-[10px] text-zinc-600">768 x 1344 px</span>
                    </button>
                    <button onclick="copyRes('1024 x 1024')" class="bg-black/40 border border-white/5 p-3 rounded-xl hover:border-cyan-500/50 group transition text-left">
                        <span class="block text-white font-bold text-xs">1:1 正方形</span>
                        <span class="text-[10px] text-zinc-600">1024 x 1024 px</span>
                    </button>
                </div>
            </div>

            <!-- 用户成就面板 -->
            <div class="bg-zinc-900/50 border border-white/5 p-6 rounded-3xl backdrop-blur-md">
                <div class="flex items-center gap-3 mb-4">
                    <div class="p-2 bg-yellow-500/10 rounded-lg text-yellow-400">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>
                    </div>
                    <h3 class="text-white font-black text-xs uppercase tracking-[0.2em]">我的成就</h3>
                </div>
                
                <div id="achievementsList" class="space-y-2 mb-3 max-h-32 overflow-y-auto">
                    <!-- 成就将通过 JavaScript 动态加载 -->
                </div>
                
                <div class="text-center">
                    <button onclick="showAllAchievements()" class="text-[10px] text-zinc-500 hover:text-white font-bold uppercase tracking-widest transition">
                        查看全部
                    </button>
                </div>
            </div>
        </div>
    </section>

    <!-- 社区互动区 -->
    <section class="max-w-[1400px] mx-auto px-8 mb-16">
        <div class="grid md:grid-cols-2 gap-6">
            <!-- Prompt 盲盒 -->
            <div class="relative group cursor-pointer overflow-hidden rounded-3xl bg-gradient-to-br from-purple-900/40 to-black border border-white/5 p-8 flex flex-col items-center justify-center text-center transition-all hover:border-purple-500/40" onclick="getBlindBox()">
                <div class="absolute top-0 right-0 p-3 opacity-20 group-hover:opacity-100 transition-opacity">
                    <svg class="w-16 h-16 text-purple-500" fill="currentColor" viewBox="0 0 24 24"><path d="M11 15h2v2h-2v-2m0-8h2v6h-2V7m1-5C6.47 2 2 6.47 2 12s4.47 10 10 10 10-4.47 10-10S17.53 2 12 2m0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"/></svg>
                </div>
                <h3 class="text-white text-xl font-black italic uppercase tracking-tighter mb-2">Prompt 盲盒</h3>
                <p class="text-zinc-500 text-xs mb-4 font-bold uppercase tracking-widest">随机生成杰作种子</p>
                <div id="blindBoxResult" class="hidden text-cyan-400 text-[10px] font-mono mb-4 bg-black/60 p-3 rounded-xl border border-cyan-500/20 w-full text-left max-h-24 overflow-y-auto"></div>
                <span class="bg-purple-600 text-white text-[10px] font-black px-6 py-2 rounded-full uppercase tracking-widest group-hover:bg-purple-400 transition">摇一摇</span>
            </div>

            <!-- 用户收藏夹 -->
            <div class="rounded-3xl bg-zinc-900/40 border border-white/5 p-8 flex flex-col justify-center">
                <div class="flex items-center gap-3 mb-4">
                    <span class="bg-red-500 w-2 h-2 rounded-full animate-ping"></span>
                    <h3 class="text-white font-black text-xs uppercase tracking-[0.2em]">我的收藏夹</h3>
                </div>
                
                <div id="favoritesList" class="space-y-2 mb-4 max-h-32 overflow-y-auto">
                    <p class="text-zinc-500 text-sm">还没有收藏任何图片</p>
                </div>
                
                <div class="flex gap-4">
                    <button onclick="clearFavorites()" class="text-[10px] font-black text-zinc-500 uppercase tracking-widest hover:text-white transition">清空收藏</button>
                    <button onclick="exportFavorites()" class="text-[10px] font-black text-zinc-500 uppercase tracking-widest hover:text-white transition">导出列表</button>
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
            if (window.userProgress) {{
                userProgress.addPromptGeneration();
                updateUserStats();
            }}
            
            notice.style.opacity = '1';
            setTimeout(() => notice.style.opacity = '0', 2000);
        }}
        
        // 随机生成 Prompt
        function generateRandomPrompt() {{
            const prompts = {json.dumps([generate_random_prompt() for _ in range(10)])};
            const randomPrompt = prompts[Math.floor(Math.random() * prompts.length)];
            
            document.getElementById('promptInput').value = randomPrompt;
            if (window.userProgress) {{
                userProgress.addPromptGeneration();
                updateUserStats();
            }}
            showNotification('🎲 随机提示词', '已生成新的创意提示词！');
        }}
        
        // 复制分辨率
        function copyRes(val) {{
            const el = document.createElement('textarea');
            el.value = val;
            document.body.appendChild(el);
            el.select();
            document.execCommand('copy');
            document.body.removeChild(el);
            showNotification('📋 已复制', `分辨率 ${{val}} 已复制到剪贴板`);
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
            showNotification('🎯 挑战已接受', '种子和提示词已复制！');
        }}
        
        function shareChallenge() {{
            const challengeUrl = window.location.href + '#challenge';
            if (navigator.share) {{
                navigator.share({{
                    title: '今日 Flux 挑战',
                    text: '来参加今天的 AI 图像生成挑战吧！',
                    url: challengeUrl
                }});
            }} else {{
                const el = document.createElement('textarea');
                el.value = challengeUrl;
                document.body.appendChild(el);
                el.select();
                document.execCommand('copy');
                document.body.removeChild(el);
                showNotification('🔗 链接已复制', '分享链接已复制到剪贴板');
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
            
            if (window.userProgress) {{
                userProgress.addPromptGeneration();
                updateUserStats();
            }}
            showNotification('🎁 盲盒开启', '神秘提示词已复制！');
        }}
        
        // 收藏功能
        function toggleFavorite(imageName) {{
            if (!window.userProgress) return;
            
            const favorites = userProgress.data.favoriteImages || [];
            const index = favorites.indexOf(imageName);
            
            if (index > -1) {{
                favorites.splice(index, 1);
                showNotification('💔 取消收藏', '已从收藏夹移除');
            }} else {{
                favorites.push(imageName);
                showNotification('❤️ 添加收藏', '已添加到收藏夹');
            }}
            
            userProgress.data.favoriteImages = favorites;
            userProgress.save();
            updateFavoritesList();
            updateFavoriteButtons();
        }}
        
        function updateFavoritesList() {{
            const favoritesList = document.getElementById('favoritesList');
            if (!favoritesList || !window.userProgress) return;
            
            const favorites = userProgress.data.favoriteImages || [];
            
            if (favorites.length === 0) {{
                favoritesList.innerHTML = '<p class="text-zinc-500 text-sm">还没有收藏任何图片</p>';
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
            if (!window.userProgress) return;
            
            const favorites = userProgress.data.favoriteImages || [];
            document.querySelectorAll('[data-favorite-btn]').forEach(btn => {{
                const imageName = btn.getAttribute('data-image');
                const isFavorited = favorites.includes(imageName);
                btn.innerHTML = isFavorited ? '💖' : '🤍';
                btn.title = isFavorited ? '取消收藏' : '添加收藏';
            }});
        }}
        
        function clearFavorites() {{
            if (!window.userProgress) return;
            
            if (confirm('确定要清空所有收藏吗？')) {{
                userProgress.data.favoriteImages = [];
                userProgress.save();
                updateFavoritesList();
                updateFavoriteButtons();
                showNotification('🗑️ 已清空', '收藏夹已清空');
            }}
        }}
        
        function exportFavorites() {{
            if (!window.userProgress) return;
            
            const favorites = userProgress.data.favoriteImages || [];
            if (favorites.length === 0) {{
                showNotification('📝 导出失败', '收藏夹为空');
                return;
            }}
            
            const exportData = favorites.join('\\n');
            const el = document.createElement('textarea');
            el.value = exportData;
            document.body.appendChild(el);
            el.select();
            document.execCommand('copy');
            document.body.removeChild(el);
            showNotification('📋 导出成功', '收藏列表已复制到剪贴板');
        }}
        
        // 成就系统
        function updateAchievementsList() {{
            const achievementsList = document.getElementById('achievementsList');
            if (!achievementsList || !window.userProgress) return;
            
            const achievements = userProgress.data.achievements || [];
            
            const allAchievements = [
                {{ id: 'first_visit', name: '初次访问', desc: '欢迎来到 FreeFineAI！', icon: '👋' }},
                {{ id: 'regular_visitor', name: '常客', desc: '访问网站 5 次', icon: '🏠' }},
                {{ id: 'download_master', name: '下载达人', desc: '下载 10 张图片', icon: '📥' }},
                {{ id: 'prompt_creator', name: 'Prompt 创作者', desc: '生成 20 个提示词', icon: '✨' }},
                {{ id: 'streak_week', name: '连续一周', desc: '连续访问 7 天', icon: '🔥' }}
            ];
            
            const recentAchievements = allAchievements
                .filter(a => achievements.includes(a.id))
                .slice(-3);
            
            if (recentAchievements.length === 0) {{
                achievementsList.innerHTML = '<p class="text-zinc-500 text-xs">完成任务解锁成就</p>';
            }} else {{
                achievementsList.innerHTML = recentAchievements.map(achievement => 
                    `<div class="flex items-center gap-2 bg-black/20 p-2 rounded-lg">
                        <span class="text-sm">${{achievement.icon}}</span>
                        <div>
                            <div class="text-white text-xs font-bold">${{achievement.name}}</div>
                            <div class="text-zinc-400 text-[10px]">${{achievement.desc}}</div>
                        </div>
                    </div>`
                ).join('');
            }}
        }}
        
        function showAllAchievements() {{
            showNotification('🏆 成就系统', '更多成就功能即将推出！');
        }}
        
        // 下载追踪
        function trackDownload(imageName) {{
            if (window.userProgress) {{
                userProgress.addDownload();
                updateUserStats();
            }}
            showNotification('📥 下载成功', '感谢支持 FreeFineAI！');
        }}
        
        // 页面加载完成后初始化
        document.addEventListener('DOMContentLoaded', function() {{
            if (window.userProgress) {{
                updateUserStats();
                updateFavoritesList();
                updateFavoriteButtons();
                updateAchievementsList();
            }}
        }});
    </script>
    '''

# === 5. 生成主页面 ===
def generate():
    setup()
    print_config_info()
    
    with open(os.path.join(CONFIG["TEMPLATE_DIR"], "head.html"), "r", encoding="utf-8") as f: 
        head = f.read()

    images = sorted([f for f in os.listdir(CONFIG["IMG_DIR"]) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))], reverse=True)
    
    # 生成图片卡片（增强版）
    cards_html = ""
    for img in images:
        name = img.split('.')[0].replace('_', ' ').title()
        cards_html += f'''
        <div class="break-inside-avoid mb-6 relative group rounded-3xl overflow-hidden bg-zinc-900 border border-white/5 shadow-2xl transition-all duration-500 hover:border-cyan-500/50">
            <img src="images/{img}" alt="{name}" loading="lazy" class="w-full h-auto transition-transform duration-700 group-hover:scale-105">
            <div class="absolute inset-0 bg-gradient-to-t from-black via-black/60 to-transparent opacity-0 group-hover:opacity-100 transition-all duration-300 p-4 flex flex-col justify-end">
                <h3 class="text-white font-bold text-sm mb-3">{name}</h3>
                <div class="flex gap-2 text-center">
                    <a href="images/{img}" download onclick="trackDownload('{img}')" class="flex-1 bg-white text-black text-[10px] font-black py-2 rounded-xl uppercase">Download</a>
                    <button onclick="toggleFavorite('{img}')" data-favorite-btn data-image="{img}" class="bg-zinc-800 text-white px-3 py-2 rounded-xl hover:bg-pink-600 transition-all" title="添加收藏">🤍</button>
                    <a href="{CONFIG["TIP_JAR_URL"]}" target="_blank" class="bg-zinc-800 text-white px-3 py-2 rounded-xl hover:bg-blue-600 transition-all">❤</a>
                </div>
            </div>
        </div>
        '''

    # 组合页面内容
    body_content = f'''
    <header class="pt-32 pb-16 px-6 text-center">
        <div class="inline-block px-4 py-1 mb-4 border border-cyan-500/20 rounded-full bg-cyan-500/5 text-cyan-400 text-[10px] font-bold uppercase tracking-widest">Flux.1 Master Library</div>
        <h1 class="text-6xl md:text-8xl font-black mb-6 leading-none hero-title text-white">FLUX RAW.</h1>
        <p class="max-w-2xl mx-auto text-zinc-500 text-base font-light leading-relaxed mb-8">
            {CONFIG["SITE_DESCRIPTION"]}
        </p>
    </header>

    {generate_enhanced_tools() if CONFIG["ENABLE_DAILY_CHALLENGE"] else ""}

    <main class="max-w-[1400px] mx-auto px-6 pb-32">
        <div class="flex flex-col md:flex-row justify-between items-end mb-8 gap-4">
            <h2 class="text-white text-2xl font-black tracking-tighter uppercase italic">最新作品</h2>
            <p class="text-[10px] text-zinc-600 font-bold uppercase tracking-[0.3em]">筛选: Flux.1-Dev</p>
        </div>
        <div class="masonry">{cards_html}</div>
        
        <section class="mt-32 p-8 md:p-16 rounded-[3rem] bg-gradient-to-br from-zinc-900/80 via-zinc-900/40 to-transparent border border-white/5 relative overflow-hidden">
            <div class="absolute -top-20 -right-20 w-80 h-80 bg-primary/10 blur-[100px] rounded-full"></div>
            
            <div class="relative z-10 max-w-3xl">
                <h2 class="text-3xl md:text-5xl font-black text-white mb-6 tracking-tighter leading-none">
                    突破 Flux.1 的<br><span class="primary-color">边界</span>
                </h2>
                
                <div class="grid md:grid-cols-2 gap-6 text-left mb-8">
                    <div>
                        <p class="text-zinc-400 text-sm leading-relaxed">
                            <span class="text-white font-bold block mb-1">标准访问</span>
                            享受我们精选的画廊，提供高质量的网络就绪资源。非常适合社交媒体、概念设计和日常灵感。永远免费，永远新鲜。
                        </p>
                    </div>
                    <div>
                        <p class="text-zinc-400 text-sm leading-relaxed">
                            <span class="text-white font-bold block mb-1">专业宝库</span>
                            为需要每个像素的人准备。解锁 4K 无损渲染、完整提示词元数据 (JSON) 和完全商业使用权。
                        </p>
                    </div>
                </div>

                <div class="flex flex-col sm:flex-row gap-4 items-center">
                    <a href="{CONFIG['MEGA_BUNDLE_URL']}" target="_blank" class="w-full sm:w-auto bg-white text-black font-black px-8 py-4 rounded-2xl hover:bg-primary transition-all transform hover:scale-105 uppercase tracking-widest text-xs shadow-2xl">
                        解锁专业宝库 — {CONFIG["BUNDLE_PRICE"]}
                    </a>
                    <div class="text-[10px] text-zinc-600 uppercase tracking-[0.2em] font-bold">
                        一次支持 • 终身更新
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer class="mt-32 border-t border-white/5 bg-zinc-950/50 py-16 px-8 relative overflow-hidden">
        <div class="absolute bottom-0 left-0 w-full h-1 bg-gradient-to-r from-transparent via-primary/20 to-transparent"></div>
        <div class="max-w-[1400px] mx-auto grid grid-cols-1 md:grid-cols-4 gap-8 text-left mb-12">
            <div class="md:col-span-1">
                <span class="text-white font-black text-2xl tracking-tighter italic uppercase block mb-3">FREEFINE<span class="primary-color">AI</span></span>
                <p class="text-zinc-500 text-xs leading-relaxed max-w-xs">Flux.1-dev 资源的独立档案。为社区而建。</p>
            </div>
            <div>
                <h4 class="text-white text-[10px] font-black uppercase tracking-[0.2em] mb-4">导航</h4>
                <ul class="space-y-3 text-xs font-bold">
                    <li><a href="#" class="text-zinc-600 hover:text-primary transition uppercase tracking-widest">画廊</a></li>
                    <li><a href="{CONFIG['MEGA_BUNDLE_URL']}" class="text-zinc-600 hover:text-primary transition uppercase tracking-widest">专业宝库</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-white text-[10px] font-black uppercase tracking-[0.2em] mb-4">法律</h4>
                <p class="text-[10px] text-zinc-600 font-bold uppercase">CC BY-NC 4.0 许可证</p>
            </div>
            <div>
                <h4 class="text-white text-[10px] font-black uppercase tracking-[0.2em] mb-4">状态</h4>
                <div class="flex items-center gap-2"><div class="w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse"></div><span class="text-[9px] text-zinc-400 uppercase font-bold">运行中</span></div>
            </div>
        </div>
        <div class="max-w-[1400px] mx-auto flex flex-col md:flex-row justify-between items-center pt-8 border-t border-white/5 gap-4">
            <p class="text-[10px] tracking-[0.5em] text-zinc-800 uppercase italic font-black">&copy; 2026 FREEFINEAI</p>
            <div class="flex gap-6">
                <a href="{CONFIG['TWITTER_URL']}" class="text-zinc-800 hover:text-white text-[9px] font-black uppercase transition">Twitter</a>
                <a href="{CONFIG['GITHUB_URL']}" class="text-zinc-800 hover:text-white text-[9px] font-black uppercase transition">GitHub</a>
            </div>
        </div>
    </footer>
    
    {generate_enhanced_scripts()}
</body>
</html>
'''

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(head + body_content)
    
    print(f"🚀 优化版网站生成成功！")
    print(f"📊 包含 {len(images)} 张图片")
    print(f"✨ 间距优化: 模块间距更紧凑，视觉更协调")
    print(f"🎨 界面改进: 圆角统一为3xl，内边距优化")
    print(f"💰 变现功能: 用户粘性提升、打赏引导优化")

if __name__ == "__main__":
    generate()