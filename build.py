"""Builds a single self-contained index.html (images + fonts inlined) from index.dev.html."""
import base64, re, mimetypes, pathlib
root = pathlib.Path(__file__).parent
src = (root / "index.dev.html").read_text(encoding="utf-8")
mime = {".jpg": "image/jpeg", ".png": "image/png", ".woff2": "font/woff2"}
def inline(m):
    path = root / m.group(0)
    data = base64.b64encode(path.read_bytes()).decode()
    return f"data:{mime[path.suffix]};base64,{data}"
out = re.sub(r"assets/[A-Za-z0-9_./-]+", inline, src)
out = out.replace(' loading="lazy"', "")
(root / "index.html").write_text(out, encoding="utf-8")
print("index.html", round(len(out.encode()) / 1024 / 1024, 2), "MB")
