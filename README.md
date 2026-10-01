# EstateGuard landing page

Single-page marketing site, built to match the Estatia template layout.

- `index.dev.html` is the editable source. It loads images and fonts from `assets/`.
- `index.html` is the self-contained build with images and fonts embedded. Open it directly or email it.
- `python build.py` regenerates `index.html` from `index.dev.html`.

## Preview locally

    python -m http.server 5173

Then open http://localhost:5173/index.dev.html

## Placeholders to replace

- Stock photos in `assets/` come from the template and are placeholders.
- Footer phone, address, email and social links.
- Items marked `[to be confirmed with counsel]`.
