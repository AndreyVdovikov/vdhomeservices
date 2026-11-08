// Shared behavior for all pages
(function(){
  var nav=document.getElementById('nav');
  if(nav){ window.addEventListener('scroll',function(){ nav.classList.toggle('scrolled',window.scrollY>10); }); }
  var b=document.querySelector('.nav-burger'), m=document.getElementById('navMobile');
  if(b&&m){
    function close(){ m.classList.remove('open'); b.setAttribute('aria-expanded','false'); document.body.classList.remove('nav-open'); }
    b.addEventListener('click',function(){
      var o=m.classList.toggle('open'); b.setAttribute('aria-expanded',o?'true':'false'); document.body.classList.toggle('nav-open',o);
    });
    m.addEventListener('click',function(e){ if(e.target.closest('a')) close(); });
    window.addEventListener('resize',function(){ if(window.innerWidth>900) close(); });
  }
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('visible'); io.unobserve(e.target); } }); },{threshold:0.1});
    document.querySelectorAll('.reveal').forEach(function(el){ io.observe(el); });
  } else { document.querySelectorAll('.reveal').forEach(function(el){ el.classList.add('visible'); }); }
})();

/* house explorer */
(function(){
if(!document.getElementById('hx-stage'))return;

const INFO = {
  gutters:  { tag:"Outside", t:"Gutter cleaning", p:"Leaves and debris block the water and spill it along your walls. A clean gutter keeps water away from the house.", c:["Gutter cleaning","Downspout check"] },
  lights:   { tag:"Seasonal", t:"Christmas light installation", p:"Professional C9 lights in any color, cut to fit your roofline and installed. I take them down in January and store them. The lights are yours.", c:["C9 lights","Any color","Takedown + storage"] },
  deck:     { tag:"Outside", t:"Deck repair & refresh", p:"Soft boards, loose railings and faded wood. I repair what is damaged and bring the deck back to life.", c:["Deck repair","Painting & staining","Pressure washing"] },
  driveway: { tag:"Outside", t:"Pressure washing", p:"Oil stains, algae and dirt on the driveway come off, and the whole front of the house looks new.", c:["Driveway","Walkways","Walls"] },
  fence:    { tag:"Outside", t:"Fence repair & painting", p:"Leaning posts, broken pickets and peeling paint. I fix the damaged parts so you do not have to replace the whole fence.", c:["Fence repair","Painting","Post repair"] },
  "paint-out": { tag:"Outside", t:"Exterior wall painting", p:"Fresh paint protects the stucco from the Florida sun and makes the whole house look new.", c:["Walls","Touch-ups","Prep & repair"] },
  shutters: { tag:"Outside", t:"Hurricane shutters", p:"Roll-down and accordion shutters for your windows, ready before storm season. I explain what applies to your address.", c:["Accordion","Roll-down","Before storm season"] },
  rot:      { tag:"Outside", t:"Wood rot & trim repair", p:"Soft, damaged columns, trim and fascia are cut out, repaired or replaced and painted to match.", c:["Wood rot repair","Trim","Painting"] },
  door:     { tag:"Outside", t:"Door painting & lock replacement", p:"A fresh coat on the front door and a new lock or deadbolt installed, so the entry looks great and feels secure.", c:["Door painting","Lock replacement","Deadbolts"] },
  pictures: { tag:"Inside", t:"Hanging pictures & mirrors", p:"Frames, mirrors and gallery walls hung level and spaced evenly, with the right anchors for your wall.", c:["Gallery walls","Mirrors","Right anchors"] },
  furniture:{ tag:"Inside", t:"Furniture assembly", p:"Flat-pack furniture from any store, assembled and secured to the wall when needed. Beds, wardrobes, desks, shelves and more.", c:["Any brand","Beds & wardrobes","Wall anchoring"] },
  cabinets: { tag:"Inside", t:"Cabinet painting & new kitchens", p:"Painting your cabinets is a budget-friendly way to refresh the kitchen. I also install new kitchens.", c:["Cabinet painting","Renovation","New kitchens"] },
  accent:   { tag:"Inside", t:"Media & accent walls", p:"TV walls, fireplaces and custom designs: slats, shiplap and board and batten.", c:["Slat walls","Shiplap","Custom designs"] },
  tv:       { tag:"Inside", t:"TV mounting", p:"Any size, on drywall, brick or stone, even over a fireplace. Cords are hidden for a clean look.", c:["43 to 98 inch","Over fireplace","Hidden wires"] },
  curtains: { tag:"Inside", t:"Curtain rods & blinds", p:"Rods and drapery hardware hung level and secure, even on high ceilings.", c:["Curtain rods","Blinds","Anchors"] },
  shelves:  { tag:"Inside", t:"Shelves", p:"Floating and heavy-duty shelves anchored properly into the wall.", c:["Floating shelves","Heavy-duty","Levelled"] },
  drywall:  { tag:"Inside", t:"Drywall repair", p:"Holes, cracks and dents patched, textured, primed and painted so the repair disappears.", c:["Holes & cracks","Texture match","Paint"] },
  "paint-in": { tag:"Inside", t:"Interior painting", p:"Walls, ceilings and trim with clean lines and protected floors.", c:["Walls","Ceilings","Trim"] }
};

const stage = document.getElementById('hx-stage');
const tip = document.getElementById('hx-tip');
const hint = document.getElementById('hx-hint');
const sceneOut = document.getElementById('hx-scene-out');
const sceneIn = document.getElementById('hx-scene-in');
const nightBtn = document.getElementById('hx-nightBtn');
const seen = new Set();
const allIds = Object.keys(INFO);
let pinned = null;

/* christmas lights bulbs along the roof edge */
(function(){
  const g = document.getElementById('hx-lights'); const cols = ['#ff4d4d','#ffd84d','#4dd2ff','#6dff7a','#ff9a3d'];
  const pts = [[228,266,832,266],[228,270,298,200],[298,200,774,200],[774,200,832,270]];
  let i = 0;
  pts.forEach(([x1,y1,x2,y2]) => {
    const len = Math.hypot(x2-x1,y2-y1), n = Math.round(len/20);
    for (let k=0;k<=n;k++){ const t=k/n; const c=document.createElementNS('http://www.w3.org/2000/svg','circle');
      c.setAttribute('cx', x1+(x2-x1)*t); c.setAttribute('cy', y1+(y2-y1)*t + 5); c.setAttribute('r', 5);
      c.setAttribute('fill', cols[i++ % cols.length]); g.appendChild(c); }
  });
  const stars = document.getElementById('hx-stars');
  for (let k=0;k<40;k++){ const c=document.createElementNS('http://www.w3.org/2000/svg','circle'); c.setAttribute('cx',(k*137)%1000); c.setAttribute('cy',(k*61)%260+10); c.setAttribute('r', k%5===0?1.8:1.1); stars.appendChild(c); }
})();

function updateProgress(){
  document.getElementById('hx-count').textContent = seen.size + ' of ' + allIds.length + ' found';
  document.getElementById('hx-pfill').style.width = (seen.size/allIds.length*100) + '%';
  document.getElementById('hx-done').classList.toggle('on', seen.size === allIds.length);
}
updateProgress();

function showTip(el){
  const id = el.dataset.id, d = INFO[id]; if (!d) return;
  tip.innerHTML = '<div class="tag">'+d.tag+'</div><h3>'+d.t+'</h3><p>'+d.p+'</p><ul>'+d.c.map(x=>'<li>'+x+'</li>').join('')+'</ul>';
  const dot = el.querySelector('.dot').getBoundingClientRect(); const sr = stage.getBoundingClientRect();
  tip.classList.add('show');
  const tw = tip.offsetWidth, th = tip.offsetHeight;
  let x = dot.left + dot.width/2 - sr.left - tw/2; x = Math.max(12, Math.min(x, sr.width - tw - 12));
  let y = dot.top - sr.top - th - 16; if (y < 8) y = dot.bottom - sr.top + 16;
  tip.style.left = x + 'px'; tip.style.top = y + 'px';
  document.querySelectorAll('#house .hs.on').forEach(n=>n.classList.remove('on')); el.classList.add('on');
  if (!seen.has(id)) { seen.add(id); el.classList.add('seen'); updateProgress(); }
  hint.classList.add('gone');
}
function hideTip(){ tip.classList.remove('show'); document.querySelectorAll('#house .hs.on').forEach(n=>n.classList.remove('on')); pinned = null; }

document.querySelectorAll('#house .hs').forEach(el => {
  el.addEventListener('pointerenter', e => { if (e.pointerType === 'mouse' && !pinned) showTip(el); });
  el.addEventListener('pointerleave', e => { if (e.pointerType === 'mouse' && !pinned) hideTip(); });
  el.addEventListener('click', e => { e.stopPropagation(); if (pinned === el) { hideTip(); } else { pinned = el; showTip(el); } });
  el.addEventListener('focus', () => showTip(el));
  el.addEventListener('blur', () => { if (!pinned) hideTip(); });
  el.addEventListener('keydown', e => { if (e.key === 'Escape') hideTip(); });
});
document.addEventListener('click', e => { if (!tip.contains(e.target)) hideTip(); });

function setScene(name){
  hideTip();
  const out = name === 'out';
  sceneOut.toggleAttribute('hidden', !out); sceneIn.toggleAttribute('hidden', out); nightBtn.hidden = !out;
  document.getElementById('hx-tab-out').setAttribute('aria-selected', out);
  document.getElementById('hx-tab-in').setAttribute('aria-selected', !out);
}
document.querySelectorAll('#house .tab').forEach(b => b.addEventListener('click', () => setScene(b.dataset.scene)));

nightBtn.addEventListener('click', () => {
  const on = nightBtn.getAttribute('aria-pressed') !== 'true';
  nightBtn.setAttribute('aria-pressed', on);
  sceneOut.classList.toggle('night', on);
  document.getElementById('hx-stars').style.opacity = on ? 1 : 0;
  document.getElementById('hx-winglow').style.opacity = on ? .85 : 0;
  hideTip();
});

})();
