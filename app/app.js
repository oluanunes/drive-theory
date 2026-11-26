'use strict';
/* DRIVE THEORY - PWA sem framework. Telas: Início, Aprender, Praticar, Erros. */
(() => {
  const $ = (s) => document.querySelector(s);
  const view = $('#view');

  // ------------------------------------------------------------------ util
  function h(tag, props, ...kids) {
    const el = document.createElement(tag);
    for (const [k, v] of Object.entries(props || {})) {
      if (v == null || v === false) continue;
      if (k === 'class') el.className = v;
      else if (k === 'text') el.textContent = v;
      else if (k.startsWith('on')) el.addEventListener(k.slice(2), v);
      else if (v === true) el.setAttribute(k, '');
      else el.setAttribute(k, v);
    }
    for (const kid of kids.flat()) {
      if (kid == null || kid === false) continue;
      el.append(kid.nodeType ? kid : document.createTextNode(String(kid)));
    }
    return el;
  }
  const plural = (n, s, p) => `${n} ${n === 1 ? s : p}`;
  const shuffle = (a) => {
    const r = a.slice();
    for (let i = r.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [r[i], r[j]] = [r[j], r[i]];
    }
    return r;
  };
  const safeUrl = (u) => (typeof u === 'string' && /^https:\/\//i.test(u) ? u : null);
  const fmtDate = (iso) => {
    try { return new Date(iso).toLocaleDateString('pt-BR'); } catch (e) { return ''; }
  };

  // ------------------------------------------------- progresso (IndexedDB)
  const Store = {
    mode: 'memoria', db: null, map: new Map(), problema: null,
    async init(name) {
      try {
        if (!window.indexedDB) throw new Error('IndexedDB indisponível');
        this.db = await new Promise((res, rej) => {
          const t = setTimeout(() => rej(new Error('tempo esgotado ao abrir o banco')), 4000);
          const r = indexedDB.open(name, 1);
          r.onupgradeneeded = () => { r.result.createObjectStore('progresso', { keyPath: 'id' }); };
          r.onsuccess = () => { clearTimeout(t); res(r.result); };
          r.onerror = () => { clearTimeout(t); rej(r.error || new Error('erro ao abrir o banco')); };
          r.onblocked = () => { clearTimeout(t); rej(new Error('banco bloqueado')); };
        });
        const all = await new Promise((res, rej) => {
          const rq = this.db.transaction('progresso', 'readonly').objectStore('progresso').getAll();
          rq.onsuccess = () => res(rq.result || []);
          rq.onerror = () => rej(rq.error);
        });
        all.forEach((r) => this.map.set(r.id, r));
        this.mode = 'indexeddb';
      } catch (e) {
        this.db = null; this.mode = 'memoria'; this.problema = String((e && e.message) || e);
      }
    },
    get(id) { return this.map.get(id) || null; },
    async put(rec) {
      this.map.set(rec.id, rec);
      if (!this.db) return;
      try {
        await new Promise((res, rej) => {
          const tx = this.db.transaction('progresso', 'readwrite');
          tx.objectStore('progresso').put(rec);
          tx.oncomplete = res;
          tx.onerror = () => rej(tx.error);
          tx.onabort = () => rej(tx.error || new Error('transação abortada'));
        });
      } catch (e) {
        this.db = null; this.mode = 'memoria'; this.problema = String((e && e.message) || e);
      }
    },
    async clear() {
      this.map.clear();
      if (!this.db) return;
      try {
        await new Promise((res, rej) => {
          const tx = this.db.transaction('progresso', 'readwrite');
          tx.objectStore('progresso').clear();
          tx.oncomplete = res;
          tx.onerror = () => rej(tx.error);
        });
      } catch (e) {
        this.db = null; this.mode = 'memoria'; this.problema = String((e && e.message) || e);
      }
    },
  };

  // ------------------------------------------------------------------ dados
  let C = null; // content.json
  let session = null;

  const qs = () => C.perguntas;
  const qsOf = (cat) => (cat && cat !== 'todas' ? qs().filter((q) => q.cat === cat) : qs());
  const isError = (q) => { const r = Store.get(q.id); return !!(r && r.erradaAlgumaVez && r.sequencia < 2); };
  const errorsOf = (cat) => qsOf(cat).filter(isError);
  const catInfo = (id) => C.categorias.find((c) => c.id === id) || { id, nome: 'Outras', regras: 0, perguntas: 0, regras_pendentes: 0, perguntas_pendentes: 0 };
  const ruleById = (id) => C.regras.find((r) => r.id === id) || null;

  function stats(list) {
    let tent = 0, ac = 0, praticadas = 0, dominadas = 0;
    for (const q of list) {
      const r = Store.get(q.id);
      if (!r) continue;
      praticadas++; tent += r.tentativas; ac += r.acertos;
      if (r.ultimoResultado) dominadas++;
    }
    return { total: list.length, praticadas, dominadas, tent, ac };
  }
  const bar = (pct, label) => h('div', { class: 'bar', role: 'progressbar', 'aria-label': label, 'aria-valuemin': '0', 'aria-valuemax': '100', 'aria-valuenow': String(Math.round(pct)) }, h('i', { style: `width:${Math.max(0, Math.min(100, pct))}%` }));

  function pendingText() {
    const p = C.pendentes;
    const parts = [];
    if (p.regras) parts.push(`${plural(p.regras, 'regra aguarda', 'regras aguardando')} validação`);
    if (p.perguntas) parts.push(`${plural(p.perguntas, 'pergunta aguarda', 'perguntas aguardando')} aprovação`);
    return parts.join(' · ');
  }
  function pendingNotice() {
    const t = pendingText();
    return t ? h('div', { class: 'notice' }, t, h('div', { class: 'small' }, 'O que não foi validado não aparece para estudo.')) : null;
  }

  // ----------------------------------------------------------------- chrome
  function setChrome(title, back, tab) {
    $('#title').textContent = title;
    const b = $('#back');
    if (back) { b.hidden = false; b.onclick = () => { location.hash = back; }; } else { b.hidden = true; b.onclick = null; }
    document.querySelectorAll('.tabbar a').forEach((a) => {
      if (a.dataset.tab === tab) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
    });
    document.title = title === 'DRIVE THEORY' ? title : `${title} · DRIVE THEORY`;
  }
  function mount(...nodes) {
    view.replaceChildren(...nodes.flat().filter(Boolean));
    window.scrollTo(0, 0);
    view.focus({ preventScroll: true });
  }
  function emptyState(title, text, actions) {
    return h('div', { class: 'empty' }, h('h2', { text: title }), h('p', { text }), actions || null);
  }

  // ------------------------------------------------------------------ Início
  function viewHome() {
    setChrome('DRIVE THEORY', null, 'home');
    const all = stats(qs());
    const nErr = errorsOf('todas').length;
    const nodes = [];

    if (!C.regras.length && !C.perguntas.length) {
      nodes.push(emptyState('Nenhum conteúdo validado ainda',
        'Este app só mostra o que tem fonte conferida e o seu OK. Assim que as primeiras regras forem validadas, elas aparecem aqui.'));
    } else {
      const pct = all.total ? (all.dominadas / all.total) * 100 : 0;
      nodes.push(h('section', { class: 'card', 'aria-labelledby': 'prog-h' },
        h('div', { class: 'eyebrow', id: 'prog-h' }, 'Progresso geral'),
        h('div', { class: 'big-num' }, `${Math.round(pct)}%`),
        h('div', { class: 'muted small' }, all.total
          ? `${all.dominadas} de ${plural(all.total, 'pergunta dominada', 'perguntas dominadas')} (última tentativa certa)`
          : 'Ainda não há perguntas aprovadas para praticar.'),
        bar(pct, 'Progresso geral'),
        all.tent ? h('div', { class: 'muted small', style: 'margin-top:10px' }, `${plural(all.tent, 'tentativa', 'tentativas')} · ${Math.round((all.ac / all.tent) * 100)}% de acerto`) : null));
    }
    nodes.push(pendingNotice());

    nodes.push(h('div', { class: 'section-title' }, 'Modos'));
    nodes.push(h('div', { class: 'mode-grid' },
      h('a', { class: 'mode', href: '#/aprender' }, h('strong', {}, 'Aprender'), h('span', {}, plural(C.regras.length, 'regra validada', 'regras validadas'))),
      h('a', { class: 'mode', href: '#/praticar' }, h('strong', {}, 'Praticar'), h('span', {}, plural(C.perguntas.length, 'pergunta', 'perguntas'))),
      h('a', { class: 'mode', href: '#/erros' }, h('strong', {}, 'Erros'), h('span', {}, nErr ? `${plural(nErr, 'pergunta', 'perguntas')} para rever` : 'Nada para rever'))));

    nodes.push(h('div', { class: 'section-title' }, 'Categorias'));
    nodes.push(h('ul', { class: 'list' }, C.categorias.map((c) => {
      const s = stats(qsOf(c.id));
      const has = c.regras || c.perguntas;
      const sub = [];
      if (has) {
        sub.push(plural(c.regras, 'regra', 'regras'));
        sub.push(c.perguntas ? `${s.dominadas}/${c.perguntas} dominadas` : 'sem perguntas');
      } else sub.push('sem conteúdo validado');
      if (c.regras_pendentes) sub.push(`${c.regras_pendentes} aguardando validação`);
      return h('li', { class: 'row' + (has ? '' : ' off') },
        h('span', { class: 'letter', 'aria-hidden': 'true' }, c.id),
        h('span', { class: 'grow' }, h('span', { class: 'name' }, c.nome), h('span', { class: 'sub' }, sub.join(' · ')),
          c.perguntas ? bar((s.dominadas / c.perguntas) * 100, `Progresso em ${c.nome}`) : null));
    })));

    // Ajustes reais: estado do armazenamento e apagar progresso
    const standalone = window.navigator.standalone === true || (window.matchMedia && window.matchMedia('(display-mode: standalone)').matches);
    const storeMsg = Store.mode === 'indexeddb'
      ? 'Seu progresso é salvo neste aparelho (IndexedDB).'
      : `Não foi possível salvar o progresso neste navegador (${Store.problema || 'motivo desconhecido'}). Ele vale só até fechar o app.`;
    nodes.push(h('div', { class: 'section-title' }, 'Dados'));
    nodes.push(h('div', { class: 'card' },
      h('p', { class: 'small' + (Store.mode === 'indexeddb' ? ' muted' : ''), style: Store.mode === 'indexeddb' ? null : 'color:var(--bad)' }, storeMsg),
      !standalone ? h('p', { class: 'small muted' }, 'Para instalar no iPhone: Safari, botão Compartilhar, "Adicionar à Tela de Início". Instalado, o iOS não limpa seus dados por inatividade.') : null,
      h('button', { class: 'btn danger', type: 'button', onclick: async () => {
        if (!window.confirm('Apagar todo o progresso deste aparelho? Isso não pode ser desfeito.')) return;
        await Store.clear(); viewHome();
      } }, 'Apagar progresso')));

    nodes.push(h('p', { class: 'foot' }, `Conteúdo gerado em ${fmtDate(C.gerado_em)} · modo ${C.modo}`));
    mount(nodes);
  }

  // ----------------------------------------------------------------- Aprender
  function viewLearnIndex() {
    setChrome('Aprender', '#/', 'aprender');
    const nodes = [pendingNotice()];
    const withRules = C.categorias.filter((c) => c.regras > 0);
    if (!withRules.length) {
      nodes.push(emptyState('Nenhuma regra validada ainda',
        'Quando você validar as primeiras regras, elas aparecem aqui, por categoria, com os termos em francês e a fonte oficial.',
        h('a', { class: 'btn', href: '#/' }, 'Voltar ao início')));
    } else {
      nodes.push(h('ul', { class: 'list' }, withRules.map((c) =>
        h('li', {}, h('a', { class: 'row', href: `#/aprender/${c.id}` },
          h('span', { class: 'letter', 'aria-hidden': 'true' }, c.id),
          h('span', { class: 'grow' }, h('span', { class: 'name' }, c.nome), h('span', { class: 'sub' }, plural(c.regras, 'regra', 'regras'))),
          h('span', { class: 'chev', 'aria-hidden': 'true' }, '›'))))));
    }
    mount(nodes);
  }

  function ruleCard(r) {
    const url = safeUrl(r.fonte && r.fonte.url);
    const f = r.fonte || {};
    const ref = [f.lei, f.rs ? `RS ${f.rs}` : null, f.artigo ? `art. ${f.artigo}` : null, f.alinea ? `al. ${f.alinea}` : null].filter(Boolean).join(' · ');
    return h('article', { class: 'card rule' },
      h('p', { class: 'text' }, r.regra_pt, r.status !== 'validado' ? h('span', { class: 'badge' }, r.status) : null),
      r.termos_fr && r.termos_fr.length ? h('div', {}, h('h3', {}, 'Em francês'), r.termos_fr.map((t) => h('span', { class: 'pill', lang: 'fr' }, `(${t})`))) : null,
      r.excecoes && r.excecoes.length ? h('div', {}, h('h3', {}, 'Exceções'), h('ul', {}, r.excecoes.map((e) => h('li', {}, e)))) : null,
      h('h3', {}, 'Fonte oficial'),
      url ? h('a', { href: url, target: '_blank', rel: 'noopener noreferrer' }, ref || 'Abrir fonte') : h('span', { class: 'muted' }, ref || 'Sem link'),
      r.verificado_em ? h('div', { class: 'muted small' }, `Verificado em ${fmtDate(r.verificado_em)}${r.versao_lei_em_vigor_desde ? ` · texto da lei em vigor desde ${fmtDate(r.versao_lei_em_vigor_desde)}` : ''}`) : null);
  }

  function viewLearnCat(letter) {
    const c = catInfo(letter);
    setChrome(c.nome, '#/aprender', 'aprender');
    const rules = C.regras.filter((r) => r.cat === letter);
    if (!rules.length) {
      mount(pendingNotice(), emptyState('Sem regras validadas nesta categoria', 'Ainda não há regras validadas aqui.', h('a', { class: 'btn', href: '#/aprender' }, 'Ver outras categorias')));
      return;
    }
    const groups = new Map();
    rules.forEach((r) => { const k = r.subtema || 'geral'; if (!groups.has(k)) groups.set(k, []); groups.get(k).push(r); });
    const nodes = [];
    for (const [sub, list] of groups) {
      nodes.push(h('div', { class: 'section-title' }, sub.replace(/-/g, ' ')));
      list.forEach((r) => nodes.push(ruleCard(r)));
    }
    mount(nodes);
  }

  // ------------------------------------------------- Praticar / Erros: índice
  function viewModeIndex(mode) {
    const isErr = mode === 'erros';
    setChrome(isErr ? 'Erros' : 'Praticar', '#/', mode);
    const list = isErr ? errorsOf('todas') : qs();
    const nodes = [];
    if (!qs().length) {
      nodes.push(pendingNotice());
      nodes.push(emptyState('Nenhuma pergunta aprovada ainda',
        'Uma pergunta só entra no treino quando está aprovada e todas as regras dela foram validadas por você.',
        h('a', { class: 'btn', href: '#/' }, 'Voltar ao início')));
      return mount(nodes);
    }
    if (isErr && !list.length) {
      nodes.push(emptyState('Nenhum erro para rever',
        'Quando você errar uma pergunta no Praticar, ela volta aqui até você acertar 2 vezes seguidas.',
        h('a', { class: 'btn primary', href: '#/praticar' }, 'Ir para Praticar')));
      return mount(nodes);
    }
    nodes.push(h('p', { class: 'muted small' }, isErr
      ? 'Só as perguntas que você errou. Cada uma sai da lista depois de 2 acertos seguidos.'
      : 'Perguntas de resposta múltipla: marque todas as alternativas certas (pode ser nenhuma). A pergunta só conta como certa se todas as marcações estiverem certas.'));
    nodes.push(h('a', { class: 'btn primary', href: `#/${mode}/todas` }, `${isErr ? 'Revisar' : 'Praticar'} todas (${list.length})`));
    nodes.push(h('div', { class: 'section-title' }, 'Por categoria'));
    const rows = C.categorias.map((c) => {
      const n = (isErr ? errorsOf(c.id) : qsOf(c.id)).length;
      return n ? h('li', {}, h('a', { class: 'row', href: `#/${mode}/${c.id}` },
        h('span', { class: 'letter', 'aria-hidden': 'true' }, c.id),
        h('span', { class: 'grow' }, h('span', { class: 'name' }, c.nome), h('span', { class: 'sub' }, plural(n, 'pergunta', 'perguntas'))),
        h('span', { class: 'chev', 'aria-hidden': 'true' }, '›'))) : null;
    }).filter(Boolean);
    nodes.push(h('ul', { class: 'list' }, rows));
    mount(nodes);
  }

  // ---------------------------------------------------------------- sessão
  function startSession(mode, cat) {
    const isErr = mode === 'erros';
    let list = isErr ? errorsOf(cat) : qsOf(cat);
    if (!isErr) {
      const unseen = shuffle(list.filter((q) => !Store.get(q.id)));
      const seen = list.filter((q) => Store.get(q.id)).sort((a, b) => (Store.get(a.id).ultimaTentativa || '').localeCompare(Store.get(b.id).ultimaTentativa || ''));
      list = unseen.concat(seen).slice(0, 20);
    } else list = shuffle(list);
    session = { key: `${mode}/${cat}`, mode, cat, queue: list, i: 0, cur: null, feedback: null, results: [], done: false };
    return session;
  }

  function viewSession(mode, cat) {
    const key = `${mode}/${cat}`;
    if (!session || session.key !== key) startSession(mode, cat);
    const s = session;
    const title = mode === 'erros' ? 'Erros' : 'Praticar';
    setChrome(title, `#/${mode}`, mode);
    if (!s.queue.length) {
      mount(emptyState(mode === 'erros' ? 'Nenhum erro para rever aqui' : 'Nenhuma pergunta nesta categoria',
        'Escolha outra categoria.', h('a', { class: 'btn', href: `#/${mode}` }, 'Voltar')));
      return;
    }
    if (s.done || s.i >= s.queue.length) return renderSummary(s);
    renderQuestion(s);
  }

  function renderQuestion(s) {
    const q = s.queue[s.i];
    if (!s.cur || s.cur.q !== q) s.cur = { q, order: shuffle(q.alternativas.map((_, i) => i)) };
    const rec = Store.get(q.id);
    const info = h('div', { class: 'progress-line' },
      h('span', {}, `Pergunta ${s.i + 1} de ${s.queue.length}`),
      h('span', {}, `${catInfo(q.cat).nome}`));
    const head = [info, bar(((s.i) / s.queue.length) * 100, 'Progresso da sessão'),
      h('div', { style: 'height:14px' }),
      s.mode === 'erros' && rec ? h('div', { class: 'muted small' }, `Acertos seguidos: ${rec.sequencia} de 2`) : null,
      h('h2', { class: 'q-text', id: 'q-text' }, q.enunciado),
      q.imagem ? h('img', { class: 'q-img', src: q.imagem, alt: 'Imagem da pergunta' }) : null];

    if (!s.feedback) {
      const boxes = s.cur.order.map((ai, k) => {
        const inp = h('input', { type: 'checkbox', value: String(ai), id: `alt-${k}` });
        return h('label', { class: 'alt', for: `alt-${k}` }, inp, h('span', { class: 'alt-body' }, q.alternativas[ai].texto));
      });
      const btn = h('button', { class: 'btn primary', type: 'button' }, 'Confirmar resposta');
      btn.addEventListener('click', async () => {
        btn.disabled = true;
        const marked = new Set(boxes.filter((l) => l.querySelector('input').checked).map((l) => Number(l.querySelector('input').value)));
        await submitAnswer(s, q, marked);
        renderQuestion(s);
      });
      mount(head, h('fieldset', { class: 'alts', 'aria-describedby': 'q-text' },
        h('legend', { class: 'hint' }, 'Marque todas as alternativas certas (pode ser nenhuma), depois confirme.'), boxes),
      btn,
      h('div', { class: 'btn-row' }, h('button', { class: 'btn', type: 'button', onclick: () => endSession(s) }, 'Encerrar sessão')));
      return;
    }

    // feedback
    const fb = s.feedback;
    const verdict = h('div', { class: `verdict ${fb.ok ? 'ok' : 'bad'}`, role: 'status' },
      fb.ok ? 'Correto' : 'Incorreto',
      h('small', {}, fb.ok ? 'Todas as marcações estão certas: 3 pontos no formato do exame.' : 'Basta uma marcação errada ou faltando: 0 pontos no formato do exame.'),
      s.mode === 'erros' ? h('small', {}, fb.ok
        ? (fb.seq >= 2 ? 'Acertou 2 vezes seguidas: saiu da lista de erros.' : `Acerto seguido ${fb.seq} de 2. Precisa de mais um para sair da lista.`)
        : 'O contador de acertos seguidos voltou a 0.') : (fb.ok ? null : h('small', {}, 'Esta pergunta foi para a lista de Erros.')));
    const alts = s.cur.order.map((ai) => {
      const a = q.alternativas[ai];
      const m = fb.marked.has(ai);
      const good = m === a.correta;
      let tag;
      if (m && a.correta) tag = '✓ Você marcou. Correta.';
      else if (m && !a.correta) tag = '✗ Você marcou. Era errada, não devia marcar.';
      else if (!m && a.correta) tag = '✗ Você não marcou. Era correta, faltou marcar.';
      else tag = '✓ Você não marcou. Certo: era errada.';
      return h('div', { class: `alt static ${good ? 'ok' : 'bad'}` },
        h('span', { class: 'alt-body' }, h('span', { class: 'tag' }, tag), a.texto,
          a.justificativa ? h('span', { class: 'just' }, a.justificativa) : null));
    });
    const e = q.explicacao || {};
    const items = [['Regra simples', e.regra_simples], ['Por que', e.por_que], ['Como identificar', e.como_identificar], ['Erro comum', e.erro_comum], ['Exceção', e.excecao]];
    const dl = h('dl', { class: 'expl' });
    items.forEach(([t, v]) => { if (v && String(v).trim()) dl.append(h('dt', {}, t), h('dd', {}, String(v))); });
    const fr = Array.isArray(e.palavras_fr) ? e.palavras_fr : (e.palavras_fr ? [e.palavras_fr] : []);
    if (fr.length) dl.append(h('dt', {}, 'Palavras em francês'), h('dd', {}, fr.map((w) => h('span', { class: 'pill', lang: 'fr' }, `(${w})`))));
    const refs = (q.regra_ids || []).map(ruleById).filter(Boolean).map((r) => {
      const url = safeUrl(r.fonte && r.fonte.url);
      const label = [r.fonte && r.fonte.lei, r.fonte && r.fonte.artigo ? `art. ${r.fonte.artigo}` : null].filter(Boolean).join(' ') || r.id;
      return url ? h('div', {}, h('a', { href: url, target: '_blank', rel: 'noopener noreferrer' }, `Fonte oficial: ${label}`)) : null;
    });
    const last = s.i + 1 >= s.queue.length;
    mount(head, verdict, h('div', { class: 'alts' }, alts),
      h('section', { class: 'card' }, h('h2', {}, 'Explicação'), dl, refs.length ? h('div', { style: 'margin-top:12px' }, refs) : null),
      h('button', { class: 'btn primary', type: 'button', onclick: () => { s.i++; s.feedback = null; s.cur = null; if (s.i >= s.queue.length) s.done = true; viewSession(s.mode, s.cat); } }, last ? 'Ver resultado' : 'Próxima pergunta'),
      h('div', { class: 'btn-row' }, h('button', { class: 'btn', type: 'button', onclick: () => endSession(s) }, 'Encerrar sessão')));
  }

  async function submitAnswer(s, q, marked) {
    const ok = q.alternativas.every((a, i) => marked.has(i) === a.correta);
    const now = new Date().toISOString();
    const old = Store.get(q.id) || { id: q.id, tentativas: 0, acertos: 0, sequencia: 0, erradaAlgumaVez: false, ultimaTentativa: null, ultimoAcerto: null, ultimoErro: null, ultimoResultado: null };
    const rec = Object.assign({}, old, {
      tentativas: old.tentativas + 1,
      acertos: old.acertos + (ok ? 1 : 0),
      sequencia: ok ? old.sequencia + 1 : 0,
      erradaAlgumaVez: old.erradaAlgumaVez || !ok,
      ultimaTentativa: now,
      ultimoAcerto: ok ? now : old.ultimoAcerto,
      ultimoErro: ok ? old.ultimoErro : now,
      ultimoResultado: ok,
    });
    await Store.put(rec);
    s.results.push({ id: q.id, ok });
    s.feedback = { ok, marked, seq: rec.sequencia };
  }

  function endSession(s) {
    if (s.results.length) { s.done = true; viewSession(s.mode, s.cat); } else { session = null; location.hash = `#/${s.mode}`; }
  }

  function renderSummary(s) {
    const n = s.results.length;
    const certas = s.results.filter((r) => r.ok).length;
    if (!n) { session = null; location.hash = `#/${s.mode}`; return; }
    const nodes = [];
    nodes.push(h('section', { class: 'card', style: 'text-align:center' },
      h('div', { class: 'eyebrow' }, 'Resultado da sessão'),
      h('div', { class: 'summary-score' }, `${certas}/${n}`),
      h('p', { class: 'muted' }, `${plural(certas, 'pergunta certa', 'perguntas certas')} · ${certas * 3} de ${n * 3} pontos (3 por pergunta totalmente certa)`)));
    const wrong = s.results.length - certas;
    if (wrong) nodes.push(h('p', { class: 'muted' }, `${plural(wrong, 'pergunta errada foi', 'perguntas erradas foram')} para a lista de Erros.`));
    const restantes = s.mode === 'erros' ? errorsOf(s.cat).length : null;
    if (restantes) nodes.push(h('p', { class: 'muted' }, `Ainda ${plural(restantes, 'pergunta', 'perguntas')} na lista de Erros.`));
    nodes.push(h('div', { class: 'btn-row' },
      h('button', { class: 'btn primary', type: 'button', onclick: () => { session = null; viewSession(s.mode, s.cat); } }, 'Nova sessão'),
      wrong && s.mode === 'praticar' ? h('a', { class: 'btn', href: '#/erros' }, 'Revisar erros') : null,
      h('a', { class: 'btn', href: '#/' }, 'Voltar ao início')));
    setChrome('Resultado', `#/${s.mode}`, s.mode);
    mount(nodes);
  }

  // ----------------------------------------------------------------- rotas
  function route() {
    if (!C) return;
    const parts = location.hash.replace(/^#\/?/, '').split('/').filter(Boolean).map(decodeURIComponent);
    const [a, b] = parts;
    if (!(a === 'praticar' || a === 'erros') || !b) session = null;
    if (!a) return viewHome();
    if (a === 'aprender') return b ? viewLearnCat(b.toUpperCase()) : viewLearnIndex();
    if (a === 'praticar' || a === 'erros') return b ? viewSession(a, b === 'todas' ? 'todas' : b.toUpperCase()) : viewModeIndex(a);
    return viewHome();
  }

  async function boot() {
    setChrome('DRIVE THEORY', null, 'home');
    mount(h('p', { class: 'empty' }, 'Carregando...'));
    try {
      const r = await fetch('data/content.json', { cache: 'no-cache' });
      if (!r.ok) throw new Error(`HTTP ${r.status}`);
      C = await r.json();
      if (!C || !Array.isArray(C.regras) || !Array.isArray(C.perguntas) || !Array.isArray(C.categorias)) throw new Error('formato inválido');
    } catch (e) {
      mount(emptyState('Não foi possível carregar o conteúdo', `Detalhe: ${(e && e.message) || e}. Se você está offline e nunca abriu o app online, conecte-se uma vez.`,
        h('button', { class: 'btn primary', type: 'button', onclick: () => location.reload() }, 'Tentar de novo')));
      return;
    }
    const draft = C.modo === 'rascunho';
    $('#draft-banner').hidden = !draft;
    document.body.classList.toggle('has-banner', draft);
    await Store.init(draft ? 'drivetheory-rascunho' : 'drivetheory');
    window.addEventListener('hashchange', route);
    route();
  }

  if ('serviceWorker' in navigator && /^https?:$/.test(location.protocol)) {
    window.addEventListener('load', () => { navigator.serviceWorker.register('sw.js').catch(() => {}); });
  }
  boot();
})();
