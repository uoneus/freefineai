import os
import json
import random
import configparser
from datetime import datetime

class ConfigManager:
    """Configuration file manager"""
    def __init__(self, config_file="settings.config"):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.load_config()
    
    def load_config(self):
        """Load configuration file"""
        if os.path.exists(self.config_file):
            self.config.read(self.config_file, encoding='utf-8')
        else:
            self.create_default_config()
    
    def create_default_config(self):
        """Create default configuration file"""
        default_config = """# FreeFineAI Website Configuration File
# Modify this file to customize your website

[BASIC]
DOMAIN = FreeFineAI.com
SITE_TITLE = FreeFineAI | Premium Flux.1 Digital Assets
SITE_DESCRIPTION = Curated, high-fidelity AI assets. Free for the community, designed for the visionaries.

[PAYMENT]
TIP_JAR_URL = https://www.paypal.com/ncp/payment/ZRQDBKWE7VBSU
MEGA_BUNDLE_URL = https://www.paypal.com/ncp/payment/AQSGVVXLW69GJ
BUNDLE_PRICE = $9.99
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
ENABLE_MULTI_PAGE = true

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
LANGUAGE = en-US

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
        """Get configuration value"""
        try:
            return self.config.get(section, key)
        except:
            return fallback
    
    def getboolean(self, section, key, fallback=False):
        """Get boolean configuration value"""
        try:
            return self.config.getboolean(section, key)
        except:
            return fallback
    
    def getint(self, section, key, fallback=0):
        """Get integer configuration value"""
        try:
            return self.config.getint(section, key)
        except:
            return fallback

# Initialize configuration manager
config = ConfigManager()

# Read settings from configuration file
CONFIG = {
    "DOMAIN": config.get("BASIC", "DOMAIN", "FreeFineAI.com"),
    "SITE_TITLE": config.get("BASIC", "SITE_TITLE", "FreeFineAI | Premium Flux.1 Digital Assets"),
    "SITE_DESCRIPTION": config.get("BASIC", "SITE_DESCRIPTION", "Curated, high-fidelity AI assets"),
    "TIP_JAR_URL": config.get("PAYMENT", "TIP_JAR_URL", "https://www.paypal.com/ncp/payment/ZRQDBKWE7VBSU"),
    "MEGA_BUNDLE_URL": config.get("PAYMENT", "MEGA_BUNDLE_URL", "https://www.paypal.com/ncp/payment/AQSGVVXLW69GJ"),
    "BUNDLE_PRICE": config.get("PAYMENT", "BUNDLE_PRICE", "$9.99"),
    "COFFEE_URL": config.get("PAYMENT", "COFFEE_URL", "https://www.freefineai.com"),
    "IMG_DIR": config.get("DIRECTORIES", "IMG_DIR", "images"),
    "TEMPLATE_DIR": config.get("DIRECTORIES", "TEMPLATE_DIR", "templates"),
    "DATA_DIR": config.get("DIRECTORIES", "DATA_DIR", "data"),
    
    # Feature toggles
    "ENABLE_ACHIEVEMENTS": config.getboolean("FEATURES", "ENABLE_ACHIEVEMENTS", True),
    "ENABLE_DAILY_CHALLENGE": config.getboolean("FEATURES", "ENABLE_DAILY_CHALLENGE", True),
    "ENABLE_FAVORITES": config.getboolean("FEATURES", "ENABLE_FAVORITES", True),
    "ENABLE_USER_STATS": config.getboolean("FEATURES", "ENABLE_USER_STATS", True),
    "ENABLE_NOTIFICATIONS": config.getboolean("FEATURES", "ENABLE_NOTIFICATIONS", True),
    "ENABLE_PWA": config.getboolean("FEATURES", "ENABLE_PWA", False),
    "ENABLE_MULTI_PAGE": config.getboolean("FEATURES", "ENABLE_MULTI_PAGE", True),
    
    # Social links
    "TWITTER_URL": config.get("SOCIAL", "TWITTER_URL", "#"),
    "GITHUB_URL": config.get("SOCIAL", "GITHUB_URL", "#"),
    "DISCORD_URL": config.get("SOCIAL", "DISCORD_URL", "#"),
    
    # Analytics
    "GOOGLE_ANALYTICS_ID": config.get("ANALYTICS", "GOOGLE_ANALYTICS_ID", ""),
    "ENABLE_TRACKING": config.getboolean("ANALYTICS", "ENABLE_TRACKING", False),
    
    # Customization
    "PRIMARY_COLOR": config.get("CUSTOMIZATION", "PRIMARY_COLOR", "cyan"),
    "ACCENT_COLOR": config.get("CUSTOMIZATION", "ACCENT_COLOR", "purple"),
    "THEME": config.get("CUSTOMIZATION", "THEME", "dark"),
    "LANGUAGE": config.get("CUSTOMIZATION", "LANGUAGE", "en-US"),
    
    # Content
    "MAX_IMAGES_PER_PAGE": config.getint("CONTENT", "MAX_IMAGES_PER_PAGE", 50),
    "ENABLE_LAZY_LOADING": config.getboolean("CONTENT", "ENABLE_LAZY_LOADING", True),
    "IMAGE_QUALITY": config.get("CONTENT", "IMAGE_QUALITY", "high"),
    "ENABLE_WATERMARK": config.getboolean("CONTENT", "ENABLE_WATERMARK", False),
    
    # Advanced
    "ENABLE_SERVICE_WORKER": config.getboolean("ADVANCED", "ENABLE_SERVICE_WORKER", False),
    "CACHE_DURATION": config.getint("ADVANCED", "CACHE_DURATION", 7),
    "DEBUG_MODE": config.getboolean("ADVANCED", "DEBUG_MODE", False)
}

# User engagement feature data
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
    """Print configuration information"""
    print("📋 Current Configuration:")
    print(f"   Site Title: {CONFIG['SITE_TITLE']}")
    print(f"   Domain: {CONFIG['DOMAIN']}")
    print(f"   Bundle Price: {CONFIG['BUNDLE_PRICE']}")
    print(f"   Primary Color: {CONFIG['PRIMARY_COLOR']}")
    print(f"   Language: {CONFIG['LANGUAGE']}")
    print(f"   Achievement System: {'✅' if CONFIG['ENABLE_ACHIEVEMENTS'] else '❌'}")
    print(f"   Daily Challenge: {'✅' if CONFIG['ENABLE_DAILY_CHALLENGE'] else '❌'}")
    print(f"   Favorites Feature: {'✅' if CONFIG['ENABLE_FAVORITES'] else '❌'}")
    print(f"   Multi-page: {'✅' if CONFIG['ENABLE_MULTI_PAGE'] else '❌'}")
    print(f"   PWA Support: {'✅' if CONFIG['ENABLE_PWA'] else '❌'}")
    print(f"   Debug Mode: {'✅' if CONFIG['DEBUG_MODE'] else '❌'}")

def setup():
    for folder in [CONFIG["IMG_DIR"], CONFIG["TEMPLATE_DIR"], CONFIG["DATA_DIR"]]:
        if not os.path.exists(folder):
            os.makedirs(folder)
    
    init_user_data()
    generate_head_template()

def init_user_data():
    """Initialize user data file"""
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
    """Get today's challenge"""
    today = datetime.now().day
    return DAILY_CHALLENGES[today % len(DAILY_CHALLENGES)]

def generate_random_prompt():
    """Generate random prompt"""
    template = random.choice(PROMPT_TEMPLATES)
    variables = {}
    
    import re
    vars_in_template = re.findall(r'\{(\w+)\}', template)
    
    for var in vars_in_template:
        if var in PROMPT_VARIABLES:
            variables[var] = random.choice(PROMPT_VARIABLES[var])
    
    result = template
    for var, value in variables.items():
        result = result.replace(f'{{{var}}}', value)
    
    return result

def generate_head_template():
    """Generate Head template"""
    primary_color = CONFIG["PRIMARY_COLOR"]
    accent_color = CONFIG["ACCENT_COLOR"]
    
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
    
    pwa_code = ""
    if CONFIG["ENABLE_PWA"]:
        pwa_code = '''
    <link rel="manifest" href="manifest.json">
    <meta name="theme-color" content="#050505">
    <link rel="apple-touch-icon" href="icon-192.png">
    '''
    
    # Navigation menu
    nav_menu = ""
    if CONFIG["ENABLE_MULTI_PAGE"]:
        nav_menu = '''
            <div class="hidden md:flex items-center gap-6 text-xs font-bold uppercase tracking-widest">
                <a href="index.html" class="text-zinc-400 hover:text-white transition">Home</a>
                <a href="gallery.html" class="text-zinc-400 hover:text-white transition">Gallery</a>
                <a href="tools.html" class="text-zinc-400 hover:text-white transition">Tools</a>
                <a href="about.html" class="text-zinc-400 hover:text-white transition">About</a>
            </div>
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
    
    {generate_notification_html() if CONFIG["ENABLE_NOTIFICATIONS"] else ""}
    
    <script>
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
            {nav_menu}
            {generate_user_stats_html() if CONFIG["ENABLE_USER_STATS"] else ""}
            <a href="{CONFIG["TIP_JAR_URL"]}" target="_blank" class="hidden sm:block text-[10px] font-bold text-zinc-500 hover:text-white uppercase tracking-widest">Support</a>
            <a href="{CONFIG["MEGA_BUNDLE_URL"]}" target="_blank" class="bg-white text-black text-[10px] font-black px-6 py-2 rounded-full uppercase tracking-tighter hover:bg-primary transition">Get Bundle {CONFIG["BUNDLE_PRICE"]}</a>
        </div>
    </nav>
'''
    
    with open(os.path.join(CONFIG["TEMPLATE_DIR"], "head.html"), "w", encoding="utf-8") as f: 
        f.write(head_content)

def generate_notification_html():
    """Generate notification HTML"""
    return '''<div id="notification" class="notification bg-gradient-to-r from-primary to-accent text-white p-4 rounded-2xl shadow-2xl max-w-sm">
        <div class="flex items-center gap-3">
            <div class="w-8 h-8 bg-white/20 rounded-full flex items-center justify-center">
                <span class="text-sm">🎉</span>
            </div>
            <div>
                <div class="font-bold text-sm" id="notificationTitle">Congratulations!</div>
                <div class="text-xs opacity-90" id="notificationText">You earned a new achievement</div>
            </div>
        </div>
    </div>'''

def generate_user_stats_html():
    """Generate user stats HTML"""
    return '''<div class="hidden md:flex items-center gap-4 text-xs">
                <div class="flex items-center gap-1">
                    <span class="primary-color">📊</span>
                    <span class="text-zinc-400" id="userStats">Visits: 0 | Downloads: 0</span>
                </div>
                <div class="flex items-center gap-1 streak-badge" id="streakBadge" style="display: none;">
                    <span class="text-yellow-400">🔥</span>
                    <span class="text-yellow-400" id="streakCount">0</span>
                </div>
            </div>'''

def generate_user_progress_js():
    """Generate user progress JavaScript"""
    return '''
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
                    console.log('User data saved:', this.data);
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
                    { id: 'first_visit', name: 'First Visit', desc: 'Welcome to FreeFineAI!', condition: () => this.data.visits >= 1 },
                    { id: 'regular_visitor', name: 'Regular Visitor', desc: 'Visit the site 5 times', condition: () => this.data.visits >= 5 },
                    { id: 'download_master', name: 'Download Master', desc: 'Download 10 images', condition: () => this.data.downloads >= 10 },
                    { id: 'prompt_creator', name: 'Prompt Creator', desc: 'Generate 20 prompts', condition: () => this.data.promptsGenerated >= 20 },
                    { id: 'streak_week', name: 'Week Streak', desc: 'Visit for 7 consecutive days', condition: () => this.data.streak >= 7 }
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
        
        const userProgress = new UserProgress();
        userProgress.addVisit();
        
        function showNotification(title, text) {
            if (window.userProgress) {
                userProgress.showNotification(title, text);
            }
        }
        
        function updateUserStats() {
            const stats = document.getElementById('userStats');
            const streakBadge = document.getElementById('streakBadge');
            const streakCount = document.getElementById('streakCount');
            
            if (stats) {
                stats.textContent = `Visits: ${userProgress.data.visits} | Downloads: ${userProgress.data.downloads}`;
            }
            
            if (userProgress.data.streak > 0 && streakBadge && streakCount) {
                streakBadge.style.display = 'flex';
                streakCount.textContent = userProgress.data.streak;
            }
        }
        
        document.addEventListener('DOMContentLoaded', updateUserStats);
    '''

# Generate enhanced feature components
def generate_enhanced_tools():
    """Generate enhanced toolbox"""
    daily_challenge = get_daily_challenge()
    
    return f'''
    <!-- Daily Challenge Banner -->
    <section class="max-w-[1400px] mx-auto px-8 mb-8">
        <div class="bg-gradient-to-r from-purple-900/40 via-blue-900/40 to-cyan-900/40 border border-purple-500/20 rounded-3xl p-6 relative overflow-hidden">
            <div class="absolute top-0 right-0 p-4">
                <div class="bg-red-500 w-2 h-2 rounded-full animate-ping"></div>
            </div>
            <div class="flex flex-col md:flex-row items-center justify-between gap-4">
                <div>
                    <h3 class="text-white font-black text-base mb-1">🎯 Daily Challenge #{daily_challenge['seed']}</h3>
                    <p class="text-zinc-300 text-sm mb-1">"{daily_challenge['prompt']}"</p>
                    <span class="text-xs text-purple-400 font-bold">Difficulty: {daily_challenge['difficulty']}</span>
                </div>
                <div class="flex gap-2">
                    <button onclick="copyChallenge('{daily_challenge['seed']}', '{daily_challenge['prompt']}')" class="bg-purple-600 hover:bg-purple-500 text-white text-xs font-black px-4 py-2 rounded-xl uppercase tracking-widest transition">
                        Accept Challenge
                    </button>
                    <button onclick="shareChallenge()" class="bg-zinc-800 hover:bg-zinc-700 text-white px-3 py-2 rounded-xl transition">
                        📤
                    </button>
                </div>
            </div>
        </div>
    </section>

    <!-- Enhanced Toolbox -->
    <section class="max-w-[1400px] mx-auto px-8 mb-12">
        <div class="grid md:grid-cols-3 gap-6">
            <!-- AI Prompt Generator -->
            <div class="bg-zinc-900/50 border border-white/5 p-6 rounded-3xl backdrop-blur-md relative overflow-hidden group">
                <div class="flex items-center gap-3 mb-4">
                    <div class="p-2 bg-cyan-500/10 rounded-lg text-cyan-400">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                    </div>
                    <h3 class="text-white font-black text-xs uppercase tracking-[0.2em]">AI Prompt Generator</h3>
                </div>
                <textarea id="promptInput" placeholder="Enter a simple concept (e.g. 'Cyberpunk City')..." class="w-full bg-black/40 border border-white/5 rounded-xl p-3 text-sm text-zinc-300 h-20 mb-3 outline-none focus:border-cyan-500/50 transition resize-none"></textarea>
                
                <div class="mb-3">
                    <select id="styleSelect" class="w-full bg-black/40 border border-white/5 rounded-xl p-2 text-xs text-zinc-300 outline-none focus:border-cyan-500/50">
                        <option value="">Choose Style</option>
                        {generate_style_options()}
                    </select>
                </div>
                
                <div class="flex gap-2">
                    <button onclick="expandPrompt()" class="flex-1 bg-zinc-800 hover:bg-white hover:text-black text-white text-[10px] font-black py-3 rounded-xl uppercase tracking-widest transition shadow-lg">
                        Enhance Prompt
                    </button>
                    <button onclick="generateRandomPrompt()" class="bg-purple-600 hover:bg-purple-500 text-white px-3 py-3 rounded-xl transition">
                        🎲
                    </button>
                </div>
                
                <div id="copyNotice" class="absolute top-3 right-6 text-[9px] text-cyan-500 font-bold opacity-0 transition-opacity uppercase tracking-widest">Copied!</div>
            </div>

            <!-- Resolution Presets -->
            <div class="bg-zinc-900/50 border border-white/5 p-6 rounded-3xl backdrop-blur-md">
                <div class="flex items-center gap-3 mb-4">
                    <div class="p-2 bg-purple-500/10 rounded-lg text-purple-400">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4"/></svg>
                    </div>
                    <h3 class="text-white font-black text-xs uppercase tracking-[0.2em]">Resolution Presets</h3>
                </div>
                <div class="grid grid-cols-1 gap-2">
                    <button onclick="copyRes('1344 x 768')" class="bg-black/40 border border-white/5 p-3 rounded-xl hover:border-cyan-500/50 group transition text-left">
                        <span class="block text-white font-bold text-xs">16:9 Cinematic</span>
                        <span class="text-[10px] text-zinc-600">1344 x 768 px</span>
                    </button>
                    <button onclick="copyRes('768 x 1344')" class="bg-black/40 border border-white/5 p-3 rounded-xl hover:border-cyan-500/50 group transition text-left">
                        <span class="block text-white font-bold text-xs">9:16 Portrait</span>
                        <span class="text-[10px] text-zinc-600">768 x 1344 px</span>
                    </button>
                    <button onclick="copyRes('1024 x 1024')" class="bg-black/40 border border-white/5 p-3 rounded-xl hover:border-cyan-500/50 group transition text-left">
                        <span class="block text-white font-bold text-xs">1:1 Square</span>
                        <span class="text-[10px] text-zinc-600">1024 x 1024 px</span>
                    </button>
                </div>
            </div>

            <!-- User Achievement Panel -->
            <div class="bg-zinc-900/50 border border-white/5 p-6 rounded-3xl backdrop-blur-md">
                <div class="flex items-center gap-3 mb-4">
                    <div class="p-2 bg-yellow-500/10 rounded-lg text-yellow-400">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>
                    </div>
                    <h3 class="text-white font-black text-xs uppercase tracking-[0.2em]">My Achievements</h3>
                </div>
                
                <div id="achievementsList" class="space-y-2 mb-3 max-h-32 overflow-y-auto">
                    <!-- Achievements will be loaded dynamically via JavaScript -->
                </div>
                
                <div class="text-center">
                    <button onclick="showAllAchievements()" class="text-[10px] text-zinc-500 hover:text-white font-bold uppercase tracking-widest transition">
                        View All
                    </button>
                </div>
            </div>
        </div>
    </section>

    <!-- Community Interaction Area -->
    <section class="max-w-[1400px] mx-auto px-8 mb-16">
        <div class="grid md:grid-cols-2 gap-6">
            <!-- Prompt Blind Box -->
            <div class="relative group cursor-pointer overflow-hidden rounded-3xl bg-gradient-to-br from-purple-900/40 to-black border border-white/5 p-8 flex flex-col items-center justify-center text-center transition-all hover:border-purple-500/40" onclick="getBlindBox()">
                <div class="absolute top-0 right-0 p-3 opacity-20 group-hover:opacity-100 transition-opacity">
                    <svg class="w-16 h-16 text-purple-500" fill="currentColor" viewBox="0 0 24 24"><path d="M11 15h2v2h-2v-2m0-8h2v6h-2V7m1-5C6.47 2 2 6.47 2 12s4.47 10 10 10 10-4.47 10-10S17.53 2 12 2m0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"/></svg>
                </div>
                <h3 class="text-white text-xl font-black italic uppercase tracking-tighter mb-2">Prompt Blind Box</h3>
                <p class="text-zinc-500 text-xs mb-4 font-bold uppercase tracking-widest">Randomly generate masterpiece seeds</p>
                <div id="blindBoxResult" class="hidden text-cyan-400 text-[10px] font-mono mb-4 bg-black/60 p-3 rounded-xl border border-cyan-500/20 w-full text-left max-h-24 overflow-y-auto"></div>
                <span class="bg-purple-600 text-white text-[10px] font-black px-6 py-2 rounded-full uppercase tracking-widest group-hover:bg-purple-400 transition">Roll the Dice</span>
            </div>

            <!-- User Favorites -->
            <div class="rounded-3xl bg-zinc-900/40 border border-white/5 p-8 flex flex-col justify-center">
                <div class="flex items-center gap-3 mb-4">
                    <span class="bg-red-500 w-2 h-2 rounded-full animate-ping"></span>
                    <h3 class="text-white font-black text-xs uppercase tracking-[0.2em]">My Favorites</h3>
                </div>
                
                <div id="favoritesList" class="space-y-2 mb-4 max-h-32 overflow-y-auto">
                    <p class="text-zinc-500 text-sm">No favorite images yet</p>
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
    """Generate style options"""
    options = ""
    for style_name in STYLE_PRESETS.keys():
        options += f'<option value="{style_name}">{style_name}</option>'
    return options

def generate_enhanced_scripts():
    """Generate enhanced JavaScript"""
    return f'''
    <script>
        function expandPrompt() {{
            const input = document.getElementById('promptInput');
            const styleSelect = document.getElementById('styleSelect');
            const notice = document.getElementById('copyNotice');
            
            if(!input.value) return;
            
            let enhancements = ", hyper-realistic, highly detailed textures, cinematic lighting, shot on 35mm lens, f/1.8, 8k resolution, masterwork, intricate details, flux style";
            
            const selectedStyle = styleSelect.value;
            if (selectedStyle) {{
                const styleEnhancements = {json.dumps(STYLE_PRESETS)};
                enhancements += styleEnhancements[selectedStyle] || "";
            }}
            
            input.value = input.value + enhancements;
            input.select();
            document.execCommand('copy');
            
            if (window.userProgress) {{
                userProgress.addPromptGeneration();
                updateUserStats();
            }}
            
            notice.style.opacity = '1';
            setTimeout(() => notice.style.opacity = '0', 2000);
        }}
        
        function generateRandomPrompt() {{
            const prompts = {json.dumps([generate_random_prompt() for _ in range(10)])};
            const randomPrompt = prompts[Math.floor(Math.random() * prompts.length)];
            
            document.getElementById('promptInput').value = randomPrompt;
            if (window.userProgress) {{
                userProgress.addPromptGeneration();
                updateUserStats();
            }}
            showNotification('🎲 Random Prompt', 'New creative prompt generated!');
        }}
        
        function copyRes(val) {{
            const el = document.createElement('textarea');
            el.value = val;
            document.body.appendChild(el);
            el.select();
            document.execCommand('copy');
            document.body.removeChild(el);
            showNotification('📋 Copied', `Resolution ${{val}} copied to clipboard`);
        }}
        
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
        
        function getBlindBox() {{
            const prompts = {json.dumps([generate_random_prompt() for _ in range(20)])};
            const random = prompts[Math.floor(Math.random() * prompts.length)];
            const display = document.getElementById('blindBoxResult');
            
            display.innerText = random;
            display.classList.remove('hidden');
            
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
            showNotification('🎁 Blind Box Opened', 'Mystery prompt copied!');
        }}
        
        function toggleFavorite(imageName) {{
            if (!window.userProgress) return;
            
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
            if (!favoritesList || !window.userProgress) return;
            
            const favorites = userProgress.data.favoriteImages || [];
            
            if (favorites.length === 0) {{
                favoritesList.innerHTML = '<p class="text-zinc-500 text-sm">No favorite images yet</p>';
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
                btn.title = isFavorited ? 'Remove from favorites' : 'Add to favorites';
            }});
        }}
        
        function clearFavorites() {{
            if (!window.userProgress) return;
            
            if (confirm('Are you sure you want to clear all favorites?')) {{
                userProgress.data.favoriteImages = [];
                userProgress.save();
                updateFavoritesList();
                updateFavoriteButtons();
                showNotification('🗑️ Cleared', 'Favorites cleared');
            }}
        }}
        
        function exportFavorites() {{
            if (!window.userProgress) return;
            
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
        
        function updateAchievementsList() {{
            const achievementsList = document.getElementById('achievementsList');
            if (!achievementsList || !window.userProgress) return;
            
            const achievements = userProgress.data.achievements || [];
            
            const allAchievements = [
                {{ id: 'first_visit', name: 'First Visit', desc: 'Welcome to FreeFineAI!', icon: '👋' }},
                {{ id: 'regular_visitor', name: 'Regular Visitor', desc: 'Visit the site 5 times', icon: '🏠' }},
                {{ id: 'download_master', name: 'Download Master', desc: 'Download 10 images', icon: '📥' }},
                {{ id: 'prompt_creator', name: 'Prompt Creator', desc: 'Generate 20 prompts', icon: '✨' }},
                {{ id: 'streak_week', name: 'Week Streak', desc: 'Visit for 7 consecutive days', icon: '🔥' }}
            ];
            
            const recentAchievements = allAchievements
                .filter(a => achievements.includes(a.id))
                .slice(-3);
            
            if (recentAchievements.length === 0) {{
                achievementsList.innerHTML = '<p class="text-zinc-500 text-xs">Complete tasks to unlock achievements</p>';
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
            showNotification('🏆 Achievement System', 'More achievement features coming soon!');
        }}
        
        function trackDownload(imageName) {{
            if (window.userProgress) {{
                userProgress.addDownload();
                updateUserStats();
            }}
            showNotification('📥 Download Success', 'Thanks for supporting FreeFineAI!');
        }}
        
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

# Generate multi-page functionality
def generate_gallery_page():
    """Generate gallery page"""
    with open(os.path.join(CONFIG["TEMPLATE_DIR"], "head.html"), "r", encoding="utf-8") as f: 
        head = f.read()
    
    images = sorted([f for f in os.listdir(CONFIG["IMG_DIR"]) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))], reverse=True)
    
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
                    <button onclick="toggleFavorite('{img}')" data-favorite-btn data-image="{img}" class="bg-zinc-800 text-white px-3 py-2 rounded-xl hover:bg-pink-600 transition-all" title="Add to favorites">🤍</button>
                    <a href="{CONFIG["TIP_JAR_URL"]}" target="_blank" class="bg-zinc-800 text-white px-3 py-2 rounded-xl hover:bg-blue-600 transition-all">❤</a>
                </div>
            </div>
        </div>
        '''
    
    gallery_content = f'''
    <header class="pt-32 pb-16 px-6 text-center">
        <h1 class="text-6xl md:text-8xl font-black mb-6 leading-none hero-title text-white">Gallery</h1>
        <p class="max-w-2xl mx-auto text-zinc-500 text-base font-light leading-relaxed mb-8">
            Browse our curated collection of Flux.1 AI-generated images
        </p>
    </header>

    <main class="max-w-[1400px] mx-auto px-6 pb-32">
        <div class="flex flex-col md:flex-row justify-between items-end mb-8 gap-4">
            <h2 class="text-white text-2xl font-black tracking-tighter uppercase italic">All Artworks</h2>
            <div class="flex gap-4 text-[10px] text-zinc-600 font-bold uppercase tracking-[0.3em]">
                <button class="hover:text-white transition">All</button>
                <button class="hover:text-white transition">Latest</button>
                <button class="hover:text-white transition">Popular</button>
            </div>
        </div>
        <div class="masonry">{cards_html}</div>
    </main>
    
    {generate_enhanced_scripts()}
</body>
</html>
'''
    
    with open("gallery.html", "w", encoding="utf-8") as f:
        f.write(head + gallery_content)

def generate_tools_page():
    """Generate tools page"""
    with open(os.path.join(CONFIG["TEMPLATE_DIR"], "head.html"), "r", encoding="utf-8") as f: 
        head = f.read()
    
    tools_content = f'''
    <header class="pt-32 pb-16 px-6 text-center">
        <h1 class="text-6xl md:text-8xl font-black mb-6 leading-none hero-title text-white">Tools</h1>
        <p class="max-w-2xl mx-auto text-zinc-500 text-base font-light leading-relaxed mb-8">
            Professional AI image generation tools and resources
        </p>
    </header>

    {generate_enhanced_tools()}
    
    <!-- More Tools -->
    <section class="max-w-[1400px] mx-auto px-8 mb-16">
        <h2 class="text-white text-2xl font-black tracking-tighter uppercase italic mb-8">More Tools</h2>
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            <!-- Image Comparison Tool -->
            <div class="bg-zinc-900/50 border border-white/5 p-6 rounded-3xl backdrop-blur-md">
                <div class="flex items-center gap-3 mb-4">
                    <div class="p-2 bg-green-500/10 rounded-lg text-green-400">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
                    </div>
                    <h3 class="text-white font-black text-xs uppercase tracking-[0.2em]">Image Compare</h3>
                </div>
                <p class="text-zinc-400 text-sm mb-4">Drag two images for A/B comparison analysis</p>
                <button class="w-full bg-zinc-800 hover:bg-green-600 text-white text-[10px] font-black py-3 rounded-xl uppercase tracking-widest transition">
                    Coming Soon
                </button>
            </div>
            
            <!-- Color Extractor -->
            <div class="bg-zinc-900/50 border border-white/5 p-6 rounded-3xl backdrop-blur-md">
                <div class="flex items-center gap-3 mb-4">
                    <div class="p-2 bg-pink-500/10 rounded-lg text-pink-400">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zM7 3H5a2 2 0 00-2 2v12a4 4 0 004 4h2a2 2 0 002-2V5a2 2 0 00-2-2z"/></svg>
                    </div>
                    <h3 class="text-white font-black text-xs uppercase tracking-[0.2em]">Color Extract</h3>
                </div>
                <p class="text-zinc-400 text-sm mb-4">Extract dominant colors and palettes from images</p>
                <button class="w-full bg-zinc-800 hover:bg-pink-600 text-white text-[10px] font-black py-3 rounded-xl uppercase tracking-widest transition">
                    Coming Soon
                </button>
            </div>
            
            <!-- Batch Downloader -->
            <div class="bg-zinc-900/50 border border-white/5 p-6 rounded-3xl backdrop-blur-md">
                <div class="flex items-center gap-3 mb-4">
                    <div class="p-2 bg-blue-500/10 rounded-lg text-blue-400">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                    </div>
                    <h3 class="text-white font-black text-xs uppercase tracking-[0.2em]">Batch Download</h3>
                </div>
                <p class="text-zinc-400 text-sm mb-4">Select multiple images for batch download</p>
                <button class="w-full bg-zinc-800 hover:bg-blue-600 text-white text-[10px] font-black py-3 rounded-xl uppercase tracking-widest transition">
                    Coming Soon
                </button>
            </div>
        </div>
    </section>
    
    {generate_enhanced_scripts()}
</body>
</html>
'''
    
    with open("tools.html", "w", encoding="utf-8") as f:
        f.write(head + tools_content)

def generate_about_page():
    """Generate about page"""
    with open(os.path.join(CONFIG["TEMPLATE_DIR"], "head.html"), "r", encoding="utf-8") as f: 
        head = f.read()
    
    about_content = f'''
    <header class="pt-32 pb-16 px-6 text-center">
        <h1 class="text-6xl md:text-8xl font-black mb-6 leading-none hero-title text-white">About Us</h1>
        <p class="max-w-2xl mx-auto text-zinc-500 text-base font-light leading-relaxed mb-8">
            Learn about FreeFineAI's story and mission
        </p>
    </header>

    <main class="max-w-[1400px] mx-auto px-6 pb-32">
        <div class="grid md:grid-cols-2 gap-12 mb-16">
            <div>
                <h2 class="text-3xl font-black text-white mb-6">Our Mission</h2>
                <p class="text-zinc-400 leading-relaxed mb-6">
                    FreeFineAI is dedicated to providing creators worldwide with the highest quality AI-generated image resources. We believe artificial intelligence should empower every creative person, not become a barrier to creation.
                </p>
                <p class="text-zinc-400 leading-relaxed">
                    Through our carefully curated Flux.1 image collection and powerful creative tools, we help designers, artists, and creative professionals turn imagination into reality.
                </p>
            </div>
            
            <div>
                <h2 class="text-3xl font-black text-white mb-6">Why Choose Us</h2>
                <div class="space-y-4">
                    <div class="flex items-start gap-3">
                        <div class="w-6 h-6 bg-cyan-500/20 rounded-full flex items-center justify-center mt-1">
                            <span class="text-cyan-400 text-xs">✓</span>
                        </div>
                        <div>
                            <h3 class="text-white font-bold mb-1">Curated Quality</h3>
                            <p class="text-zinc-400 text-sm">Every image is manually selected to ensure the highest visual quality</p>
                        </div>
                    </div>
                    
                    <div class="flex items-start gap-3">
                        <div class="w-6 h-6 bg-cyan-500/20 rounded-full flex items-center justify-center mt-1">
                            <span class="text-cyan-400 text-xs">✓</span>
                        </div>
                        <div>
                            <h3 class="text-white font-bold mb-1">Completely Free</h3>
                            <p class="text-zinc-400 text-sm">Core features are permanently free, supporting creative democratization</p>
                        </div>
                    </div>
                    
                    <div class="flex items-start gap-3">
                        <div class="w-6 h-6 bg-cyan-500/20 rounded-full flex items-center justify-center mt-1">
                            <span class="text-cyan-400 text-xs">✓</span>
                        </div>
                        <div>
                            <h3 class="text-white font-bold mb-1">Continuous Updates</h3>
                            <p class="text-zinc-400 text-sm">Daily new content, keeping pace with AI technology development</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Platform Statistics -->
        <section class="bg-zinc-900/50 border border-white/5 rounded-3xl p-8 mb-16">
            <h2 class="text-2xl font-black text-white mb-8 text-center">Platform Statistics</h2>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-8">
                <div class="text-center">
                    <div class="text-3xl font-black text-cyan-400 mb-2">1000+</div>
                    <div class="text-zinc-400 text-sm uppercase tracking-widest">Curated Images</div>
                </div>
                <div class="text-center">
                    <div class="text-3xl font-black text-purple-400 mb-2">50K+</div>
                    <div class="text-zinc-400 text-sm uppercase tracking-widest">Total Downloads</div>
                </div>
                <div class="text-center">
                    <div class="text-3xl font-black text-green-400 mb-2">10K+</div>
                    <div class="text-zinc-400 text-sm uppercase tracking-widest">Active Users</div>
                </div>
                <div class="text-center">
                    <div class="text-3xl font-black text-yellow-400 mb-2">24/7</div>
                    <div class="text-zinc-400 text-sm uppercase tracking-widest">Online Service</div>
                </div>
            </div>
        </section>
        
        <!-- Contact Information -->
        <section class="text-center">
            <h2 class="text-3xl font-black text-white mb-6">Contact Us</h2>
            <p class="text-zinc-400 mb-8 max-w-2xl mx-auto">
                Have questions, suggestions, or collaboration ideas? We'd love to hear from you.
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="mailto:hello@freefineai.com" class="bg-zinc-800 hover:bg-cyan-600 text-white px-8 py-3 rounded-xl transition font-bold">
                    📧 Send Email
                </a>
                <a href="{CONFIG['TWITTER_URL']}" class="bg-zinc-800 hover:bg-blue-600 text-white px-8 py-3 rounded-xl transition font-bold">
                    🐦 Twitter
                </a>
                <a href="{CONFIG['GITHUB_URL']}" class="bg-zinc-800 hover:bg-gray-600 text-white px-8 py-3 rounded-xl transition font-bold">
                    💻 GitHub
                </a>
            </div>
        </section>
    </main>
    
    {generate_enhanced_scripts()}
</body>
</html>
'''
    
    with open("about.html", "w", encoding="utf-8") as f:
        f.write(head + about_content)

# Generate main page
def generate():
    setup()
    print_config_info()
    
    with open(os.path.join(CONFIG["TEMPLATE_DIR"], "head.html"), "r", encoding="utf-8") as f: 
        head = f.read()

    images = sorted([f for f in os.listdir(CONFIG["IMG_DIR"]) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))], reverse=True)
    
    cards_html = ""
    for img in images[:12]:  # Show only first 12 images on homepage
        name = img.split('.')[0].replace('_', ' ').title()
        cards_html += f'''
        <div class="break-inside-avoid mb-6 relative group rounded-3xl overflow-hidden bg-zinc-900 border border-white/5 shadow-2xl transition-all duration-500 hover:border-cyan-500/50">
            <img src="images/{img}" alt="{name}" loading="lazy" class="w-full h-auto transition-transform duration-700 group-hover:scale-105">
            <div class="absolute inset-0 bg-gradient-to-t from-black via-black/60 to-transparent opacity-0 group-hover:opacity-100 transition-all duration-300 p-4 flex flex-col justify-end">
                <h3 class="text-white font-bold text-sm mb-3">{name}</h3>
                <div class="flex gap-2 text-center">
                    <a href="images/{img}" download onclick="trackDownload('{img}')" class="flex-1 bg-white text-black text-[10px] font-black py-2 rounded-xl uppercase">Download</a>
                    <button onclick="toggleFavorite('{img}')" data-favorite-btn data-image="{img}" class="bg-zinc-800 text-white px-3 py-2 rounded-xl hover:bg-pink-600 transition-all" title="Add to favorites">🤍</button>
                    <a href="{CONFIG["TIP_JAR_URL"]}" target="_blank" class="bg-zinc-800 text-white px-3 py-2 rounded-xl hover:bg-blue-600 transition-all">❤</a>
                </div>
            </div>
        </div>
        '''

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
            <h2 class="text-white text-2xl font-black tracking-tighter uppercase italic">Featured Works</h2>
            <a href="gallery.html" class="text-[10px] text-zinc-600 font-bold uppercase tracking-[0.3em] hover:text-white transition">View All →</a>
        </div>
        <div class="masonry">{cards_html}</div>
        
        <section class="mt-32 p-8 md:p-16 rounded-[3rem] bg-gradient-to-br from-zinc-900/80 via-zinc-900/40 to-transparent border border-white/5 relative overflow-hidden">
            <div class="absolute -top-20 -right-20 w-80 h-80 bg-primary/10 blur-[100px] rounded-full"></div>
            
            <div class="relative z-10 max-w-3xl">
                <h2 class="text-3xl md:text-5xl font-black text-white mb-6 tracking-tighter leading-none">
                    Push the Boundaries <br><span class="primary-color">of Flux.1</span>
                </h2>
                
                <div class="grid md:grid-cols-2 gap-6 text-left mb-8">
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

                <div class="flex flex-col sm:flex-row gap-4 items-center">
                    <a href="{CONFIG['MEGA_BUNDLE_URL']}" target="_blank" class="w-full sm:w-auto bg-white text-black font-black px-8 py-4 rounded-2xl hover:bg-primary transition-all transform hover:scale-105 uppercase tracking-widest text-xs shadow-2xl">
                        Unlock Pro Vault — {CONFIG["BUNDLE_PRICE"]}
                    </a>
                    <div class="text-[10px] text-zinc-600 uppercase tracking-[0.2em] font-bold">
                        One-time support • Lifetime updates
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
                <p class="text-zinc-500 text-xs leading-relaxed max-w-xs">Independent archive for Flux.1-dev assets. Built for the community.</p>
            </div>
            <div>
                <h4 class="text-white text-[10px] font-black uppercase tracking-[0.2em] mb-4">Navigation</h4>
                <ul class="space-y-3 text-xs font-bold">
                    <li><a href="index.html" class="text-zinc-600 hover:text-primary transition uppercase tracking-widest">Home</a></li>
                    <li><a href="gallery.html" class="text-zinc-600 hover:text-primary transition uppercase tracking-widest">Gallery</a></li>
                    <li><a href="tools.html" class="text-zinc-600 hover:text-primary transition uppercase tracking-widest">Tools</a></li>
                    <li><a href="about.html" class="text-zinc-600 hover:text-primary transition uppercase tracking-widest">About</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-white text-[10px] font-black uppercase tracking-[0.2em] mb-4">Legal</h4>
                <p class="text-[10px] text-zinc-600 font-bold uppercase">CC BY-NC 4.0 License</p>
            </div>
            <div>
                <h4 class="text-white text-[10px] font-black uppercase tracking-[0.2em] mb-4">Status</h4>
                <div class="flex items-center gap-2"><div class="w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse"></div><span class="text-[9px] text-zinc-400 uppercase font-bold">Operational</span></div>
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
    
    # Generate multi-page
    if CONFIG["ENABLE_MULTI_PAGE"]:
        generate_gallery_page()
        generate_tools_page()
        generate_about_page()
        print(f"📄 Multi-page generated: index.html, gallery.html, tools.html, about.html")
    
    print(f"🚀 English website generated successfully!")
    print(f"📊 Contains {len(images)} images")
    print(f"✨ All text converted to English")
    print(f"🎨 Interface optimized: compact spacing, visual coordination")
    print(f"💰 Monetization features: improved user engagement, optimized donation guidance")

if __name__ == "__main__":
    generate()