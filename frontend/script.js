const chatEl = document.getElementById('chat');
const typingEl = document.getElementById('typing');
const msgEl = document.getElementById('msg');
const sendBtn = document.getElementById('sendBtn');
const emptyEl = document.getElementById('empty');

function add(text, cls) {
  const d = document.createElement('div');
  d.className = 'msg ' + cls;
  d.innerHTML = text;
  chatEl.appendChild(d);
  emptyEl.style.display = 'none';
  chatEl.scrollTop = chatEl.scrollHeight;
}

function setTyping(on){
  typingEl.style.display = on ? 'flex' : 'none';
}

async function send(){
  const q = msgEl.value.trim();
  if(!q) return;
  add(q, 'user');
  msgEl.value = '';

  setTyping(true);

  try{
    const res = await fetch('http://127.0.0.1:5000/chat',{
      method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({query:q})
    });
    const data = await res.json();
    setTyping(false);
    add(data.answer, 'bot');
  }catch(e){
    setTyping(false);
    add('Sorry — unable to reach the server. Please ensure the backend is running.', 'bot');
  }
}

sendBtn.addEventListener('click', send);
msgEl.addEventListener('keydown', (e)=>{ if(e.key==='Enter') send(); });
