(function(){
  function hardNavigation(){
    document.addEventListener('click',function(e){
      if(e.defaultPrevented||e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey) return;
      var a=e.target.closest&&e.target.closest('a[href]');
      if(!a||a.target==='_blank'||a.hasAttribute('download')) return;
      var u;
      try{u=new URL(a.href,location.href);}catch(err){return;}
      if(u.origin!==location.origin) return;
      /* Let normal browser navigation load the complete HTML/CSS for every page. */
    },false);
  }

  function init(){
    document.documentElement.setAttribute('data-ui','business');
    hardNavigation();
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',init);
  else init();
})();
