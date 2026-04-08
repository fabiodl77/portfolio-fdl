/* =============================================
   1. BARRA DE PROGRESSO DE SCROLL
   ============================================= */
const progressBar = document.getElementById('progress-bar');

function updateProgress() {
  const scrollTop = window.scrollY;
  const docHeight = document.documentElement.scrollHeight - window.innerHeight;
  progressBar.style.width = (scrollTop / docHeight * 100) + '%';
}
window.addEventListener('scroll', updateProgress, { passive: true });


/* =============================================
   2. NAVBAR: scroll + active link
   ============================================= */
const navbar = document.getElementById('navbar');
const navLinks = document.querySelectorAll('nav ul a');
const sections = document.querySelectorAll('section[id], header[id]');

window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 40);
}, { passive: true });

const sectionObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navLinks.forEach(a => {
        const active = a.getAttribute('href') === `#${entry.target.id}`;
        a.classList.toggle('active', active);
      });
    }
  });
}, { threshold: 0.4 });

sections.forEach(s => sectionObserver.observe(s));


/* =============================================
   3. PARTÍCULAS NO HERO (Canvas)
   ============================================= */
const canvas = document.getElementById('particles-canvas');
const ctx = canvas.getContext('2d');

function resizeCanvas() {
  canvas.width  = canvas.offsetWidth;
  canvas.height = canvas.offsetHeight;
}
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

const PARTICLE_COUNT = 55;
const particles = [];

function randBetween(a, b) { return a + Math.random() * (b - a); }

for (let i = 0; i < PARTICLE_COUNT; i++) {
  particles.push({
    x:  Math.random() * window.innerWidth,
    y:  Math.random() * window.innerHeight,
    r:  randBetween(1.5, 3.5),
    vx: randBetween(-0.4, 0.4),
    vy: randBetween(-0.5, -0.1),
    alpha: randBetween(0.3, 0.8),
  });
}

function drawParticles() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  particles.forEach((p, i) => {
    // draw dot
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
    ctx.fillStyle = `rgba(255,255,255,${p.alpha})`;
    ctx.fill();

    // draw connecting lines to nearby particles
    for (let j = i + 1; j < particles.length; j++) {
      const q = particles[j];
      const dx = p.x - q.x, dy = p.y - q.y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      if (dist < 110) {
        ctx.beginPath();
        ctx.moveTo(p.x, p.y);
        ctx.lineTo(q.x, q.y);
        ctx.strokeStyle = `rgba(255,255,255,${0.12 * (1 - dist / 110)})`;
        ctx.lineWidth = 0.8;
        ctx.stroke();
      }
    }

    // move
    p.x += p.vx;
    p.y += p.vy;

    // wrap around
    if (p.y < -10)              p.y = canvas.height + 10;
    if (p.x < -10)              p.x = canvas.width + 10;
    if (p.x > canvas.width + 10) p.x = -10;
  });

  requestAnimationFrame(drawParticles);
}
drawParticles();


/* =============================================
   4. TYPEWRITER NO HERO
   ============================================= */
const twEl = document.getElementById('typewriter');
const words = typeof TARGETS !== 'undefined' ? TARGETS : [];
let wIndex = 0, cIndex = 0, deleting = false;

function typeWriter() {
  const word = words[wIndex] || '';
  if (!deleting) {
    twEl.textContent = word.slice(0, cIndex + 1);
    cIndex++;
    if (cIndex === word.length) {
      deleting = true;
      setTimeout(typeWriter, 1800);
      return;
    }
  } else {
    twEl.textContent = word.slice(0, cIndex - 1);
    cIndex--;
    if (cIndex === 0) {
      deleting = false;
      wIndex = (wIndex + 1) % words.length;
    }
  }
  setTimeout(typeWriter, deleting ? 55 : 90);
}
if (words.length) typeWriter();


/* =============================================
   5. CONTADOR ANIMADO NOS STAT CARDS
   ============================================= */
function animateCounter(el) {
  const target = parseInt(el.dataset.target, 10);
  const duration = 1500;
  const start = performance.now();

  function step(now) {
    const elapsed = now - start;
    const progress = Math.min(elapsed / duration, 1);
    // ease out cubic
    const eased = 1 - Math.pow(1 - progress, 3);
    el.textContent = Math.round(eased * target);
    if (progress < 1) requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
}

const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting && entry.target.dataset.target) {
      animateCounter(entry.target);
      counterObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('.stat-num[data-target]').forEach(el => counterObserver.observe(el));


/* =============================================
   6. SKILLS: STAGGER DE ENTRADA
   ============================================= */
const skillPills = document.querySelectorAll('.skill-pill');

const skillObserver = new IntersectionObserver((entries) => {
  if (entries.some(e => e.isIntersecting)) {
    skillPills.forEach((pill, i) => {
      setTimeout(() => pill.classList.add('visible'), i * 55);
    });
    skillObserver.disconnect();
  }
}, { threshold: 0.1 });

const skillsSection = document.getElementById('habilidades');
if (skillsSection) skillObserver.observe(skillsSection);


/* =============================================
   7. FADE-IN GENÉRICO (cards, etc.)
   ============================================= */
const fadeEls = document.querySelectorAll(
  '.stat-card, .timeline-card, .edu-card, .course-card, .contact-card, .about-text, .video-wrapper, .map-wrapper'
);

fadeEls.forEach(el => el.classList.add('fade-in'));

const fadeObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      setTimeout(() => entry.target.classList.add('visible'), i * 60);
      fadeObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

fadeEls.forEach(el => fadeObserver.observe(el));
