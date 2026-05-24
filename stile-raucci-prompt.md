# PROMPT — STILE RAUCCI

## Uso
Incolla questo prompt all'inizio di ogni richiesta di lezione, poi descrivi a parte i contenuti specifici della lezione. Il prompt definisce solo l'identità visiva, narrativa e tecnica — non i contenuti.

---

Crea una pagina HTML cinematografica in un singolo file, in italiano, secondo lo "Stile Raucci". Tutto incluso: zero file esterni, zero build step, pronta per essere caricata su GitHub Pages e aperta da un doppio clic.

## IDENTITÀ VISIVA

**Palette unica** (non cambiare per sezione, mantieni costante):
- Sfondo base `--bg-0:#070d0e` / `--bg-1:#0a1417`
- Inchiostro `--ink:#eef4f1` e dimmed `--ink-dim:#9bb1ad`
- Accento primario teal `--teal:#6df0d2` (con variante profonda `#0eaf95`)
- Accento secondario gold `--gold:#f7c873` (con variante profonda `#d49a37`)
- Accento di errore rose `--rose:#ff8a8a`
- Linee `rgba(109,240,210,0.18)` e `rgba(247,200,115,0.22)`
- Pannelli `rgba(7,13,14,0.7)` con backdrop-filter blur

**Tipografia** (tre famiglie, mai sostituire):
- `Fraunces` serif (300/500/700, supporto italic) per titoli, citazioni, descrizioni narrative
- `Space Grotesk` sans (400/500/700) per testo UI, body funzionale, etichette dei dati
- `JetBrains Mono` (400/500/700) per codice, micro-etichette in maiuscolo spaziato (`letter-spacing: 0.16em–0.32em`), HUD, numerazioni di sezione

**Trattamento visivo a strati sovrapposti** (in quest'ordine):
1. `<canvas id="bg-canvas">` — shader Three.js a tutto schermo
2. `.grid-overlay` — griglia 80px×80px in teal-fog (`rgba(109,240,210,0.06)`) con mask radiale che la dissolve ai bordi
3. `.vignette` — vignettatura radiale (transparent 45% → black 100%)
4. `.scanline` — righe orizzontali ogni 3-4px in mix-blend-mode overlay (look CRT vintage)
5. `.hud` fisso in alto — barra orizzontale con punto dorato pulsante, etichetta della lezione a sinistra, sezione corrente e percentuale a destra
6. `.rail` fissa a destra a metà altezza — nodi romboidali (`transform:rotate(45deg)`) numerati in stile `00 · NOME`, attivo in teal con glow

## TECNOLOGIA

Esattamente queste librerie da CDN (non sostituirle):
- Three.js r128 (per lo shader fragment di sfondo)
- GSAP 3.12.5 + ScrollTrigger (per gli ingressi cinematici)
- Lenis 1.0.42 dal path `/dist/lenis.min.js` su jsdelivr (questo path è confermato funzionante)
- KaTeX 0.16.9 quando servono formule matematiche tipografate

## SHADER FRAGMENT (parte caratterizzante)

Lo shader deve generare uno sfondo a strati atmosferici stratificati con domain warping. Schema obbligatorio:

```glsl
// strati orizzontali "atmosfera"
float layers = sin(p.y*8.0 + fbm(p*1.6 + t)*2.2 + uScroll*3.0) * 0.5 + 0.5;
// domain warp con FBM a 5 ottave
vec2 q = vec2(fbm(p*1.3 + vec2(0,t)), fbm(p*1.3 + vec2(5.2,-t*0.9)));
vec2 r = vec2(fbm(p*1.7 + 3.6*q + vec2(1.7,9.2) + t*0.6),
              fbm(p*1.7 + 3.6*q + vec2(8.3,2.8) - t*0.4));
float n = fbm(p*2.0 + 2.8*r);
// palette: nero → petrolio → teal → gold (solo sui picchi sotto il cursore)
// glow ciano sotto il cursore, intensità decresce con distanza
// grana, vignetta, tinta che vira da teal a gold con lo scroll (uScroll)
```

Uniformi: `uTime`, `uResolution`, `uMouse`, `uScroll`. Lo scroll è collegato a Lenis con `lenis.on('scroll', ...)`. Il cursore trascina la texture con una funzione `warp = smoothstep(0, 0.65, 1.0 - dM*0.85)`.

**Niente cursore custom DOM**. Il cursore agisce solo sullo shader.

## ARCHITETTURA TIPOGRAFICA

**HERO**:
- `.eyebrow` in mono uppercase, letter-spacing 0.32em, oro
- `h1` in Fraunces 300, dimensioni `clamp(54px, 9vw, 140px)`, line-height 0.92
- All'interno di `h1`, le parole chiave in `<em>` diventano teal corsivo; un eventuale `<span class="stamp">` diventa una "targa" in Space Grotesk uppercase oro sotto il titolo
- `.sub` in Space Grotesk, max-width 680px, line-height 1.85
- `.meta` con campi `OBIETTIVO / NUOVI CONCETTI / REGOLA D'ORO`, etichetta in mono, valore in teal Space Grotesk
- `.scroll-cue` in basso al centro con linea verticale animata

**SEZIONI** — ognuna è `min-height:100vh, padding:120px 8vw, justify-content:center`. Ogni sezione comincia con `.section-head`:
- `.num` in mono uppercase `§ NN · titolo breve`, oro
- `h2` in Fraunces 300, `clamp(40px, 6.5vw, 92px)`, con `<em>` teal e `<span class="accent">` oro corsivo per le parole chiave
- `.lead` in Space Grotesk, max-width 760px, line-height 1.8

## COMPONENTI DA USARE (sceglili in base ai contenuti)

- `.pact` — griglia a 2 colonne, etichetta mono uppercase, lista con `›` come bullet, una colonna teal e una gold
- `.golden` — citazione editoriale ampia (Fraunces italic, clamp 22–38px) tra `«` e `»` dorati, su gradiente teal/gold
- `.planner` — tabella a 3 colonne (numero / topic / applicazione), una riga marcata `.current` con barra oro a sinistra
- `.timeline` — 5 step orizzontali separati da frecce `→` in teal, ognuno con numero mono, titolo Space Grotesk bold, descrizione Fraunces italic
- `.prompts` — due card affiancate `.bad` (rose) vs `.good` (teal), ciascuna con citazione in `<q>`
- `.cycle` — 6 step orizzontali con frecce, uno `.critical` evidenziato in oro
- `.code-stage` — finestra con angoli grafici teal nei vertici opposti, header con tre dots (rosso/oro/teal stile macOS) ed etichetta "repl · python 3.x", body in JetBrains Mono con classi `kw bi st nm cm fn op` per syntax highlighting
- `.code-notes` — riga di 4 celle sotto al codice, ognuna con tag mono uppercase, titolo Space Grotesk bold, testo Fraunces italic
- `.isa-box` (o equivalente) — formule KaTeX su un lato, costanti tabulari sull'altro
- `.val-table` — tabella di validazione monospaziata con prima colonna oro bold, una riga `.highlight` su sfondo oro tenue
- `.translate-prompt` — riquadro con etichetta mono teal "PROMPT · DA PYTHON A WEB", titolo Fraunces italic, contenuto in `<q>` su sfondo molto scuro con border-left teal
- `.demo-wrap` — finestra con header in stile browser (URL fittizio in cui il nome del repo è in oro) e `<iframe>` interno (`height:740px`)
- `.gh-steps` — 4 step orizzontali stile timeline, per la procedura GitHub Pages
- `.callout` — banda con etichetta mono uppercase oro e testo Fraunces italic
- `.closing` — chiusura con `h2` ampio in Fraunces italic 300, blocchetto `.next` con prossimi argomenti, `.motto` finale centrato

## TONO NARRATIVO

Scrivi come si scrive un saggio tecnico colto, non come un manuale scolastico. Tratti distintivi:

- **Frasi compiute, ritmate**, non bullet list ovunque
- **Esempi storici reali** quando possibile (Mars Climate Orbiter, Tacoma, voli reali, normative citate per nome)
- **Verbi forti** ("la sonda si disintegra", "il calcolo perde senso", "il prompt è un disegno tecnico")
- **Apertura di sezione spesso narrativa**, non definitoria: si parte dal problema o dall'aneddoto, la definizione arriva dopo
- **Niente entusiasmo posticcio** ("Fantastico!", "Ora vediamo come...") — il tono è asciutto, professionale, leggermente solenne
- Termini tecnici **mai annacquati**: si dice "stratosfera", "fattore di carico ultimo", "gradient termico verticale" con la stessa naturalezza con cui si dice "casa"
- Frasi corte alternate a frasi più lunghe (ritmo editoriale)
- **Citazioni golden** in stile sentenza tecnica: una verità densa, in 1–2 frasi, isolata

## ANIMAZIONI GSAP

Per ogni gruppo di elementi: `gsap.from(...)` con `opacity:0, y:30, duration:0.8–1.1, ease:"power3.out"`, con `stagger:0.12–0.18` per le sequenze, e `scrollTrigger:{ trigger: el, start:"top 82%", toggleActions:"play none none reverse" }`. L'hero va animato con un timeline `gsap.from()` cumulativo: prima eyebrow, poi h1, poi stamp con `letterSpacing:"0.3em"→0` (effetto "stamp che converge"), poi sub, poi meta in stagger.

Il body cambia leggermente colore con uno `scrub:true` sull'intera pagina (`backgroundColor:"#080f10"` come target).

## INTEGRAZIONE LENIS + SHADER + GSAP

```js
const lenis = new Lenis({duration: 1.4, easing: t => Math.min(1, 1.001 - Math.pow(2, -10*t))});
function raf(t){ lenis.raf(t); requestAnimationFrame(raf); } requestAnimationFrame(raf);
lenis.on('scroll', ScrollTrigger.update);
gsap.ticker.add(t => lenis.raf(t * 1000));
gsap.ticker.lagSmoothing(0);
// E in più: lenis.on('scroll', ({scroll, limit}) => { scrollNorm = scroll/limit; });
// nel render loop dello shader: uniforms.uScroll.value += (scrollNorm - uniforms.uScroll.value) * 0.05;
```

## HUD + RAIL — comportamento

L'HUD in alto mostra `SYS · [NOME LEZIONE]` a sinistra, e a destra `SEC · NN · NOME` + `PRG · NN%` aggiornati in tempo reale. Le voci della rail si attivano con `ScrollTrigger.create({trigger:'#id', start:"top 50%", end:"bottom 50%", onToggle:...})`. Click sulla voce della rail → `lenis.scrollTo(target, {offset:-60, duration:1.4})`.

## VINCOLI

- Tutto in `index.html`, nessun file separato
- Niente librerie diverse da quelle elencate
- Niente cursore custom DOM
- Niente palette differenti per sezione: i colori sono **gli stessi ovunque**, l'evoluzione si percepisce solo dallo `uScroll` che vira lentamente verso il gold
- Mai sostituire Fraunces con Cormorant o altre serif: la corretta resa dei corsivi è parte dello stile
- I titoli `h2` devono sempre avere almeno una parola in `<em>` teal e idealmente una in `<span class="accent">` gold

## TESTO TIPO CHE DEVE COMPARIRE

In ogni lezione devono comparire (adattati al tema):
- una **golden quote** centrale con una "morale tecnica" in due frasi
- almeno un **aneddoto storico** reale o ben circostanziato
- almeno una **code-stage** con codice Python commentato
- una **timeline** o una **cycle**
- un **callout** finale con la regola d'oro della lezione
- una **closing** con `.next` (cosa viene dopo) e una `.motto` di chiusura
