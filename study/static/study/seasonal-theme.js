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

  function focusPlayer(){
    if(document.getElementById('focusMusic'))return;
    var tracks=[
      {name:'Tokutei Focus 01',src:'/static/study/music/focus-01.mp3'},
      {name:'Tokutei Focus 02',src:'/static/study/music/focus-02.mp3'},
      {name:'Tokutei Focus 03',src:'/static/study/music/focus-03.mp3'},
      {name:'Tokutei Focus 04',src:'/static/study/music/focus-04.mp3'},
      {name:'Tokutei Focus 05',src:'/static/study/music/focus-05.mp3'}
    ];
    var index=0, audio=new Audio(), playing=false;
    audio.preload='none'; audio.volume=.28;

    var box=document.createElement('div'); box.id='focusMusic'; box.className='focus-music invite';
    box.innerHTML='<button class="focus-close" type="button" aria-label="Đóng">×</button><div class="focus-invite"><div class="focus-emoji">🎧</div><div><strong>Học hơi căng rồi hả?</strong><span>Bật chút nhạc nhẹ để tập trung hơn nè ✨</span><button class="focus-start" type="button">▶ Nghe nhạc cùng mình</button></div></div><div class="focus-controls"><div class="focus-now"><span>🎧 Đang tập trung ♪</span><small>Tokutei Focus Mix</small></div><div class="focus-buttons"><button data-act="prev" type="button">⏮</button><button data-act="play" type="button">▶</button><button data-act="next" type="button">⏭</button><label>🔉 <input class="focus-volume" type="range" min="0" max="1" step="0.05" value="0.28" aria-label="Âm lượng"></label></div></div><button class="focus-mini" type="button">🎧 Nhạc tập trung</button>';
    document.body.appendChild(box);
    var start=box.querySelector('.focus-start'), play=box.querySelector('[data-act="play"]'), now=box.querySelector('.focus-now small');

    function load(i){index=(i+tracks.length)%tracks.length;audio.src=tracks[index].src;now.textContent=tracks[index].name;}
    function startPlay(){if(!audio.src)load(index);audio.play().then(function(){playing=true;play.textContent='⏸';box.classList.remove('invite');box.classList.add('active');}).catch(function(){box.classList.add('missing-audio');now.textContent='Đang chờ thêm nhạc 🎵';});}
    function toggle(){if(playing){audio.pause();playing=false;play.textContent='▶';}else startPlay();}
    function change(step){load(index+step);startPlay();}
    start.addEventListener('click',startPlay); play.addEventListener('click',toggle);
    box.querySelector('[data-act="prev"]').addEventListener('click',function(){change(-1)});
    box.querySelector('[data-act="next"]').addEventListener('click',function(){change(1)});
    box.querySelector('.focus-volume').addEventListener('input',function(){audio.volume=parseFloat(this.value)});
    box.querySelector('.focus-close').addEventListener('click',function(){audio.pause();playing=false;box.classList.add('hidden');});
    box.querySelector('.focus-mini').addEventListener('click',function(){box.classList.remove('hidden');box.classList.add('invite');});
    audio.addEventListener('ended',function(){change(1)});
    window.addEventListener('pagehide',function(){audio.pause();audio.currentTime=0;});
  }

  function init(){decorate();focusPlayer();}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
