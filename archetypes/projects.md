+++
date = '{{ .Date }}'
title = '{{ replace .File.ContentBaseName "-" " " | title }}'
# Optional: title shown in Google results and the browser tab. Falls back to "Title - Muhammed Sheheem".
seoTitle = '{{ replace .File.ContentBaseName "-" " " | title }} – Short phrase people search for'
# ~150-160 characters. Shown under the link in Google and in link previews.
description = ''
# Optional: search phrases, e.g. 'break reminder linux', 'xyz alternative'.
keywords = []
# 1200x630 preview image in static/ (make one with scripts/og-image.py).
# Leave it out to use the site-wide /profile-og.jpg.
images = ['/{{ .File.ContentBaseName }}-og.png']
tags = []
+++

What problem it solves and why you built it.

**Source:** [github.com/sheheemmulakkal/{{ .File.ContentBaseName }}](https://github.com/sheheemmulakkal/{{ .File.ContentBaseName }})
