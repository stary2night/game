import base64, re, mimetypes, os

SRC  = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')
DEST = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'GreenShieldGuardian_standalone.html')
BASE = os.path.dirname(os.path.abspath(__file__))

with open(SRC, 'r', encoding='utf-8') as f:
    html = f.read()

def read_b64(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode()

def audio_mime(path):
    ext = os.path.splitext(path)[1].lower().lstrip('.')
    return {'mp3': 'audio/mpeg', 'wav': 'audio/wav', 'ogg': 'audio/ogg'}.get(ext, 'audio/mpeg')

# 替换 src="assets/images/..." 图片引用
def embed_img(m):
    path = os.path.join(BASE, m.group(1))
    if not os.path.exists(path):
        return m.group(0)
    mime = mimetypes.guess_type(path)[0] or 'image/png'
    print(f'  img   {m.group(1)}')
    return f'src="data:{mime};base64,{read_b64(path)}"'

# 替换单引号音频路径
def embed_audio_single(m):
    path = os.path.join(BASE, m.group(1))
    if not os.path.exists(path):
        return m.group(0)
    print(f'  audio {m.group(1)}')
    return f"'data:{audio_mime(path)};base64,{read_b64(path)}'"

# 替换双引号音频路径
def embed_audio_double(m):
    path = os.path.join(BASE, m.group(1))
    if not os.path.exists(path):
        return m.group(0)
    print(f'  audio {m.group(1)}')
    return f'"data:{audio_mime(path)};base64,{read_b64(path)}"'

print('Embedding images...')
html = re.sub(r'src="(assets/images/[^"]+)"', embed_img, html)

print('Embedding audio...')
html = re.sub(r"'(assets/audio/[^']+)'", embed_audio_single, html)
html = re.sub(r'"(assets/audio/[^"]+)"', embed_audio_double, html)

with open(DEST, 'w', encoding='utf-8') as f:
    f.write(html)

size_mb = os.path.getsize(DEST) / 1024 / 1024
print(f'\nDone! -> {os.path.basename(DEST)}  ({size_mb:.1f} MB)')
