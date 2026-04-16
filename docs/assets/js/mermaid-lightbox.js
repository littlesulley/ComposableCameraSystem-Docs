/**
 * Mermaid diagram lightbox — click any rendered mermaid diagram to view
 * it fullscreen in an overlay. Click the overlay (or press Escape) to close.
 *
 * Waits for mermaid to finish rendering (MutationObserver on <svg> insertion)
 * before attaching click handlers.
 */
(function () {
  "use strict";

  function createOverlay() {
    var overlay = document.createElement("div");
    overlay.className = "mermaid-lightbox-overlay";
    overlay.addEventListener("click", function () {
      overlay.classList.remove("active");
      setTimeout(function () {
        overlay.remove();
      }, 250);
    });
    document.addEventListener("keydown", function handler(e) {
      if (e.key === "Escape" && overlay.parentNode) {
        overlay.classList.remove("active");
        setTimeout(function () {
          overlay.remove();
        }, 250);
        document.removeEventListener("keydown", handler);
      }
    });
    return overlay;
  }

  function attachClickHandler(mermaidDiv) {
    if (mermaidDiv.dataset.lightboxBound) return;
    mermaidDiv.dataset.lightboxBound = "true";
    mermaidDiv.addEventListener("click", function () {
      var svg = mermaidDiv.querySelector("svg");
      if (!svg) return;
      var overlay = createOverlay();
      var clone = svg.cloneNode(true);
      // Remove fixed dimensions so CSS max-width/max-height can govern sizing
      clone.removeAttribute("width");
      clone.style.width = "auto";
      clone.style.height = "auto";
      overlay.appendChild(clone);
      document.body.appendChild(overlay);
      // Trigger transition on next frame
      requestAnimationFrame(function () {
        overlay.classList.add("active");
      });
    });
  }

  function bindAll() {
    var diagrams = document.querySelectorAll("div.mermaid");
    for (var i = 0; i < diagrams.length; i++) {
      // Only bind once mermaid has rendered the SVG inside
      if (diagrams[i].querySelector("svg")) {
        attachClickHandler(diagrams[i]);
      }
    }
  }

  // Mermaid renders asynchronously — observe DOM for SVG insertion
  var observer = new MutationObserver(function () {
    bindAll();
  });

  // Run on DOMContentLoaded and also observe for late renders
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      bindAll();
      observer.observe(document.body, { childList: true, subtree: true });
    });
  } else {
    bindAll();
    observer.observe(document.body, { childList: true, subtree: true });
  }
})();
