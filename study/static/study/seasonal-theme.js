(function(){
  var month=(new Date()).getMonth()+1;
  var season=(month===3||month===4)?'sakura':(month===5||month===6)?'rainy':(month===7||month===8)?'summer':(month>=9&&month<=11)?'autumn':'winter';
  var symbols={sakura:['🌸','✿'],rainy:['✾','•'],summer:['✦','·'],autumn:['◆','🍁'],winter:['❄','·']};
  document.documentElement.setAttribute('data-season',season);
  function decorate(){if(document.querySelector('.seasonal-float'))return;for(var i=0;i<12;i++){var e=document.createElement('span');e.className='seasonal-float';e.textContent=symbols[season][i%2];e.style.left=(3+Math.random()*94)+'vw';e.style.animationDuration=(9+Math.random()*9)+'s';e.style.animationDelay=(-Math.random()*16)+'s';e.style.fontSize=(12+Math.random()*14)+'px';document.body.appendChild(e)}}
  function focusPlayer(){
    if(document.getElementById('focusMusic'))return;
    var KEY='tokuteiFocusMusicV2',BASE='/static/../tokutei_focus_mix_7_mp3_96k/';
    var tracks=[
      ['Relaxing Piano Music','piano_solo_nhac_nen_piano-relaxing-piano-music-nhac-nen-video-227817-96k.mp3'],
      ['Peaceful Piano Music','piano_solo_nhac_nen_piano-peaceful-piano-music-piano-bgm-227820-96k.mp3'],
      ['Beautiful Piano – Study & Relax','piano_solo_nhac_nen_piano-beautiful-piano-tracks-for-studying-relaxation-sleep-piano-bgm-227821-96k.mp3'],
      ['Khi Tình Yêu Nở Hoa','piano_solo_nhac_nen_piano-khi-tinh-yeu-no-hoa-nhac-nen-video-227815-96k.mp3'],
      ['Tuổi Thơ Hồn Nhiên Thơ Ngây','piano_solo_nhac_nen_piano-tuoi-tho-hon-nhien-tho-ngay-nhac-nen-video-227569-96k.mp3'],
      ['Serene Study Sessions','piano_solo_nhac_nen_piano-serene-study-sessions-piano-version-nhac-nen-video-269279-96k.mp3'],
      ['Ghế Mây Lắc Lư','piano_solo_nhac_nen_piano-ghe-may-lac-lu-thu-gian-that-nhe-nhang-nhac-nen-video-223280-96k.mp3']
    ];
    var saved={};try{saved=JSON.parse(sessionStorage.getItem(KEY)||'{}')}catch(e){}
    var index=Number.isInteger(saved.index)?Math.max(0,Math.min(6,saved.index)):0;
    var audio=new Audio();audio.preload='metadata';audio.volume=saved.volume!=null?saved.volume:.38;
    var box=document.createElement('div');box.id='focusMusic';box.className='focus-music invite';box.innerHTML='<button class="focus-close" type="button">×</button><div class="focus-invite"><div class="focus-emoji">🎧</div><div><strong>Học hơi căng rồi hả?</strong><span>Bật chút piano nhẹ để tập trung hơn nè ✨</span><button class="focus-start" type="button">▶ Nghe nhạc cùng mình</button></div></div><div class="focus-controls"><div class="focus-now"><span>🎹 Tokutei Focus Mix ♪</span><small>7 bài piano</small></div><div class="focus-buttons"><button data-act="prev" type="button">⏮</button><button data-act="play" type="button">▶</button><button data-act="next" type="button">⏭</button><label>🔉 <input class="focus-volume" type="range" min="0" max="1" step="0.05" value="'+audio.volume+'"></label></div></div><button class="focus-mini" type="button">🎧 Nhạc tập trung</button>';document.body.appendChild(box);
    var start=box.querySelector('.focus-start'),play=box.querySelector('[data-act="play"]'),now=box.querySelector('.focus-now small'),vol=box.querySelector('.focus-volume');
    function url(i){return '/tokutei_focus_mix_7_mp3_96k/'+encodeURIComponent(tracks[i][1])}
    function save(wasPlaying){try{sessionStorage.setItem(KEY,JSON.stringify({index:index,time:isFinite(audio.currentTime)?audio.currentTime:0,volume:audio.volume,playing:wasPlaying==null?!audio.paused:wasPlaying}))}catch(e){}}
    function load(i,time){index=(i+tracks.length)%tracks.length;audio.src=url(index);audio.load();now.textContent=(index+1)+'/7 · '+tracks[index][0];if(time>0)audio.addEventListener('loadedmetadata',function seek(){audio.removeEventListener('loadedmetadata',seek);audio.currentTime=Math.min(time,Math.max(0,(audio.duration||time)-.2))})}
    function begin(){if(!audio.src)load(index,saved.time||0);var p=audio.play();if(p&&p.then)p.then(function(){play.textContent='⏸';box.classList.remove('invite');box.classList.add('active');save(true)}).catch(function(){now.textContent='Bấm ▶ để tiếp tục nhạc'})}
    function pause(){audio.pause();play.textContent='▶';save(false)}
    function toggle(){audio.paused?begin():pause()}
    function change(n){var shouldPlay=!audio.paused;save(false);load(index+n,0);if(shouldPlay||n!==0)begin()}
    audio.addEventListener('ended',function(){load(index+1,0);begin()});audio.addEventListener('play',function(){play.textContent='⏸'});audio.addEventListener('pause',function(){play.textContent='▶'});audio.addEventListener('error',function(){now.textContent='Không tải được MP3 · kiểm tra đường dẫn nhạc'});
    start.addEventListener('click',begin);play.addEventListener('click',toggle);box.querySelector('[data-act="prev"]').addEventListener('click',function(){change(-1)});box.querySelector('[data-act="next"]').addEventListener('click',function(){change(1)});vol.addEventListener('input',function(){audio.volume=parseFloat(this.value);save()});box.querySelector('.focus-close').addEventListener('click',function(){pause();box.classList.add('hidden')});box.querySelector('.focus-mini').addEventListener('click',function(){box.classList.remove('hidden');box.classList.add('invite')});window.addEventListener('pagehide',function(){save(!audio.paused)});
    load(index,saved.time||0);if(saved.playing){box.classList.remove('invite');box.classList.add('active');now.textContent=(index+1)+'/7 · '+tracks[index][0]+' · bấm ▶ để tiếp tục'}
  }
  function init(){decorate();focusPlayer()}if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
