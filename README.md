# MBK Capital — corporate website

Static HTML site for MBK Capital, built from the MBK Capital Brand Guidelines and the
Brand Book Creative Brief. No build step, no framework: upload the folder to any static
host (S3/CloudFront, Netlify, Cloudflare Pages, nginx) and it works.

## Structure

```
index.html            Home
about.html            About: purpose, mission and vision, values, personality
services.html         Six service areas with anchors (#brokerage, #advice, #portfolio, #research, #risk, #family-office)
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
assets/fonts/         Self-hosted Marcellus and Tenor Sans (OFL)
favicon.svg, site.webmanifest, robots.txt, sitemap.xml
```

Header and footer are repeated in every page. When you change navigation or footer text,
update all HTML files.

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

Typography: the brand's display face, Classico, is a commercial font. Until it is licensed
for web use the site uses Marcellus (self-hosted) for headings and Tenor Sans (the brand's
body face, self-hosted) for text. To switch to Classico, add its `@font-face` rules and change
`--font-display` in `main.css`.

Photography: the images come from the brand book and are rendered as duotones to match it.
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
