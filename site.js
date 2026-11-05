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
