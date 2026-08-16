
(function(){
  var month=(new Date()).getMonth()+1;
  var season=(month===3||month===4)?'sakura':(month===5||month===6)?'rainy':(month===7||month===8)?'summer':(month>=9&&month<=11)?'autumn':'winter';
  var symbols={sakura:['🌸','✿'],rainy:['✾','•'],summer:['✦','·'],autumn:['◆','🍁'],winter:['❄','·']};
  document.documentElement.setAttribute('data-season',season);
  function decorate(){
    if(document.querySelector('.seasonal-float'))return;
    for(var i=0;i<12;i++){
      var e=document.createElement('span');e.className='seasonal-float';e.textContent=symbols[season][i%2];
      e.style.left=(3+Math.random()*94)+'vw';e.style.animationDuration=(9+Math.random()*9)+'s';e.style.animationDelay=(-Math.random()*16)+'s';e.style.fontSize=(12+Math.random()*14)+'px';document.body.appendChild(e);
    }
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',decorate);else decorate();
})();
