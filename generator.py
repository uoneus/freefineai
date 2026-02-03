import os

# 配置
IMG_DIR = "images"
HTML_FILE = "index.html"
DOMAIN = "FreeFineAI.com"

def generate():
    # 1. 扫描图片
    if not os.path.exists(IMG_DIR):
        print(f"找不到 {IMG_DIR} 文件夹！")
        return

    images = [f for f in os.listdir(IMG_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    print(f"🚀 检测到 {len(images)} 张 Flux 作品...")

    # 2. 生成图片卡片 HTML
    cards_html = ""
    for img in images:
        # 去掉文件后缀作为标题
        display_name = img.split('.')[0]
        cards_html += f'''
        <div class="break-inside-avoid mb-8 relative group rounded-2xl overflow-hidden bg-zinc-900 border border-white/5 hover:border-cyan-500/50 transition-all duration-500 shadow-2xl">
            <img src="images/{img}" class="w-full h-auto transition-transform duration-700 group-hover:scale-110">
            <div class="absolute inset-0 bg-gradient-to-t from-black via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-all duration-300 p-6 flex flex-col justify-end">
                <p class="text-cyan-400 font-mono text-[10px] tracking-[0.2em] mb-2 uppercase">Flux Model Output</p>
                <h3 class="text-white font-bold text-sm mb-4 opacity-80 truncate">{display_name}</h3>
                <div class="flex gap-2">
                    <a href="images/{img}" download class="flex-1 bg-white text-black text-center py-2.5 rounded-xl font-black text-xs hover:bg-cyan-400 transition-colors uppercase tracking-wider">Download</a>
                    <a href="https://www.buymeacoffee.com/uoneus" target="_blank" class="bg-zinc-800 text-white p-2.5 rounded-xl border border-white/10 hover:bg-white hover:text-black transition-all">☕</a>
                </div>
            </div>
        </div>
        '''

    # 3. 完整的 HTML 模板 (含高级 CSS)
    full_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{DOMAIN} | Curated AI Excellence</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {{ background-color: #030303; }}
        .masonry {{ column-count: 1; column-gap: 2rem; }}
        @media (min-width: 640px) {{ .masonry {{ column-count: 2; }} }}
        @media (min-width: 1024px) {{ .masonry {{ column-count: 3; }} }}
        @media (min-width: 1536px) {{ .masonry {{ column-count: 4; }} }}
    </style>
</head>
<body class="text-zinc-400 antialiased font-sans">
    <nav class="fixed top-0 w-full z-50 bg-black/60 backdrop-blur-xl border-b border-white/5 px-6 py-4 flex justify-between items-center">
        <div class="flex items-center gap-3">
            <div class="w-7 h-7 bg-white rounded-md flex items-center justify-center text-black font-black text-xs">F</div>
            <span class="text-white font-black tracking-tighter text-lg uppercase">FreeFine<span class="text-cyan-500">AI</span></span>
        </div>
        <a href="https://www.buymeacoffee.com/uoneus" target="_blank" class="text-[10px] font-bold tracking-widest text-zinc-500 hover:text-white transition uppercase">Support Project</a>
    </nav>

    <header class="pt-32 pb-16 px-6 text-center">
        <h1 class="text-5xl md:text-7xl font-black text-white tracking-tighter mb-4">FINEST FLUX.</h1>
        <p class="max-w-xl mx-auto text-zinc-500 text-sm md:text-base font-light leading-relaxed italic">
            "A curated collection of high-fidelity AI generations, refined for the modern creator."
        </p>
    </header>

    <main class="max-w-[1600px] mx-auto px-6 pb-32">
        <div class="masonry">
            {cards_html}
        </div>
    </main>

    <footer class="py-20 border-t border-white/5 text-center">
        <p class="text-[10px] tracking-[0.4em] text-zinc-600 uppercase">&copy; 2026 {DOMAIN} / All Rights Free</p>
    </footer>
</body>
</html>
'''
    # 4. 写入文件
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(full_content)
    
    print(f"✨ 成功！高级版网页已生成。")
    print(f"👉 提示：请确保本地双击 index.html 看到图后，再执行 git push。")

if __name__ == "__main__":
    generate()