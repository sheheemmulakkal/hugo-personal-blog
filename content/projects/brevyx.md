+++
date = '2026-03-03T10:18:06+05:30'
title = 'Brevyx'
description = 'A Linux wellness daemon — full-screen GTK4 reminders for eye rest, hydration, movement and breaks.'
+++

<small><em>⚠️ AI-generated write-up, to be revised later. Project built with AI (Claude) — I don't know Rust. A personal experimental tool, not a serious project.</em></small>

I spend long hours at the screen and wanted something that would *force* me to look away — like [LookAway](https://www.lookaway.app/) on macOS, but for Linux. Nothing quite like it existed, so I built **Brevyx**.

It runs silently as a systemd user service and shows **full-screen animated overlay reminders** at configurable intervals:

- **20-20-20 rule** — an eye-rest overlay every 20 minutes, with an animated blinking/breathing eye
- **Hydration, movement and break** reminders, each on its own independent schedule
- **Skip button** with a configurable delay before it appears — or disable it entirely for no-skip mode
- **System tray icon** to pause, resume or quit
- **Hot-reload config** — edit `~/.config/brevyx/config.toml` and changes apply within seconds, no restart

Built with Rust and GTK4, installable with a one-line script or a `.deb` — no Rust toolchain needed.

**Source:** [github.com/sheheemmulakkal/brevyx](https://github.com/sheheemmulakkal/brevyx)
