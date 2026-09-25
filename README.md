# sheheem.in

Personal site and blog, built with [Hugo](https://gohugo.io/) and the
[hugo-ink](themes/hugo-ink) theme. Pushing to `master` builds and deploys it
to GitHub Pages ([.github/workflows/deploy.yml](.github/workflows/deploy.yml)).

## Run locally

```bash
hugo server        # http://localhost:1313, reloads on save
```

`public/` is build output. Don't edit it by hand; the deploy job regenerates it
with `hugo --minify`.

## Layout

| Path | What's in it |
| --- | --- |
| `content/blogs/` | Blog posts |
| `content/projects/` | Project write-ups |
| `content/about/` | About page |
| `content/_index.md` | Homepage text and its SEO fields |
| `static/` | Images, video, CSS, served from `/` (`static/foo.png` → `/foo.png`) |
| `archetypes/` | Templates used by `hugo new` |
| `layouts/partials/header.html` | Override of the theme's `<head>` (SEO tags) |
| `scripts/og-image.py` | Generates link-preview images |

## New blog post

```bash
hugo new content blogs/my-post-title.md
```

This creates the file from [archetypes/blogs.md](archetypes/blogs.md). Fill in
`description`, add `tags`, write the post below the `+++` block. The file name
becomes the URL: `/blogs/my-post-title/`.

## New project

```bash
hugo new content projects/my-project.md
```

This creates the file from [archetypes/projects.md](archetypes/projects.md),
with all the SEO fields ready to fill in:

1. Write the `description` and `seoTitle` (see [SEO fields](#seo-fields)).
2. Make the preview image (see below) and save it as `static/my-project-og.png`,
   or delete the `images` line to use the default card.
3. Keep a `github.com/<user>/<repo>` link in the post. The first one found is
   used as the project's source link in the structured data.

### Preview image

Link previews (WhatsApp, Slack, LinkedIn, X, Discord) use a 1200×630 image.
Generate one with:

```bash
python3 scripts/og-image.py --title "My Project" \
  --line "What it does in a few words" --line "for Linux (Ubuntu)" \
  --tags "Rust · GTK4" \
  --art path/to/icon.png \
  --out static/my-project-og.png
```

- `--shape rounded` for a screenshot, `--shape circle` for a photo, default
  `none` for a transparent icon.
- `--title "Clipboard\nManager"` splits a long title over two lines.
- `--top` / `--bottom` take hex colours for the background gradient.
- Needs Pillow: `python3 -m pip install pillow`.

Open the image and check that the text doesn't run into the artwork.

## SEO fields

All optional, set in a page's front matter. The `<head>` template picks them up
automatically. There's nothing to change in HTML.

| Field | Used for | If missing |
| --- | --- | --- |
| `description` | Snippet under the link in Google, link-preview text | No meta description; Google picks its own snippet |
| `seoTitle` | `<title>` in Google results and the browser tab | `Title - Muhammed Sheheem` |
| `keywords` | `<meta name="keywords">` (Bing and others; Google ignores it) | Tag left out |
| `images` | Link-preview thumbnail (`og:image`, `twitter:image`) | `/profile-og.jpg` (set in `hugo.toml`) |

Tips:

- Keep `description` around 150–160 characters and use the words people would
  actually search for ("break reminder for Ubuntu", not "wellness daemon").
- Use those same phrases in the post body too. That matters more than the tags.
- Project pages also get `SoftwareApplication` structured data (name,
  description, image, free, Linux, source repo).

After deploying, check a page's preview with
[opengraph.xyz](https://www.opengraph.xyz/) or LinkedIn's
[Post Inspector](https://www.linkedin.com/post-inspector/). For Google, submit
`https://sheheem.in/sitemap.xml` in [Search Console](https://search.google.com/search-console)
and request indexing for new pages.
