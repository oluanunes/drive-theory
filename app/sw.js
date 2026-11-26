/* DRIVE THEORY - service worker. Mude CACHE ao alterar a lista de arquivos. */
const CACHE = 'drive-theory-v1';
const SHELL = [
  './', 'index.html', 'style.css', 'app.js', 'manifest.webmanifest',
  'icons/icon.svg', 'icons/icon-192.png', 'icons/icon-512.png',
  'icons/icon-maskable-512.png', 'icons/apple-touch-icon.png'
];
const DATA = ['data/content.json'];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE).then((c) =>
      Promise.all(SHELL.concat(DATA).map((u) =>
        fetch(u, { cache: 'reload' }).then((r) => { if (r.ok) return c.put(u, r); })
          .catch(() => {})))
    ).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((ks) => Promise.all(ks.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;

  // Conteudo: rede primeiro (regras validadas mudam), cache se offline.
  if (url.pathname.includes('/data/')) {
    e.respondWith(
      fetch(req, { cache: 'no-cache' }).then((r) => {
        if (r.ok) { const copy = r.clone(); caches.open(CACHE).then((c) => c.put(req, copy)); }
        return r;
      }).catch(() => caches.match(req, { ignoreSearch: true }))
    );
    return;
  }

  // Resto: cache primeiro, atualiza em segundo plano.
  e.respondWith(
    caches.match(req, { ignoreSearch: true }).then((hit) => {
      const net = fetch(req).then((r) => {
        if (r.ok) { const copy = r.clone(); caches.open(CACHE).then((c) => c.put(req, copy)); }
        return r;
      }).catch(() => hit);
      return hit || net;
    })
  );
});
