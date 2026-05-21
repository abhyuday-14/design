import re

with open('c:\\Users\\capta\\Downloads\\python\\prot\\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS
css_search = r'\.grid-4-5 \{\s*display: grid;\s*grid-template-columns: repeat\(auto-fill, minmax\(200px, 1fr\)\);\s*gap: 12px;\s*\}\s*\.grid-16-9 \{\s*display: grid;\s*grid-template-columns: repeat\(auto-fill, minmax\(320px, 1fr\)\);\s*gap: 12px;\s*\}\s*\.grid-1-1 \{\s*display: grid;\s*grid-template-columns: repeat\(auto-fill, minmax\(250px, 1fr\)\);\s*gap: 12px;\s*\}'

css_replace = """    .grid-4-5, .grid-16-9, .grid-1-1 {
      display: flex;
      overflow-x: auto;
      scroll-snap-type: x mandatory;
      scroll-behavior: smooth;
      gap: 16px;
      padding-bottom: 24px;
      -ms-overflow-style: none; /* IE and Edge */
      scrollbar-width: none; /* Firefox */
    }
    .grid-4-5::-webkit-scrollbar, .grid-16-9::-webkit-scrollbar, .grid-1-1::-webkit-scrollbar {
      display: none; /* Chrome, Safari, Opera */
    }
    
    .grid-4-5 .gallery-card { width: 260px; flex: 0 0 auto; scroll-snap-align: start; }
    .grid-16-9 .gallery-card { width: 420px; flex: 0 0 auto; scroll-snap-align: start; }
    .grid-1-1 .gallery-card { width: 300px; flex: 0 0 auto; scroll-snap-align: start; }
    
    /* Navigation Buttons */
    .gallery-nav {
      display: flex;
      gap: 8px;
    }
    .nav-btn {
      background: none;
      border: 1px solid var(--glass-bdr);
      color: var(--muted);
      width: 32px; height: 32px;
      display: flex; align-items: center; justify-content: center;
      cursor: none;
      transition: color 0.2s, border-color 0.2s;
    }
    .nav-btn:hover {
      color: var(--accent);
      border-color: var(--accent);
    }
    """
content = re.sub(css_search, css_replace, content)

# 2. Add Modal CSS additions
content = content.replace('.modal-img-area svg { width: 48px; height: 48px; stroke: rgba(59,130,246,.2); fill: none; }', '.modal-img-area svg { width: 48px; height: 48px; stroke: rgba(59,130,246,.2); fill: none; }\n    #modal-img { max-width: 100%; max-height: 60vh; object-fit: contain; }')

# 3. Update HTML for Category Labels
html_label_social = '<div class="gallery-category-label">Social Media Posts — 4:5</div>'
html_label_social_new = '<div class="gallery-category-label">Social Media Posts — 4:5<div class="gallery-nav"><button class="nav-btn prev" data-target="grid-social">←</button><button class="nav-btn next" data-target="grid-social">→</button></div></div>'
content = content.replace(html_label_social, html_label_social_new)

html_label_posters = '<div class="gallery-category-label">Posters — 4:5</div>'
html_label_posters_new = '<div class="gallery-category-label">Posters — 4:5<div class="gallery-nav"><button class="nav-btn prev" data-target="grid-posters">←</button><button class="nav-btn next" data-target="grid-posters">→</button></div></div>'
content = content.replace(html_label_posters, html_label_posters_new)

html_label_merch = '<div class="gallery-category-label">Merch — 16:9</div>'
html_label_merch_new = '<div class="gallery-category-label">Merch — 16:9<div class="gallery-nav"><button class="nav-btn prev" data-target="grid-merch">←</button><button class="nav-btn next" data-target="grid-merch">→</button></div></div>'
content = content.replace(html_label_merch, html_label_merch_new)

html_label_thumbs = '<div class="gallery-category-label">Thumbnails — 16:9</div>'
html_label_thumbs_new = '<div class="gallery-category-label">Thumbnails — 16:9<div class="gallery-nav"><button class="nav-btn prev" data-target="grid-thumbs">←</button><button class="nav-btn next" data-target="grid-thumbs">→</button></div></div>'
content = content.replace(html_label_thumbs, html_label_thumbs_new)

html_label_logos = '<div class="gallery-category-label">Logos — 1:1</div>'
html_label_logos_new = '<div class="gallery-category-label">Logos — 1:1<div class="gallery-nav"><button class="nav-btn prev" data-target="grid-logos">←</button><button class="nav-btn next" data-target="grid-logos">→</button></div></div>'
content = content.replace(html_label_logos, html_label_logos_new)

# 4. Add Modal HTML before <script>
modal_html = """  <div id="modal-overlay">
    <button class="modal-close" id="modal-close-btn">CLOSE</button>
    <div class="modal-box">
      <div class="modal-img-area">
        <img id="modal-img" src="" alt="" style="display:none;">
        <svg id="modal-placeholder" viewBox="0 0 24 24" stroke-width="1"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>
      </div>
      <h3 class="modal-title" id="modal-title">Project Title</h3>
      <div class="modal-desc" id="modal-desc">Project Description</div>
    </div>
  </div>

  <script>"""
content = content.replace('  <script>', modal_html)

# 5. JS makeCard onclick
content = content.replace('      return card;\n    }', "      card.addEventListener('click', () => openModal(item.title, item.tag, item.image));\n      return card;\n    }")

# 6. JS openModal update
openModal_old = """    function openModal(title, tag) {
      document.getElementById('modal-title').textContent = title;
      document.getElementById('modal-desc').textContent  =
        `This is a placeholder for the ${title} project. Replace this with an image and project description once your design assets are ready.`;
      overlay.classList.add('open');
    }"""
openModal_new = """    function openModal(title, tag, imageUrl) {
      document.getElementById('modal-title').textContent = title;
      document.getElementById('modal-desc').textContent  = `Project category: ${tag}. Visual identity and creative direction for ${title}.`;
      const imgEl = document.getElementById('modal-img');
      const placeholder = document.getElementById('modal-placeholder');
      if (imageUrl) {
        imgEl.src = encodeURI(imageUrl);
        imgEl.style.display = 'block';
        placeholder.style.display = 'none';
      } else {
        imgEl.style.display = 'none';
        placeholder.style.display = 'block';
      }
      overlay.classList.add('open');
    }"""
content = content.replace(openModal_old, openModal_new)

# 7. Add JS for scrolling
js_scrolling = """    /* ── RE-OBSERVE CARDS AFTER POPULATION ─────── */
    
    // Horizontal Mouse Wheel Scrolling
    document.querySelectorAll('.grid-4-5, .grid-16-9, .grid-1-1').forEach(container => {
      container.addEventListener('wheel', (e) => {
        e.preventDefault();
        container.scrollLeft += e.deltaY;
      });
    });

    // Arrow Button Scrolling
    document.querySelectorAll('.nav-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const target = document.getElementById(btn.dataset.target);
        const scrollAmount = target.clientWidth * 0.75;
        if (btn.classList.contains('prev')) {
          target.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        } else {
          target.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        }
      });
    });
    
    // Wire custom cursor to the new modal button and nav buttons
    document.querySelectorAll('.modal-close, .nav-btn').forEach(btn => {
      btn.addEventListener('mouseenter', () => document.body.classList.add('cursor-hover'));
      btn.addEventListener('mouseleave', () => document.body.classList.remove('cursor-hover'));
    });
"""
content = content.replace('    /* ── RE-OBSERVE CARDS AFTER POPULATION ─────── */', js_scrolling)

with open('c:\\Users\\capta\\Downloads\\python\\prot\\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('UI Updated')
