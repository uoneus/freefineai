import os

# 1. 配置
IMG_DIR = "images"
HTML_FILE = "index.html"

# 2. 扫描图片
if not os.path.exists(IMG_DIR):
    os.makedirs(IMG_DIR)
    print(f"Error: Please put images into '{IMG_DIR}' folder first!")
    exit()

images = [f for f in os.listdir(IMG_DIR) if f.endswith(('.png', '.jpg', '.jpeg', '.webp'))]

# 3. 生成图片卡片 HTML (匹配高级版 UI)
cards_html = ""
for img in images:
    # 自动生成一个简单的标题（取文件名）
    title = img.split('.')[0].replace('_', ' ').title()
    
    cards_html += f'''
    <div class="img-card break-inside-avoid mb-6 relative group rounded-2xl overflow-hidden bg-slate-900 border border-white/5">
        <img src="images/{img}" class="w-full h-auto">
        <div class="absolute inset-0 bg-gradient-to-t from-black via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-all duration-300 p-8 flex flex-col justify-end">
            <p class="text-cyan-400 font-mono text-xs mb-2 tracking-widest uppercase">AI GENERATED</p>
            <h3 class="text-xl font-bold mb-4 leading-tight text-white">{title}</h3>
            <div class="flex gap-3">
                <a href="images/{img}" download class="flex-1 bg-white/10 backdrop-blur-md border border-white/20 text-center py-3 rounded-xl font-bold text-sm hover:bg-white hover:text-black transition">Download HD</a>
                <button class="bg-cyan-500/20 text-cyan-400 p-3 rounded-xl border border-cyan-500/30">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                </button>
            </div>
        </div>
    </div>
    '''

# 4. 读取现有的 index.html 并替换内容
# 注意：你需要手动在 index.html 里找个地方放 和 标记
# 或者我直接帮你生成一个完整的
# (为了简单，我建议你直接运行这个脚本生成整站)

print(f"Found {len(images)} images. Generating index.html...")
# ... 此处省略部分逻辑，直接覆盖写入 ...