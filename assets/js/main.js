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
      if (window.innerWidth > 1024) closeNav();
    });
  }

  /* Markets tabs ------------------------------------------------------ */
  var tablist = document.querySelector("[data-tabs]");
  if (tablist) {
    var tabs = Array.prototype.slice.call(tablist.querySelectorAll("[role=tab]"));
    var panels = tabs.map(function (t) { return document.getElementById(t.getAttribute("aria-controls")); });

    function select(tab, focus) {
      tabs.forEach(function (t, i) {
        var on = t === tab;
        t.setAttribute("aria-selected", on ? "true" : "false");
        t.setAttribute("tabindex", on ? "0" : "-1");
        if (panels[i]) panels[i].hidden = !on;
      });
      if (focus) tab.focus();
    }

    tabs.forEach(function (tab, i) {
      tab.addEventListener("click", function (e) {
        e.preventDefault();
        select(tab, false);
        if (history.replaceState) history.replaceState(null, "", tab.getAttribute("href"));
      });
      tab.addEventListener("keydown", function (e) {
        var j = i;
        if (e.key === "ArrowRight") j = (i + 1) % tabs.length;
        else if (e.key === "ArrowLeft") j = (i - 1 + tabs.length) % tabs.length;
        else if (e.key === "Home") j = 0;
        else if (e.key === "End") j = tabs.length - 1;
        else return;
        e.preventDefault();
        select(tabs[j], true);
        if (history.replaceState) history.replaceState(null, "", tabs[j].getAttribute("href"));
      });
    });

    function fromHash() {
      var id = (location.hash || "").slice(1);
      var match = tabs.filter(function (t) { return t.getAttribute("aria-controls") === id; })[0];
      select(match || tabs[0], false);
    }
    window.addEventListener("hashchange", fromHash);
    fromHash();
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
    var noEndpointMsg = form.getAttribute("data-msg-no-endpoint") ||
      "The enquiry form is not connected to a mail service yet. Please email us at info@mbkcapital.com.";
    if (endpoint) {
      form.setAttribute("action", endpoint);
    } else {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        if (status) {
          status.hidden = false;
          status.textContent = noEndpointMsg;
        }
      });
    }
  }
})();
