#!/usr/bin/env python3
"""
Builds the MBK Capital static site from the content below.

    python3 tools/build.py

No dependencies beyond the Python 3 standard library. Edit the copy in CONTENT,
run the script, commit the output. Generated HTML is overwritten on every build.
"""
import html
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://www.mbkcapital.com"
YEAR = "2026"
DRAFT = True  # adds a noindex meta tag to every page; set to False for launch

PORTAL_URL = "https://portal.mbkcapital.com/"
BACKOFFICE_URL = "https://backoffice.mbkcapital.com/"

PH = '<span class="placeholder">{}</span>'  # content awaiting confirmation


def ph(text):
    return PH.format(text)


# ---------------------------------------------------------------------------
# Shared content
# ---------------------------------------------------------------------------
NAV = [("about.html", "About"), ("services.html", "Services"), ("markets.html", "Markets"),
       ("pricing.html", "Pricing"), ("clients.html", "Clients"), ("regulation.html", "Regulation"),
       ("contact.html", "Contact")]
FOOTER_COMPANY = [("about.html", "About"), ("services.html", "Services"), ("markets.html", "Markets"),
                  ("pricing.html", "Pricing"), ("clients.html", "Clients"), ("contact.html", "Contact")]
FOOTER_REG = [("regulation.html", "Regulatory information"), ("regulation.html#protection", "Client protection"),
              ("regulation.html#complaints", "Complaints"), ("regulation.html#documents", "Documents"),
              ("legal.html#privacy", "Privacy notice"), ("legal.html#cookies", "Cookie policy")]

TAGLINE = "A trusted investment partner for intelligent growth."
RISK = ("<strong>Risk warning.</strong> Investing in financial instruments involves risk. The value of investments "
        "and the income from them can go down as well as up, and you may not get back the amount invested. "
        "Past performance is not a reliable indicator of future results. Information on this website is provided "
        "for general information only and does not constitute investment advice, a personal recommendation, or an "
        "offer or solicitation to buy or sell any financial instrument. Services are provided subject to MBK "
        "Capital&rsquo;s regulatory authorisations and to client suitability and appropriateness assessments.")
REG_LINE = ph("MBK Capital Ltd is authorised and regulated by the Cyprus Securities and Exchange Commission (CySEC) "
              "as a Cyprus Investment Firm, licence number 000/00.")
REG_COMPANY = ("MBK Capital Ltd is registered in the Republic of Cyprus, registration number " + ph("HE 000000") +
               ". Registered office: " + ph("[Registered address], Cyprus") + ".")

SERVICES = [
    ("brokerage", "Brokerage and market access",
     "Multi-asset execution across equities, fixed income, futures, options, exchange-traded and structured products, through established counterparties and market infrastructure.",
     "About brokerage",
     "We provide access to global financial markets through established counterparties, custodians and market infrastructure, with professional execution across asset classes.",
     ["Equities and exchange-traded products", "Bonds and fixed-income instruments", "Futures and options", "Structured products", "Selected over-the-counter instruments", "Professional execution and dealing-desk support"]),
    ("advice", "Investment advice",
     "Personalised consultation, strategy development and suitability-based proposals for sophisticated and professional investors.",
     "About investment advice",
     "Advice starts with listening. We take time to understand your objectives, constraints and experience before proposing anything, and every recommendation is assessed for suitability.",
     ["Personalised investment consultation", "Investment strategy development", "Portfolio-structure recommendations", "Market and product guidance", "Suitability-based investment proposals", "Support for sophisticated and professional investors"]),
    ("portfolio", "Portfolio management",
     "Discretionary and mandate-based management with professional portfolio construction, active monitoring and disciplined rebalancing.",
     "About portfolio management",
     "Where you prefer to delegate, we manage portfolios under a clearly defined mandate, with professional construction, active monitoring and disciplined rebalancing.",
     ["Discretionary portfolio management", "Mandate-based investment management", "Strategic and tactical allocation", "Professional portfolio construction", "Active monitoring and rebalancing", "Transparent reporting"]),
    ("research", "Research and analytics",
     "Market analysis, portfolio and risk analytics, macroeconomic commentary and decision support for your own judgement.",
     "About research",
     "We provide more than execution. Analysis, experience and informed judgement form part of the relationship, so you can make decisions with better information.",
     ["Market analysis and investment research", "Portfolio analytics", "Risk analysis", "Macroeconomic commentary", "Instrument and opportunity assessment", "Decision-support tools and professional insight"]),
    ("risk", "Active risk management",
     "Exposure and concentration analysis, hedging solutions, scenario work and clear communication in significant market conditions.",
     "About active risk management",
     "Risk is managed actively, not reported after the fact. We monitor exposures, discuss scenarios in advance and communicate clearly when markets move.",
     ["Portfolio risk monitoring", "Exposure and concentration analysis", "Hedging solutions", "Scenario analysis", "Drawdown and volatility awareness", "Active communication during significant market conditions"]),
    ("family-office", "Family office and wealth manager support",
     "Consolidated brokerage relationships, customised account structures and professional communication with authorised representatives.",
     "About this service",
     "Family offices, external asset managers and wealth advisers need a counterparty that understands complex structures and communicates professionally with authorised representatives.",
     ["Consolidated brokerage relationships", "Execution and reporting support", "Access to products and counterparties", "Customised account structures", "Professional communication with authorised representatives", "Support for complex ownership and investment arrangements"]),
]

VALUES = [
    ("Disciplined selectivity", "We choose our business relationships, partners and clients with care, prioritising mutual value, shared standards and long-term compatibility over short-term revenue."),
    ("Uncompromising transparency", "We communicate directly, clearly and honestly. Clients always receive straightforward answers, full clarity on costs and objective evaluations of risk."),
    ("Applied financial intelligence", "We pair deep research, active risk monitoring and institutional market access with practical human judgement to guide every decision."),
    ("Deliverability and ownership", "We promise only what we can stand behind, and we take full personal responsibility for the quality, accuracy and reliability of our execution."),
    ("Integrated partnership", "We merge sophisticated digital infrastructure with direct access to experienced professionals, so the relationship evolves as our clients&rsquo; requirements expand."),
]

PERSONALITY = [
    ("Trustworthy and secure", "Calm, stable and highly disciplined. Confidence comes from regulated European standards, asset safety and operational excellence, not from loud messaging."),
    ("Intelligent and experienced", "Analytical, thoughtful and articulate. Expertise shows in the quality of our execution and market insight."),
    ("Personal and attentive", "Warm, approachable and responsive. Every client is an individual partner, never an account number."),
    ("Calm and discreet", "Composed, understated and respectful of privacy across high-stakes environments and shifting market conditions."),
    ("Global and sophisticated", "Internationally relevant and institutionally credible across major financial centres, with a clear and accessible tone."),
]

# Markets: one entry per asset class. Commission and spread figures are placeholders.
MARKETS = [
    dict(id="stocks", tab="Stocks &amp; ETFs", h="Stocks &amp; ETFs",
         lede="Listed shares, ETFs and other exchange-traded products on the main US, European and Asian exchanges, with direct market access and live prices.",
         points=["Direct market access through established executing brokers and custodians",
                 "Live prices; market depth available on request",
                 "Dividends, corporate actions and tax reporting handled by our operations team",
                 "Multi-currency accounts, so you trade in the local currency of each exchange"],
         cols=["Exchange", "Code", "Country", "Indicative commission"],
         rows=[("New York Stock Exchange", "XNYS", "United States", "from 0.02 USD per share"),
               ("Nasdaq", "XNAS", "United States", "from 0.02 USD per share"),
               ("London Stock Exchange", "XLON", "United Kingdom", "from 0.05%"),
               ("Deutsche B&ouml;rse Xetra", "XETR", "Germany", "from 0.05%"),
               ("Euronext Paris", "XPAR", "France", "from 0.05%"),
               ("Euronext Amsterdam", "XAMS", "Netherlands", "from 0.05%"),
               ("SIX Swiss Exchange", "XSWX", "Switzerland", "from 0.05%"),
               ("Borsa Italiana", "XMIL", "Italy", "from 0.05%"),
               ("BME Spanish Exchanges", "XMAD", "Spain", "from 0.05%"),
               ("Nasdaq Stockholm", "XSTO", "Sweden", "from 0.05%"),
               ("Hong Kong Exchanges", "XHKG", "Hong Kong", "from 0.08%"),
               ("Tokyo Stock Exchange", "XTKS", "Japan", "from 0.08%"),
               ("Toronto Stock Exchange", "XTSE", "Canada", "from 0.02 CAD per share"),
               ("Australian Securities Exchange", "XASX", "Australia", "from 0.08%"),
               ("Athens Exchange", "XATH", "Greece", "from 0.10%"),
               ("Cyprus Stock Exchange", "XCYS", "Cyprus", "from 0.10%")],
         note="Indicative list. Final market coverage and commissions are confirmed in the client agreement and the costs and charges disclosure. Commissions include execution, exchange and clearing fees unless stated otherwise."),
    dict(id="currencies", tab="Currencies", h="Currencies",
         lede="Spot FX in major, minor and selected emerging-market pairs, for trading and for funding positions in other markets.",
         points=["Interbank liquidity aggregated from several providers",
                 "Settlement conversions at the same transparent rates",
                 "Quoted around the clock from Monday morning in Asia to Friday close in New York",
                 "Forwards and hedging solutions on request"],
         cols=["Pair group", "Examples", "Trading hours", "Indicative spread"],
         rows=[("Majors", "EUR/USD, GBP/USD, USD/JPY, USD/CHF, AUD/USD, USD/CAD", "24/5", "from 0.3 pips"),
               ("Crosses", "EUR/GBP, EUR/CHF, EUR/JPY, GBP/JPY, AUD/JPY", "24/5", "from 0.6 pips"),
               ("Scandinavian", "EUR/SEK, EUR/NOK, EUR/DKK", "24/5", "from 2 pips"),
               ("Emerging markets", "USD/PLN, USD/CZK, USD/HUF, USD/ZAR, USD/MXN", "24/5", "from 5 pips"),
               ("Spot precious metals", "XAU/USD, XAG/USD", "23/5", "from 0.20 USD")],
         note="Spreads are indicative and vary with market conditions and trade size. Leveraged FX is available to clients for whom it is appropriate."),
    dict(id="futures", tab="Futures", h="Futures",
         lede="Exchange-traded futures on indices, interest rates, energy, metals, agriculture and currencies, on the main derivatives exchanges.",
         points=["Index, rates, commodity and FX contracts on one account",
                 "Margin requirements aligned with exchange and clearing-house rules",
                 "Roll and expiry monitoring by the dealing desk",
                 "Real-time margin and exposure reporting"],
         cols=["Exchange", "Code", "Country", "Typical contracts", "Indicative commission"],
         rows=[("CME Group (CME, CBOT, NYMEX, COMEX)", "XCME", "United States", "S&amp;P 500, Treasuries, crude oil, gold", "from 1.50 USD per contract"),
               ("ICE Futures US", "IFUS", "United States", "Sugar, coffee, cotton, US Dollar Index", "from 1.50 USD per contract"),
               ("ICE Futures Europe", "IFEU", "United Kingdom", "Brent crude, gas oil, FTSE 100", "from 1.50 GBP per contract"),
               ("Eurex", "XEUR", "Germany", "Euro Stoxx 50, DAX, Bund, Bobl, Schatz", "from 1.50 EUR per contract"),
               ("Euronext Derivatives", "XMAT", "France, Netherlands", "CAC 40, AEX", "from 1.50 EUR per contract"),
               ("Cboe Futures Exchange", "XCBF", "United States", "VIX", "from 1.50 USD per contract"),
               ("Osaka Exchange", "XOSE", "Japan", "Nikkei 225", "from 200 JPY per contract"),
               ("Hong Kong Futures Exchange", "XHKF", "Hong Kong", "Hang Seng", "from 15 HKD per contract"),
               ("Singapore Exchange", "XSES", "Singapore", "FTSE China A50, MSCI indices", "from 2 SGD per contract")],
         note="Futures are leveraged instruments and losses can exceed the initial margin. Availability depends on client categorisation and an appropriateness assessment."),
    dict(id="options", tab="Options", h="Options",
         lede="Listed equity, index and futures options for income, hedging and directional strategies, with multi-leg order support.",
         points=["Equity and ETF options in the United States and Europe",
                 "Index options on the S&amp;P 500, Euro Stoxx 50, DAX and others",
                 "Multi-leg strategies (spreads, straddles, collars) placed as single orders",
                 "Risk-based margining, with exercise and assignment handled by our desk"],
         cols=["Exchange", "Code", "Country", "Products", "Indicative commission"],
         rows=[("Cboe", "XCBO", "United States", "Equity, ETF and index options (SPX, VIX)", "from 1.50 USD per contract"),
               ("Nasdaq PHLX", "XPHL", "United States", "Equity and ETF options", "from 1.50 USD per contract"),
               ("CME Group", "XCME", "United States", "Options on futures", "from 1.50 USD per contract"),
               ("Eurex", "XEUR", "Germany", "Equity and index options (Euro Stoxx 50, DAX)", "from 1.50 EUR per contract"),
               ("Euronext", "XPAR", "France, Netherlands, Belgium", "Equity and index options", "from 1.50 EUR per contract"),
               ("ICE Futures Europe", "IFEU", "United Kingdom", "Options on futures", "from 1.50 GBP per contract")],
         note="Options are complex instruments. Writing uncovered options can lead to losses greater than the premium received. Availability depends on an appropriateness assessment."),
    dict(id="bonds", tab="Bonds", h="Bonds",
         lede="Government, corporate and emerging-market bonds, exchange-traded and over the counter, with prices sourced from several dealers.",
         points=["Developed-market sovereigns and investment-grade corporates",
                 "High-yield and emerging-market issues on request",
                 "Eurobonds in USD, EUR and GBP",
                 "Coupons and maturities handled automatically; holdings reported at market value"],
         cols=["Segment", "Examples", "Typical minimum", "Indicative commission"],
         rows=[("Government bonds", "US Treasuries, German Bunds, UK Gilts, French OATs", "1,000 nominal", "from 0.05%"),
               ("Investment-grade corporates", "EUR and USD issues from large, rated issuers", "1,000 to 100,000 nominal, by issue", "from 0.10%"),
               ("High yield", "Sub-investment-grade corporate issues", "100,000 nominal", "from 0.15%"),
               ("Emerging-market sovereigns", "Hard-currency Eurobonds", "100,000 nominal", "from 0.15%"),
               ("Money market", "Treasury bills and short-dated notes", "1,000 nominal", "from 0.03%")],
         note="Minimum sizes are set by the issue documentation. Bond prices include a dealer spread, which is disclosed in the costs and charges information for each trade."),
    dict(id="structured-notes", tab="Structured notes", h="Structured notes",
         lede="Capital-protected, yield-enhancement and participation notes from established issuers, selected for a specific objective rather than sold off the shelf.",
         points=["Issuer selection with attention to credit quality and documentation",
                 "Payoff structures explained in plain terms before you invest",
                 "Secondary-market liquidity and valuations through the issuer",
                 "Bespoke structuring for professional clients from an agreed minimum size"],
         cols=["Type", "Typical underlying", "Typical term", "Indicative fee"],
         rows=[("Capital-protected notes", "Equity indices, baskets, interest rates", "3 to 5 years", "from 0.50%"),
               ("Autocallables and reverse convertibles", "Single stocks, indices", "1 to 3 years", "from 0.50%"),
               ("Participation and tracker notes", "Indices, commodities, thematic baskets", "1 to 5 years", "from 0.50%"),
               ("Credit-linked notes", "Corporate and sovereign credit", "2 to 5 years", "from 0.50%"),
               ("Bespoke structures", "Agreed with the client", "As structured", "On request")],
         note="Structured products are complex instruments and carry issuer credit risk. Appropriateness is assessed before any transaction. Please read the risk disclosure and the product documentation."),
]

PRICING_TABLES = [
    ("Commissions by asset class",
     "Commissions apply per trade. Third-party exchange, clearing and regulatory fees are passed through at cost and shown separately on your confirmation.",
     ["Asset class", "Commission", "Minimum per trade", "Notes"],
     [("Stocks &amp; ETFs, United States", "0.02 USD per share", "2 USD", "Exchange and regulatory fees passed through"),
      ("Stocks &amp; ETFs, Europe", "0.05% of trade value", "5 EUR", "Stamp duties and transaction taxes where applicable"),
      ("Stocks &amp; ETFs, Asia-Pacific", "0.08% of trade value", "10 USD", ""),
      ("Currencies", "Spread from 0.3 pips, plus 0.01%", "None", "Spot and settlement conversions"),
      ("Futures", "1.50 USD, EUR or GBP per contract", "None", "Exchange and clearing fees passed through"),
      ("Options", "1.50 USD or EUR per contract", "None", "Exercise and assignment at the same rate"),
      ("Bonds", "0.03% to 0.15% of nominal, by segment", "50 EUR", "Dealer spread disclosed per trade"),
      ("Structured notes", "From 0.50% of nominal", "None", "Issuer fees embedded in the note are disclosed separately")]),
    ("Account and custody",
     "There is no fee for opening or holding an account. Custody is charged on the value of assets held.",
     ["Item", "Fee", "Notes"],
     [("Account opening", "None", "Individual, corporate and trust accounts"),
      ("Custody", "0.10% per year, charged monthly", "On the market value of securities held"),
      ("Inactivity", "None", ""),
      ("Incoming transfers", "None", "Bank charges of the sending bank may apply"),
      ("Outgoing transfers, SEPA", "10 EUR", ""),
      ("Outgoing transfers, SWIFT", "25 EUR", "Correspondent bank charges may apply"),
      ("Securities transfers in or out", "25 EUR per line", ""),
      ("Market data", "Real-time prices included", "Market depth and professional feeds at exchange cost"),
      ("Statements and reports", "Included", "Monthly statements, trade confirmations, annual tax report")]),
]

LEGAL_TERMS = [
    ("Information only", "The content of this website is for general information about MBK Capital and its services. It does not constitute investment advice, a personal recommendation, or an offer or solicitation to buy or sell any financial instrument, and it should not be relied upon in making investment decisions. Services are provided only under a written agreement and subject to our regulatory authorisations and client acceptance procedures."),
    ("Jurisdiction", "This website is not directed at persons in any jurisdiction where its publication or availability would be contrary to local law or regulation. Persons accessing this website are responsible for informing themselves about, and observing, any such restrictions."),
    ("Accuracy and liability", "We take reasonable care to ensure that the information on this website is accurate at the time of publication, but we do not guarantee its completeness or accuracy and may change it without notice. To the extent permitted by law, we accept no liability for loss arising from the use of this website or reliance on its content."),
    ("Intellectual property", "The MBK Capital name, logo and the content of this website are the property of MBK Capital Ltd or its licensors and may not be reproduced without prior written consent."),
    ("Governing law", "These terms are governed by the laws of the Republic of Cyprus, and the courts of Cyprus have exclusive jurisdiction over any dispute arising from them."),
]

REG_DOCS = [
    ("Terms of business", "General terms governing the provision of investment services."),
    ("Client categorisation policy", "How clients are classified as retail, professional or eligible counterparty under MiFID II, and what protections apply."),
    ("Order execution policy", "How we obtain the best possible result when executing client orders."),
    ("Conflicts of interest policy", "How we identify, prevent and manage conflicts of interest."),
    ("Risk disclosure statement", "The nature and risks of the financial instruments we offer."),
    ("Complaints handling procedure", "How to raise a complaint and how it will be handled."),
    ("Investor Compensation Fund notice", "Coverage available to eligible clients."),
    ("Client asset safeguarding statement", "How client funds and financial instruments are held and protected."),
    ("Costs and charges disclosure", "Ex-ante and ex-post information on costs and charges."),
    ("Privacy notice", "How we process personal data."),
]


# ---------------------------------------------------------------------------
# Building blocks
# ---------------------------------------------------------------------------
def picture(name, alt, sizes="100vw", cls="", loading="lazy", extra="", widths=(1000, 1920)):
    cls_attr = f' class="{cls}"' if cls else ""
    webp = ", ".join(f"assets/img/{name}-{w}.webp {w}w" for w in widths)
    jpg = ", ".join(f"assets/img/{name}-{w}.jpg {w}w" for w in widths)
    return f'''<picture>
  <source type="image/webp" srcset="{webp}" sizes="{sizes}">
  <img src="assets/img/{name}-{widths[-1]}.jpg" srcset="{jpg}" sizes="{sizes}" alt="{alt}"{cls_attr} loading="{loading}" decoding="async"{extra}>
</picture>'''


def head(title, desc, path):
    full = "MBK Capital | The Architecture of Capital" if path == "index.html" else f"{title} | MBK Capital"
    canonical = DOMAIN + "/" + ("" if path == "index.html" else path)
    robots = '\n<meta name="robots" content="noindex, nofollow"><!-- draft preview: remove before launch -->' if DRAFT else ""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="MBK Capital">
<meta property="og:title" content="{html.escape(full)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{DOMAIN}/assets/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#041522">{robots}
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="icon" href="assets/logo/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="assets/logo/apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<link rel="preload" href="assets/fonts/classico-bold.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/tenorsans-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/main.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
'''


def header(path):
    items = ""
    for href, label in NAV:
        cur = ' aria-current="page"' if href == path else ""
        items += f'        <li><a class="nav__link" href="{href}"{cur}>{label}</a></li>\n'
    return f'''<header class="site-header">
  <div class="container site-header__inner">
    <a class="brand" href="index.html" aria-label="MBK Capital — home">
      <img src="assets/logo/mbk-logo-horizontal-on-dark.svg" alt="MBK Capital" width="499" height="274">
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">
      <span class="nav-toggle__bar"></span><span class="visually-hidden">Menu</span>
    </button>
    <nav class="nav" id="site-nav" aria-label="Main">
      <ul class="nav__list">
{items}      </ul>
      <a class="btn btn--outline" href="front-office.html">Client portal</a>
    </nav>
  </div>
</header>
'''


def footer():
    company = "".join(f'          <li><a href="{h}">{l}</a></li>\n' for h, l in FOOTER_COMPANY)
    reg = "".join(f'          <li><a href="{h}">{l}</a></li>\n' for h, l in FOOTER_REG)
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="site-footer__top">
      <div class="site-footer__brand">
        <img src="assets/logo/mbk-logo-horizontal-on-dark.svg" alt="MBK Capital" width="499" height="274">
        <p>{TAGLINE}</p>
      </div>
      <div>
        <h2>Company</h2>
        <ul>
{company}        </ul>
      </div>
      <div>
        <h2>Regulation</h2>
        <ul>
{reg}        </ul>
      </div>
      <div>
        <h2>Access</h2>
        <ul>
          <li><a href="front-office.html">Client portal</a></li>
          <li><a href="back-office.html">Back office</a></li>
        </ul>
        <h2>Contact</h2>
        <ul>
          <li><a href="mailto:info@mbkcapital.com">info@mbkcapital.com</a></li>
          <li><a href="tel:+35700000000">{ph("+357 00 000 000")}</a></li>
          <li>{ph("Limassol, Cyprus")}</li>
        </ul>
      </div>
    </div>
    <div class="site-footer__bottom">
      <p class="site-footer__legal">{RISK}</p>
      <p class="site-footer__legal">{REG_LINE} {REG_COMPANY}</p>
      <div class="site-footer__meta">
        <span>&copy; <span data-year>{YEAR}</span> MBK Capital Ltd. All rights reserved.</span>
        <a href="legal.html#terms">Terms of use</a>
        <a href="legal.html#privacy">Privacy</a>
        <a href="legal.html#cookies">Cookies</a>
      </div>
    </div>
  </div>
</footer>
<div class="cookie" id="cookie-banner" hidden role="region" aria-label="Cookie consent">
  <p>We use essential cookies to make this site work. With your consent we would also like to use analytics
    cookies to understand how the site is used. See our <a href="legal.html#cookies">cookie policy</a>.</p>
  <div class="cookie__actions">
    <button class="btn btn--gold btn--small" type="button" data-consent="all">Accept all</button>
    <button class="btn btn--outline btn--small" type="button" data-consent="essential">Essential only</button>
  </div>
</div>
<script src="assets/js/main.js" defer></script>
</body>
</html>
'''


def write_page(path, title, desc, body, chrome=True):
    out = head(title, desc, path)
    if chrome:
        out += header(path)
    out += body
    if chrome:
        out += footer()
    else:
        out += '<script src="assets/js/main.js" defer></script>\n</body>\n</html>\n'
    with open(os.path.join(ROOT, path), "w", encoding="utf-8") as f:
        f.write(out)


def values_list(items):
    return '<ul class="values">\n' + "".join(f'  <li><h3>{t}</h3><p>{d}</p></li>\n' for t, d in items) + '</ul>\n'


def page_hero(h1, lede, image=None, extra=""):
    pic = picture(image, "", cls="page-hero__bg", loading="eager") if image else ""
    return f'''<section class="page-hero">
  {pic}
  <div class="container">
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>{extra}
  </div>
</section>
'''


def table(cls, cols, rows, placeholder_last=False):
    head_html = "".join(f"<th>{c}</th>" for c in cols)
    body = ""
    for r in rows:
        cells = list(r)
        if placeholder_last and cells[-1]:
            cells[-1] = f'<span class="num">{ph(cells[-1])}</span>'
        body += "<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>\n"
    return f'''<div class="table-wrap">
<table class="{cls}">
  <thead><tr>{head_html}</tr></thead>
  <tbody>
{body}  </tbody>
</table>
</div>
'''


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------
def build_home():
    rows = "".join(f'''  <div class="dl__row">
    <dt>{name}</dt>
    <dd><p>{short}</p><a class="text-link" href="services.html#{anchor}">{link}</a></dd>
  </div>
''' for anchor, name, short, link, _intro, _items in SERVICES)
    return f'''<main id="main">
<section class="hero">
  <div class="hero__panel">
    <h1 class="hero__title">The Architecture <span class="gold hero__accent">of&nbsp;Capital.</span></h1>
    <p class="hero__lede">MBK Capital is a Cyprus-based investment firm that brings brokerage, advice, portfolio management, research and active risk management into one coordinated relationship.</p>
    <div class="hero__actions actions">
      <a class="btn btn--gold" href="contact.html">Start a conversation</a>
      <a class="text-link" href="services.html">See what we do</a>
    </div>
  </div>
  <figure class="hero__figure">
    {picture("nautilus", "Cross-section of a nautilus shell, its chambers following a logarithmic spiral", sizes="(max-width: 860px) 100vw, 62vw", loading="eager", extra=' fetchpriority="high"', widths=(1000, 1920, 2560))}
  </figure>
</section>

<section class="section" id="intro">
  <div class="container phi">
    <h2 class="statement">One relationship, built around your objectives.</h2>
    <div class="prose">
      <p>Sophisticated investing needs more than a trading account. It needs a partner who understands what you are trying to achieve, gives you access to the right markets and instruments, and stays dependable when conditions change.</p>
      <p>We combine experienced people, professional infrastructure and modern technology, and we take responsibility for the quality of the relationship. Technology supports access to our team; it does not replace it.</p>
      <p><a class="text-link" href="about.html">About MBK Capital</a></p>
    </div>
  </div>
</section>

<section class="section section--mist" id="services">
  <div class="container">
    <div class="section__head">
      <h2>What we do</h2>
      <p class="lede">Six capabilities, coordinated by one team, so you do not have to manage fragmented providers.</p>
    </div>
    <dl class="dl">
{rows}    </dl>
  </div>
</section>

<section class="section--navy" id="clients">
  <div class="split">
    <figure class="split__figure">
      {picture("hexwood", "Concentric hexagonal timber panels converging on a single point", sizes="(max-width: 860px) 100vw, 38vw")}
    </figure>
    <div class="split__body">
      <div class="section__head">
        <h2>Who we work with</h2>
      </div>
      <div class="audience">
        <h3>Private clients and family offices</h3>
        <p>Entrepreneurs, senior executives, multi-generational wealth holders, and the family offices and advisers who represent them. Preservation and intelligent growth of capital, discreet service and direct access to experienced professionals.</p>
      </div>
      <div class="audience">
        <h3>Professional traders and investors</h3>
        <p>Active traders, portfolio managers, fund principals and wealth managers who need reliable execution, broad instrument coverage, competitive pricing and a dealing desk that responds.</p>
      </div>
      <div class="audience">
        <p>We are selective by design. We work where we can create mutual value, and we say so clearly when we cannot.</p>
        <p><a class="text-link" href="clients.html">More about our clients</a></p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="values">
  <div class="container">
    <div class="section__head">
      <h2>How we work</h2>
      <p class="lede">Five commitments that shape every decision we take on a client&rsquo;s behalf.</p>
    </div>
{values_list(VALUES)}  </div>
</section>

<div class="reg-strip" id="regulation">
  <div class="container reg-strip__inner">
    <p>{REG_LINE} Client assets are held separately from the firm&rsquo;s own, and eligible clients are covered by the Investor Compensation Fund.</p>
    <a class="text-link" href="regulation.html">Regulatory information</a>
  </div>
</div>

<section class="section" id="contact">
  <div class="container phi phi--center">
    <h2 class="statement">Start a conversation.</h2>
    <div>
      <p class="lede" style="margin-bottom:1.4em">Tell us about your objectives and how you prefer to work. We will tell you plainly what we can do, what it costs and what we would not recommend.</p>
      <div class="actions">
        <a class="btn btn--navy" href="contact.html">Contact us</a>
        <a class="text-link" href="mailto:info@mbkcapital.com">info@mbkcapital.com</a>
      </div>
    </div>
  </div>
</section>
</main>
'''


def build_about():
    return f'''<main id="main">
{page_hero("About MBK Capital", "A complete investment partner built around knowledge, trust and intelligent growth.", "muqarnas")}
<section class="section">
  <div class="container phi">
    <h2 class="statement">Why we exist</h2>
    <div class="prose">
      <p>MBK Capital provides a complete, integrated investment partnership for high-net-worth individuals, family offices and professional traders. Operating as a Cyprus-based, CySEC-regulated investment firm, we combine institutional European governance with agile global market access, modern trading infrastructure and direct personal service.</p>
      <p>We look beyond isolated transactional platforms. MBK Capital unifies multi-asset brokerage, discretionary portfolio management, structured advisory, deep market analytics and active risk management into one coordinated relationship. Grounded in transparency, disciplined selectivity and human expertise, we listen carefully, act with precision and deliver tailored solutions built for long-term capital preservation and intelligent growth.</p>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="container phi">
    <h2 class="statement">Mission and vision</h2>
    <div class="prose">
      <h3>Our mission</h3>
      <p>To be the preferred long-term brokerage and investment-services partner for sophisticated clients by combining trusted relationships, intelligent market access, advanced technology and highly personalised service.</p>
      <h3>Our vision</h3>
      <p>To become a trusted international all-in-one brokerage and investment partner that grows alongside its clients.</p>
      <p class="muted">We intend to begin with a carefully selected group of clients, establish a strong operating foundation and progressively expand our services, capabilities and international reach. Growth is not measured only in clients or assets. It is measured in stronger relationships, broader market access, better execution and more complete solutions, built together with the people we serve.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head">
      <h2>Our core values</h2>
    </div>
{values_list(VALUES)}  </div>
</section>

<section class="section section--mist">
  <div class="container">
    <div class="section__head">
      <h2>How we behave</h2>
      <p class="lede">The character you should recognise in every interaction with us, whether with a relationship manager, a trader or a digital system.</p>
    </div>
{values_list(PERSONALITY)}  </div>
</section>

<section class="section">
  <div class="container phi">
    <h2 class="statement">Selective by design</h2>
    <div class="prose">
      <p>We are selective in the relationships, counterparties, solutions and business engagements we accept. Selectivity is not exclusivity for its own sake. It means we operate according to clearly defined values, choose partners carefully, and prioritise long-term compatibility over short-term revenue.</p>
      <p>We remain prepared to decline engagements that are unsuitable, unsustainable or inconsistent with our principles, and we say so directly. Clients should expect candour, commercial clarity and realistic promises.</p>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="container phi">
    <h2 class="statement">A Cyprus foundation, an international outlook</h2>
    <div class="prose">
      <p>MBK Capital is established in Cyprus and operates within the European regulatory framework under the supervision of the Cyprus Securities and Exchange Commission. That foundation gives our clients the governance, investor protection and operational discipline expected of a European financial institution.</p>
      <p>Cyprus is our regulated base, not the limit of our ambition. We are built to serve an international client base and to expand into additional jurisdictions as the business develops, subject to the relevant authorisations.</p>
      <p><a class="text-link" href="regulation.html">Regulatory information</a></p>
    </div>
  </div>
</section>
</main>
'''


def build_services():
    subnav = "".join(f'<li><a href="#{a}">{n}</a></li>\n' for a, n, *_ in SERVICES)
    sections = ""
    for i, (anchor, name, short, _link, intro, items) in enumerate(SERVICES):
        lis = "".join(f"<li>{it}</li>" for it in items)
        tone = " section--mist" if i % 2 == 1 else ""
        sections += f'''<section class="section{tone}" id="{anchor}">
  <div class="container phi">
    <h2 class="statement">{name}</h2>
    <div class="prose">
      <p class="lede">{short}</p>
      <p>{intro}</p>
      <ul>{lis}</ul>
    </div>
  </div>
</section>
'''
    return f'''<main id="main">
{page_hero("Services", "Brokerage, advice, portfolio management, research and risk management, delivered as one coordinated relationship.", "waves")}
<div class="container" style="padding-top:clamp(32px,5vw,56px)">
  <ul class="subnav">
{subnav}  </ul>
</div>
{sections}
<section class="section">
  <div class="container phi">
    <h2 class="statement">Only what we can stand behind</h2>
    <div class="prose">
      <p>We focus on solutions we understand, can deliver properly and are prepared to stand behind. If a service, product or expectation is not appropriate for you, we will say so.</p>
      <p class="note">Services are provided subject to MBK Capital&rsquo;s regulatory authorisations and to client suitability and appropriateness assessments. Availability of specific instruments, markets and services may vary by client category and jurisdiction.</p>
      <div class="actions">
        <a class="btn btn--navy" href="contact.html">Discuss your requirements</a>
        <a class="text-link" href="clients.html">Who we work with</a>
      </div>
    </div>
  </div>
</section>
</main>
'''


def build_markets():
    tabs = "".join(
        f'    <li role="presentation"><a role="tab" id="tab-{m["id"]}" href="#{m["id"]}" aria-controls="{m["id"]}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}">{m["tab"]}</a></li>\n'
        for i, m in enumerate(MARKETS))
    panels = ""
    for i, m in enumerate(MARKETS):
        lis = "".join(f"<li>{p}</li>" for p in m["points"])
        panels += f'''<section class="tab-panel" id="{m["id"]}" role="tabpanel" aria-labelledby="tab-{m["id"]}"{"" if i == 0 else " hidden"}>
  <div class="tab-panel__head phi">
    <h2>{m["h"]}</h2>
    <div class="prose">
      <p class="lede">{m["lede"]}</p>
      <ul>{lis}</ul>
    </div>
  </div>
{table("market-table", m["cols"], m["rows"], placeholder_last=True)}  <p class="table-note">{m["note"]}</p>
</section>
'''
    stats = f'''
    <div class="stats">
      <div class="stat"><strong>{ph("50+")}</strong><span>exchanges and trading venues</span></div>
      <div class="stat"><strong>6</strong><span>asset classes on one account</span></div>
      <div class="stat"><strong>{ph("24/5")}</strong><span>dealing desk and support</span></div>
    </div>
    <div class="actions">
      <a class="btn btn--gold" href="pricing.html">Pricing</a>
      <a class="text-link" href="contact.html">Open an account</a>
    </div>'''
    return f'''<main id="main">
{page_hero("Markets", "Direct access to global exchanges and OTC markets across six asset classes, through one account and one relationship.", "building", extra=stats)}
<section class="section section--tight">
  <div class="container">
    <ul class="tabs" role="tablist" aria-label="Asset classes" data-tabs>
{tabs}    </ul>
{panels}  </div>
</section>

<section class="section section--mist">
  <div class="container">
    <div class="section__head">
      <h2>Pricing and commissions</h2>
      <p class="lede">One commission schedule across all asset classes. Third-party fees are passed through at cost and shown separately.</p>
    </div>
    <div class="link-cards">
      <a class="link-card" href="pricing.html">
        <h3>Pricing</h3>
        <p>Commissions by asset class, account and custody fees, currency conversion and what is not included.</p>
      </a>
      <a class="link-card" href="regulation.html#documents">
        <h3>Costs and charges disclosure</h3>
        <p>Ex-ante and ex-post cost information as required under MiFID II, for every instrument you trade.</p>
      </a>
    </div>
    <p class="note">Access to specific markets and instruments depends on client categorisation, appropriateness and suitability assessments, and MBK Capital&rsquo;s regulatory authorisations.</p>
  </div>
</section>
</main>
'''


def build_pricing():
    sections = ""
    for i, (h, intro, cols, rows) in enumerate(PRICING_TABLES):
        tone = " section--mist" if i % 2 == 1 else ""
        sections += f'''<section class="section{tone}">
  <div class="container">
    <div class="section__head">
      <h2>{h}</h2>
      <p class="lede">{intro}</p>
    </div>
{table("price-table", cols, rows)}  </div>
</section>
'''
    return f'''<main id="main">
{page_hero("Pricing", "One commission schedule, no hidden fees. What you see here is what you pay, plus third-party costs passed through at cost.", "ribbed")}
<div class="container" style="padding-top:clamp(28px,4vw,44px)">
  <p class="note">{ph("All figures on this page are placeholders pending approval of the fee schedule.")} Final rates are set out in the client agreement and the costs and charges disclosure.</p>
</div>
{sections}
<section class="section">
  <div class="container phi">
    <h2 class="statement">Currency conversion</h2>
    <div class="prose">
      <p>Conversions for trading and settlement are executed at the interbank rate plus {ph("0.10%")}. The rate applied is shown on every confirmation and statement. Accounts can hold balances in several currencies, so you convert only when you choose to.</p>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="container phi">
    <h2 class="statement">Advice and portfolio management</h2>
    <div class="prose">
      <p>Investment advice is charged on a retainer or per project, agreed in advance in writing. Discretionary portfolio management carries a management fee from {ph("0.75% per year")} on assets under management, charged quarterly. A performance fee applies only where it is agreed in the mandate, and always with a high-water mark.</p>
      <p>Brokerage commissions on transactions within a managed portfolio are charged at the rates above, and we do not receive inducements from product providers.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container phi">
    <h2 class="statement">What is not included</h2>
    <div class="prose">
      <ul>
        <li>Exchange, clearing and regulatory fees charged by third parties, passed through at cost</li>
        <li>Stamp duties and financial transaction taxes, for example UK stamp duty reserve tax, French and Italian financial transaction taxes</li>
        <li>Fees embedded by issuers in structured products and funds, disclosed separately before you invest</li>
        <li>Correspondent-bank charges on international transfers</li>
      </ul>
      <p class="note">Before any transaction we provide ex-ante information on all costs and charges, and once a year a statement of the costs you actually paid, in line with MiFID II.</p>
      <div class="actions">
        <a class="btn btn--navy" href="contact.html">Request the full fee schedule</a>
        <a class="text-link" href="markets.html">Markets we cover</a>
      </div>
    </div>
  </div>
</section>
</main>
'''


def build_clients():
    a1 = "".join(f"<li>{i}</li>" for i in [
        "Preservation and intelligent growth of capital", "Access to multiple asset classes and markets through one relationship",
        "Discreet, dependable service and direct access to experienced professionals", "Confidence in the regulatory and operational framework",
        "Research, strategic insight, and portfolio and risk-management support", "Transparent costs and processes, and fast, competent responses"])
    a2 = "".join(f"<li>{i}</li>" for i in [
        "Reliable execution and competitive pricing", "Access to a broad range of instruments and quality counterparties",
        "Professional trading infrastructure, market data and analytics", "Responsive dealing and support teams",
        "Flexible account and reporting structures, with appropriate risk controls", "Access to less standardised opportunities and investment solutions"])
    steps = "".join(f'        <li><div><h3>{t}</h3><p>{d}</p></div></li>\n' for t, d in [
        ("Introductory conversation", "We discuss your objectives, experience and how you prefer to work, and we tell you plainly whether we are the right partner."),
        ("Suitability and documentation", "Client categorisation, suitability or appropriateness assessment, and identity and source-of-funds verification, organised to respect your time."),
        ("Account structure and access", "Accounts, mandates and reporting are set up to match your structure, and you receive access to the client portal and your relationship team."),
        ("An evolving relationship", "Services, access and capabilities develop as your capital, experience and requirements grow.")])
    return f'''<main id="main">
{page_hero("Clients", "Two audiences, equally important to us: private wealth and professional market participants.", "fins")}
<section class="section">
  <div class="container phi">
    <h2 class="statement">Private clients and family offices</h2>
    <div class="prose">
      <p>Entrepreneurs, company owners, senior executives, private investors and multi-generational wealth holders, together with the family offices, external asset managers and advisers who represent them.</p>
      <h3>What matters to you</h3>
      <ul>{a1}</ul>
      <p>You should never feel like a standardised retail client. Service, communication and solutions reflect your circumstances, experience, portfolio and preferred way of working.</p>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="container phi">
    <h2 class="statement">Professional traders and sophisticated investors</h2>
    <div class="prose">
      <p>Professional traders, active private investors, portfolio managers, fund principals, wealth managers and experienced derivatives traders, including clients with substantial portfolios or high trading volumes.</p>
      <h3>What matters to you</h3>
      <ul>{a2}</ul>
      <p class="muted">Trading, reporting and relationship management are integrated, so you are not handed between disconnected systems and teams.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container phi">
    <h2 class="statement">Family offices and wealth managers</h2>
    <div class="prose">
      <p>We support authorised representatives with consolidated brokerage relationships, execution and reporting, customised account structures, and professional communication across complex ownership and investment arrangements.</p>
      <p><a class="text-link" href="services.html#family-office">Family office and wealth manager support</a></p>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="container phi">
    <h2 class="statement">Emerging investors</h2>
    <div class="prose">
      <p>We also work with a smaller number of emerging affluent investors who want a more advisory-led relationship: guidance on portfolio construction, strategy selection, risk awareness and structured access to financial markets, with progressively more sophisticated services as the relationship develops.</p>
      <p class="muted">Acceptance criteria, service levels and product suitability vary with a client&rsquo;s experience, capital and objectives. Minimum relationship sizes apply and are discussed individually.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container phi">
    <h2 class="statement">Becoming a client</h2>
    <div>
      <ol class="steps">
{steps}      </ol>
      <div class="actions" style="margin-top:32px">
        <a class="btn btn--navy" href="contact.html">Start a conversation</a>
      </div>
    </div>
  </div>
</section>
</main>
'''


def build_regulation():
    aside = "".join(f'        <li><a href="{h}">{l}</a></li>\n' for h, l in [
        ("#status", "Regulatory status"), ("#framework", "Regulatory framework"), ("#protection", "Client protection"),
        ("#execution", "Best execution and conflicts"), ("#complaints", "Complaints"), ("#documents", "Documents"), ("#risk", "Risk warning")])
    docs = "".join(f'<tr><td><a href="#" class="placeholder">{t} (PDF)</a></td><td>{d}</td></tr>' for t, d in REG_DOCS)
    return f'''<main id="main">
{page_hero("Regulation and client protection", "Security, risk awareness, regulation, discretion and operational discipline support every client relationship.", "hexwood")}
<section class="section">
  <div class="container phi">
    <aside class="aside-nav" aria-label="On this page">
      <ul>
{aside}      </ul>
    </aside>
    <div class="prose">
      <h2 id="status">Regulatory status</h2>
      <p>{REG_LINE}</p>
      <p>MBK Capital Ltd is registered in the Republic of Cyprus under registration number {ph("HE 000000")}, with its registered office at {ph("[Registered address], Cyprus")}. The firm&rsquo;s authorisation can be verified in the CySEC register of regulated entities at <a href="https://www.cysec.gov.cy" rel="noopener">cysec.gov.cy</a>.</p>
      <p class="note">Statements about regulation, licences, services and jurisdictions on this website will be adapted to the company&rsquo;s actual authorisations and regulatory status at the time of publication. Items highlighted on this page are awaiting confirmation.</p>

      <h2 id="framework">Regulatory framework</h2>
      <p>As a Cyprus Investment Firm, MBK Capital operates under the Investment Services and Activities and Regulated Markets Law of 2017 (Law 87(I)/2017), which transposes the Markets in Financial Instruments Directive (MiFID II) into Cypriot law, and under the directives and circulars issued by CySEC.</p>
      <p>Clients are categorised as retail clients, professional clients or eligible counterparties. Categorisation determines the level of regulatory protection that applies and the services and instruments that may be appropriate. Clients may request a different categorisation, subject to the criteria set out in our client categorisation policy.</p>
      <p>Before providing investment advice or portfolio management we assess suitability: your knowledge and experience, financial situation and investment objectives. Before providing other services in complex instruments we assess appropriateness. We may decline to provide a service where an assessment indicates it is not appropriate.</p>

      <h2 id="protection">Client protection</h2>
      <h3>Segregation of client assets</h3>
      <p>Client funds are held in segregated client accounts with credit institutions, separate from the firm&rsquo;s own funds. Client financial instruments are held with custodians in accounts that identify them as belonging to clients. Reconciliations are performed regularly.</p>
      <h3>Investor Compensation Fund</h3>
      <p>MBK Capital is a member of the Investor Compensation Fund for clients of Cyprus Investment Firms. The Fund covers eligible clients, up to the limits set by law, where a member firm is unable to meet its obligations. Professional clients and eligible counterparties are generally not covered. Details are in our Investor Compensation Fund notice.</p>
      <h3>Information security and privacy</h3>
      <p>We protect client information and operational integrity through professional systems, controls and responsible conduct. Our <a href="legal.html#privacy">privacy notice</a> explains how personal data is processed.</p>

      <h2 id="execution">Best execution and conflicts of interest</h2>
      <p>When executing orders or transmitting them to other entities for execution, we take all sufficient steps to obtain the best possible result for clients, taking into account price, costs, speed, likelihood of execution and settlement, size, nature and any other relevant consideration. Our order execution policy describes the execution venues and counterparties we use.</p>
      <p>We maintain a conflicts of interest policy and organisational arrangements to identify, prevent and manage conflicts between the firm, its staff and its clients, or between clients. Where arrangements are not sufficient to prevent a risk of damage to client interests, we disclose the conflict before acting.</p>

      <h2 id="complaints">Complaints</h2>
      <p>If you are dissatisfied with any aspect of our service, please tell us. Complaints can be submitted in writing to <a href="mailto:complaints@mbkcapital.com">complaints@mbkcapital.com</a> or by post to our registered office. We acknowledge complaints promptly, investigate them impartially and respond in writing within the timeframes required by CySEC.</p>
      <p>If you are not satisfied with our final response, you may refer the matter to the Financial Ombudsman of the Republic of Cyprus or to CySEC, in accordance with the procedure set out in our complaints handling procedure.</p>

      <h2 id="documents">Documents</h2>
      <div class="table-wrap">
      <table>
        <thead><tr><th>Document</th><th>What it covers</th></tr></thead>
        <tbody>{docs}</tbody>
      </table>
      </div>
      <p class="note">Document links are placeholders until the final versions are approved by compliance.</p>

      <h2 id="risk">Risk warning</h2>
      <p>{RISK}</p>
      <p>Derivatives, structured products and leveraged instruments carry additional risks, including the possibility of losses exceeding the initial investment. Investments denominated in foreign currencies are also exposed to exchange-rate movements. Please read our risk disclosure statement before trading.</p>
    </div>
  </div>
</section>
</main>
'''


def build_legal():
    terms = "".join(f"      <h3>{h}</h3>\n      <p>{p}</p>\n" for h, p in LEGAL_TERMS)
    return f'''<main id="main">
{page_hero("Legal", "Terms of use, privacy notice and cookie policy for this website.")}
<section class="section">
  <div class="container phi">
    <aside class="aside-nav" aria-label="On this page">
      <ul>
        <li><a href="#terms">Terms of use</a></li>
        <li><a href="#privacy">Privacy notice</a></li>
        <li><a href="#cookies">Cookie policy</a></li>
      </ul>
    </aside>
    <div class="prose">
      <p class="note">These texts are drafts for compliance and legal review. Highlighted items are awaiting confirmation.</p>

      <h2 id="terms">Terms of use</h2>
      <p>This website is operated by MBK Capital Ltd (&ldquo;MBK Capital&rdquo;, &ldquo;we&rdquo;, &ldquo;us&rdquo;). By using this website you agree to these terms.</p>
{terms}
      <h2 id="privacy">Privacy notice</h2>
      <p>MBK Capital Ltd is the controller of personal data collected through this website and in the course of providing its services. We process personal data in accordance with the General Data Protection Regulation (EU) 2016/679 and Cyprus data protection law.</p>
      <h3>What we collect and why</h3>
      <ul>
        <li>Contact details and the content of enquiries you send us, to respond to you and to assess whether we can act for you (legitimate interests and steps prior to entering into a contract).</li>
        <li>Identity, financial and suitability information from clients and prospective clients, to comply with anti-money-laundering, client categorisation and suitability obligations (legal obligation and contract).</li>
        <li>Technical data such as IP address, browser type and pages visited, to keep the website secure and, with your consent, to understand how it is used (legitimate interests and consent).</li>
      </ul>
      <h3>Sharing and transfers</h3>
      <p>We share personal data with service providers who act on our instructions, with counterparties, custodians and banks where necessary to provide services, and with regulators and authorities where required by law. Where data is transferred outside the European Economic Area we use safeguards recognised under the GDPR.</p>
      <h3>Retention</h3>
      <p>We keep personal data for as long as needed for the purposes described above and to meet regulatory record-keeping requirements, which for client records is generally at least five years after the relationship ends.</p>
      <h3>Your rights</h3>
      <p>You have the right to access your personal data, to have it corrected or erased, to restrict or object to its processing, to data portability, and to withdraw consent where processing is based on consent. You may complain to the Office of the Commissioner for Personal Data Protection of the Republic of Cyprus.</p>
      <h3>Contact</h3>
      <p>Data protection enquiries: <a href="mailto:privacy@mbkcapital.com">privacy@mbkcapital.com</a>. Data Protection Officer: {ph("[name / to be appointed]")}.</p>

      <h2 id="cookies">Cookie policy</h2>
      <p>Cookies are small text files stored on your device. This website uses the following categories.</p>
      <div class="table-wrap">
      <table>
        <thead><tr><th>Category</th><th>Purpose</th><th>Consent</th></tr></thead>
        <tbody>
          <tr><td>Essential</td><td>Remembering your cookie preference and keeping the site secure. Includes the <code>mbk-cookie-consent</code> setting stored in your browser.</td><td>Not required</td></tr>
          <tr><td>Analytics</td><td>Understanding how visitors use the site so we can improve it. {ph("No analytics tool is currently installed.")}</td><td>Required</td></tr>
        </tbody>
      </table>
      </div>
      <p>You can change your preference at any time by clearing this website&rsquo;s data in your browser settings, after which the consent banner will appear again. You can also block cookies through your browser, although some parts of the website may then not function correctly.</p>
    </div>
  </div>
</section>
</main>
'''


def build_contact():
    opts = "".join(f'              <option value="{v}">{l}</option>\n' for v, l in [
        ("private", "A private investor"), ("family-office", "Representing a family office"),
        ("professional", "A professional trader or investment professional"),
        ("wealth-manager", "A wealth manager or external asset manager"), ("other", "Something else")])
    msg = html.escape("The enquiry form is not connected to a mail service yet. Please email us at info@mbkcapital.com.")
    return f'''<main id="main">
{page_hero("Contact", "Tell us about your objectives. We will tell you plainly what we can do.", "agave")}
<section class="section">
  <div class="container phi">
    <div>
      <ul class="contact-list">
        <li><strong>Email</strong><a href="mailto:info@mbkcapital.com">info@mbkcapital.com</a></li>
        <li><strong>Telephone</strong><a href="tel:+35700000000">{ph("+357 00 000 000")}</a><br><span class="small">Monday to Friday, 09:00 to 18:00 (Cyprus time)</span></li>
        <li><strong>Office</strong>{ph("[Street address]<br>Limassol, Cyprus")}</li>
        <li><strong>Existing clients</strong>Your relationship manager remains your first point of contact. You can also sign in to the <a href="front-office.html">client portal</a>.</li>
        <li><strong>Complaints</strong><a href="mailto:complaints@mbkcapital.com">complaints@mbkcapital.com</a><br><span class="small"><a href="regulation.html#complaints">How complaints are handled</a></span></li>
      </ul>
    </div>
    <div>
      <h2>Send an enquiry</h2>
      <form class="form" id="contact-form" method="post" action="#" data-endpoint="" data-msg-no-endpoint="{msg}" novalidate>
        <div class="form__row">
          <div class="field"><label for="f-name">Full name</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
          <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
        </div>
        <div class="form__row">
          <div class="field"><label for="f-phone">Telephone (optional)</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
          <div class="field"><label for="f-type">I am</label>
            <select id="f-type" name="client_type">
{opts}            </select>
          </div>
        </div>
        <div class="field"><label for="f-message">How can we help?</label><textarea id="f-message" name="message" required></textarea></div>
        <label class="checkbox"><input type="checkbox" name="consent" required><span>I agree that MBK Capital may process the information above to respond to my enquiry, as described in the <a href="legal.html#privacy">privacy notice</a>.</span></label>
        <p class="form__status" id="form-status" hidden></p>
        <div class="actions">
          <button class="btn btn--navy" type="submit">Send enquiry</button>
          <span class="small muted">We reply within one business day.</span>
        </div>
      </form>
    </div>
  </div>
</section>
</main>
'''


def build_gateway(h1, text, button, url, note):
    return f'''<main id="main" class="gateway">
  {picture("fins", "", cls="gateway__bg", loading="eager")}
  <div class="gateway__panel">
    <a href="index.html" aria-label="MBK Capital — home"><img class="gateway__mark" src="assets/logo/mbk-monogram-on-dark.svg" alt="MBK Capital monogram" width="175" height="274"></a>
    <h1>{h1}</h1>
    <p>{text}</p>
    <div class="gateway__actions">
      <a class="btn btn--gold btn--block" href="{url}" rel="noopener">{button}</a>
    </div>
    <p class="gateway__note">{note}</p>
    <p class="gateway__links"><a class="gateway__back" href="index.html">Back to mbkcapital.com</a></p>
  </div>
</main>
'''


def build_notfound():
    return f'''<main id="main">
{page_hero("Page not found", "The page you were looking for does not exist or has moved.")}
<section class="section">
  <div class="container">
    <div class="actions">
      <a class="btn btn--navy" href="index.html">Go to the home page</a>
      <a class="text-link" href="contact.html">Contact us</a>
    </div>
  </div>
</section>
</main>
'''


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------
def build():
    write_page("index.html", "Home",
               "MBK Capital is a Cyprus-based, CySEC-regulated investment firm bringing brokerage, investment advice, portfolio management, research and active risk management into one relationship.",
               build_home())
    write_page("about.html", "About",
               "MBK Capital is a Cyprus-based, CySEC-regulated investment firm combining institutional governance with personal service, professional infrastructure and global market access.",
               build_about())
    write_page("services.html", "Services",
               "Multi-asset brokerage, investment advice, discretionary portfolio management, research and analytics, active risk management and family office support from MBK Capital.",
               build_services())
    write_page("markets.html", "Markets",
               "Stocks and ETFs, currencies, futures, options, bonds and structured notes on global exchanges and OTC markets, through one MBK Capital account.",
               build_markets())
    write_page("pricing.html", "Pricing",
               "MBK Capital commissions by asset class, account and custody fees, currency conversion and what is not included.",
               build_pricing())
    write_page("clients.html", "Clients",
               "MBK Capital serves high-net-worth individuals, family offices, wealth managers, professional traders and sophisticated investors with a personalised, integrated brokerage relationship.",
               build_clients())
    write_page("regulation.html", "Regulation and client protection",
               "MBK Capital's regulatory status, MiFID II framework, client protection, best execution, conflicts of interest, complaints procedure and regulatory documents.",
               build_regulation())
    write_page("legal.html", "Legal", "Terms of use, privacy notice and cookie policy for the MBK Capital website.", build_legal())
    write_page("contact.html", "Contact",
               "Contact MBK Capital in Limassol, Cyprus. Email info@mbkcapital.com or send an enquiry about brokerage, advisory and portfolio management services.",
               build_contact())
    write_page("front-office.html", "Client portal",
               "Sign in to the MBK Capital client portal to view your accounts, positions, reports and messages.",
               build_gateway("Client portal", "Sign in to view your accounts, positions, reports and messages from your relationship team.",
                             "Open the client portal", PORTAL_URL,
                             'MBK Capital will never ask for your password by email or telephone. If you have trouble signing in, contact your relationship manager or <a href="mailto:support@mbkcapital.com">support@mbkcapital.com</a>.'),
               chrome=False)
    write_page("back-office.html", "Back office", "MBK Capital back office. Access for authorised staff only.",
               build_gateway("Back office", "Access for authorised MBK Capital staff only. All activity is logged.",
                             "Open the back office", BACKOFFICE_URL,
                             'If you are a client, please use the <a href="front-office.html">client portal</a> instead. Staff access issues: <a href="mailto:it@mbkcapital.com">it@mbkcapital.com</a>.'),
               chrome=False)
    write_page("404.html", "Page not found", "The page you were looking for could not be found.", build_notfound())

    public = ["", "about.html", "services.html", "markets.html", "pricing.html", "clients.html", "regulation.html",
              "legal.html", "contact.html", "front-office.html"]
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for p in public:
            f.write(f"  <url><loc>{DOMAIN}/{p}</loc></url>\n")
        f.write("</urlset>\n")
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /back-office.html\nSitemap: {DOMAIN}/sitemap.xml\n")
    print("built 12 pages, sitemap.xml and robots.txt")


if __name__ == "__main__":
    build()
