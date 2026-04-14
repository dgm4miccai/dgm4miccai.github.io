from jinja2 import Environment, FileSystemLoader, select_autoescape
import os, sys
import json

TEMPLATES_DIR = "templates"
# common source filename candidates for index
candidates = [
    "index.html.j2",
    "index.j2",
    "index.html.tpl",
    "index.tpl",
    "index.jinja2",
    "index.jinja",
    "index.html",
]

env = Environment(
    loader=FileSystemLoader(TEMPLATES_DIR),
    autoescape=select_autoescape(["html", "xml"]),
)

# find first existing candidate template file
src_name = None
for c in candidates:
    if os.path.exists(os.path.join(TEMPLATES_DIR, c)):
        src_name = c
        break

if not src_name:
    # fallback: pick first file in templates/ with a jinja-like extension
    for fname in sorted(os.listdir(TEMPLATES_DIR)):
        if fname.endswith((".j2", ".jinja2", ".jinja", ".tpl", ".html")):
            src_name = fname
            break

if not src_name:
    print(
        "No template file found in templates/ to render for index.html", file=sys.stderr
    )
    sys.exit(1)

template = env.get_template(src_name)
with open("config.json", "r") as f:
    context = json.load(f)

rendered = template.render(**context)

out_path = "index.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(rendered)

print(f"Rendered {src_name} -> {out_path}")
