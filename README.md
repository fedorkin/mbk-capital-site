# MBK Capital — corporate website

Static HTML site for MBK Capital, built from the MBK Capital Brand Guidelines and the
Brand Book Creative Brief. No framework and no runtime dependencies: upload the folder to
any static host (S3/CloudFront, Netlify, Cloudflare Pages, GitHub Pages, nginx) and it works.

## How to edit copy

The site is English only. All copy lives in `tools/build.py` (the `SERVICES`, `MARKETS`,
`PRICING_TABLES` lists and the `build_*` functions). To change text, edit the script and rebuild:

```bash
python3 tools/build.py
```

The script rewrites every HTML page plus `sitemap.xml` and `robots.txt`. Do not edit the
generated HTML by hand; the next build would overwrite it. `DRAFT = True` at the top of the
script adds the `noindex` tag to every page; set it to `False` for launch.

## Structure

```
index.html            Home
tools/build.py        Page generator with all copy
about.html            About: purpose, mission and vision, values, personality
services.html         Six service areas with anchors (#brokerage, #advice, #portfolio, #research, #risk, #family-office)
markets.html          Asset classes as tabs (#stocks, #currencies, #futures, #options, #bonds, #structured-notes) with venue tables
pricing.html          Commission schedule, account and custody fees, currency conversion, exclusions
clients.html          Audiences and the onboarding sequence
regulation.html       Regulatory status, MiFID II framework, client protection, complaints, documents, risk warning
legal.html            Terms of use, privacy notice, cookie policy
contact.html          Contact details and enquiry form
front-office.html     Client portal gateway (front office) — button links to the external portal
back-office.html      Back office gateway for staff — button links to the external back office
404.html              Not found page (configure your host to serve it)
assets/css/main.css   All styles (design tokens at the top)
assets/js/main.js     Mobile menu, cookie consent, enquiry form hook
assets/img/           Brand imagery as steel-blue duotones, 1000w and 1920w, JPEG and WebP; og.jpg for link previews
assets/logo/          Logo SVGs (colour, on-dark, white, navy), monogram, favicons
assets/fonts/         Classico Regular and Bold (brand package, WOFF2) and Tenor Sans (OFL)
favicon.svg, site.webmanifest, robots.txt, sitemap.xml
```

Header and footer are generated into every page from `tools/build.py`.

## Portal links

* Client portal button: `front-office.html`, `href="https://portal.mbkcapital.com/"`
* Back office button: `back-office.html`, `href="https://backoffice.mbkcapital.com/"`

Both URLs are placeholders. The back office page is excluded from search engines in
`robots.txt` and is linked from the footer only.

## Placeholders awaiting confirmation

Everything wrapped in `<span class="placeholder">` is highlighted in gold on the page so it
is easy to spot during review. Remove the class (or the highlight rule in `main.css`) once
the content is final.

* CySEC licence number and the regulatory statement (footer, home page strip, regulation page)
* Company registration number (HE) and registered address
* Telephone number and office address
* Data Protection Officer
* Regulatory document PDFs (regulation page, "Documents" table)
* Analytics tool in the cookie policy
* Every commission, spread, fee and venue count on `markets.html` and `pricing.html`. The
  venue lists are indicative and need to match the executing brokers actually contracted.

Compliance should review `regulation.html`, `legal.html`, the footer risk warning and any
statement about services before publication. The brief requires that public statements match
the firm's actual authorisations at the time of publication.

## Enquiry form

The form on `contact.html` has no backend. Set `data-endpoint` on the `<form>` to a
form-handling service URL (Formspree, Basin, Netlify Forms, or your own endpoint) and
submissions will post there. Until then, submitting shows a message pointing to
info@mbkcapital.com.

## Cookies and analytics

The consent banner stores the visitor's choice in `localStorage` under
`mbk-cookie-consent`. Load analytics only when the stored choice is `all`; the hook is in
`main.js` next to the comment "Hook: load analytics here".

## Brand tokens

| Token | Value |
|---|---|
| Dark Navy | `#041522` |
| Gold | `#B08632` |
| Midnight Navy Ink | `#0A1A28` |
| Steel Slate Navy | `#3B4E61` |
| Deep Bronze Amber | `#85601F` |
| Light Harvest Gold | `#E0B673` |

Typography: Classico (Regular and Bold) from the brand package is used for headings, in line
with the brand guidelines (H1 to H3 in Classico Bold), and Tenor Sans for body text. Both are
self-hosted as WOFF2. Confirm that the Classico licence covers web embedding before launch.

Photography: the images are the duotone JPEGs delivered with the brand package (Images
folder, 8000 px), resized to 1000, 1920 and (for the home hero) 2560 px with light sharpening.
Confirm the licence for each photo before launch.

Home hero: the nautilus photo is shown without an overlay for now. A drawn-line effect
over the shell was tried and set aside; a different hero effect may be added later.

## Draft preview

Every page carries `<meta name="robots" content="noindex, nofollow">` while the site is a draft.
Remove that line from all pages before launching on the production domain.

## Local preview

```bash
python3 -m http.server 8765
```

Then open http://localhost:8765/.
