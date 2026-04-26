from nicegui import ui, app

# ── Serve uploaded images ──────────────────────────────────────────────────────
app.add_static_files('/images', '/mnt/user-data/uploads')

# ── Theme colors ──────────────────────────────────────────────────────────────
GOLD   = '#C9A84C'
GOLD2  = '#E8C96C'

DARK = {
    'bg':       '#0d0d0d',
    'bg2':      '#141414',
    'bg3':      '#1c1c1c',
    'card':     'rgba(201,168,76,0.07)',
    'border':   'rgba(201,168,76,0.25)',
    'text':     '#e8e0d0',
    'muted':    '#9A8A6A',
    'heading':  '#C9A84C',
    'sub':      'rgba(232,224,208,0.6)',
    'navbar':   'rgba(10,10,10,0.97)',
    'hr':       'rgba(201,168,76,0.25)',
}

LIGHT = {
    'bg':       '#FFFFFF',
    'bg2':      '#F5F0E8',
    'bg3':      '#EDE5D0',
    'card':     'rgba(201,168,76,0.05)',
    'border':   'rgba(201,168,76,0.25)',
    'text':     '#2C2416',
    'muted':    '#6B5C3E',
    'heading':  '#C9A84C',
    'sub':      'rgba(44,36,22,0.6)',
    'navbar':   'rgba(245,240,232,0.97)',
    'hr':       'rgba(201,168,76,0.3)',
}

# ── Shared state ──────────────────────────────────────────────────────────────
theme_mode = {'dark': True}   # mutable dict so inner functions can mutate it

def T():
    return DARK if theme_mode['dark'] else LIGHT

# ── Google Fonts ──────────────────────────────────────────────────────────────
FONTS = '''
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400&family=Raleway:wght@300;400;500;600;700&family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&display=swap" rel="stylesheet">
'''

BASE_CSS = '''
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { font-family: 'Raleway', sans-serif; overflow-x: hidden; }
h1,h2,h3,h4 { font-family: 'Playfair Display', serif; }
.nicegui-content { padding: 0 !important; }

.page-wrap   { min-height: 100vh; transition: background 0.3s, color 0.3s; }
.content-area { max-width: 1100px; margin: 0 auto; padding: 80px 40px 60px; }

/* ── Nav ── */
.topnav {
    position: fixed; top: 0; left: 0; right: 0; z-index: 999;
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 40px; height: 62px;
    backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(201,168,76,0.25);
    transition: background 0.3s;
}
.nav-brand {
    font-family: 'Playfair Display', serif;
    font-size: 1.1rem; font-weight: 900; color: #C9A84C;
    text-decoration: none; letter-spacing: 0.03em;
}
.nav-links { display: flex; gap: 6px; align-items: center; flex-wrap: wrap; }
.nav-link {
    font-family: 'Raleway', sans-serif; font-size: 0.78rem;
    font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase;
    padding: 6px 13px; border-radius: 3px; cursor: pointer;
    transition: background 0.2s, color 0.2s; text-decoration: none;
    border: none; background: transparent;
}
.nav-link:hover  { background: rgba(201,168,76,0.15); color: #C9A84C !important; }
.nav-link-active { background: rgba(201,168,76,0.15); color: #C9A84C !important; }

.theme-btn {
    font-size: 1rem; cursor: pointer; padding: 5px 10px;
    border-radius: 20px; border: 1px solid rgba(201,168,76,0.4);
    background: transparent; color: #C9A84C; transition: all 0.2s;
}
.theme-btn:hover { background: rgba(201,168,76,0.15); }

/* ── Hero ── */
.hero {
    min-height: 92vh; display: flex; align-items: center; justify-content: center;
    text-align: center; padding: 80px 40px 60px;
    background: linear-gradient(160deg, rgba(201,168,76,0.05) 0%, transparent 60%);
    position: relative; overflow: hidden;
}
.hero::before {
    content: '𝄞'; position: absolute; font-size: 28rem;
    color: rgba(201,168,76,0.03); right: -4rem; top: -4rem; line-height: 1; pointer-events: none;
}
.hero-inner { max-width: 800px; }
.hero-eyebrow {
    font-family: 'Raleway', sans-serif; font-size: 0.7rem; font-weight: 700;
    letter-spacing: 0.3em; text-transform: uppercase; color: #C9A84C; margin-bottom: 1rem;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.5rem, 8vw, 5.5rem); font-weight: 900;
    line-height: 1.05; color: #C9A84C; margin-bottom: 1rem;
    text-shadow: 0 4px 30px rgba(201,168,76,0.2);
}
.hero-sub {
    font-family: 'Cormorant Garamond', serif; font-size: clamp(1rem, 3vw, 1.5rem);
    font-style: italic; margin-bottom: 2.5rem; opacity: 0.75;
}
.hero-btns { display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; }
.btn-gold {
    display: inline-block; padding: 13px 38px; border-radius: 3px;
    background: linear-gradient(135deg, #C9A84C, #E8C96C);
    color: #fff !important; font-family: 'Raleway', sans-serif;
    font-size: 0.82rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase;
    text-decoration: none; border: none; cursor: pointer;
    box-shadow: 0 6px 24px rgba(201,168,76,0.28); transition: all 0.25s;
}
.btn-gold:hover { opacity: 0.87; transform: translateY(-2px); box-shadow: 0 10px 32px rgba(201,168,76,0.38); }
.btn-outline {
    display: inline-block; padding: 12px 36px; border-radius: 3px;
    background: transparent; color: #C9A84C !important;
    font-family: 'Raleway', sans-serif; font-size: 0.82rem; font-weight: 700;
    letter-spacing: 0.14em; text-transform: uppercase; text-decoration: none;
    border: 1.5px solid #C9A84C; cursor: pointer; transition: all 0.25s;
}
.btn-outline:hover { background: rgba(201,168,76,0.12); }

/* ── Stats grid ── */
.stat-grid {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 16px; margin: 40px 0;
}
.stat-box {
    border-radius: 4px; padding: 28px 20px; text-align: center;
    border: 1px solid rgba(201,168,76,0.22);
    background: rgba(201,168,76,0.05); transition: border-color 0.2s;
}
.stat-box:hover { border-color: #C9A84C; }
.stat-num {
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.8rem, 5vw, 2.8rem); font-weight: 900; color: #C9A84C; display: block;
}
.stat-lbl {
    font-size: 0.65rem; font-weight: 700; letter-spacing: 0.16em;
    text-transform: uppercase; color: #9A8A6A; margin-top: 6px;
}

/* ── Cards ── */
.card {
    border-radius: 4px; padding: 22px 24px; margin-bottom: 14px;
    border: 1px solid rgba(201,168,76,0.2); background: rgba(201,168,76,0.05);
    transition: border-color 0.2s, box-shadow 0.2s;
}
.card:hover { border-color: rgba(201,168,76,0.5); box-shadow: 0 4px 20px rgba(201,168,76,0.08); }
.card-title { font-family: 'Playfair Display', serif; font-size: 1.05rem; color: #C9A84C; margin-bottom: 8px; }

/* ── Pull quote ── */
.pull-quote {
    border-left: 3px solid #C9A84C; padding: 14px 22px;
    background: rgba(201,168,76,0.07); border-radius: 0 4px 4px 0; margin: 24px 0;
}
.pull-quote p {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(1rem, 3vw, 1.25rem); font-style: italic;
}

/* ── Section titles ── */
.sec-eyebrow {
    font-size: 0.63rem; font-weight: 700; letter-spacing: 0.28em;
    text-transform: uppercase; color: #C9A84C; margin-bottom: 6px;
}
.sec-h1 { font-family: 'Playfair Display', serif; font-size: clamp(1.8rem, 5vw, 3rem); font-weight: 900; color: #C9A84C; }
.sec-h2 { font-family: 'Playfair Display', serif; font-size: clamp(1.3rem, 4vw, 2rem); font-weight: 700; color: #C9A84C; margin: 28px 0 12px; }
.sec-h3 { font-family: 'Playfair Display', serif; font-size: clamp(1rem, 3vw, 1.45rem); font-weight: 700; color: #C9A84C; margin: 20px 0 10px; }
.sec-lead {
    font-family: 'Cormorant Garamond', serif; font-size: clamp(0.95rem, 2.5vw, 1.15rem);
    font-style: italic; opacity: 0.72; margin-bottom: 30px; line-height: 1.65;
}
.sec-body { font-size: 0.95rem; line-height: 1.85; opacity: 0.88; }
.gold-hr { border: none; height: 1px; background: linear-gradient(90deg, transparent, rgba(201,168,76,0.35), transparent); margin: 32px 0; }

/* ── Timeline ── */
.timeline-item { display: flex; gap: 16px; margin-bottom: 28px; align-items: flex-start; }
.tl-year {
    font-family: 'Playfair Display', serif; font-size: clamp(0.85rem, 2.5vw, 1.2rem);
    font-weight: 900; color: #C9A84C; min-width: 72px; text-align: right; padding-top: 2px;
}
.tl-dot {
    width: 13px; height: 13px; background: #C9A84C; border-radius: 50%;
    margin-top: 4px; flex-shrink: 0; position: relative;
}
.tl-dot::after {
    content: ''; position: absolute; top: 13px; left: 5px;
    width: 2px; height: 50px; background: linear-gradient(to bottom, rgba(201,168,76,0.4), transparent);
}
.tl-content h4 { font-family: 'Playfair Display', serif; font-size: 0.98rem; color: #C9A84C; margin-bottom: 4px; }
.tl-content p  { font-size: 0.88rem; line-height: 1.65; opacity: 0.78; margin: 0; }

/* ── Two-col layout ── */
.two-col { display: grid; grid-template-columns: 2fr 1fr; gap: 40px; align-items: start; }
.two-col-eq { display: grid; grid-template-columns: 1fr 1fr; gap: 32px; align-items: start; }
@media (max-width: 680px) { .two-col, .two-col-eq { grid-template-columns: 1fr; } }

/* ── Photo ── */
.photo-wrap { border-radius: 6px; overflow: hidden; border: 1px solid rgba(201,168,76,0.25); }
.photo-wrap img { width: 100%; height: auto; display: block; }
.photo-caption {
    font-family: 'Cormorant Garamond', serif; font-style: italic;
    font-size: 0.78rem; color: #9A8A6A; padding: 8px 10px; text-align: center;
}

/* ── Fact chip ── */
.fact-chip {
    display: flex; gap: 12px; align-items: center;
    border-radius: 3px; padding: 10px 14px; margin-bottom: 8px;
    background: rgba(201,168,76,0.05); border: 1px solid rgba(201,168,76,0.15);
    font-size: 0.87rem; line-height: 1.4;
}

/* ── Platform links ── */
.platform-link {
    display: flex; align-items: center; gap: 12px;
    border-radius: 4px; padding: 10px 16px; margin-bottom: 8px;
    background: rgba(201,168,76,0.06); border: 1px solid rgba(201,168,76,0.2);
    text-decoration: none; transition: background 0.2s;
}
.platform-link:hover { background: rgba(201,168,76,0.14); }
.platform-link .pl-name { font-weight: 600; font-size: 0.9rem; }
.platform-link .pl-action { margin-left: auto; font-size: 0.75rem; color: #C9A84C; font-weight: 600; }

/* ── Song table ── */
.song-row {
    display: flex; justify-content: space-between; flex-wrap: wrap; gap: 6px;
    border-radius: 4px; padding: 12px 16px; margin-bottom: 8px;
    background: rgba(201,168,76,0.04); border: 1px solid rgba(201,168,76,0.15);
}
.song-title { font-family: 'Playfair Display', serif; font-size: 0.95rem; font-weight: 700; }
.song-year  { font-size: 0.8rem; color: #C9A84C; font-weight: 700; flex-shrink: 0; }
.song-artist { font-size: 0.85rem; opacity: 0.7; width: 100%; }
.song-note  { font-family: 'Cormorant Garamond', serif; font-style: italic; font-size: 0.82rem; opacity: 0.55; width: 100%; }

/* ── New release banner ── */
.release-banner {
    background: linear-gradient(135deg, rgba(201,168,76,0.12), rgba(201,168,76,0.04));
    border: 1px solid #C9A84C; border-radius: 6px; padding: 36px;
    text-align: center; margin: 36px 0;
    box-shadow: 0 8px 40px rgba(201,168,76,0.1);
}

/* ── Artist grid ── */
.artist-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; margin-top: 20px; }

/* ── Contact form ── */
.contact-grid { display: grid; grid-template-columns: 3fr 2fr; gap: 40px; }
@media (max-width: 680px) { .contact-grid { grid-template-columns: 1fr; } }

/* ── Footer ── */
.site-footer {
    border-top: 1px solid rgba(201,168,76,0.2); padding-top: 24px; margin-top: 60px;
    text-align: center;
}
.site-footer p {
    font-family: 'Cormorant Garamond', serif; font-style: italic;
    font-size: 0.82rem; color: #9A8A6A;
}

/* ── Video wrapper ── */
.video-wrap {
    position: relative; width: 100%; padding-bottom: 56.25%;
    height: 0; overflow: hidden; border-radius: 6px; margin: 20px 0;
}
.video-wrap iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-thumb { background: rgba(201,168,76,0.4); border-radius: 3px; }

@media (max-width: 680px) {
    .topnav { padding: 0 16px; }
    .content-area { padding: 72px 18px 40px; }
    .hero { padding: 72px 18px 40px; }
    .nav-links .nav-link { font-size: 0.68rem; padding: 4px 8px; letter-spacing: 0.06em; }
}
</style>
'''

# ── Navigation builder ──────────────────────────────────────────────────────────
PAGES = [
    ('🏠 Home',           '/'),
    ('👥 Meet the Twins', '/twins'),
    ('👤 Melvin',         '/melvin'),
    ('👤 Mervin',         '/mervin'),
    ('🎵 With You Jesus', '/wyj'),
    ('🎼 Legacy',         '/legacy'),
    ('✉️ Contact',        '/contact'),
]

def nav(current: str):
    t = T()
    ui.add_head_html(FONTS + BASE_CSS)
    ui.query('body').style(f'background:{t["bg"]};color:{t["text"]};')
    ui.query('.nicegui-content').style('padding:0 !important;')
    with ui.element('nav').classes('topnav').style(f'background:{t["navbar"]};'):
        ui.link('THE STEALS BROTHERS', '/').classes('nav-brand')
        with ui.row().classes('nav-links items-center gap-1'):
            for label, path in PAGES:
                active = 'nav-link-active' if current == path else ''
                ui.link(label, path).classes(f'nav-link {active}').style(f'color:{t["text"]};')
            # Dark/Light toggle
            def toggle():
                theme_mode['dark'] = not theme_mode['dark']
                ui.navigate.reload()
            icon = '☀️' if theme_mode['dark'] else '🌙'
            ui.button(icon, on_click=toggle).classes('theme-btn').props('flat dense')

def footer():
    ui.html('<div class="site-footer"><p>© 2025 Melvin Steals Sr. & Mervin Steals Sr. · The Steals Brothers · All Rights Reserved · Aliquippa, Pennsylvania</p></div>')

def gold_hr():
    ui.html('<hr class="gold-hr">')

# ══════════════════════════════════════════════════════════════════════════════
# HOME PAGE
# ══════════════════════════════════════════════════════════════════════════════
@ui.page('/')
def page_home():
    t = T()
    nav('/')
    with ui.element('div').classes('page-wrap').style(f'background:{t["bg"]};color:{t["text"]};'):
        # Hero
        with ui.element('div').classes('hero'):
            with ui.element('div').classes('hero-inner'):
                ui.html('<p class="hero-eyebrow">Mystro & Lyric · Aliquippa, Pennsylvania</p>')
                ui.html('<h1 class="hero-title">The Steals<br>Brothers</h1>')
                ui.html('<p class="hero-sub">Melvin Harold Steals Sr. & Mervin Howard Steals Sr.<br>Twin Brothers · Grammy Winners · Musical Legends</p>')
                ui.html('''
                <div class="hero-btns">
                    <a class="btn-gold" href="/wyj">🎵 With You Jesus</a>
                    <a class="btn-outline" href="/twins">Meet the Twins</a>
                </div>''')

        # Stats
        with ui.element('div').classes('content-area').style('padding-top:0;'):
            ui.html('<div class="stat-grid">'
                    '<div class="stat-box"><span class="stat-num">2</span><span class="stat-lbl">Grammy Nominations</span></div>'
                    '<div class="stat-box"><span class="stat-num">1</span><span class="stat-lbl">Grammy Win</span></div>'
                    '<div class="stat-box"><span class="stat-num">100+</span><span class="stat-lbl">Songs Written</span></div>'
                    '<div class="stat-box"><span class="stat-num">4M+</span><span class="stat-lbl">Radio Spins</span></div>'
                    '<div class="stat-box"><span class="stat-num">47</span><span class="stat-lbl">Still Played Worldwide</span></div>'
                    '</div>')

            gold_hr()

            # New release banner
            with ui.element('div').classes('release-banner'):
                ui.html('<span class="sec-eyebrow">New Gospel Single</span>')
                ui.html('<h2 class="sec-h1" style="margin:10px 0 8px;">With You Jesus</h2>')
                ui.html('<p class="sec-lead" style="margin-bottom:20px;">A gospel reimagining of the classic "Could It Be I\'m Falling in Love" · The Philly Mix</p>')
                ui.html('''<div class="hero-btns">
                    <a class="btn-gold" href="https://open.spotify.com/album/1XoeZnbaHFVmTAqooppyIG" target="_blank">🟢 Spotify</a>
                    <a class="btn-gold" href="https://music.apple.com/us/album/with-you-jesus-philly-mix-single/1874032863" target="_blank">🎵 Apple Music</a>
                    <a class="btn-gold" href="https://youtu.be/98ajxKlR5Dk?feature=shared" target="_blank">▶ YouTube</a>
                </div>''')

            gold_hr()

            # Photos side by side
            ui.html('<p class="sec-eyebrow">Then & Now</p>')
            ui.html('<h2 class="sec-h2" style="margin-top:6px;">A Lifetime of Music</h2>')
            with ui.element('div').classes('two-col-eq'):
                with ui.element('div').classes('photo-wrap'):
                    ui.image('/images/twinsOldHouse.webp').style('width:100%;display:block;')
                    ui.html('<p class="photo-caption">Melvin & Mervin on their porch in Aliquippa — the early years</p>')
                with ui.element('div').classes('photo-wrap'):
                    ui.image('/images/MoreCurrentPic.webp').style('width:100%;display:block;')
                    ui.html('<p class="photo-caption">Melvin & Mervin Steals Sr. — still brothers, still writing history</p>')

            gold_hr()

            # Pull quote
            ui.html('''<div class="pull-quote"><p>"Born together. Inseparable in music.<br>
                Two halves of one extraordinary gift."</p></div>''')

            gold_hr()

            # Artists who recorded their songs
            ui.html('<p class="sec-eyebrow">Recorded by Legends</p>')
            ui.html('<h2 class="sec-h2" style="margin-top:6px;">Artists Who Recorded Steals Brothers Classics</h2>')
            artists = [
                ("The Spinners", "Could It Be I'm Falling in Love"),
                ("Gloria Gaynor", "Honey Bee"),
                ("Archie Bell & The Drells", "Go For What You Know"),
                ("The Trammps", "Trusting Heart"),
                ("Blue Magic", "Steals Brothers Composition"),
                ("Harold Melvin & The Blue Notes", "Steals Brothers Composition"),
                ("Donnie Osmond", "Could It Be… (cover)"),
                ("Regina Belle", "Could It Be… (cover)"),
                ("A$AP Rocky", "Back Home (sample)"),
                ("Mary J. Blige", "Treat 'Em Right (sample)"),
                ("Kaytranada ft. Kali Uchis", "10% — 2021 Grammy Winner"),
                ("The Impressions", "Steals Brothers Composition"),
            ]
            with ui.element('div').classes('artist-grid'):
                for artist, song in artists:
                    ui.html(f'''<div class="card" style="padding:14px 16px;">
                        <div class="card-title" style="font-size:0.95rem;">{artist}</div>
                        <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-size:0.83rem;opacity:0.6;">{song}</div>
                    </div>''')

            footer()


# ══════════════════════════════════════════════════════════════════════════════
# MEET THE TWINS
# ══════════════════════════════════════════════════════════════════════════════
@ui.page('/twins')
def page_twins():
    t = T()
    nav('/twins')
    with ui.element('div').classes('page-wrap').style(f'background:{t["bg"]};color:{t["text"]};'):
        with ui.element('div').classes('content-area'):
            ui.html('<p class="sec-eyebrow">Mystro & Lyric</p>')
            ui.html('<h1 class="sec-h1">Meet the Steals Brothers</h1>')
            ui.html('<p class="sec-lead">Twin brothers. Lifelong partners. One vision divided between words and melody.</p>')

            ui.html('''<div class="pull-quote"><p>"Melvin was the wordsmith — Lyric — and Mervin crafted the melodies on piano — Mystro.
                Together they were complete."</p></div>''')

            # Photos
            with ui.element('div').classes('two-col-eq'):
                with ui.element('div').classes('photo-wrap'):
                    ui.image('/images/twinsOldHouse.webp').style('width:100%;display:block;')
                    ui.html('<p class="photo-caption">Melvin & Mervin on their porch in Aliquippa — the early years</p>')
                with ui.element('div').classes('photo-wrap'):
                    ui.image('/images/MoreCurrentPic.webp').style('width:100%;display:block;')
                    ui.html('<p class="photo-caption">Melvin & Mervin Steals Sr. — still brothers, still writing history</p>')

            gold_hr()

            # Side-by-side bios
            with ui.element('div').classes('two-col-eq'):
                # Melvin
                with ui.element('div'):
                    ui.html(f'''<div style="background:linear-gradient(160deg,rgba(201,168,76,0.1),rgba(201,168,76,0.02));
                        border:1px solid rgba(201,168,76,0.35);border-radius:4px;padding:32px;text-align:center;margin-bottom:16px;">
                        <div style="font-size:3.5rem;line-height:1;margin-bottom:12px;">♪</div>
                        <div style="font-family:'Playfair Display',serif;font-size:1.7rem;font-weight:900;color:#C9A84C;">Melvin Steals Sr.</div>
                        <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-size:1rem;margin-top:6px;opacity:0.7;">
                            Known as <strong style="color:#C9A84C;">"Lyric"</strong>
                        </div>
                        <hr style="border:none;height:1px;background:linear-gradient(90deg,transparent,rgba(201,168,76,0.3),transparent);margin:16px 0;">
                        <div style="font-size:0.9rem;line-height:1.75;">
                            The wordsmith of the duo. Melvin had an extraordinary gift for lyrics that felt lived-in — because they were. Every line came from real life: real love, real faith, real longing.
                        </div>
                    </div>''')
                    for icon, fact in [
                        ("✍️", "Lyricist — 'Could It Be I'm Falling in Love'"),
                        ("❤️", "Inspired by childhood sweetheart Adrena, his wife"),
                        ("🏫", "English teacher & Principal in Aliquippa schools"),
                        ("🙏", "Gospel songwriter — 'With You Jesus'"),
                        ("🏆", "Grammy Award Winner, 2021"),
                        ("👨‍👩‍👧‍👦", "1 son and 2 daughters"),
                    ]:
                        ui.html(f'<div class="fact-chip"><span>{icon}</span><span style="font-size:0.85rem;">{fact}</span></div>')

                # Mervin
                with ui.element('div'):
                    ui.html(f'''<div style="background:linear-gradient(160deg,rgba(42,74,107,0.18),rgba(42,74,107,0.03));
                        border:1px solid rgba(42,74,107,0.45);border-radius:4px;padding:32px;text-align:center;margin-bottom:16px;">
                        <div style="font-size:3.5rem;line-height:1;margin-bottom:12px;">♫</div>
                        <div style="font-family:'Playfair Display',serif;font-size:1.7rem;font-weight:900;color:#C9A84C;">Mervin Steals Sr.</div>
                        <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-size:1rem;margin-top:6px;opacity:0.7;">
                            Known as <strong style="color:#C9A84C;">"Mystro"</strong>
                        </div>
                        <hr style="border:none;height:1px;background:linear-gradient(90deg,transparent,rgba(42,74,107,0.45),transparent);margin:16px 0;">
                        <div style="font-size:0.9rem;line-height:1.75;">
                            The melodic architect of the duo. Mervin composed on piano — the musical foundation that gave Melvin's words somewhere to live. His melodies were immediately memorable, emotional, and undeniably soulful.
                        </div>
                    </div>''')
                    for icon, fact in [
                        ("🎹", "Pianist & melodist — composer of the duo"),
                        ("🎵", "Co-wrote all 100+ Steals Brothers songs"),
                        ("🪚", "Skilled carpenter — craftsman beyond the keys"),
                        ("⚒️", "Free Mason & Shriner — brotherhood & service"),
                        ("🤝", "Business partner of McKinley Jackson (Marvin Gaye's musical director)"),
                        ("📀", "47 songs still played in the world market today"),
                        ("🏆", "Grammy Award Winner, 2021"),
                        ("👨‍👩‍👧‍👦", "4 sons and 1 daughter"),
                    ]:
                        ui.html(f'<div class="fact-chip" style="background:rgba(42,74,107,0.1);border-color:rgba(42,74,107,0.25);"><span>{icon}</span><span style="font-size:0.85rem;">{fact}</span></div>')

            gold_hr()

            ui.html('<h2 class="sec-h2" style="text-align:center;">The Perfect Partnership</h2>')
            ui.html(f'<p style="text-align:center;max-width:700px;margin:0 auto 28px;line-height:1.85;font-size:0.97rem;color:{t["sub"]};">In music, two halves rarely fit as perfectly as words and melody — and rarer still are cases where those two halves are literally born together. Melvin and Mervin were not just brothers; they were each other\'s creative completion.</p>')

            with ui.element('div').style('display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;'):
                for icon, title, desc in [
                    ("🎼", "Born as One", "Twin brothers from Aliquippa, sharing a dream before either had the words for it."),
                    ("🏫", "Cheyney State College", "They enrolled together at America's oldest HBCU, where Eddie Holman opened the door to Philadelphia's music world."),
                    ("🤝", "Gamble & Huff", "The legendary producing duo heard something special and immediately put them to work — two halves greater than the sum of their parts."),
                ]:
                    ui.html(f'''<div class="card" style="text-align:center;padding:28px 20px;">
                        <div style="font-size:2rem;margin-bottom:12px;">{icon}</div>
                        <div class="card-title">{title}</div>
                        <div style="font-size:0.85rem;line-height:1.6;opacity:0.75;">{desc}</div>
                    </div>''')

            footer()


# ══════════════════════════════════════════════════════════════════════════════
# ABOUT MELVIN
# ══════════════════════════════════════════════════════════════════════════════
@ui.page('/melvin')
def page_melvin():
    t = T()
    nav('/melvin')
    with ui.element('div').classes('page-wrap').style(f'background:{t["bg"]};color:{t["text"]};'):
        with ui.element('div').classes('content-area'):
            ui.html('<p class="sec-eyebrow">Biography</p>')
            ui.html('<h1 class="sec-h1">Melvin Steals Sr.</h1>')
            ui.html('<p class="sec-lead">"Lyric" · Wordsmith · Educator · Gospel Songwriter · Grammy Award Winner</p>')

            with ui.element('div').classes('two-col'):
                with ui.element('div'):
                    ui.html('''<div class="pull-quote"><p>"Could It Be I'm Falling in Love was inspired by my childhood sweetheart Adrena, whom I dated as a teenager — and later married."</p></div>''')
                    for heading, body in [
                        ("Early Life in Aliquippa",
                         "Melvin Steals Sr. was born and raised in Aliquippa, Pennsylvania — a Beaver County town on the Ohio River better known for producing NFL Hall of Famers than music legends. Alongside his twin brother Mervin, Melvin grew up with an innate gift for language and storytelling that would one day give The Spinners one of the most beloved songs in American R&B history."),
                        ("Cheyney State & The Philadelphia Door",
                         "After graduating high school in 1964, the twins enrolled at <strong style='color:#C9A84C;'>Cheyney State College</strong>, America's oldest HBCU, just outside Philadelphia. They met Eddie Holman and entered the orbit of Kenny Gamble and Leon Huff — the architects of the Philadelphia Sound. Melvin walked through that door as <em style='color:#C9A84C;'>Lyric</em>: every word of every Steals Brothers composition flowed from his pen. He wrote from life, and the love song that became 'Could It Be I'm Falling in Love' came directly from his romance with <strong style='color:#C9A84C;'>Adrena</strong>, his childhood sweetheart and wife."),
                        ("Educator of Aliquippa",
                         "Even as his songs climbed the charts, Melvin returned to Aliquippa and dedicated himself to education — a career entirely separate from his music. He taught in the local school system, eventually becoming Principal, pouring the same passion for words into his students that he brought to his songwriting. Students who sat in his classroom had no idea their teacher's song was playing on radio stations across the country."),
                        ("From Soul to Spirit",
                         "Guided by deepening faith, Melvin eventually turned his songwriting toward gospel music. His song <strong style='color:#C9A84C;'>'With You Jesus'</strong> represents the full arc of his journey — the man who wrote the anthem for falling in love, now writing about the deepest love of all."),
                    ]:
                        ui.html(f'<h3 class="sec-h3">{heading}</h3><p class="sec-body">{body}</p>')

                # Right column
                with ui.element('div'):
                    with ui.element('div').classes('photo-wrap').style('margin-bottom:20px;'):
                        ui.image('/images/MelvinandAdrena.jpg').style('width:100%;display:block;')
                        ui.html('<p class="photo-caption">Melvin and Adrena Steals with Billy Henderson of The Spinners at the Civic Arena, 1976</p>')
                    for icon, title, sub in [
                        ("🏆", "Grammy Award Winner", "2021 Best Dance Recording"),
                        ("📚", "Educator & Principal", "Aliquippa School System"),
                        ("✍️", "Lyricist", "100+ Recorded Compositions"),
                        ("❤️", "Love Story", "Married childhood sweetheart Adrena — 1 son, 2 daughters"),
                        ("🎓", "Cheyney State College", "America's Oldest HBCU"),
                        ("🙏", "Gospel Songwriter", "'With You Jesus' — man of faith"),
                    ]:
                        ui.html(f'''<div class="card" style="padding:12px 16px;margin-bottom:8px;">
                            <div style="display:flex;align-items:center;gap:12px;">
                                <span style="font-size:1.2rem;">{icon}</span>
                                <div>
                                    <div style="font-weight:700;font-size:0.82rem;">{title}</div>
                                    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-size:0.78rem;color:#9A8A6A;">{sub}</div>
                                </div>
                            </div>
                        </div>''')

            footer()


# ══════════════════════════════════════════════════════════════════════════════
# ABOUT MERVIN
# ══════════════════════════════════════════════════════════════════════════════
@ui.page('/mervin')
def page_mervin():
    t = T()
    nav('/mervin')
    with ui.element('div').classes('page-wrap').style(f'background:{t["bg"]};color:{t["text"]};'):
        with ui.element('div').classes('content-area'):
            ui.html('<p class="sec-eyebrow">Biography</p>')
            ui.html('<h1 class="sec-h1">Mervin Steals Sr.</h1>')
            ui.html('<p class="sec-lead">"Mystro" · Melodist & Pianist · Co-writer · Grammy Award Winner · Craftsman · Free Mason & Shriner</p>')

            with ui.element('div').classes('two-col'):
                with ui.element('div'):
                    ui.html('''<div class="pull-quote"><p>"Mervin crafted the melodies on piano. Without the melody, the words have no home. He gave every song its soul."</p></div>''')
                    for heading, body in [
                        ("The Architect of Sound",
                         "Mervin Steals Sr. was the musical engine of the Steals Brothers. While twin brother Melvin brought the poetry of lived experience to the page, Mervin sat at the piano and found the notes that made those words soar. His melodic instincts were impeccable — the kind of ear that immediately understood what a singer needed, what a room demanded, and what would last for decades. Known in the industry as <em style='color:#C9A84C;'>'Mystro,'</em> his piano compositions were the foundation beneath every Steals Brothers classic."),
                        ("Aliquippa to Philadelphia",
                         "Born February 9, 1946 — the youngest of eight children — Mervin grew up in Aliquippa alongside twin brother Melvin. After graduating high school in 1964 they enrolled at Cheyney State College where their friendship with Eddie Holman opened the door to the Philadelphia music world. There, Mervin's talent caught the attention of Kenny Gamble, Leon Huff, and Thom Bell — the architects of the Philadelphia Sound."),
                        ("McKinley Jackson & The Grammy",
                         "Mervin's business partnership with McKinley Jackson — who served as Marvin Gaye's musical director — proved pivotal. That collaboration ultimately led to co-writing credits on Kaytranada's '10%' featuring Kali Uchis, which won the <strong style='color:#C9A84C;'>2021 Grammy for Best Dance Recording</strong>. Nearly 50 years after 'Could It Be I'm Falling in Love,' Mervin was still at the top."),
                        ("Life Beyond Music",
                         "Like his brother, Mervin built a full life beyond the music industry. A skilled carpenter by trade, he brought the same precision and craftsmanship to his work that he brought to his melodies. He is an active member of the Shriners and Free Masons, serving his community with the same dedication that always defined him personally. He has 4 sons and 1 daughter."),
                    ]:
                        ui.html(f'<h3 class="sec-h3">{heading}</h3><p class="sec-body">{body}</p>')

                # Right column
                with ui.element('div'):
                    with ui.element('div').classes('photo-wrap').style('margin-bottom:20px;'):
                        ui.image('/images/twinsOldHouse.webp').style('width:100%;display:block;')
                        ui.html('<p class="photo-caption">Mervin (left) and Melvin on their porch in Aliquippa — the early years</p>')
                    for icon, title, sub in [
                        ("🏆", "Grammy Award Winner", "2021 Best Dance Recording"),
                        ("🎹", "Pianist & Composer", "'Mystro' — the melodic architect"),
                        ("📀", "47 Songs", "Still played in the world market today"),
                        ("🪚", "Master Carpenter", "Craftsman beyond the keys"),
                        ("⚒️", "Free Mason & Shriner", "Brotherhood, service & philanthropy"),
                        ("🤝", "McKinley Jackson", "Business partner — Marvin Gaye's musical director"),
                        ("👨‍👩‍👧‍👦", "Family Man", "4 sons and 1 daughter"),
                    ]:
                        ui.html(f'''<div class="card" style="padding:12px 16px;margin-bottom:8px;background:rgba(42,74,107,0.08);border-color:rgba(42,74,107,0.3);">
                            <div style="display:flex;align-items:center;gap:12px;">
                                <span style="font-size:1.2rem;">{icon}</span>
                                <div>
                                    <div style="font-weight:700;font-size:0.82rem;">{title}</div>
                                    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-size:0.78rem;color:#9A8A6A;">{sub}</div>
                                </div>
                            </div>
                        </div>''')

            footer()


# ══════════════════════════════════════════════════════════════════════════════
# WITH YOU JESUS
# ══════════════════════════════════════════════════════════════════════════════
@ui.page('/wyj')
def page_wyj():
    t = T()
    nav('/wyj')
    with ui.element('div').classes('page-wrap').style(f'background:{t["bg"]};color:{t["text"]};'):
        with ui.element('div').classes('content-area'):
            ui.html('<p class="sec-eyebrow">New Gospel Single</p>')
            ui.html('<h1 class="sec-h1">With You Jesus</h1>')
            ui.html('<p class="sec-lead">Melvin Steals Sr. · The Philly Mix · A gospel reimagining of a timeless classic</p>')

            with ui.element('div').classes('two-col'):
                # Left — story & video
                with ui.element('div'):
                    ui.html('''<div class="pull-quote"><p>"The man who wrote the anthem for falling in love, now writing about the deepest love of all."</p></div>''')
                    ui.html('<h3 class="sec-h3">The Story Behind the Song</h3>')
                    ui.html(f'<p class="sec-body" style="margin-bottom:16px;">In 1972, Melvin and Mervin Steals wrote "Could It Be I\'m Falling in Love" for The Spinners. The song went to #1 on R&B, hit #4 on the Billboard Hot 100, sold over a million copies, and was played over 4 million times on American radio. Now, over 50 years later, Melvin has transformed that beloved melody into a gospel anthem — <strong style="color:#C9A84C;">With You Jesus</strong>.</p>')
                    ui.html(f'<p class="sec-body" style="margin-bottom:24px;">The Philly Mix honors the original\'s lush Philadelphia soul production while channeling a lifetime of faith and devotion. It is a full-circle moment — from a teenage love letter to Adrena, to a song of spiritual surrender to the Lord.</p>')

                    # Embedded YouTube
                    ui.html('''<div class="video-wrap">
                        <iframe src="https://www.youtube.com/embed/98ajxKlR5Dk"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                            allowfullscreen></iframe>
                    </div>''')

                    gold_hr()

                    # Ministry licensing
                    ui.html('<h3 class="sec-h3">Church & Ministry Licensing</h3>')
                    with ui.element('div').style('display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:14px;margin-top:14px;'):
                        for title, price, desc in [
                            ("Personal",          "$1.29", "Single download for personal listening and devotion."),
                            ("Church / Ministry",  "$25",   "Licensed for worship services & events (up to 200 members)."),
                            ("Large Organization", "$75",   "Broadcast rights, large congregations, conference use."),
                        ]:
                            ui.html(f'''<div class="card" style="text-align:center;padding:24px 16px;">
                                <div style="font-size:0.65rem;letter-spacing:0.2em;text-transform:uppercase;color:#9A8A6A;margin-bottom:6px;">{title}</div>
                                <div style="font-family:'Playfair Display',serif;font-size:2rem;font-weight:900;color:#C9A84C;margin-bottom:8px;">{price}</div>
                                <div style="font-size:0.82rem;line-height:1.55;opacity:0.72;">{desc}</div>
                            </div>''')

                # Right — purchase card
                with ui.element('div'):
                    with ui.element('div').style(f'background:{t["bg3"]};border:1px solid #C9A84C;border-radius:6px;padding:32px;text-align:center;box-shadow:0 8px 40px rgba(201,168,76,0.1);margin-bottom:20px;'):
                        ui.html('<div style="font-size:0.68rem;letter-spacing:0.25em;text-transform:uppercase;color:#9A8A6A;margin-bottom:8px;">Digital Download</div>')
                        ui.html('<div style="font-family:\'Playfair Display\',serif;font-size:1.8rem;font-weight:900;color:#C9A84C;margin-bottom:4px;">With You Jesus</div>')
                        ui.html('<div style="font-family:\'Cormorant Garamond\',serif;font-style:italic;font-size:0.95rem;opacity:0.6;margin-bottom:16px;">Melvin Steals Sr. · of The Steals Brothers</div>')
                        ui.html('<div style="font-family:\'Playfair Display\',serif;font-size:2.8rem;font-weight:900;color:#C9A84C;">$1.29</div>')
                        ui.html('<div style="font-size:0.78rem;color:#9A8A6A;margin-bottom:20px;">MP3 · High Quality · Instant Download</div>')

                        def on_purchase():
                            ui.notify('Thank you! Your download link will arrive by email. God bless you! 🙏', type='positive')
                        ui.button('🎵 Purchase & Download — $1.29', on_click=on_purchase).classes('btn-gold').style('width:100%;font-size:0.85rem;padding:14px;border-radius:3px;')

                    ui.html('<div style="text-align:center;margin:16px 0 8px;font-size:0.68rem;letter-spacing:0.2em;text-transform:uppercase;color:#9A8A6A;">Also Available On</div>')
                    for icon, name, url in [
                        ("🎵", "Apple Music",   "https://music.apple.com/us/album/with-you-jesus-philly-mix-single/1874032863"),
                        ("🟢", "Spotify",       "https://open.spotify.com/album/1XoeZnbaHFVmTAqooppyIG"),
                        ("▶️", "YouTube",        "https://youtu.be/98ajxKlR5Dk?feature=shared"),
                    ]:
                        ui.html(f'''<a class="platform-link" href="{url}" target="_blank">
                            <span style="font-size:1.1rem;">{icon}</span>
                            <span class="pl-name">{name}</span>
                            <span class="pl-action">Stream →</span>
                        </a>''')

                    ui.html('''<div class="card" style="margin-top:16px;">
                        <div style="font-size:0.72rem;letter-spacing:0.15em;text-transform:uppercase;color:#C9A84C;margin-bottom:8px;">What You Get</div>
                        <div style="font-size:0.85rem;line-height:1.8;">
                            ✓ High-quality MP3 (320kbps)<br>
                            ✓ Instant digital delivery<br>
                            ✓ Personal use license<br>
                            ✓ Direct support to the artist
                        </div>
                    </div>''')

            footer()


# ══════════════════════════════════════════════════════════════════════════════
# LEGACY & DISCOGRAPHY
# ══════════════════════════════════════════════════════════════════════════════
@ui.page('/legacy')
def page_legacy():
    t = T()
    nav('/legacy')
    with ui.element('div').classes('page-wrap').style(f'background:{t["bg"]};color:{t["text"]};'):
        with ui.element('div').classes('content-area'):
            ui.html('<p class="sec-eyebrow">50+ Years of Music</p>')
            ui.html('<h1 class="sec-h1">Legacy & Discography</h1>')
            ui.html('<p class="sec-lead">From the streets of Aliquippa to the Grammys — a timeline of excellence.</p>')

            # Timeline
            gold_hr()
            ui.html('<h2 class="sec-h2">Career Timeline</h2>')
            timeline = [
                ("1946", "Born in Aliquippa, PA", "Melvin Harold and Mervin Howard Steals are born on February 9 — the youngest of eight children. Their father, a steelworker, passed away in 1951 at age 48."),
                ("1964", "High School Graduation", "The twins graduate and enroll at Cheyney State College, America's oldest HBCU, just outside Philadelphia."),
                ("1965", "Meeting Eddie Holman", "At Cheyney State they meet singer Eddie Holman — a friendship that opens the door to Philadelphia's storied music world."),
                ("1970", "Gamble & Huff", "Kenny Gamble and Leon Huff — architects of Philadelphia Soul — hear the brothers' talent and begin working with them."),
                ("1972", "Thom Bell Hears Seven Songs", "On a Pittsburgh scouting trip, Thom Bell hears seven Steals Brothers songs and agrees to find artists to record them. One is destined for history."),
                ("Dec 1972", '"Could It Be I\'m Falling in Love"', 'Melvin (Lyric) writes the words; Mervin (Mystro) composes the melody. Thom Bell produces it for The Spinners at Sigma Sound Studios with MFSB. A gold record is born.'),
                ("1973", "#1 R&B · #4 Billboard · Gold", "The song peaks at #1 R&B, #4 Billboard Hot 100, and sells over a million copies. The Steals Brothers are legends."),
                ("1974", '"Honey Bee" — Gloria Gaynor', "Their composition becomes a successful single for future disco queen Gloria Gaynor, showing the breadth of the brothers' musical range."),
                ("70s–80s", "Prolific Catalog", "The twins write 100+ songs for Blue Magic, Harold Melvin & The Blue Notes, The Trammps, O.C. Smith, The Impressions, Eddie Kendricks, and many more."),
                ("80s–90s", "Educator, Craftsman & Community", "Melvin teaches and becomes Principal in Aliquippa. Mervin deepens his business partnership with McKinley Jackson while practicing carpentry."),
                ("2021", "Grammy Award — Best Dance Recording", 'Melvin, Mervin, and McKinley Jackson receive Grammy Awards as co-writers of "10%" by Kaytranada feat. Kali Uchis. Nearly 50 years in — still at the top.'),
                ("2020s", '"With You Jesus" — Melvin Steals Sr.', "Melvin releases his gospel single, channeling a lifetime of faith, music, and brotherhood into a song of spiritual devotion."),
            ]
            with ui.element('div').style('margin-top:28px;'):
                for year, title, desc in timeline:
                    ui.html(f'''<div class="timeline-item">
                        <div class="tl-year">{year}</div>
                        <div class="tl-dot"></div>
                        <div class="tl-content"><h4>{title}</h4><p>{desc}</p></div>
                    </div>''')

            gold_hr()

            # Original sheet music
            ui.html('<p class="sec-eyebrow" style="text-align:center;">Original Sheet Music</p>')
            ui.html('<h2 class="sec-h2" style="text-align:center;">"Could It Be I\'m Falling in Love"</h2>')
            ui.html('<p style="text-align:center;font-family:\'Cormorant Garamond\',serif;font-style:italic;opacity:0.65;margin-bottom:20px;">Words and Music by Melvin Steals and Mervin Steals</p>')
            with ui.element('div').style('max-width:700px;margin:0 auto;'):
                with ui.element('div').classes('photo-wrap'):
                    ui.image('/images/Notes.jpg').style('width:100%;display:block;')
                    ui.html('<p class="photo-caption">Original sheet music — words by Melvin (Lyric), music by Mervin (Mystro)</p>')

            gold_hr()

            # Notable compositions
            ui.html('<h2 class="sec-h2">Notable Compositions</h2>')
            songs = [
                ("Could It Be I'm Falling in Love", "The Spinners",              "1972", "#1 R&B · #4 Billboard · Gold"),
                ("Honey Bee",                        "Gloria Gaynor",             "1974", "Top 40 Hit"),
                ("Trusting Heart",                   "The Trammps",               "1970s","Philly Soul Staple"),
                ("Go For What You Know",             "Archie Bell & The Drells",  "Early 70s", "B-Side Hit"),
                ("I'm Not Strong Enough",            "The Four Perfections",      "1972", "UK Northern Soul Classic"),
                ("10% (co-write)",                   "Kaytranada ft. Kali Uchis", "2020", "Grammy Award — Best Dance Recording 2021"),
                ("Back Home (sample)",               "A$AP Rocky",                "2010s","Hip-Hop Sample"),
                ("Treat 'Em Right (sample)",         "Mary J. Blige",             "1990s","R&B/Hip-Hop Sample"),
                ("Gotta Find My Way Back Home",      "The Jaggerz",               "1970s","Local Aliquippa Favorite"),
                ("With You Jesus",                   "Melvin Steals Sr.",         "2020s","Gospel Single — Available Now"),
            ]
            with ui.element('div').style('margin-top:16px;'):
                for song, artist, year, notes in songs:
                    ui.html(f'''<div class="song-row">
                        <span class="song-title">{song}</span>
                        <span class="song-year">{year}</span>
                        <span class="song-artist">{artist}</span>
                        <span class="song-note">{notes}</span>
                    </div>''')

            footer()


# ══════════════════════════════════════════════════════════════════════════════
# CONTACT
# ══════════════════════════════════════════════════════════════════════════════
@ui.page('/contact')
def page_contact():
    t = T()
    nav('/contact')
    with ui.element('div').classes('page-wrap').style(f'background:{t["bg"]};color:{t["text"]};'):
        with ui.element('div').classes('content-area'):
            ui.html('<p class="sec-eyebrow">Get in Touch</p>')
            ui.html('<h1 class="sec-h1">Contact & Booking</h1>')
            ui.html('<p class="sec-lead">For bookings, licensing, media inquiries, and ministry partnerships</p>')

            with ui.element('div').classes('contact-grid'):
                # Left — form
                with ui.element('div'):
                    ui.html('<h3 class="sec-h3">Send a Message</h3>')
                    name_in    = ui.input('Full Name *', placeholder='Your name').style('width:100%;margin-bottom:12px;')
                    email_in   = ui.input('Email Address *', placeholder='your@email.com').style('width:100%;margin-bottom:12px;')
                    recip_sel  = ui.select(
                        label='Who are you contacting? *',
                        options=['Melvin Steals Sr.', 'Mervin Steals Sr.', 'Both / The Steals Brothers']
                    ).style('width:100%;margin-bottom:12px;')
                    subj_sel   = ui.select(
                        label='Subject *',
                        options=['Booking / Live Performance', 'Song Licensing', 'Media / Press Inquiry',
                                 'Ministry Partnership', 'Purchase Support', 'General Message']
                    ).style('width:100%;margin-bottom:12px;')
                    msg_in     = ui.textarea('Your Message *', placeholder='Write your message here...').style('width:100%;margin-bottom:16px;')

                    def send_msg():
                        if name_in.value and email_in.value and msg_in.value and recip_sel.value and subj_sel.value:
                            ui.notify(f'✓ Message sent to {recip_sel.value}! We\'ll be in touch within 2–3 business days. God bless you! 🙏', type='positive')
                        else:
                            ui.notify('Please fill in all required fields before sending.', type='warning')
                    ui.button('Send Message →', on_click=send_msg).classes('btn-gold').style('font-size:0.85rem;padding:13px 32px;border-radius:3px;')

                # Right — info cards
                with ui.element('div'):
                    with ui.element('div').classes('card').style('margin-bottom:16px;'):
                        ui.html('<div class="card-title" style="font-size:1.1rem;">Contact Details</div>')
                        for icon, label, val in [
                            ("📍", "Location",  "Aliquippa, Pennsylvania"),
                            ("🎤", "Bookings",  "Available for speaking engagements, gospel concerts & ministry events"),
                            ("📜", "Licensing", "Song licensing for churches, media & commercial use"),
                            ("📰", "Press",     "Media kits and interviews available on request"),
                        ]:
                            ui.html(f'''<div style="display:flex;gap:14px;margin-top:14px;align-items:flex-start;">
                                <span style="font-size:1.1rem;padding-top:2px;">{icon}</span>
                                <div>
                                    <div style="font-size:0.65rem;letter-spacing:0.16em;text-transform:uppercase;color:#9A8A6A;">{label}</div>
                                    <div style="font-size:0.87rem;margin-top:3px;line-height:1.5;opacity:0.85;">{val}</div>
                                </div>
                            </div>''')

                    with ui.element('div').classes('card').style('text-align:center;'):
                        ui.html('<div class="card-title">The Steals Brothers — Speaking & Ministry</div>')
                        ui.html(f'<p style="font-size:0.85rem;line-height:1.65;opacity:0.75;margin:10px 0 14px;">Together and individually, Melvin and Mervin are available to share their remarkable story — two twins from a steel town who wrote the soundtrack to a generation, and never forgot where they came from.</p>')
                        ui.html('<div style="font-family:\'Cormorant Garamond\',serif;font-style:italic;color:#C9A84C;font-size:0.9rem;">"Born together. Still singing together."</div>')

            footer()


# ── Run ───────────────────────────────────────────────────────────────────────
ui.run(title='The Steals Brothers', host='127.0.0.1', port=8080, favicon='🎵')
