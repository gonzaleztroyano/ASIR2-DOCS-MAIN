  var _paq = window._paq = window._paq || [];
  /* tracker methods like "setCustomDimension" should be called before "trackPageView" */
  _paq.push(["setDocumentTitle", document.domain + "/" + document.title]);
  _paq.push(["setCookieDomain", "*.gonzaleztroyano.es"]);
  _paq.push(["setDomains", ["*.gonzaleztroyano.es","*.asir.gonzaleztroyano.es","*.blog.gonzaleztroyano.es","*.cgis.gonzaleztroyano.es","*.iaw.gonzaleztroyano.es","*.pfc.gonzaleztroyano.es","*.syad.gonzaleztroyano.es"]]);
  _paq.push(["setExcludedQueryParams", ["_gl"]]);
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var u="//stats.gonzaleztroyano.es/";
    _paq.push(['setTrackerUrl', u+'matomo.php']);
    _paq.push(['setSiteId', '1']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.async=true; g.src=u+'matomo.js'; s.parentNode.insertBefore(g,s);
  })();