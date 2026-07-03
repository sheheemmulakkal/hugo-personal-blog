+++
date = '2026-02-24T18:50:41+05:30'
title = 'Clipboard Manager'
description = 'A Win+V style clipboard history popup for Ubuntu. Text and screenshots, built with Rust and GTK4.'
+++

<small><em>⚠️ AI-generated write-up, to be revised later. Project built with AI (Claude) — I don't know Rust. A personal experimental tool, not a serious project.</em></small>

One thing I missed after moving from Windows to Ubuntu was **Win+V** — the built-in clipboard history popup. Ubuntu has nothing like it out of the box, so I built one.

Press **Ctrl+Alt+C** anywhere and a popup shows everything you've recently copied — click an item and it's pasted instantly. It handles both **text and screenshots**.

Some things it does:

- **Paste on click**, with a separate button for pasting into terminals (Ctrl+Shift+V)
- **Pin items** so they're never evicted from history
- **Label and color-code** items (right-click a row) so important ones stand out
- **Search** through history from the popup
- **Image support** — copied screenshots show as thumbnails, deduplicated by hash, stored on disk and never loaded into RAM until pasted
- Works on both **X11 and Wayland** (via the RemoteDesktop and GlobalShortcuts portals)

Built with Rust and GTK4. Installable with a one-line script or a `.deb` from releases — no Rust toolchain needed.

**Source:** [github.com/sheheemmulakkal/clipboard-manager](https://github.com/sheheemmulakkal/clipboard-manager)
