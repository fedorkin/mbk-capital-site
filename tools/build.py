#!/usr/bin/env python3
"""
Builds the MBK Capital static site from the content dictionaries below.

    python3 tools/build.py

English pages are written to the repository root, Russian pages to /ru/.
No dependencies beyond the Python 3 standard library. Edit the copy in the
CONTENT dictionaries (one per language), run the script, commit the output.
"""
import html
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://www.mbkcapital.com"
YEAR = "2026"
DRAFT = True  # adds a noindex meta tag to every page; set to False for launch

PAGES = ["index.html", "about.html", "services.html", "clients.html", "regulation.html",
         "legal.html", "contact.html", "front-office.html", "back-office.html", "404.html"]

LANGS = {
    "en": dict(code="en", dir="", prefix="", other="ru", other_label="RU", other_prefix="ru/", other_name="Русская версия"),
    "ru": dict(code="ru", dir="ru/", prefix="../", other="en", other_label="EN", other_prefix="../", other_name="English version"),
}

# ---------------------------------------------------------------------------
# Content
# ---------------------------------------------------------------------------
CONTENT = {}

CONTENT["en"] = dict(
    site_title="MBK Capital | The Architecture of Capital",
    skip="Skip to content",
    menu="Menu",
    brand_aria="MBK Capital — home",
    nav=[("about.html", "About"), ("services.html", "Services"), ("clients.html", "Clients"),
         ("regulation.html", "Regulation"), ("contact.html", "Contact")],
    portal="Client portal",
    tagline="A trusted investment partner for intelligent growth.",
    footer_company="Company", footer_regulation="Regulation", footer_access="Access", footer_contact="Contact",
    footer_reg_links=[("regulation.html", "Regulatory information"), ("regulation.html#protection", "Client protection"),
                      ("regulation.html#complaints", "Complaints"), ("regulation.html#documents", "Documents"),
                      ("legal.html#privacy", "Privacy notice"), ("legal.html#cookies", "Cookie policy")],
    back_office="Back office",
    phone="+357 00 000 000", city="Limassol, Cyprus",
    risk=("<strong>Risk warning.</strong> Investing in financial instruments involves risk. The value of investments "
          "and the income from them can go down as well as up, and you may not get back the amount invested. "
          "Past performance is not a reliable indicator of future results. Information on this website is provided "
          "for general information only and does not constitute investment advice, a personal recommendation, or an "
          "offer or solicitation to buy or sell any financial instrument. Services are provided subject to MBK "
          "Capital&rsquo;s regulatory authorisations and to client suitability and appropriateness assessments."),
    reg_line=('<span class="placeholder">MBK Capital Ltd is authorised and regulated by the Cyprus Securities and '
              'Exchange Commission (CySEC) as a Cyprus Investment Firm, licence number 000/00.</span>'),
    reg_company=('MBK Capital Ltd is registered in the Republic of Cyprus, registration number '
                 '<span class="placeholder">HE 000000</span>. Registered office: '
                 '<span class="placeholder">[Registered address], Cyprus</span>.'),
    copyright="MBK Capital Ltd. All rights reserved.",
    terms="Terms of use", privacy="Privacy", cookies="Cookies",
    cookie_text=('We use essential cookies to make this site work. With your consent we would also like to use analytics '
                 'cookies to understand how the site is used. See our <a href="legal.html#cookies">cookie policy</a>.'),
    cookie_all="Accept all", cookie_essential="Essential only",

    # Home
    home=dict(
        title="Home",
        desc="MBK Capital is a Cyprus-based, CySEC-regulated investment firm bringing brokerage, investment advice, portfolio management, research and active risk management into one relationship.",
        h1='The Architecture <span class="gold hero__accent">of&nbsp;Capital.</span>',
        lede="MBK Capital is a Cyprus-based investment firm that brings brokerage, advice, portfolio management, research and active risk management into one coordinated relationship.",
        cta="Start a conversation", cta2="See what we do",
        hero_alt="Cross-section of a nautilus shell, its chambers following a logarithmic spiral",
        statement="One relationship, built around your objectives.",
        statement_p1="Sophisticated investing needs more than a trading account. It needs a partner who understands what you are trying to achieve, gives you access to the right markets and instruments, and stays dependable when conditions change.",
        statement_p2="We combine experienced people, professional infrastructure and modern technology, and we take responsibility for the quality of the relationship. Technology supports access to our team; it does not replace it.",
        statement_link="About MBK Capital",
        services_h="What we do",
        services_lede="Six capabilities, coordinated by one team, so you do not have to manage fragmented providers.",
        clients_h="Who we work with",
        clients_alt="Concentric hexagonal timber panels converging on a single point",
        aud1_h="Private clients and family offices",
        aud1_p="Entrepreneurs, senior executives, multi-generational wealth holders, and the family offices and advisers who represent them. Preservation and intelligent growth of capital, discreet service and direct access to experienced professionals.",
        aud2_h="Professional traders and investors",
        aud2_p="Active traders, portfolio managers, fund principals and wealth managers who need reliable execution, broad instrument coverage, competitive pricing and a dealing desk that responds.",
        selective="We are selective by design. We work where we can create mutual value, and we say so clearly when we cannot.",
        clients_link="More about our clients",
        values_h="How we work",
        values_lede="Five commitments that shape every decision we take on a client&rsquo;s behalf.",
        reg_strip="Client assets are held separately from the firm&rsquo;s own, and eligible clients are covered by the Investor Compensation Fund.",
        reg_link="Regulatory information",
        cta_h="Start a conversation.",
        cta_p="Tell us about your objectives and how you prefer to work. We will tell you plainly what we can do, what it costs and what we would not recommend.",
        cta_btn="Contact us",
    ),
    services=[
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
    ],
    values=[
        ("Disciplined selectivity", "We choose our business relationships, partners and clients with care, prioritising mutual value, shared standards and long-term compatibility over short-term revenue."),
        ("Uncompromising transparency", "We communicate directly, clearly and honestly. Clients always receive straightforward answers, full clarity on costs and objective evaluations of risk."),
        ("Applied financial intelligence", "We pair deep research, active risk monitoring and institutional market access with practical human judgement to guide every decision."),
        ("Deliverability and ownership", "We promise only what we can stand behind, and we take full personal responsibility for the quality, accuracy and reliability of our execution."),
        ("Integrated partnership", "We merge sophisticated digital infrastructure with direct access to experienced professionals, so the relationship evolves as our clients&rsquo; requirements expand."),
    ],
    personality=[
        ("Trustworthy and secure", "Calm, stable and highly disciplined. Confidence comes from regulated European standards, asset safety and operational excellence, not from loud messaging."),
        ("Intelligent and experienced", "Analytical, thoughtful and articulate. Expertise shows in the quality of our execution and market insight."),
        ("Personal and attentive", "Warm, approachable and responsive. Every client is an individual partner, never an account number."),
        ("Calm and discreet", "Composed, understated and respectful of privacy across high-stakes environments and shifting market conditions."),
        ("Global and sophisticated", "Internationally relevant and institutionally credible across major financial centres, with a clear and accessible tone."),
    ],
    about=dict(
        title="About",
        desc="MBK Capital is a Cyprus-based, CySEC-regulated investment firm combining institutional governance with personal service, professional infrastructure and global market access.",
        h1="About MBK Capital",
        lede="A complete investment partner built around knowledge, trust and intelligent growth.",
        why_h="Why we exist",
        why_p1="MBK Capital provides a complete, integrated investment partnership for high-net-worth individuals, family offices and professional traders. Operating as a Cyprus-based, CySEC-regulated investment firm, we combine institutional European governance with agile global market access, modern trading infrastructure and direct personal service.",
        why_p2="We look beyond isolated transactional platforms. MBK Capital unifies multi-asset brokerage, discretionary portfolio management, structured advisory, deep market analytics and active risk management into one coordinated relationship. Grounded in transparency, disciplined selectivity and human expertise, we listen carefully, act with precision and deliver tailored solutions built for long-term capital preservation and intelligent growth.",
        mv_h="Mission and vision",
        mission_h="Our mission",
        mission="To be the preferred long-term brokerage and investment-services partner for sophisticated clients by combining trusted relationships, intelligent market access, advanced technology and highly personalised service.",
        vision_h="Our vision",
        vision="To become a trusted international all-in-one brokerage and investment partner that grows alongside its clients.",
        vision_p="We intend to begin with a carefully selected group of clients, establish a strong operating foundation and progressively expand our services, capabilities and international reach. Growth is not measured only in clients or assets. It is measured in stronger relationships, broader market access, better execution and more complete solutions, built together with the people we serve.",
        values_h="Our core values",
        behave_h="How we behave",
        behave_lede="The character you should recognise in every interaction with us, whether with a relationship manager, a trader or a digital system.",
        sel_h="Selective by design",
        sel_p1="We are selective in the relationships, counterparties, solutions and business engagements we accept. Selectivity is not exclusivity for its own sake. It means we operate according to clearly defined values, choose partners carefully, and prioritise long-term compatibility over short-term revenue.",
        sel_p2="We remain prepared to decline engagements that are unsuitable, unsustainable or inconsistent with our principles, and we say so directly. Clients should expect candour, commercial clarity and realistic promises.",
        cy_h="A Cyprus foundation, an international outlook",
        cy_p1="MBK Capital is established in Cyprus and operates within the European regulatory framework under the supervision of the Cyprus Securities and Exchange Commission. That foundation gives our clients the governance, investor protection and operational discipline expected of a European financial institution.",
        cy_p2="Cyprus is our regulated base, not the limit of our ambition. We are built to serve an international client base and to expand into additional jurisdictions as the business develops, subject to the relevant authorisations.",
        reg_link="Regulatory information",
    ),
    services_page=dict(
        title="Services",
        desc="Multi-asset brokerage, investment advice, discretionary portfolio management, research and analytics, active risk management and family office support from MBK Capital.",
        h1="Services",
        lede="Brokerage, advice, portfolio management, research and risk management, delivered as one coordinated relationship.",
        close_h="Only what we can stand behind",
        close_p="We focus on solutions we understand, can deliver properly and are prepared to stand behind. If a service, product or expectation is not appropriate for you, we will say so.",
        close_note="Services are provided subject to MBK Capital&rsquo;s regulatory authorisations and to client suitability and appropriateness assessments. Availability of specific instruments, markets and services may vary by client category and jurisdiction.",
        close_btn="Discuss your requirements", close_link="Who we work with",
    ),
    clients=dict(
        title="Clients",
        desc="MBK Capital serves high-net-worth individuals, family offices, wealth managers, professional traders and sophisticated investors with a personalised, integrated brokerage relationship.",
        h1="Clients",
        lede="Two audiences, equally important to us: private wealth and professional market participants.",
        a1_h="Private clients and family offices",
        a1_p="Entrepreneurs, company owners, senior executives, private investors and multi-generational wealth holders, together with the family offices, external asset managers and advisers who represent them.",
        matters="What matters to you",
        a1_items=["Preservation and intelligent growth of capital", "Access to multiple asset classes and markets through one relationship", "Discreet, dependable service and direct access to experienced professionals", "Confidence in the regulatory and operational framework", "Research, strategic insight, and portfolio and risk-management support", "Transparent costs and processes, and fast, competent responses"],
        a1_close="You should never feel like a standardised retail client. Service, communication and solutions reflect your circumstances, experience, portfolio and preferred way of working.",
        a2_h="Professional traders and sophisticated investors",
        a2_p="Professional traders, active private investors, portfolio managers, fund principals, wealth managers and experienced derivatives traders, including clients with substantial portfolios or high trading volumes.",
        a2_items=["Reliable execution and competitive pricing", "Access to a broad range of instruments and quality counterparties", "Professional trading infrastructure, market data and analytics", "Responsive dealing and support teams", "Flexible account and reporting structures, with appropriate risk controls", "Access to less standardised opportunities and investment solutions"],
        a2_close="Trading, reporting and relationship management are integrated, so you are not handed between disconnected systems and teams.",
        fo_h="Family offices and wealth managers",
        fo_p="We support authorised representatives with consolidated brokerage relationships, execution and reporting, customised account structures, and professional communication across complex ownership and investment arrangements.",
        fo_link="Family office and wealth manager support",
        em_h="Emerging investors",
        em_p="We also work with a smaller number of emerging affluent investors who want a more advisory-led relationship: guidance on portfolio construction, strategy selection, risk awareness and structured access to financial markets, with progressively more sophisticated services as the relationship develops.",
        em_note="Acceptance criteria, service levels and product suitability vary with a client&rsquo;s experience, capital and objectives. Minimum relationship sizes apply and are discussed individually.",
        steps_h="Becoming a client",
        steps=[("Introductory conversation", "We discuss your objectives, experience and how you prefer to work, and we tell you plainly whether we are the right partner."),
               ("Suitability and documentation", "Client categorisation, suitability or appropriateness assessment, and identity and source-of-funds verification, organised to respect your time."),
               ("Account structure and access", "Accounts, mandates and reporting are set up to match your structure, and you receive access to the client portal and your relationship team."),
               ("An evolving relationship", "Services, access and capabilities develop as your capital, experience and requirements grow.")],
        steps_btn="Start a conversation",
    ),
    regulation=dict(
        title="Regulation and client protection",
        desc="MBK Capital's regulatory status, MiFID II framework, client protection, best execution, conflicts of interest, complaints procedure and regulatory documents.",
        h1="Regulation and client protection",
        lede="Security, risk awareness, regulation, discretion and operational discipline support every client relationship.",
        aside=[("#status", "Regulatory status"), ("#framework", "Regulatory framework"), ("#protection", "Client protection"),
               ("#execution", "Best execution and conflicts"), ("#complaints", "Complaints"), ("#documents", "Documents"), ("#risk", "Risk warning")],
        on_page="On this page",
        status_h="Regulatory status",
        status_p=('MBK Capital Ltd is registered in the Republic of Cyprus under registration number <span class="placeholder">HE 000000</span>, '
                  'with its registered office at <span class="placeholder">[Registered address], Cyprus</span>. The firm&rsquo;s authorisation can be '
                  'verified in the CySEC register of regulated entities at <a href="https://www.cysec.gov.cy" rel="noopener">cysec.gov.cy</a>.'),
        status_note="Statements about regulation, licences, services and jurisdictions on this website will be adapted to the company&rsquo;s actual authorisations and regulatory status at the time of publication. Items highlighted on this page are awaiting confirmation.",
        fw_h="Regulatory framework",
        fw_p1="As a Cyprus Investment Firm, MBK Capital operates under the Investment Services and Activities and Regulated Markets Law of 2017 (Law 87(I)/2017), which transposes the Markets in Financial Instruments Directive (MiFID II) into Cypriot law, and under the directives and circulars issued by CySEC.",
        fw_p2="Clients are categorised as retail clients, professional clients or eligible counterparties. Categorisation determines the level of regulatory protection that applies and the services and instruments that may be appropriate. Clients may request a different categorisation, subject to the criteria set out in our client categorisation policy.",
        fw_p3="Before providing investment advice or portfolio management we assess suitability: your knowledge and experience, financial situation and investment objectives. Before providing other services in complex instruments we assess appropriateness. We may decline to provide a service where an assessment indicates it is not appropriate.",
        prot_h="Client protection",
        seg_h="Segregation of client assets",
        seg_p="Client funds are held in segregated client accounts with credit institutions, separate from the firm&rsquo;s own funds. Client financial instruments are held with custodians in accounts that identify them as belonging to clients. Reconciliations are performed regularly.",
        icf_h="Investor Compensation Fund",
        icf_p="MBK Capital is a member of the Investor Compensation Fund for clients of Cyprus Investment Firms. The Fund covers eligible clients, up to the limits set by law, where a member firm is unable to meet its obligations. Professional clients and eligible counterparties are generally not covered. Details are in our Investor Compensation Fund notice.",
        sec_h="Information security and privacy",
        sec_p='We protect client information and operational integrity through professional systems, controls and responsible conduct. Our <a href="legal.html#privacy">privacy notice</a> explains how personal data is processed.',
        exec_h="Best execution and conflicts of interest",
        exec_p1="When executing orders or transmitting them to other entities for execution, we take all sufficient steps to obtain the best possible result for clients, taking into account price, costs, speed, likelihood of execution and settlement, size, nature and any other relevant consideration. Our order execution policy describes the execution venues and counterparties we use.",
        exec_p2="We maintain a conflicts of interest policy and organisational arrangements to identify, prevent and manage conflicts between the firm, its staff and its clients, or between clients. Where arrangements are not sufficient to prevent a risk of damage to client interests, we disclose the conflict before acting.",
        comp_h="Complaints",
        comp_p1='If you are dissatisfied with any aspect of our service, please tell us. Complaints can be submitted in writing to <a href="mailto:complaints@mbkcapital.com">complaints@mbkcapital.com</a> or by post to our registered office. We acknowledge complaints promptly, investigate them impartially and respond in writing within the timeframes required by CySEC.',
        comp_p2="If you are not satisfied with our final response, you may refer the matter to the Financial Ombudsman of the Republic of Cyprus or to CySEC, in accordance with the procedure set out in our complaints handling procedure.",
        docs_h="Documents", doc_col1="Document", doc_col2="What it covers", pdf="PDF",
        docs=[("Terms of business", "General terms governing the provision of investment services."),
              ("Client categorisation policy", "How clients are classified as retail, professional or eligible counterparty under MiFID II, and what protections apply."),
              ("Order execution policy", "How we obtain the best possible result when executing client orders."),
              ("Conflicts of interest policy", "How we identify, prevent and manage conflicts of interest."),
              ("Risk disclosure statement", "The nature and risks of the financial instruments we offer."),
              ("Complaints handling procedure", "How to raise a complaint and how it will be handled."),
              ("Investor Compensation Fund notice", "Coverage available to eligible clients."),
              ("Client asset safeguarding statement", "How client funds and financial instruments are held and protected."),
              ("Costs and charges disclosure", "Ex-ante and ex-post information on costs and charges."),
              ("Privacy notice", "How we process personal data.")],
        docs_note="Document links are placeholders until the final versions are approved by compliance.",
        risk_h="Risk warning",
        risk_p2="Derivatives, structured products and leveraged instruments carry additional risks, including the possibility of losses exceeding the initial investment. Investments denominated in foreign currencies are also exposed to exchange-rate movements. Please read our risk disclosure statement before trading.",
    ),
    legal=dict(
        title="Legal", desc="Terms of use, privacy notice and cookie policy for the MBK Capital website.",
        h1="Legal", lede="Terms of use, privacy notice and cookie policy for this website.",
        aside=[("#terms", "Terms of use"), ("#privacy", "Privacy notice"), ("#cookies", "Cookie policy")], on_page="On this page",
        note="These texts are drafts for compliance and legal review. Highlighted items are awaiting confirmation.",
        terms_h="Terms of use",
        terms_intro="This website is operated by MBK Capital Ltd (&ldquo;MBK Capital&rdquo;, &ldquo;we&rdquo;, &ldquo;us&rdquo;). By using this website you agree to these terms.",
        terms=[("Information only", "The content of this website is for general information about MBK Capital and its services. It does not constitute investment advice, a personal recommendation, or an offer or solicitation to buy or sell any financial instrument, and it should not be relied upon in making investment decisions. Services are provided only under a written agreement and subject to our regulatory authorisations and client acceptance procedures."),
               ("Jurisdiction", "This website is not directed at persons in any jurisdiction where its publication or availability would be contrary to local law or regulation. Persons accessing this website are responsible for informing themselves about, and observing, any such restrictions."),
               ("Accuracy and liability", "We take reasonable care to ensure that the information on this website is accurate at the time of publication, but we do not guarantee its completeness or accuracy and may change it without notice. To the extent permitted by law, we accept no liability for loss arising from the use of this website or reliance on its content."),
               ("Intellectual property", "The MBK Capital name, logo and the content of this website are the property of MBK Capital Ltd or its licensors and may not be reproduced without prior written consent."),
               ("Governing law", "These terms are governed by the laws of the Republic of Cyprus, and the courts of Cyprus have exclusive jurisdiction over any dispute arising from them.")],
        privacy_h="Privacy notice",
        privacy_intro="MBK Capital Ltd is the controller of personal data collected through this website and in the course of providing its services. We process personal data in accordance with the General Data Protection Regulation (EU) 2016/679 and Cyprus data protection law.",
        collect_h="What we collect and why",
        collect=["Contact details and the content of enquiries you send us, to respond to you and to assess whether we can act for you (legitimate interests and steps prior to entering into a contract).",
                 "Identity, financial and suitability information from clients and prospective clients, to comply with anti-money-laundering, client categorisation and suitability obligations (legal obligation and contract).",
                 "Technical data such as IP address, browser type and pages visited, to keep the website secure and, with your consent, to understand how it is used (legitimate interests and consent)."],
        share_h="Sharing and transfers",
        share_p="We share personal data with service providers who act on our instructions, with counterparties, custodians and banks where necessary to provide services, and with regulators and authorities where required by law. Where data is transferred outside the European Economic Area we use safeguards recognised under the GDPR.",
        retain_h="Retention",
        retain_p="We keep personal data for as long as needed for the purposes described above and to meet regulatory record-keeping requirements, which for client records is generally at least five years after the relationship ends.",
        rights_h="Your rights",
        rights_p="You have the right to access your personal data, to have it corrected or erased, to restrict or object to its processing, to data portability, and to withdraw consent where processing is based on consent. You may complain to the Office of the Commissioner for Personal Data Protection of the Republic of Cyprus.",
        contact_h="Contact",
        contact_p='Data protection enquiries: <a href="mailto:privacy@mbkcapital.com">privacy@mbkcapital.com</a>. Data Protection Officer: <span class="placeholder">[name / to be appointed]</span>.',
        cookies_h="Cookie policy",
        cookies_intro="Cookies are small text files stored on your device. This website uses the following categories.",
        cookie_cols=("Category", "Purpose", "Consent"),
        cookie_rows=[("Essential", "Remembering your cookie preference and keeping the site secure. Includes the <code>mbk-cookie-consent</code> setting stored in your browser.", "Not required"),
                     ("Analytics", 'Understanding how visitors use the site so we can improve it. <span class="placeholder">No analytics tool is currently installed.</span>', "Required")],
        cookies_close="You can change your preference at any time by clearing this website&rsquo;s data in your browser settings, after which the consent banner will appear again. You can also block cookies through your browser, although some parts of the website may then not function correctly.",
    ),
    contact=dict(
        title="Contact",
        desc="Contact MBK Capital in Limassol, Cyprus. Email info@mbkcapital.com or send an enquiry about brokerage, advisory and portfolio management services.",
        h1="Contact", lede="Tell us about your objectives. We will tell you plainly what we can do.",
        email_h="Email", phone_h="Telephone", hours="Monday to Friday, 09:00 to 18:00 (Cyprus time)",
        office_h="Office", street="[Street address]",
        existing_h="Existing clients",
        existing_p='Your relationship manager remains your first point of contact. You can also sign in to the <a href="front-office.html">client portal</a>.',
        complaints_h="Complaints", complaints_link="How complaints are handled",
        form_h="Send an enquiry",
        f_name="Full name", f_email="Email", f_phone="Telephone (optional)", f_type="I am",
        f_types=[("private", "A private investor"), ("family-office", "Representing a family office"),
                 ("professional", "A professional trader or investment professional"),
                 ("wealth-manager", "A wealth manager or external asset manager"), ("other", "Something else")],
        f_message="How can we help?",
        f_consent='I agree that MBK Capital may process the information above to respond to my enquiry, as described in the <a href="legal.html#privacy">privacy notice</a>.',
        f_submit="Send enquiry", f_reply="We reply within one business day.",
        f_no_endpoint="The enquiry form is not connected to a mail service yet. Please email us at info@mbkcapital.com.",
    ),
    front=dict(
        title="Client portal", desc="Sign in to the MBK Capital client portal to view your accounts, positions, reports and messages.",
        h1="Client portal",
        p="Sign in to view your accounts, positions, reports and messages from your relationship team.",
        btn="Open the client portal",
        note='MBK Capital will never ask for your password by email or telephone. If you have trouble signing in, contact your relationship manager or <a href="mailto:support@mbkcapital.com">support@mbkcapital.com</a>.',
    ),
    back=dict(
        title="Back office", desc="MBK Capital back office. Access for authorised staff only.",
        h1="Back office",
        p="Access for authorised MBK Capital staff only. All activity is logged.",
        btn="Open the back office",
        note='If you are a client, please use the <a href="front-office.html">client portal</a> instead. Staff access issues: <a href="mailto:it@mbkcapital.com">it@mbkcapital.com</a>.',
    ),
    gateway_back="Back to mbkcapital.com",
    monogram_alt="MBK Capital monogram",
    notfound=dict(title="Page not found", desc="The page you were looking for could not be found.",
                  h1="Page not found", lede="The page you were looking for does not exist or has moved.",
                  home="Go to the home page", contact="Contact us"),
)

CONTENT["ru"] = dict(
    site_title="MBK Capital | Архитектура капитала",
    skip="Перейти к содержанию",
    menu="Меню",
    brand_aria="MBK Capital — на главную",
    nav=[("about.html", "О компании"), ("services.html", "Услуги"), ("clients.html", "Клиенты"),
         ("regulation.html", "Регулирование"), ("contact.html", "Контакты")],
    portal="Личный кабинет",
    tagline="Надёжный инвестиционный партнёр для разумного роста.",
    footer_company="Компания", footer_regulation="Регулирование", footer_access="Доступ", footer_contact="Контакты",
    footer_reg_links=[("regulation.html", "Регуляторная информация"), ("regulation.html#protection", "Защита клиентов"),
                      ("regulation.html#complaints", "Жалобы"), ("regulation.html#documents", "Документы"),
                      ("legal.html#privacy", "Политика конфиденциальности"), ("legal.html#cookies", "Политика cookie")],
    back_office="Бэк-офис",
    phone="+357 00 000 000", city="Лимасол, Кипр",
    risk=("<strong>Предупреждение о рисках.</strong> Инвестиции в финансовые инструменты связаны с риском. Стоимость "
          "инвестиций и доход от них могут как расти, так и снижаться, и вы можете не вернуть вложенную сумму. "
          "Прошлые результаты не являются надёжным индикатором будущих. Информация на этом сайте носит общий характер "
          "и не является инвестиционной консультацией, персональной рекомендацией, предложением или приглашением "
          "купить или продать какой-либо финансовый инструмент. Услуги предоставляются в рамках регуляторных "
          "разрешений MBK Capital и с учётом оценки их соответствия и уместности для клиента."),
    reg_line=('<span class="placeholder">MBK Capital Ltd имеет лицензию Кипрской комиссии по ценным бумагам и биржам '
              '(CySEC) как кипрская инвестиционная компания, номер лицензии 000/00.</span>'),
    reg_company=('MBK Capital Ltd зарегистрирована в Республике Кипр, регистрационный номер '
                 '<span class="placeholder">HE 000000</span>. Юридический адрес: '
                 '<span class="placeholder">[адрес], Кипр</span>.'),
    copyright="MBK Capital Ltd. Все права защищены.",
    terms="Условия использования", privacy="Конфиденциальность", cookies="Cookie",
    cookie_text=('Мы используем необходимые cookie для работы сайта. С вашего согласия мы также хотели бы использовать '
                 'аналитические cookie, чтобы понимать, как используется сайт. См. нашу '
                 '<a href="legal.html#cookies">политику cookie</a>.'),
    cookie_all="Принять все", cookie_essential="Только необходимые",

    home=dict(
        title="Главная",
        desc="MBK Capital — инвестиционная компания на Кипре под регулированием CySEC, объединяющая брокерское обслуживание, инвестиционные консультации, управление портфелем, аналитику и управление рисками в одном партнёрстве.",
        h1='Архитектура <span class="gold hero__accent">капитала.</span>',
        lede="MBK Capital — инвестиционная компания на Кипре, которая объединяет брокерское обслуживание, инвестиционные консультации, управление портфелем, аналитику и активное управление рисками в одном партнёрстве.",
        cta="Обсудить задачи", cta2="Что мы делаем",
        hero_alt="Разрез раковины наутилуса: камеры следуют логарифмической спирали",
        statement="Одно партнёрство, выстроенное вокруг ваших целей.",
        statement_p1="Серьёзные инвестиции требуют большего, чем торговый счёт. Нужен партнёр, который понимает, чего вы хотите достичь, открывает доступ к нужным рынкам и инструментам и остаётся надёжным, когда условия меняются.",
        statement_p2="Мы объединяем опытных людей, профессиональную инфраструктуру и современные технологии и берём на себя ответственность за качество отношений. Технологии упрощают доступ к нашей команде, но не заменяют его.",
        statement_link="О компании",
        services_h="Что мы делаем",
        services_lede="Шесть направлений, которые координирует одна команда, чтобы вам не приходилось управлять разрозненными провайдерами.",
        clients_h="С кем мы работаем",
        clients_alt="Концентрические шестиугольные деревянные панели, сходящиеся в одной точке",
        aud1_h="Частные клиенты и семейные офисы",
        aud1_p="Предприниматели, топ-менеджеры, владельцы семейного капитала, а также семейные офисы и консультанты, которые их представляют. Сохранение и разумный рост капитала, конфиденциальный сервис и прямой доступ к опытным профессионалам.",
        aud2_h="Профессиональные трейдеры и инвесторы",
        aud2_p="Активные трейдеры, портфельные управляющие, руководители фондов и управляющие капиталом, которым нужны надёжное исполнение, широкий выбор инструментов, конкурентные условия и дилинг, который отвечает.",
        selective="Мы избирательны по замыслу. Мы работаем там, где можем создать взаимную ценность, и прямо говорим, когда не можем.",
        clients_link="Подробнее о клиентах",
        values_h="Как мы работаем",
        values_lede="Пять принципов, которые определяют каждое решение, принимаемое от имени клиента.",
        reg_strip="Активы клиентов хранятся отдельно от средств компании, а клиенты, имеющие на это право, защищены Фондом компенсации инвесторов.",
        reg_link="Регуляторная информация",
        cta_h="Начнём диалог.",
        cta_p="Расскажите о своих целях и о том, как вам удобно работать. Мы прямо скажем, что можем сделать, сколько это стоит и чего мы бы не рекомендовали.",
        cta_btn="Связаться с нами",
    ),
    services=[
        ("brokerage", "Брокерское обслуживание и доступ к рынкам",
         "Исполнение сделок по акциям, облигациям, фьючерсам, опционам, биржевым и структурным продуктам через надёжных контрагентов и рыночную инфраструктуру.",
         "О брокерском обслуживании",
         "Мы обеспечиваем доступ к глобальным финансовым рынкам через надёжных контрагентов, кастодианов и рыночную инфраструктуру с профессиональным исполнением по всем классам активов.",
         ["Акции и биржевые продукты", "Облигации и инструменты с фиксированным доходом", "Фьючерсы и опционы", "Структурные продукты", "Отдельные внебиржевые инструменты", "Профессиональное исполнение и поддержка дилинга"]),
        ("advice", "Инвестиционные консультации",
         "Персональные консультации, разработка стратегии и предложения с учётом оценки соответствия для опытных и профессиональных инвесторов.",
         "Об инвестиционных консультациях",
         "Консультация начинается с того, что мы слушаем. Прежде чем что-то предлагать, мы разбираемся в ваших целях, ограничениях и опыте, и каждая рекомендация проходит оценку соответствия.",
         ["Персональные инвестиционные консультации", "Разработка инвестиционной стратегии", "Рекомендации по структуре портфеля", "Ориентиры по рынкам и продуктам", "Предложения с учётом оценки соответствия", "Поддержка опытных и профессиональных инвесторов"]),
        ("portfolio", "Управление портфелем",
         "Дискреционное управление и управление по мандату: профессиональное формирование портфеля, постоянный мониторинг и дисциплинированная ребалансировка.",
         "Об управлении портфелем",
         "Если вы предпочитаете делегировать, мы управляем портфелем в рамках чётко определённого мандата: профессиональное формирование, постоянный мониторинг и дисциплинированная ребалансировка.",
         ["Дискреционное управление портфелем", "Управление по мандату", "Стратегическая и тактическая аллокация", "Профессиональное формирование портфеля", "Постоянный мониторинг и ребалансировка", "Прозрачная отчётность"]),
        ("research", "Аналитика и исследования",
         "Анализ рынков, портфельная и риск-аналитика, макроэкономические комментарии и поддержка ваших собственных решений.",
         "Об аналитике",
         "Мы даём больше, чем исполнение. Анализ, опыт и взвешенное суждение — часть отношений, чтобы вы принимали решения на основе лучшей информации.",
         ["Анализ рынков и инвестиционные исследования", "Портфельная аналитика", "Анализ рисков", "Макроэкономические комментарии", "Оценка инструментов и возможностей", "Инструменты поддержки решений и профессиональная экспертиза"]),
        ("risk", "Активное управление рисками",
         "Анализ экспозиции и концентрации, решения по хеджированию, сценарный анализ и ясная коммуникация в периоды значимых рыночных событий.",
         "Об управлении рисками",
         "Рисками управляют активно, а не отчитываются о них постфактум. Мы отслеживаем экспозицию, заранее обсуждаем сценарии и ясно информируем, когда рынки приходят в движение.",
         ["Мониторинг портфельных рисков", "Анализ экспозиции и концентрации", "Решения по хеджированию", "Сценарный анализ", "Контроль просадок и волатильности", "Активная коммуникация в периоды значимых рыночных событий"]),
        ("family-office", "Поддержка семейных офисов и управляющих",
         "Консолидированные брокерские отношения, индивидуальные структуры счетов и профессиональное взаимодействие с уполномоченными представителями.",
         "Об этой услуге",
         "Семейным офисам, независимым управляющим и консультантам по капиталу нужен контрагент, который понимает сложные структуры и профессионально взаимодействует с уполномоченными представителями.",
         ["Консолидированные брокерские отношения", "Поддержка исполнения и отчётности", "Доступ к продуктам и контрагентам", "Индивидуальные структуры счетов", "Профессиональное взаимодействие с уполномоченными представителями", "Поддержка сложных структур владения и инвестирования"]),
    ],
    values=[
        ("Дисциплинированная избирательность", "Мы тщательно выбираем деловые отношения, партнёров и клиентов, отдавая приоритет взаимной ценности, общим стандартам и долгосрочной совместимости, а не краткосрочной выручке."),
        ("Бескомпромиссная прозрачность", "Мы общаемся прямо, ясно и честно. Клиенты всегда получают понятные ответы, полную ясность по издержкам и объективную оценку рисков."),
        ("Прикладной финансовый интеллект", "Мы соединяем глубокие исследования, активный мониторинг рисков и институциональный доступ к рынкам с практическим человеческим суждением в каждом решении."),
        ("Ответственность и выполнимость", "Мы обещаем только то, за что можем отвечать, и несём полную персональную ответственность за качество, точность и надёжность исполнения."),
        ("Интегрированное партнёрство", "Мы объединяем современную цифровую инфраструктуру с прямым доступом к опытным профессионалам, и отношения развиваются вместе с потребностями клиентов."),
    ],
    personality=[
        ("Надёжность и безопасность", "Спокойствие, стабильность и строгая дисциплина. Уверенность рождается из европейских регуляторных стандартов, сохранности активов и операционного совершенства, а не из громких обещаний."),
        ("Компетентность и опыт", "Аналитичность, вдумчивость и ясность формулировок. Экспертиза видна в качестве исполнения и рыночных суждений."),
        ("Внимание к человеку", "Тепло, доступность и отзывчивость. Каждый клиент — индивидуальный партнёр, а не номер счёта."),
        ("Спокойствие и сдержанность", "Выдержка, отсутствие показного и уважение к частной жизни в условиях высоких ставок и меняющихся рынков."),
        ("Глобальность и профессионализм", "Международная релевантность и институциональная репутация в крупных финансовых центрах при ясном и доступном стиле общения."),
    ],
    about=dict(
        title="О компании",
        desc="MBK Capital — инвестиционная компания на Кипре под регулированием CySEC, сочетающая институциональные стандарты управления с персональным сервисом, профессиональной инфраструктурой и доступом к глобальным рынкам.",
        h1="О компании MBK Capital",
        lede="Полноценный инвестиционный партнёр, построенный на знаниях, доверии и разумном росте.",
        why_h="Зачем мы существуем",
        why_p1="MBK Capital предлагает полноценное интегрированное инвестиционное партнёрство для состоятельных частных клиентов, семейных офисов и профессиональных трейдеров. Как инвестиционная компания, зарегистрированная на Кипре и регулируемая CySEC, мы соединяем институциональные европейские стандарты управления с гибким доступом к глобальным рынкам, современной торговой инфраструктурой и прямым персональным сервисом.",
        why_p2="Мы смотрим дальше отдельных транзакционных платформ. MBK Capital объединяет мультиактивное брокерское обслуживание, дискреционное управление портфелем, структурированные консультации, глубокую рыночную аналитику и активное управление рисками в одном скоординированном партнёрстве. Опираясь на прозрачность, дисциплинированную избирательность и человеческую экспертизу, мы внимательно слушаем, действуем точно и предлагаем решения, созданные для долгосрочного сохранения и разумного роста капитала.",
        mv_h="Миссия и видение",
        mission_h="Наша миссия",
        mission="Быть предпочтительным долгосрочным партнёром по брокерским и инвестиционным услугам для взыскательных клиентов, соединяя доверительные отношения, разумный доступ к рынкам, передовые технологии и по-настоящему персональный сервис.",
        vision_h="Наше видение",
        vision="Стать надёжным международным партнёром по брокерским и инвестиционным услугам «всё в одном», который растёт вместе со своими клиентами.",
        vision_p="Мы намерены начать с тщательно отобранной группы клиентов, создать прочную операционную основу и постепенно расширять услуги, возможности и международное присутствие. Рост измеряется не только числом клиентов или активами. Он измеряется более прочными отношениями, более широким доступом к рынкам, лучшим исполнением и более полными решениями, созданными вместе с теми, кому мы служим.",
        values_h="Наши ценности",
        behave_h="Как мы себя ведём",
        behave_lede="Характер, который вы должны узнавать в каждом взаимодействии с нами: с менеджером по работе с клиентами, трейдером или цифровой системой.",
        sel_h="Избирательность по замыслу",
        sel_p1="Мы избирательны в отношениях, контрагентах, решениях и деловых обязательствах, которые принимаем. Избирательность — это не эксклюзивность ради эксклюзивности. Это значит, что мы действуем по чётко определённым ценностям, тщательно выбираем партнёров и ставим долгосрочную совместимость выше краткосрочной выручки.",
        sel_p2="Мы готовы отказаться от проектов, которые неуместны, неустойчивы или противоречат нашим принципам, и говорим об этом прямо. Клиенты могут рассчитывать на откровенность, коммерческую ясность и реалистичные обещания.",
        cy_h="Кипрская основа, международный взгляд",
        cy_p1="MBK Capital учреждена на Кипре и работает в европейском регуляторном поле под надзором Кипрской комиссии по ценным бумагам и биржам. Эта основа даёт нашим клиентам управление, защиту инвесторов и операционную дисциплину, которых ожидают от европейского финансового института.",
        cy_p2="Кипр — наша регулируемая база, а не предел амбиций. Мы созданы для международной клиентской базы и планируем выход в другие юрисдикции по мере развития бизнеса, при получении соответствующих разрешений.",
        reg_link="Регуляторная информация",
    ),
    services_page=dict(
        title="Услуги",
        desc="Мультиактивное брокерское обслуживание, инвестиционные консультации, дискреционное управление портфелем, аналитика, активное управление рисками и поддержка семейных офисов от MBK Capital.",
        h1="Услуги",
        lede="Брокерское обслуживание, консультации, управление портфелем, аналитика и управление рисками как одно скоординированное партнёрство.",
        close_h="Только то, за что мы отвечаем",
        close_p="Мы сосредоточены на решениях, которые понимаем, можем качественно реализовать и за которые готовы отвечать. Если услуга, продукт или ожидание вам не подходят, мы так и скажем.",
        close_note="Услуги предоставляются в рамках регуляторных разрешений MBK Capital и с учётом оценки соответствия и уместности для клиента. Доступность отдельных инструментов, рынков и услуг может зависеть от категории клиента и юрисдикции.",
        close_btn="Обсудить ваши задачи", close_link="С кем мы работаем",
    ),
    clients=dict(
        title="Клиенты",
        desc="MBK Capital работает с состоятельными частными клиентами, семейными офисами, управляющими капиталом, профессиональными трейдерами и опытными инвесторами в формате персонального интегрированного брокерского партнёрства.",
        h1="Клиенты",
        lede="Две одинаково важные для нас аудитории: частный капитал и профессиональные участники рынка.",
        a1_h="Частные клиенты и семейные офисы",
        a1_p="Предприниматели, владельцы бизнеса, топ-менеджеры, частные инвесторы и владельцы семейного капитала нескольких поколений, а также семейные офисы, независимые управляющие и консультанты, которые их представляют.",
        matters="Что для вас важно",
        a1_items=["Сохранение и разумный рост капитала", "Доступ к разным классам активов и рынкам через одно партнёрство", "Конфиденциальный, надёжный сервис и прямой доступ к опытным профессионалам", "Уверенность в регуляторной и операционной основе", "Аналитика, стратегические идеи, поддержка в управлении портфелем и рисками", "Прозрачные издержки и процессы, быстрые и компетентные ответы"],
        a1_close="Вы никогда не должны чувствовать себя стандартным розничным клиентом. Сервис, коммуникация и решения учитывают ваши обстоятельства, опыт, портфель и предпочтительный формат работы.",
        a2_h="Профессиональные трейдеры и опытные инвесторы",
        a2_p="Профессиональные трейдеры, активные частные инвесторы, портфельные управляющие, руководители фондов, управляющие капиталом и опытные трейдеры деривативами, включая клиентов с крупными портфелями или высокими торговыми оборотами.",
        a2_items=["Надёжное исполнение и конкурентные условия", "Доступ к широкому набору инструментов и качественным контрагентам", "Профессиональная торговая инфраструктура, рыночные данные и аналитика", "Отзывчивые команды дилинга и поддержки", "Гибкие структуры счетов и отчётности с адекватным риск-контролем", "Доступ к нестандартным возможностям и инвестиционным решениям"],
        a2_close="Торговля, отчётность и работа с клиентом интегрированы, поэтому вас не передают между разрозненными системами и командами.",
        fo_h="Семейные офисы и управляющие капиталом",
        fo_p="Мы поддерживаем уполномоченных представителей: консолидированные брокерские отношения, исполнение и отчётность, индивидуальные структуры счетов и профессиональное взаимодействие при сложных структурах владения и инвестирования.",
        fo_link="Поддержка семейных офисов и управляющих",
        em_h="Начинающие инвесторы",
        em_p="Мы также работаем с небольшим числом растущих состоятельных инвесторов, которым нужны более консультационные отношения: помощь в формировании портфеля, выборе стратегии, понимании рисков и структурированный доступ к финансовым рынкам с постепенным расширением услуг по мере развития отношений.",
        em_note="Критерии принятия, уровень сервиса и уместность продуктов зависят от опыта, капитала и целей клиента. Минимальный размер отношений обсуждается индивидуально.",
        steps_h="Как стать клиентом",
        steps=[("Вводный разговор", "Мы обсуждаем ваши цели, опыт и предпочтительный формат работы и прямо говорим, подходим ли мы вам как партнёр."),
               ("Оценка соответствия и документы", "Категоризация клиента, оценка соответствия или уместности, проверка личности и источника средств, организованные так, чтобы беречь ваше время."),
               ("Структура счёта и доступ", "Счета, мандаты и отчётность настраиваются под вашу структуру; вы получаете доступ к личному кабинету и своей команде."),
               ("Развитие отношений", "Услуги, доступ и возможности развиваются вместе с вашим капиталом, опытом и потребностями.")],
        steps_btn="Обсудить задачи",
    ),
    regulation=dict(
        title="Регулирование и защита клиентов",
        desc="Регуляторный статус MBK Capital, требования MiFID II, защита клиентов, наилучшее исполнение, конфликты интересов, порядок рассмотрения жалоб и регуляторные документы.",
        h1="Регулирование и защита клиентов",
        lede="Безопасность, понимание рисков, регулирование, конфиденциальность и операционная дисциплина лежат в основе каждого клиентского отношения.",
        aside=[("#status", "Регуляторный статус"), ("#framework", "Регуляторная база"), ("#protection", "Защита клиентов"),
               ("#execution", "Наилучшее исполнение и конфликты"), ("#complaints", "Жалобы"), ("#documents", "Документы"), ("#risk", "Предупреждение о рисках")],
        on_page="На этой странице",
        status_h="Регуляторный статус",
        status_p=('MBK Capital Ltd зарегистрирована в Республике Кипр под номером <span class="placeholder">HE 000000</span>, '
                  'юридический адрес: <span class="placeholder">[адрес], Кипр</span>. Разрешение компании можно проверить в реестре '
                  'регулируемых организаций CySEC на сайте <a href="https://www.cysec.gov.cy" rel="noopener">cysec.gov.cy</a>.'),
        status_note="Заявления о регулировании, лицензиях, услугах и юрисдикциях на этом сайте будут приведены в соответствие с фактическими разрешениями и регуляторным статусом компании на момент публикации. Выделенные фрагменты ожидают подтверждения.",
        fw_h="Регуляторная база",
        fw_p1="Как кипрская инвестиционная компания, MBK Capital работает в соответствии с Законом об инвестиционных услугах и деятельности и регулируемых рынках 2017 года (Закон 87(I)/2017), который имплементирует Директиву о рынках финансовых инструментов (MiFID II) в законодательство Кипра, а также с директивами и циркулярами CySEC.",
        fw_p2="Клиенты классифицируются как розничные, профессиональные или приемлемые контрагенты. Категория определяет уровень регуляторной защиты, а также услуги и инструменты, которые могут быть уместны. Клиент может запросить иную категорию при соблюдении критериев, изложенных в нашей политике категоризации клиентов.",
        fw_p3="Прежде чем предоставлять инвестиционные консультации или управление портфелем, мы оцениваем соответствие: ваши знания и опыт, финансовое положение и инвестиционные цели. Перед предоставлением других услуг по сложным инструментам мы оцениваем уместность. Мы можем отказать в услуге, если оценка показывает, что она вам не подходит.",
        prot_h="Защита клиентов",
        seg_h="Разделение активов клиентов",
        seg_p="Средства клиентов хранятся на отдельных клиентских счетах в кредитных учреждениях, обособленно от собственных средств компании. Финансовые инструменты клиентов хранятся у кастодианов на счетах, идентифицирующих их как принадлежащие клиентам. Сверки проводятся регулярно.",
        icf_h="Фонд компенсации инвесторов",
        icf_p="MBK Capital является участником Фонда компенсации инвесторов для клиентов кипрских инвестиционных компаний. Фонд покрывает клиентов, имеющих право на компенсацию, в пределах, установленных законом, если компания-участник не может выполнить свои обязательства. Профессиональные клиенты и приемлемые контрагенты, как правило, не покрываются. Подробности — в нашем уведомлении о Фонде компенсации инвесторов.",
        sec_h="Информационная безопасность и конфиденциальность",
        sec_p='Мы защищаем информацию клиентов и операционную целостность с помощью профессиональных систем, контролей и ответственного поведения. Наша <a href="legal.html#privacy">политика конфиденциальности</a> объясняет, как обрабатываются персональные данные.',
        exec_h="Наилучшее исполнение и конфликты интересов",
        exec_p1="Исполняя поручения клиентов или передавая их для исполнения другим организациям, мы предпринимаем все достаточные меры для достижения наилучшего возможного результата с учётом цены, издержек, скорости, вероятности исполнения и расчётов, объёма, характера и любых других значимых факторов. Наша политика исполнения поручений описывает используемые площадки и контрагентов.",
        exec_p2="Мы поддерживаем политику в отношении конфликтов интересов и организационные меры, позволяющие выявлять, предотвращать и контролировать конфликты между компанией, её сотрудниками и клиентами или между клиентами. Если эти меры недостаточны для предотвращения риска ущерба интересам клиента, мы раскрываем конфликт до совершения действий.",
        comp_h="Жалобы",
        comp_p1='Если вас не устраивает какой-либо аспект нашего сервиса, сообщите нам. Жалобы принимаются в письменной форме на <a href="mailto:complaints@mbkcapital.com">complaints@mbkcapital.com</a> или по почте на наш юридический адрес. Мы оперативно подтверждаем получение, беспристрастно рассматриваем жалобу и отвечаем письменно в сроки, установленные CySEC.',
        comp_p2="Если вас не удовлетворит наш окончательный ответ, вы можете обратиться к Финансовому омбудсмену Республики Кипр или в CySEC в порядке, описанном в нашей процедуре рассмотрения жалоб.",
        docs_h="Документы", doc_col1="Документ", doc_col2="Содержание", pdf="PDF",
        docs=[("Условия обслуживания", "Общие условия предоставления инвестиционных услуг."),
              ("Политика категоризации клиентов", "Как клиенты классифицируются как розничные, профессиональные или приемлемые контрагенты по MiFID II и какая защита применяется."),
              ("Политика исполнения поручений", "Как мы добиваемся наилучшего результата при исполнении поручений клиентов."),
              ("Политика в отношении конфликтов интересов", "Как мы выявляем, предотвращаем и контролируем конфликты интересов."),
              ("Раскрытие рисков", "Характер и риски финансовых инструментов, которые мы предлагаем."),
              ("Процедура рассмотрения жалоб", "Как подать жалобу и как она будет рассмотрена."),
              ("Уведомление о Фонде компенсации инвесторов", "Покрытие, доступное клиентам, имеющим на него право."),
              ("Заявление о защите активов клиентов", "Как хранятся и защищаются средства и финансовые инструменты клиентов."),
              ("Раскрытие издержек и сборов", "Предварительная и последующая информация об издержках и сборах."),
              ("Политика конфиденциальности", "Как мы обрабатываем персональные данные.")],
        docs_note="Ссылки на документы — заглушки до утверждения финальных версий комплаенсом.",
        risk_h="Предупреждение о рисках",
        risk_p2="Деривативы, структурные продукты и инструменты с кредитным плечом несут дополнительные риски, включая возможность убытков, превышающих первоначальные вложения. Инвестиции в иностранной валюте также подвержены риску курсовых колебаний. Пожалуйста, ознакомьтесь с нашим раскрытием рисков перед началом торговли.",
    ),
    legal=dict(
        title="Правовая информация", desc="Условия использования, политика конфиденциальности и политика cookie сайта MBK Capital.",
        h1="Правовая информация", lede="Условия использования, политика конфиденциальности и политика cookie этого сайта.",
        aside=[("#terms", "Условия использования"), ("#privacy", "Политика конфиденциальности"), ("#cookies", "Политика cookie")], on_page="На этой странице",
        note="Эти тексты — черновики для проверки комплаенсом и юристами. Выделенные фрагменты ожидают подтверждения.",
        terms_h="Условия использования",
        terms_intro="Этот сайт принадлежит MBK Capital Ltd («MBK Capital», «мы»). Используя сайт, вы соглашаетесь с настоящими условиями.",
        terms=[("Только для информации", "Содержание сайта — общая информация о MBK Capital и её услугах. Оно не является инвестиционной консультацией, персональной рекомендацией, предложением или приглашением купить или продать какой-либо финансовый инструмент, и на него не следует полагаться при принятии инвестиционных решений. Услуги предоставляются только на основании письменного договора, в рамках наших регуляторных разрешений и процедур приёма клиентов."),
               ("Юрисдикция", "Сайт не адресован лицам в юрисдикциях, где его публикация или доступность противоречат местному законодательству. Посетители сайта самостоятельно отвечают за соблюдение таких ограничений."),
               ("Точность и ответственность", "Мы прилагаем разумные усилия, чтобы информация на сайте была точной на момент публикации, но не гарантируем её полноту или точность и можем менять её без уведомления. В пределах, допустимых законом, мы не несём ответственности за убытки, возникшие в связи с использованием сайта или доверием к его содержанию."),
               ("Интеллектуальная собственность", "Название и логотип MBK Capital, а также содержание сайта принадлежат MBK Capital Ltd или её лицензиарам и не могут воспроизводиться без предварительного письменного согласия."),
               ("Применимое право", "Настоящие условия регулируются правом Республики Кипр; споры относятся к исключительной юрисдикции судов Кипра.")],
        privacy_h="Политика конфиденциальности",
        privacy_intro="MBK Capital Ltd является контролёром персональных данных, собираемых через этот сайт и в ходе оказания услуг. Мы обрабатываем персональные данные в соответствии с Общим регламентом по защите данных (ЕС) 2016/679 и законодательством Кипра о защите данных.",
        collect_h="Что мы собираем и зачем",
        collect=["Контактные данные и содержание ваших обращений — чтобы ответить вам и оценить, можем ли мы с вами работать (законный интерес и действия до заключения договора).",
                 "Идентификационные, финансовые данные и сведения для оценки соответствия от клиентов и потенциальных клиентов — для выполнения обязательств по противодействию отмыванию денег, категоризации клиентов и оценке соответствия (правовая обязанность и договор).",
                 "Технические данные, такие как IP-адрес, тип браузера и посещённые страницы — для безопасности сайта и, с вашего согласия, для понимания того, как он используется (законный интерес и согласие)."],
        share_h="Передача данных",
        share_p="Мы передаём персональные данные поставщикам услуг, действующим по нашим инструкциям, контрагентам, кастодианам и банкам, когда это необходимо для оказания услуг, а также регуляторам и органам власти, когда этого требует закон. При передаче данных за пределы Европейской экономической зоны мы применяем гарантии, признанные GDPR.",
        retain_h="Сроки хранения",
        retain_p="Мы храним персональные данные столько, сколько необходимо для описанных целей и для выполнения регуляторных требований к хранению записей, которые для клиентских записей составляют, как правило, не менее пяти лет после окончания отношений.",
        rights_h="Ваши права",
        rights_p="Вы имеете право на доступ к своим персональным данным, их исправление или удаление, ограничение обработки или возражение против неё, переносимость данных, а также на отзыв согласия, если обработка основана на согласии. Вы можете подать жалобу в Офис комиссара по защите персональных данных Республики Кипр.",
        contact_h="Контакты",
        contact_p='Запросы по защите данных: <a href="mailto:privacy@mbkcapital.com">privacy@mbkcapital.com</a>. Ответственный за защиту данных: <span class="placeholder">[имя / будет назначен]</span>.',
        cookies_h="Политика cookie",
        cookies_intro="Cookie — это небольшие текстовые файлы, сохраняемые на вашем устройстве. Сайт использует следующие категории.",
        cookie_cols=("Категория", "Назначение", "Согласие"),
        cookie_rows=[("Необходимые", "Сохранение вашего выбора по cookie и безопасность сайта. Включает настройку <code>mbk-cookie-consent</code>, сохраняемую в браузере.", "Не требуется"),
                     ("Аналитические", 'Понимание того, как посетители используют сайт, чтобы улучшать его. <span class="placeholder">Аналитический инструмент пока не установлен.</span>', "Требуется")],
        cookies_close="Вы можете изменить свой выбор в любое время, очистив данные этого сайта в настройках браузера, после чего баннер согласия появится снова. Вы также можете блокировать cookie в браузере, однако некоторые части сайта могут работать некорректно.",
    ),
    contact=dict(
        title="Контакты",
        desc="Контакты MBK Capital в Лимасоле, Кипр. Напишите на info@mbkcapital.com или отправьте запрос о брокерских, консультационных услугах и управлении портфелем.",
        h1="Контакты", lede="Расскажите о своих целях. Мы прямо скажем, что можем сделать.",
        email_h="Email", phone_h="Телефон", hours="Понедельник–пятница, 09:00–18:00 (время Кипра)",
        office_h="Офис", street="[Адрес]",
        existing_h="Действующим клиентам",
        existing_p='Ваш менеджер по работе с клиентами остаётся первым контактом. Вы также можете войти в <a href="front-office.html">личный кабинет</a>.',
        complaints_h="Жалобы", complaints_link="Как рассматриваются жалобы",
        form_h="Отправить запрос",
        f_name="Имя и фамилия", f_email="Email", f_phone="Телефон (необязательно)", f_type="Кто вы",
        f_types=[("private", "Частный инвестор"), ("family-office", "Представляю семейный офис"),
                 ("professional", "Профессиональный трейдер или инвестиционный специалист"),
                 ("wealth-manager", "Управляющий капиталом или независимый управляющий"), ("other", "Другое")],
        f_message="Чем мы можем помочь?",
        f_consent='Я даю согласие на обработку MBK Capital указанной информации для ответа на мой запрос в соответствии с <a href="legal.html#privacy">политикой конфиденциальности</a>.',
        f_submit="Отправить запрос", f_reply="Отвечаем в течение одного рабочего дня.",
        f_no_endpoint="Форма пока не подключена к почтовому сервису. Пожалуйста, напишите нам на info@mbkcapital.com.",
    ),
    front=dict(
        title="Личный кабинет", desc="Вход в личный кабинет MBK Capital: счета, позиции, отчёты и сообщения.",
        h1="Личный кабинет",
        p="Войдите, чтобы увидеть счета, позиции, отчёты и сообщения от вашей команды.",
        btn="Открыть личный кабинет",
        note='MBK Capital никогда не запрашивает пароль по email или телефону. Если не удаётся войти, обратитесь к своему менеджеру или на <a href="mailto:support@mbkcapital.com">support@mbkcapital.com</a>.',
    ),
    back=dict(
        title="Бэк-офис", desc="Бэк-офис MBK Capital. Доступ только для уполномоченных сотрудников.",
        h1="Бэк-офис",
        p="Доступ только для уполномоченных сотрудников MBK Capital. Все действия протоколируются.",
        btn="Открыть бэк-офис",
        note='Если вы клиент, воспользуйтесь <a href="front-office.html">личным кабинетом</a>. Проблемы с доступом сотрудников: <a href="mailto:it@mbkcapital.com">it@mbkcapital.com</a>.',
    ),
    gateway_back="Вернуться на mbkcapital.com",
    monogram_alt="Монограмма MBK Capital",
    notfound=dict(title="Страница не найдена", desc="Запрошенная страница не найдена.",
                  h1="Страница не найдена", lede="Страница, которую вы искали, не существует или была перемещена.",
                  home="На главную", contact="Связаться с нами"),
)

# ---------------------------------------------------------------------------
# Building blocks
# ---------------------------------------------------------------------------
PORTAL_URL = "https://portal.mbkcapital.com/"
BACKOFFICE_URL = "https://backoffice.mbkcapital.com/"


def picture(P, name, alt, sizes="100vw", cls="", loading="lazy", extra=""):
    cls_attr = f' class="{cls}"' if cls else ""
    return f'''<picture>
  <source type="image/webp" srcset="{P}assets/img/{name}-1000.webp 1000w, {P}assets/img/{name}-1920.webp 1920w" sizes="{sizes}">
  <img src="{P}assets/img/{name}-1920.jpg" srcset="{P}assets/img/{name}-1000.jpg 1000w, {P}assets/img/{name}-1920.jpg 1920w" sizes="{sizes}" alt="{alt}"{cls_attr} loading="{loading}" decoding="async"{extra}>
</picture>'''


def url_for(lang, path):
    p = "" if path == "index.html" else path
    return f"{DOMAIN}/{LANGS[lang]['dir']}{p}"


def head(L, T, title, desc, path):
    P = L["prefix"]
    full = T["site_title"] if path == "index.html" else f"{title} | MBK Capital"
    robots = '\n<meta name="robots" content="noindex, nofollow"><!-- draft preview: remove before launch -->' if DRAFT else ""
    return f'''<!DOCTYPE html>
<html lang="{L["code"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url_for(L["code"], path)}">
<link rel="alternate" hreflang="en" href="{url_for("en", path)}">
<link rel="alternate" hreflang="ru" href="{url_for("ru", path)}">
<link rel="alternate" hreflang="x-default" href="{url_for("en", path)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="MBK Capital">
<meta property="og:title" content="{html.escape(full)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{DOMAIN}/assets/img/og.jpg">
<meta property="og:locale" content="{"ru_RU" if L["code"] == "ru" else "en_GB"}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#041522">{robots}
<link rel="icon" href="{P}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{P}assets/logo/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{P}assets/logo/apple-touch-icon.png">
<link rel="manifest" href="{P}site.webmanifest">
<link rel="preload" href="{P}assets/fonts/{"forum-cyrillic" if L["code"] == "ru" else "marcellus-latin"}.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{P}assets/fonts/{"tenorsans-cyrillic" if L["code"] == "ru" else "tenorsans-latin"}.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{P}assets/css/main.css">
</head>
<body>
<a class="skip-link" href="#main">{T["skip"]}</a>
'''


def lang_switch(L, path):
    return (f'<a class="lang-switch" href="{L["other_prefix"]}{path}" hreflang="{L["other"]}" lang="{L["other"]}" '
            f'title="{L["other_name"]}">{L["other_label"]}</a>')


def header(L, T, path):
    P = L["prefix"]
    items = ""
    for href, label in T["nav"]:
        cur = ' aria-current="page"' if href == path else ""
        items += f'        <li><a class="nav__link" href="{href}"{cur}>{label}</a></li>\n'
    return f'''<header class="site-header">
  <div class="container site-header__inner">
    <a class="brand" href="index.html" aria-label="{T["brand_aria"]}">
      <img src="{P}assets/logo/mbk-logo-horizontal-on-dark.svg" alt="MBK Capital" width="499" height="274">
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">
      <span class="nav-toggle__bar"></span><span class="visually-hidden">{T["menu"]}</span>
    </button>
    <nav class="nav" id="site-nav" aria-label="Main">
      <ul class="nav__list">
{items}      </ul>
      {lang_switch(L, path)}
      <a class="btn btn--outline" href="front-office.html">{T["portal"]}</a>
    </nav>
  </div>
</header>
'''


def footer(L, T):
    P = L["prefix"]
    company = "".join(f'          <li><a href="{h}">{l}</a></li>\n' for h, l in T["nav"] if h != "regulation.html")
    reg = "".join(f'          <li><a href="{h}">{l}</a></li>\n' for h, l in T["footer_reg_links"])
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="site-footer__top">
      <div class="site-footer__brand">
        <img src="{P}assets/logo/mbk-logo-horizontal-on-dark.svg" alt="MBK Capital" width="499" height="274">
        <p>{T["tagline"]}</p>
      </div>
      <div>
        <h2>{T["footer_company"]}</h2>
        <ul>
{company}        </ul>
      </div>
      <div>
        <h2>{T["footer_regulation"]}</h2>
        <ul>
{reg}        </ul>
      </div>
      <div>
        <h2>{T["footer_access"]}</h2>
        <ul>
          <li><a href="front-office.html">{T["portal"]}</a></li>
          <li><a href="back-office.html">{T["back_office"]}</a></li>
        </ul>
        <h2>{T["footer_contact"]}</h2>
        <ul>
          <li><a href="mailto:info@mbkcapital.com">info@mbkcapital.com</a></li>
          <li><a href="tel:+35700000000"><span class="placeholder">{T["phone"]}</span></a></li>
          <li><span class="placeholder">{T["city"]}</span></li>
        </ul>
      </div>
    </div>
    <div class="site-footer__bottom">
      <p class="site-footer__legal">{T["risk"]}</p>
      <p class="site-footer__legal">{T["reg_line"]} {T["reg_company"]}</p>
      <div class="site-footer__meta">
        <span>&copy; <span data-year>{YEAR}</span> {T["copyright"]}</span>
        <a href="legal.html#terms">{T["terms"]}</a>
        <a href="legal.html#privacy">{T["privacy"]}</a>
        <a href="legal.html#cookies">{T["cookies"]}</a>
      </div>
    </div>
  </div>
</footer>
<div class="cookie" id="cookie-banner" hidden role="region" aria-label="Cookie consent">
  <p>{T["cookie_text"]}</p>
  <div class="cookie__actions">
    <button class="btn btn--gold btn--small" type="button" data-consent="all">{T["cookie_all"]}</button>
    <button class="btn btn--outline btn--small" type="button" data-consent="essential">{T["cookie_essential"]}</button>
  </div>
</div>
<script src="{P}assets/js/main.js" defer></script>
</body>
</html>
'''


def write_page(L, T, path, title, desc, body, chrome=True):
    out = head(L, T, title, desc, path)
    if chrome:
        out += header(L, T, path)
    out += body
    if chrome:
        out += footer(L, T)
    else:
        out += f'<script src="{L["prefix"]}assets/js/main.js" defer></script>\n</body>\n</html>\n'
    target = os.path.join(ROOT, L["dir"], path)
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(out)


def values_list(items):
    return '<ul class="values">\n' + "".join(f'  <li><h3>{t}</h3><p>{d}</p></li>\n' for t, d in items) + '</ul>\n'


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------
def build_home(L, T):
    P, H = L["prefix"], T["home"]
    rows = "".join(f'''  <div class="dl__row">
    <dt>{name}</dt>
    <dd><p>{short}</p><a class="text-link" href="services.html#{anchor}">{link}</a></dd>
  </div>
''' for anchor, name, short, link, _intro, _items in T["services"])
    return f'''<main id="main">
<section class="hero">
  <div class="hero__panel">
    <h1 class="hero__title">{H["h1"]}</h1>
    <p class="hero__lede">{H["lede"]}</p>
    <div class="hero__actions actions">
      <a class="btn btn--gold" href="contact.html">{H["cta"]}</a>
      <a class="text-link" href="services.html">{H["cta2"]}</a>
    </div>
  </div>
  <figure class="hero__figure">
    {picture(P, "nautilus", H["hero_alt"], sizes="(max-width: 860px) 100vw, 62vw", loading="eager", extra=' fetchpriority="high"')}
  </figure>
</section>

<section class="section" id="intro">
  <div class="container phi">
    <h2 class="statement">{H["statement"]}</h2>
    <div class="prose">
      <p>{H["statement_p1"]}</p>
      <p>{H["statement_p2"]}</p>
      <p><a class="text-link" href="about.html">{H["statement_link"]}</a></p>
    </div>
  </div>
</section>

<section class="section section--mist" id="services">
  <div class="container">
    <div class="section__head">
      <h2>{H["services_h"]}</h2>
      <p class="lede">{H["services_lede"]}</p>
    </div>
    <dl class="dl">
{rows}    </dl>
  </div>
</section>

<section class="section--navy" id="clients">
  <div class="split">
    <figure class="split__figure">
      {picture(P, "hexwood", H["clients_alt"], sizes="(max-width: 860px) 100vw, 38vw")}
    </figure>
    <div class="split__body">
      <div class="section__head">
        <h2>{H["clients_h"]}</h2>
      </div>
      <div class="audience">
        <h3>{H["aud1_h"]}</h3>
        <p>{H["aud1_p"]}</p>
      </div>
      <div class="audience">
        <h3>{H["aud2_h"]}</h3>
        <p>{H["aud2_p"]}</p>
      </div>
      <div class="audience">
        <p>{H["selective"]}</p>
        <p><a class="text-link" href="clients.html">{H["clients_link"]}</a></p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="values">
  <div class="container">
    <div class="section__head">
      <h2>{H["values_h"]}</h2>
      <p class="lede">{H["values_lede"]}</p>
    </div>
{values_list(T["values"])}  </div>
</section>

<div class="reg-strip" id="regulation">
  <div class="container reg-strip__inner">
    <p>{T["reg_line"]} {H["reg_strip"]}</p>
    <a class="text-link" href="regulation.html">{H["reg_link"]}</a>
  </div>
</div>

<section class="section" id="contact">
  <div class="container phi phi--center">
    <h2 class="statement">{H["cta_h"]}</h2>
    <div>
      <p class="lede" style="margin-bottom:1.4em">{H["cta_p"]}</p>
      <div class="actions">
        <a class="btn btn--navy" href="contact.html">{H["cta_btn"]}</a>
        <a class="text-link" href="mailto:info@mbkcapital.com">info@mbkcapital.com</a>
      </div>
    </div>
  </div>
</section>
</main>
'''


def build_about(L, T):
    P, A = L["prefix"], T["about"]
    return f'''<main id="main">
<section class="page-hero">
  {picture(P, "muqarnas", "", cls="page-hero__bg", loading="eager")}
  <div class="container">
    <h1>{A["h1"]}</h1>
    <p class="lede">{A["lede"]}</p>
  </div>
</section>

<section class="section">
  <div class="container phi">
    <h2 class="statement">{A["why_h"]}</h2>
    <div class="prose">
      <p>{A["why_p1"]}</p>
      <p>{A["why_p2"]}</p>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="container phi">
    <h2 class="statement">{A["mv_h"]}</h2>
    <div class="prose">
      <h3>{A["mission_h"]}</h3>
      <p>{A["mission"]}</p>
      <h3>{A["vision_h"]}</h3>
      <p>{A["vision"]}</p>
      <p class="muted">{A["vision_p"]}</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head">
      <h2>{A["values_h"]}</h2>
    </div>
{values_list(T["values"])}  </div>
</section>

<section class="section section--mist">
  <div class="container">
    <div class="section__head">
      <h2>{A["behave_h"]}</h2>
      <p class="lede">{A["behave_lede"]}</p>
    </div>
{values_list(T["personality"])}  </div>
</section>

<section class="section">
  <div class="container phi">
    <h2 class="statement">{A["sel_h"]}</h2>
    <div class="prose">
      <p>{A["sel_p1"]}</p>
      <p>{A["sel_p2"]}</p>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="container phi">
    <h2 class="statement">{A["cy_h"]}</h2>
    <div class="prose">
      <p>{A["cy_p1"]}</p>
      <p>{A["cy_p2"]}</p>
      <p><a class="text-link" href="regulation.html">{A["reg_link"]}</a></p>
    </div>
  </div>
</section>
</main>
'''


def build_services(L, T):
    P, S = L["prefix"], T["services_page"]
    subnav = "".join(f'<li><a href="#{a}">{n}</a></li>\n' for a, n, *_ in T["services"])
    sections = ""
    for anchor, name, short, _link, intro, items in T["services"]:
        lis = "".join(f"<li>{i}</li>" for i in items)
        sections += f'''<section class="section section--tight" id="{anchor}">
  <div class="container phi">
    <h2>{name}</h2>
    <div class="prose">
      <p class="lede">{short}</p>
      <p>{intro}</p>
      <ul>{lis}</ul>
    </div>
  </div>
</section>
'''
    return f'''<main id="main">
<section class="page-hero">
  {picture(P, "waves", "", cls="page-hero__bg", loading="eager")}
  <div class="container">
    <h1>{S["h1"]}</h1>
    <p class="lede">{S["lede"]}</p>
  </div>
</section>
<div class="container" style="padding-top:clamp(32px,5vw,56px)">
  <ul class="subnav">
{subnav}  </ul>
</div>
{sections}
<section class="section section--mist">
  <div class="container phi">
    <h2 class="statement">{S["close_h"]}</h2>
    <div class="prose">
      <p>{S["close_p"]}</p>
      <p class="note">{S["close_note"]}</p>
      <div class="actions">
        <a class="btn btn--navy" href="contact.html">{S["close_btn"]}</a>
        <a class="text-link" href="clients.html">{S["close_link"]}</a>
      </div>
    </div>
  </div>
</section>
</main>
'''


def build_clients(L, T):
    P, C = L["prefix"], T["clients"]
    a1 = "".join(f"<li>{i}</li>" for i in C["a1_items"])
    a2 = "".join(f"<li>{i}</li>" for i in C["a2_items"])
    steps = "".join(f'        <li><div><h3>{t}</h3><p>{d}</p></div></li>\n' for t, d in C["steps"])
    return f'''<main id="main">
<section class="page-hero">
  {picture(P, "fins", "", cls="page-hero__bg", loading="eager")}
  <div class="container">
    <h1>{C["h1"]}</h1>
    <p class="lede">{C["lede"]}</p>
  </div>
</section>

<section class="section">
  <div class="container phi">
    <h2 class="statement">{C["a1_h"]}</h2>
    <div class="prose">
      <p>{C["a1_p"]}</p>
      <h3>{C["matters"]}</h3>
      <ul>{a1}</ul>
      <p>{C["a1_close"]}</p>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="container phi">
    <h2 class="statement">{C["a2_h"]}</h2>
    <div class="prose">
      <p>{C["a2_p"]}</p>
      <h3>{C["matters"]}</h3>
      <ul>{a2}</ul>
      <p class="muted">{C["a2_close"]}</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container phi">
    <h2 class="statement">{C["fo_h"]}</h2>
    <div class="prose">
      <p>{C["fo_p"]}</p>
      <p><a class="text-link" href="services.html#family-office">{C["fo_link"]}</a></p>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="container phi">
    <h2 class="statement">{C["em_h"]}</h2>
    <div class="prose">
      <p>{C["em_p"]}</p>
      <p class="muted">{C["em_note"]}</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container phi">
    <h2 class="statement">{C["steps_h"]}</h2>
    <div>
      <ol class="steps">
{steps}      </ol>
      <div class="actions" style="margin-top:32px">
        <a class="btn btn--navy" href="contact.html">{C["steps_btn"]}</a>
      </div>
    </div>
  </div>
</section>
</main>
'''


def build_regulation(L, T):
    P, R = L["prefix"], T["regulation"]
    aside = "".join(f'        <li><a href="{h}">{l}</a></li>\n' for h, l in R["aside"])
    docs = "".join(f'<tr><td><a href="#" class="placeholder">{t} ({R["pdf"]})</a></td><td>{d}</td></tr>' for t, d in R["docs"])
    return f'''<main id="main">
<section class="page-hero">
  {picture(P, "hexwood", "", cls="page-hero__bg", loading="eager")}
  <div class="container">
    <h1>{R["h1"]}</h1>
    <p class="lede">{R["lede"]}</p>
  </div>
</section>

<section class="section">
  <div class="container phi">
    <aside class="aside-nav" aria-label="{R["on_page"]}">
      <ul>
{aside}      </ul>
    </aside>
    <div class="prose">
      <h2 id="status">{R["status_h"]}</h2>
      <p>{T["reg_line"]}</p>
      <p>{R["status_p"]}</p>
      <p class="note">{R["status_note"]}</p>

      <h2 id="framework">{R["fw_h"]}</h2>
      <p>{R["fw_p1"]}</p>
      <p>{R["fw_p2"]}</p>
      <p>{R["fw_p3"]}</p>

      <h2 id="protection">{R["prot_h"]}</h2>
      <h3>{R["seg_h"]}</h3>
      <p>{R["seg_p"]}</p>
      <h3>{R["icf_h"]}</h3>
      <p>{R["icf_p"]}</p>
      <h3>{R["sec_h"]}</h3>
      <p>{R["sec_p"]}</p>

      <h2 id="execution">{R["exec_h"]}</h2>
      <p>{R["exec_p1"]}</p>
      <p>{R["exec_p2"]}</p>

      <h2 id="complaints">{R["comp_h"]}</h2>
      <p>{R["comp_p1"]}</p>
      <p>{R["comp_p2"]}</p>

      <h2 id="documents">{R["docs_h"]}</h2>
      <div class="table-wrap">
      <table>
        <thead><tr><th>{R["doc_col1"]}</th><th>{R["doc_col2"]}</th></tr></thead>
        <tbody>{docs}</tbody>
      </table>
      </div>
      <p class="note">{R["docs_note"]}</p>

      <h2 id="risk">{R["risk_h"]}</h2>
      <p>{T["risk"]}</p>
      <p>{R["risk_p2"]}</p>
    </div>
  </div>
</section>
</main>
'''


def build_legal(L, T):
    G = T["legal"]
    aside = "".join(f'        <li><a href="{h}">{l}</a></li>\n' for h, l in G["aside"])
    terms = "".join(f"      <h3>{h}</h3>\n      <p>{p}</p>\n" for h, p in G["terms"])
    collect = "".join(f"        <li>{i}</li>\n" for i in G["collect"])
    c1, c2, c3 = G["cookie_cols"]
    rows = "".join(f"          <tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>\n" for a, b, c in G["cookie_rows"])
    return f'''<main id="main">
<section class="page-hero">
  <div class="container">
    <h1>{G["h1"]}</h1>
    <p class="lede">{G["lede"]}</p>
  </div>
</section>

<section class="section">
  <div class="container phi">
    <aside class="aside-nav" aria-label="{G["on_page"]}">
      <ul>
{aside}      </ul>
    </aside>
    <div class="prose">
      <p class="note">{G["note"]}</p>

      <h2 id="terms">{G["terms_h"]}</h2>
      <p>{G["terms_intro"]}</p>
{terms}
      <h2 id="privacy">{G["privacy_h"]}</h2>
      <p>{G["privacy_intro"]}</p>
      <h3>{G["collect_h"]}</h3>
      <ul>
{collect}      </ul>
      <h3>{G["share_h"]}</h3>
      <p>{G["share_p"]}</p>
      <h3>{G["retain_h"]}</h3>
      <p>{G["retain_p"]}</p>
      <h3>{G["rights_h"]}</h3>
      <p>{G["rights_p"]}</p>
      <h3>{G["contact_h"]}</h3>
      <p>{G["contact_p"]}</p>

      <h2 id="cookies">{G["cookies_h"]}</h2>
      <p>{G["cookies_intro"]}</p>
      <div class="table-wrap">
      <table>
        <thead><tr><th>{c1}</th><th>{c2}</th><th>{c3}</th></tr></thead>
        <tbody>
{rows}        </tbody>
      </table>
      </div>
      <p>{G["cookies_close"]}</p>
    </div>
  </div>
</section>
</main>
'''


def build_contact(L, T):
    P, K = L["prefix"], T["contact"]
    opts = "".join(f'              <option value="{v}">{l}</option>\n' for v, l in K["f_types"])
    return f'''<main id="main">
<section class="page-hero">
  {picture(P, "agave", "", cls="page-hero__bg", loading="eager")}
  <div class="container">
    <h1>{K["h1"]}</h1>
    <p class="lede">{K["lede"]}</p>
  </div>
</section>

<section class="section">
  <div class="container phi">
    <div>
      <ul class="contact-list">
        <li><strong>{K["email_h"]}</strong><a href="mailto:info@mbkcapital.com">info@mbkcapital.com</a></li>
        <li><strong>{K["phone_h"]}</strong><a href="tel:+35700000000"><span class="placeholder">{T["phone"]}</span></a><br><span class="small">{K["hours"]}</span></li>
        <li><strong>{K["office_h"]}</strong><span class="placeholder">{K["street"]}<br>{T["city"]}</span></li>
        <li><strong>{K["existing_h"]}</strong>{K["existing_p"]}</li>
        <li><strong>{K["complaints_h"]}</strong><a href="mailto:complaints@mbkcapital.com">complaints@mbkcapital.com</a><br><span class="small"><a href="regulation.html#complaints">{K["complaints_link"]}</a></span></li>
      </ul>
    </div>
    <div>
      <h2>{K["form_h"]}</h2>
      <form class="form" id="contact-form" method="post" action="#" data-endpoint="" data-msg-no-endpoint="{html.escape(K["f_no_endpoint"])}" novalidate>
        <div class="form__row">
          <div class="field"><label for="f-name">{K["f_name"]}</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
          <div class="field"><label for="f-email">{K["f_email"]}</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
        </div>
        <div class="form__row">
          <div class="field"><label for="f-phone">{K["f_phone"]}</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
          <div class="field"><label for="f-type">{K["f_type"]}</label>
            <select id="f-type" name="client_type">
{opts}            </select>
          </div>
        </div>
        <div class="field"><label for="f-message">{K["f_message"]}</label><textarea id="f-message" name="message" required></textarea></div>
        <label class="checkbox"><input type="checkbox" name="consent" required><span>{K["f_consent"]}</span></label>
        <p class="form__status" id="form-status" hidden></p>
        <div class="actions">
          <button class="btn btn--navy" type="submit">{K["f_submit"]}</button>
          <span class="small muted">{K["f_reply"]}</span>
        </div>
      </form>
    </div>
  </div>
</section>
</main>
'''


def build_gateway(L, T, G, url, path):
    P = L["prefix"]
    return f'''<main id="main" class="gateway">
  {picture(P, "fins", "", cls="gateway__bg", loading="eager")}
  <div class="gateway__panel">
    <a href="index.html" aria-label="{T["brand_aria"]}"><img class="gateway__mark" src="{P}assets/logo/mbk-monogram-on-dark.svg" alt="{T["monogram_alt"]}" width="175" height="274"></a>
    <h1>{G["h1"]}</h1>
    <p>{G["p"]}</p>
    <div class="gateway__actions">
      <a class="btn btn--gold btn--block" href="{url}" rel="noopener">{G["btn"]}</a>
    </div>
    <p class="gateway__note">{G["note"]}</p>
    <p class="gateway__links"><a class="gateway__back" href="index.html">{T["gateway_back"]}</a> {lang_switch(L, path)}</p>
  </div>
</main>
'''


def build_notfound(L, T):
    N = T["notfound"]
    return f'''<main id="main">
<section class="page-hero">
  <div class="container">
    <h1>{N["h1"]}</h1>
    <p class="lede">{N["lede"]}</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="actions">
      <a class="btn btn--navy" href="index.html">{N["home"]}</a>
      <a class="text-link" href="contact.html">{N["contact"]}</a>
    </div>
  </div>
</section>
</main>
'''


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------
def build():
    for code, L in LANGS.items():
        T = CONTENT[code]
        write_page(L, T, "index.html", T["home"]["title"], T["home"]["desc"], build_home(L, T))
        write_page(L, T, "about.html", T["about"]["title"], T["about"]["desc"], build_about(L, T))
        write_page(L, T, "services.html", T["services_page"]["title"], T["services_page"]["desc"], build_services(L, T))
        write_page(L, T, "clients.html", T["clients"]["title"], T["clients"]["desc"], build_clients(L, T))
        write_page(L, T, "regulation.html", T["regulation"]["title"], T["regulation"]["desc"], build_regulation(L, T))
        write_page(L, T, "legal.html", T["legal"]["title"], T["legal"]["desc"], build_legal(L, T))
        write_page(L, T, "contact.html", T["contact"]["title"], T["contact"]["desc"], build_contact(L, T))
        write_page(L, T, "front-office.html", T["front"]["title"], T["front"]["desc"],
                   build_gateway(L, T, T["front"], PORTAL_URL, "front-office.html"), chrome=False)
        write_page(L, T, "back-office.html", T["back"]["title"], T["back"]["desc"],
                   build_gateway(L, T, T["back"], BACKOFFICE_URL, "back-office.html"), chrome=False)
        write_page(L, T, "404.html", T["notfound"]["title"], T["notfound"]["desc"], build_notfound(L, T))
        print(f"built {code}: {len(PAGES)} pages")

    public = [p for p in PAGES if p not in ("back-office.html", "404.html")]
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n')
        for p in public:
            for code in LANGS:
                f.write(f"  <url><loc>{url_for(code, p)}</loc>\n")
                for alt in LANGS:
                    f.write(f'    <xhtml:link rel="alternate" hreflang="{alt}" href="{url_for(alt, p)}"/>\n')
                f.write("  </url>\n")
        f.write("</urlset>\n")
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /back-office.html\nDisallow: /ru/back-office.html\nSitemap: {DOMAIN}/sitemap.xml\n")
    print("sitemap.xml and robots.txt written")


if __name__ == "__main__":
    build()
