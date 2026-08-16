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
      {name:'Morning Café',bpm:88,prog:[[60,64,67],[57,60,64],[53,57,60],[55,59,62]]},
      {name:'Soft Study',bpm:94,prog:[[62,65,69],[59,62,65],[55,59,62],[57,60,64]]},
      {name:'Tokyo Desk',bpm:90,prog:[[60,63,67],[56,60,63],[53,56,60],[58,62,65]]},
      {name:'Quiet Momentum',bpm:98,prog:[[64,67,71],[60,64,67],[57,60,64],[59,62,66]]},
      {name:'Night Review',bpm:86,prog:[[59,62,66],[55,59,62],[52,55,59],[57,60,64]]}
    ];
    var index=0,ctx=null,master=null,timer=null,playing=false,nextTime=0,step=0,trackStarted=0;

    var box=document.createElement('div'); box.id='focusMusic'; box.className='focus-music invite';
    box.innerHTML='<button class="focus-close" type="button" aria-label="Đóng">×</button><div class="focus-invite"><div class="focus-emoji">🎧</div><div><strong>Học hơi căng rồi hả?</strong><span>Bật chút nhạc nhẹ để tập trung hơn nè ✨</span><button class="focus-start" type="button">▶ Nghe nhạc cùng mình</button></div></div><div class="focus-controls"><div class="focus-now"><span>🎧 Đang tập trung ♪</span><small>Tokutei Focus Mix</small></div><div class="focus-buttons"><button data-act="prev" type="button">⏮</button><button data-act="play" type="button">▶</button><button data-act="next" type="button">⏭</button><label>🔉 <input class="focus-volume" type="range" min="0" max="1" step="0.05" value="0.22" aria-label="Âm lượng"></label></div></div><button class="focus-mini" type="button">🎧 Nhạc tập trung</button>';
    document.body.appendChild(box);
    var start=box.querySelector('.focus-start'),play=box.querySelector('[data-act="play"]'),now=box.querySelector('.focus-now small'),vol=box.querySelector('.focus-volume');

    function freq(m){return 440*Math.pow(2,(m-69)/12)}
    function initAudio(){
      if(ctx)return;
      var AC=window.AudioContext||window.webkitAudioContext; if(!AC){now.textContent='Trình duyệt chưa hỗ trợ âm thanh';return;}
      ctx=new AC(); master=ctx.createGain(); master.gain.value=parseFloat(vol.value); master.connect(ctx.destination);
    }
    function tone(f,t,d,g,type){
      var o=ctx.createOscillator(),v=ctx.createGain(); o.type=type||'sine';o.frequency.value=f;v.gain.setValueAtTime(0,t);v.gain.linearRampToValueAtTime(g,t+.025);v.gain.exponentialRampToValueAtTime(.0001,t+d);o.connect(v);v.connect(master);o.start(t);o.stop(t+d+.04);
    }
    function noiseHit(t,d,g){
      var len=Math.max(1,Math.floor(ctx.sampleRate*d)),buf=ctx.createBuffer(1,len,ctx.sampleRate),a=buf.getChannelData(0);for(var i=0;i<len;i++)a[i]=(Math.random()*2-1)*Math.pow(1-i/len,2);var s=ctx.createBufferSource(),v=ctx.createGain();s.buffer=buf;v.gain.value=g;s.connect(v);v.connect(master);s.start(t);
    }
    function scheduleBeat(t){
      var tr=tracks[index],beat=60/tr.bpm,barStep=step%8,chord=tr.prog[Math.floor(step/8)%tr.prog.length];
      if(barStep===0){for(var j=0;j<chord.length;j++){tone(freq(chord[j]-12),t,beat*3.8,.035/(j+1),'sine');tone(freq(chord[j]),t,beat*1.9,.012/(j+1),'triangle')}}
      if(barStep%2===0){var notes=[0,2,4,7,9],root=chord[0]+12+notes[(step+index*2)%notes.length];tone(freq(root),t,beat*.72,.035,'triangle')}
      if(barStep===0||barStep===4)tone(70,t,.12,.035,'sine');
      if(barStep===2||barStep===6)noiseHit(t,.08,.012);
      noiseHit(t,.025,.0038);
      step++;
    }
    function scheduler(){
      if(!playing||!ctx)return;
      var beat=60/tracks[index].bpm/2;
      while(nextTime<ctx.currentTime+.35){scheduleBeat(nextTime);nextTime+=beat}
      if(ctx.currentTime-trackStarted>120){change(1)}
    }
    function begin(){
      initAudio(); if(!ctx)return; ctx.resume(); playing=true;play.textContent='⏸';box.classList.remove('invite');box.classList.add('active');now.textContent=tracks[index].name;step=0;nextTime=ctx.currentTime+.08;trackStarted=ctx.currentTime;if(timer)clearInterval(timer);timer=setInterval(scheduler,120);scheduler();
    }
    function stop(){playing=false;play.textContent='▶';if(timer){clearInterval(timer);timer=null}}
    function toggle(){if(playing)stop();else begin()}
    function change(n){index=(index+n+tracks.length)%tracks.length;stop();if(ctx){nextTime=ctx.currentTime+.08}begin()}
    function shutdown(){stop();if(ctx){try{ctx.close()}catch(e){}ctx=null;master=null}}

    start.addEventListener('click',begin);play.addEventListener('click',toggle);
    box.querySelector('[data-act="prev"]').addEventListener('click',function(){change(-1)});
    box.querySelector('[data-act="next"]').addEventListener('click',function(){change(1)});
    vol.addEventListener('input',function(){if(master)master.gain.setTargetAtTime(parseFloat(this.value),ctx.currentTime,.03)});
    box.querySelector('.focus-close').addEventListener('click',function(){shutdown();box.classList.add('hidden')});
    box.querySelector('.focus-mini').addEventListener('click',function(){box.classList.remove('hidden');box.classList.add('invite')});
    window.addEventListener('pagehide',shutdown);
  }

  function init(){decorate();focusPlayer()}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
