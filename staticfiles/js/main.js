// Entry point for frontend JavaScript.

// iOS Blend Mode Fallback
(function() {
    var ua = window.navigator.userAgent;
    var iOS = /iPad|iPhone|iPod/.test(ua) && !window.MSStream;
    if (iOS) {
        document.body.classList.add('ios-blend-fallback');
    }
})();