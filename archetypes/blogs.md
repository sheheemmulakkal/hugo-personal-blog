+++
date = '{{ .Date }}'
title = '{{ replace .File.ContentBaseName "-" " " | title }}'
# ~150-160 characters. Shown under the link in Google and in link previews.
description = ''
# Optional: search phrases for this post.
keywords = []
# Optional: 1200x630 preview image in static/. Leave it out to use /profile-og.jpg.
# images = ['/{{ .File.ContentBaseName }}-og.png']
tags = []
+++

