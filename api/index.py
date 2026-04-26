from nicegui import ui, app
import os

# ── Serve uploaded images ──────────────────────────────────────────────────────
app.add_static_files('/images', os.path.dirname(os.path.abspath(__file__)))

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
theme_mode = {'dark': True}

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

.site-footer {
    border-top: 1px solid rgba(201,168,76,0.2); padding-top: 24px; margin-top: 60px;
    text-align: center;
}
.site-footer p {
    font-family: 'Cormorant Garamond', serif; font-style: italic;
    font-size: 0.82rem; color: #9A8A6A;
}

.two-col { display: grid; grid-template-columns: 2fr 1fr; gap: 40px; align-items: start; }
.two-col-eq { display: grid; grid-template-columns: 1fr 1fr; gap: 32px; align-items: start; }
@media (max-width: 680px) { .two-col, .two-col-eq { grid-template-columns: 1fr; } }

.photo-wrap { border-radius: 6px; overflow: hidden; border: 1px solid rgba(201,168,76,0.25); }
.photo-wrap img { width: 100%; height: auto; display: block; }
.photo-caption {
    font-family: 'Cormorant Garamond', serif; font-style: italic;
    font-size: 0.78rem; color: #9A8A6A; padding: 8px 10px; text-align: center;
}

@media (max-width: 680px) {
    .topnav { padding: 0 16px; }
    .content-area { padding: 72px 18px 40px; }
    .hero { padding: 72px 18px 40px; }
}
</style>
'''

theme_mode = {'dark': True}

def T():
    return DARK if theme_mode['dark'] else LIGHT

def nav(current: str):
    t = T()
    ui.add_head_html(FONTS + BASE_CSS)
    ui.query('body').style(f'background:{t["bg"]};color:{t["text"]};')
    ui.query('.nicegui-content').style('padding:0 !important;')
    with ui.element('nav').classes('topnav').style(f'background:{t["navbar"]};'):
        ui.link('THE STEALS BROTHERS', '/').classes('nav-brand')
        with ui.row().classes('nav-links items-center gap-1'):
            for label, path in [
                ('🏠 Home',           '/'),
                ('👥 Meet the Twins', '/twins'),
                ('👤 Melvin',         '/melvin'),
                ('👤 Mervin',         '/mervin'),
                ('🎵 With You Jesus', '/wyj'),
                ('🎼 Legacy',         '/legacy'),
                ('✉️ Contact',        '/contact'),
            ]:
                active = 'nav-link-active' if current == path else ''
                ui.link(label, path).classes(f'nav-link {active}').style(f'color:{t["text"]};')
            def toggle():
                theme_mode['dark'] = not theme_mode['dark']
                ui.navigate.reload()
            icon = '☀️' if theme_mode['dark'] else '🌙'
            ui.button(icon, on_click=toggle).classes('theme-btn').props('flat dense')

def footer():
    ui.html('<div class="site-footer"><p>© 2025 Melvin Steals Sr. & Mervin Steals Sr. · The Steals Brothers · All Rights Reserved · Aliquippa, Pennsylvania</p></div>')

def gold_hr():
    ui.html('<hr class="gold-hr">')

# HOME PAGE - minimal version
@ui.page('/')
def page_home():
    t = T()
    nav('/')
    with ui.element('div').classes('page-wrap').style(f'background:{t["bg"]};color:{t["text"]};'):
        with ui.element('div').classes('hero'):
            with ui.element('div').classes('hero-inner'):
                ui.html('<p class="hero-eyebrow">Mystro & Lyric · Aliquippa, Pennsylvania</p>')
                ui.html('<h1 class="hero-title">The Steals<br>Brothers</h1>')
                ui.html('<p class="hero-sub">Melvin Harold & Mervin Howard Steals Sr.<br>Twin Brothers · Grammy Winners · Musical Legends</p>')
                ui.html('''
                <div class="hero-btns">
                    <a class="btn-gold" href="/wyj">🎵 With You Jesus</a>
                    <a class="btn-outline" href="/twins">Meet the Twins</a>
                </div>''')

        with ui.element('div').classes('content-area').style('padding-top:0;'):
            ui.html('<div class="stat-grid">'
                    '<div class="stat-box"><span class="stat-num">100+</span><span class="stat-lbl">Songs Written</span></div>'
                    '<div class="stat-box"><span class="stat-num">4M+</span><span class="stat-lbl">Radio Spins</span></div>'
                    '<div class="stat-box"><span class="stat-num">1</span><span class="stat-lbl">Grammy Win</span></div>'
                    '<div class="stat-box"><span class="stat-num">50+</span><span class="stat-lbl">Years Together</span></div>'
                    '</div>')
            gold_hr()
            ui.html('''
            <div style="background: linear-gradient(135deg, rgba(201,168,76,0.12), rgba(201,168,76,0.04));
                        border: 1px solid #C9A84C; border-radius: 6px; padding: 36px;
                        text-align: center;">
                <h2 class="sec-h1" style="margin:0 0 8px;">With You Jesus</h2>
                <p class="sec-lead" style="margin-bottom:20px;">A gospel reimagining of "Could It Be I'm Falling in Love" · Available Now</p>
                <div class="hero-btns">
                    <a class="btn-gold" href="https://open.spotify.com/album/1XoeZnbaHFVmTAqooppyIG" target="_blank">🟢 Spotify</a>
                    <a class="btn-gold" href="https://music.apple.com/us/album/with-you-jesus-philly-mix-single/1874032863" target="_blank">🎵 Apple Music</a>
                </div>
            </div>
            ''')
            footer()

# SIMPLE PAGES
@ui.page('/twins')
def page_twins():
    t = T()
    nav('/twins')
    with ui.element('div').classes('page-wrap').style(f'background:{t["bg"]};color:{t["text"]};'):
        with ui.element('div').classes('content-area'):
            ui.html('<p class="sec-eyebrow">Mystro & Lyric</p>')
            ui.html('<h1 class="sec-h1">Meet the Steals Brothers</h1>')
            ui.html('<p class="sec-lead">Twin brothers born February 9, 1946. One vision divided between words (Melvin/Lyric) and melody (Mervin/Mystro).</p>')
            ui.html('''<div class="pull-quote"><p>"Melvin was the wordsmith and Mervin crafted the melodies. Together they were complete."</p></div>''')
            ui.html('<h2 class="sec-h2">Melvin Steals Sr. — "Lyric"</h2>')
            ui.html('<p class="sec-body">The lyricist of the duo. Inspired his high school sweetheart Adrena to write "Could It Be I'm Falling in Love." Later became an English teacher and Principal in Aliquippa schools. 1 son, 2 daughters.</p>')
            ui.html('<h2 class="sec-h2">Mervin Steals Sr. — "Mystro"</h2>')
            ui.html('<p class="sec-body">The melodist and pianist. Composed the foundation for every Steals Brothers classic. Also a skilled carpenter and active member of the Freemasons and Shriners. 4 sons, 1 daughter.</p>')
            footer()

@ui.page('/melvin')
def page_melvin():
    t = T()
    nav('/melvin')
    with ui.element('div').classes('page-wrap').style(f'background:{t["bg"]};color:{t["text"]};'):
        with ui.element('div').classes('content-area'):
            ui.html('<h1 class="sec-h1">Melvin Steals Sr.</h1>')
            ui.html('<p class="sec-lead">"Lyric" · Wordsmith · Educator · Gospel Songwriter · Grammy Award Winner</p>')
            ui.html('<h2 class="sec-h2">His Story</h2>')
            ui.html('<p class="sec-body">Born in Aliquippa, Pennsylvania, Melvin grew up with an extraordinary gift for lyrics. He enrolled at Cheyney State College (America\'s oldest HBCU) where he met Eddie Holman and entered the Philadelphia music world.</p>')
            ui.html('<p class="sec-body">His love song to childhood sweetheart Adrena became "Could It Be I'm Falling in Love" — a #1 R&B hit for The Spinners (1973) that sold over 1 million copies.</p>')
            ui.html('<p class="sec-body">Even as his songs climbed the charts, Melvin returned to Aliquippa to teach English and eventually became Principal — a career separate from his music that shaped young minds for decades.</p>')
            ui.html('<p class="sec-body">In 2021, he received a Grammy Award (along with Mervin and McKinley Jackson) as co-writer of "10%" by Kaytranada featuring Kali Uchis.</p>')
            ui.html('<p class="sec-body">His latest project, "With You Jesus," represents his spiritual journey — the man who wrote about falling in love now writing about the deepest love of all.</p>')
            footer()

@ui.page('/mervin')
def page_mervin():
    t = T()
    nav('/mervin')
    with ui.element('div').classes('page-wrap').style(f'background:{t["bg"]};color:{t["text"]};'):
        with ui.element('div').classes('content-area'):
            ui.html('<h1 class="sec-h1">Mervin Steals Sr.</h1>')
            ui.html('<p class="sec-lead">"Mystro" · Melodist & Pianist · Co-writer · Grammy Award Winner</p>')
            ui.html('<h2 class="sec-h2">His Story</h2>')
            ui.html('<p class="sec-body">The musical architect of the Steals Brothers. While Melvin brought poetry to the page, Mervin sat at the piano and found the notes that made those words soar. His melodic instincts were impeccable.</p>')
            ui.html('<p class="sec-body">Known in the industry as "Mystro," his compositions were the foundation beneath every classic. From "Could It Be I\'m Falling in Love" to "Honey Bee," Mervin\'s melodies were immediately memorable and undeniably soulful.</p>')
            ui.html('<p class="sec-body">Beyond music, Mervin worked as a skilled carpenter and became an active member of the Shriners and Free Masons, serving his community with the same dedication that defined him.</p>')
            ui.html('<p class="sec-body">In 2021, he received a Grammy Award as co-writer of "10%" by Kaytranada featuring Kali Uchis — proof that nearly 50 years after their first hit, the Steals Brothers were still at the top.</p>')
            ui.html('<p class="sec-body">Mervin has 4 sons and 1 daughter, and 47 of his songs continue to be played worldwide.</p>')
            footer()

@ui.page('/wyj')
def page_wyj():
    t = T()
    nav('/wyj')
    with ui.element('div').classes('page-wrap').style(f'background:{t["bg"]};color:{t["text"]};'):
        with ui.element('div').classes('content-area'):
            ui.html('<h1 class="sec-h1">With You Jesus</h1>')
            ui.html('<p class="sec-lead">A Gospel Reimagining · Melvin Steals Sr. · The Philly Mix</p>')
            ui.html('<h2 class="sec-h2">The Song</h2>')
            ui.html('<p class="sec-body">In 1972, Melvin and Mervin wrote "Could It Be I\'m Falling in Love" for The Spinners. Over 50 years later, Melvin has transformed that beloved melody into a gospel anthem.</p>')
            ui.html('<p class="sec-body">The Philly Mix honors the original\'s lush Philadelphia soul production while channeling a lifetime of faith and devotion. It is a full-circle moment — from a teenage love letter to Adrena, to a song of spiritual surrender.</p>')
            ui.html('<div class="hero-btns" style="margin:30px 0;"><a class="btn-gold" href="https://youtu.be/98ajxKlR5Dk" target="_blank">▶ Watch on YouTube</a></div>')
            ui.html('<h2 class="sec-h2">Streaming & Download</h2>')
            ui.html('<p class="sec-body"><strong>Spotify:</strong> <a href="https://open.spotify.com/album/1XoeZnbaHFVmTAqooppyIG" target="_blank">Listen Now</a></p>')
            ui.html('<p class="sec-body"><strong>Apple Music:</strong> <a href="https://music.apple.com/us/album/with-you-jesus-philly-mix-single/1874032863" target="_blank">Listen Now</a></p>')
            ui.html('<p class="sec-body"><strong>YouTube:</strong> <a href="https://youtu.be/98ajxKlR5Dk" target="_blank">Watch Video</a></p>')
            footer()

@ui.page('/legacy')
def page_legacy():
    t = T()
    nav('/legacy')
    with ui.element('div').classes('page-wrap').style(f'background:{t["bg"]};color:{t["text"]};'):
        with ui.element('div').classes('content-area'):
            ui.html('<h1 class="sec-h1">Legacy & Discography</h1>')
            ui.html('<p class="sec-lead">50+ Years of Musical Excellence</p>')
            ui.html('<h2 class="sec-h2">Iconic Songs</h2>')
            songs = [
                ('Could It Be I\'m Falling in Love', 'The Spinners', '1973', '#1 R&B, #4 Billboard, Gold Certified'),
                ('Honey Bee', 'Gloria Gaynor', '1974', 'Top 40 Hit'),
                ('Trusting Heart', 'The Trammps', '1970s', 'Philly Soul Classic'),
                ('Go For What You Know', 'Archie Bell & The Drells', 'Early 70s', 'B-Side Hit'),
                ('10% (co-write)', 'Kaytranada ft. Kali Uchis', '2020', '2021 Grammy Award - Best Dance Recording'),
                ('With You Jesus', 'Melvin Steals Sr.', '2025', 'Gospel Single'),
            ]
            for song, artist, year, notes in songs:
                ui.html(f'<p class="sec-body"><strong>{song}</strong> by {artist} ({year}) — {notes}</p>')
            ui.html('<h2 class="sec-h2">Facts</h2>')
            ui.html('<p class="sec-body">• 100+ songs written and recorded</p>')
            ui.html('<p class="sec-body">• 4 million+ radio spins for "Could It Be I\'m Falling in Love"</p>')
            ui.html('<p class="sec-body">• 47 songs still played worldwide today</p>')
            ui.html('<p class="sec-body">• 1 Grammy Award (2021) · 2 Grammy Nominations</p>')
            ui.html('<p class="sec-body">• Sampled by A$AP Rocky, Mary J. Blige, and many modern artists</p>')
            footer()

@ui.page('/contact')
def page_contact():
    t = T()
    nav('/contact')
    with ui.element('div').classes('page-wrap').style(f'background:{t["bg"]};color:{t["text"]};'):
        with ui.element('div').classes('content-area'):
            ui.html('<h1 class="sec-h1">Contact & Booking</h1>')
            ui.html('<p class="sec-lead">For bookings, licensing, and inquiries</p>')
            ui.html('<h2 class="sec-h2">Get in Touch</h2>')
            name_in = ui.input('Name *').style('width:100%;margin-bottom:12px;')
            email_in = ui.input('Email *').style('width:100%;margin-bottom:12px;')
            msg_in = ui.textarea('Message *').style('width:100%;margin-bottom:12px;')
            def send():
                if name_in.value and email_in.value and msg_in.value:
                    ui.notify('Message received! We\'ll be in touch soon. 🎵', type='positive')
                else:
                    ui.notify('Please fill in all fields', type='warning')
            ui.button('Send Message', on_click=send).classes('btn-gold')
            ui.html('<h2 class="sec-h2" style="margin-top:40px;">Contact Information</h2>')
            ui.html('<p class="sec-body"><strong>📍 Location:</strong> Aliquippa, Pennsylvania</p>')
            ui.html('<p class="sec-body"><strong>🎤 Bookings:</strong> Available for speaking engagements and gospel concerts</p>')
            ui.html('<p class="sec-body"><strong>📜 Licensing:</strong> Song licensing for churches, media, and commercial use</p>')
            footer()

app.native.window_args['resizable'] = True
