/* MBK Capital — site behaviour (no dependencies) */
(function () {
  "use strict";

  /* Mobile navigation ------------------------------------------------- */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");

  function closeNav() {
    if (!nav || !toggle) return;
    nav.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
    document.body.classList.remove("nav-open");
  }

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
      document.body.classList.toggle("nav-open", open);
    });
    nav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", closeNav);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) {
        closeNav();
        toggle.focus();
      }
    });
    window.addEventListener("resize", function () {
      if (window.innerWidth > 900) closeNav();
    });
  }

  /* Cookie consent ----------------------------------------------------- */
  var banner = document.getElementById("cookie-banner");
  var KEY = "mbk-cookie-consent";
  var stored = null;
  try { stored = window.localStorage.getItem(KEY); } catch (e) { /* storage unavailable */ }

  /* Automated browsers (crawlers, screenshot tools) do not need the banner. */
  if (banner && !stored && !navigator.webdriver) {
    banner.hidden = false;
    banner.querySelectorAll("[data-consent]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var record = { choice: btn.getAttribute("data-consent"), at: new Date().toISOString() };
        try { window.localStorage.setItem(KEY, JSON.stringify(record)); } catch (e) { /* ignore */ }
        banner.hidden = true;
        /* Hook: load analytics here only when record.choice === "all". */
      });
    });
  }

  /* Current year in the footer ---------------------------------------- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  /* Enquiry form ------------------------------------------------------- */
  /* Static site: set data-endpoint on the <form> to a form service URL
     (e.g. Formspree, Basin, Netlify Forms) to make submissions work. */
  var form = document.getElementById("contact-form");
  if (form) {
    var endpoint = form.getAttribute("data-endpoint");
    var status = document.getElementById("form-status");
    if (endpoint) {
      form.setAttribute("action", endpoint);
    } else {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        if (status) {
          status.hidden = false;
          status.textContent =
            "The enquiry form is not connected to a mail service yet. Please email us at info@mbkcapital.com.";
        }
      });
    }
  }
})();
