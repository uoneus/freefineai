import os

# === 商业配置区 ===
IMG_DIR = "images"
HTML_FILE = "index.html"
DOMAIN = "FreeFineAI.com"

# 你的 PayPal 支付链接
TIP_JAR_URL = "https://www.paypal.com/ncp/payment/ZRQDBKWE7VBSU"  # $1.09
MEGA_BUNDLE_URL = "https://www.paypal.com/ncp/payment/AQSGVVXLW69GJ" # $9.99
COFFEE_URL = "https://www.buymeacoffee.com/uoneus"

def generate():
    if not os.path.exists(IMG_DIR):
        os.makedirs(IMG_DIR)
        return

    images = [f for f in os.listdir(IMG_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    
    # 1. 生成图片卡片
    cards_html = ""
    for img in images:
        display_name = img.split('.')[0].replace('_', ' ').title()
        cards_html += f'''
        <div class="break-inside-avoid mb-8 relative group rounded-3xl overflow-hidden bg-zinc-900 border border-white/5 shadow-2xl transition-all duration-500 hover:border-cyan-500/50">
            <img src="images/{img}" alt="{display_name}" loading="lazy" class="w-full h-auto transition-transform duration-700 group-hover:scale-105">
            <div class="absolute inset-0 bg-gradient-to-t from-black via-black/60 to-transparent opacity-0 group-hover:opacity-100 transition-all duration-300 p-6 flex flex-col justify-end">
                <h3 class="text-white font-bold text-sm mb-4 opacity-90">{display_name}</h3>
                <div class="flex gap-2">
                    <a href="images/{img}" download class="flex-1 bg-white text-black text-[10px] font-black py-3 rounded-xl hover:bg-cyan-400 transition-colors uppercase tracking-tighter">Free Download</a>
                    <a href="{TIP_JAR_URL}" target="_blank" class="bg-zinc-800/80 backdrop-blur-md text-white px-4 py-3 rounded-xl hover:bg-blue-600 transition-all" title="Tip $1.09">
                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z" fill-opacity="0.2"/><path d="M12 17V7M7 12H17" stroke="white" stroke-width="2" stroke-linecap="round"/></svg>
                    </a>
                </div>
            </div>
        </div>
        '''

    # 2. 完整 HTML
    full_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FreeFineAI | Premium Flux Assets</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {{ background-color: #050505; color: #a1a1aa; font-family: 'Inter', sans-serif; }}
        .masonry {{ column-count: 1; column-gap: 1.5rem; }}
        @media (min-width: 768px) {{ .masonry {{ column-count: 2; }} }}
        @media (min-width: 1280px) {{ .masonry {{ column-count: 3; }} }}
    </style>
</head>
<body class="antialiased">
    <nav class="fixed top-0 w-full z-50 bg-black/80 backdrop-blur-lg border-b border-white/5 px-8 py-5 flex justify-between items-center">
        <div class="flex items-center gap-2">
            <span class="text-white font-black text-xl tracking-tighter italic">FREEFINE<span class="text-cyan-500">AI</span></span>
        </div>
        <div class="flex gap-4">
            <a href="{TIP_JAR_URL}" target="_blank" class="text-[10px] font-bold text-zinc-400 hover:text-white mt-2 transition uppercase tracking-widest">Tip Jar</a>
            <a href="{MEGA_BUNDLE_URL}" target="_blank" class="bg-cyan-600 hover:bg-cyan-400 text-white text-[10px] font-black px-5 py-2.5 rounded-full transition transform hover:scale-105 uppercase tracking-widest shadow-lg shadow-cyan-500/20">Get Mega Bundle $9.99</a>
        </div>
    </nav>

    <header class="pt-48 pb-24 px-6 text-center">
        <h1 class="text-7xl md:text-9xl font-black text-white tracking-tighter mb-8 leading-none">FLUX<br><span class="text-zinc-800">UNLIMITED.</span></h1>
        <p class="max-w-2xl mx-auto text-zinc-500 text-lg font-light leading-relaxed">
            Premium, high-fidelity AI generations for visionaries. <br>
            <span class="text-cyan-500/80 font-mono text-sm uppercase tracking-widest">Free to use. Powered by your support.</span>
        </p>
    </header>

    <main class="max-w-[1400px] mx-auto px-6 pb-40">
        <div class="masonry">{cards_html}</div>
        
        <section class="mt-20 p-12 rounded-[3rem] bg-gradient-to-b from-zinc-900 to-black border border-white/5 text-center">
            <h2 class="text-3xl font-bold text-white mb-4">Support the Collection</h2>
            <p class="mb-8 text-zinc-400">Get instant access to our entire 4K Raw collection (100+ Assets).</p>
            <a href="{MEGA_BUNDLE_URL}" target="_blank" class="inline-block bg-white text-black font-black px-10 py-4 rounded-2xl hover:bg-cyan-400 transition-all uppercase tracking-widest text-sm">Download Mega Bundle $9.99</a>
        </section>
    </main>

    <footer class="py-20 border-t border-white/5 text-center text-[10px] tracking-[0.5em] text-zinc-700 uppercase">
        &copy; 2026 FreeFineAI / Global Digital Assets
    </footer>
</body>
</html>
'''
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(full_content)
    print("✨ Production Ready HTML Generated!")

if __name__ == "__main__":
    generate()