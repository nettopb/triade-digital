const $=id=>document.getElementById(id);let students=[],classes=[];
const api=async(path,opts={})=>{const r=await fetch('/api'+path,{headers:{'Content-Type':'application/json'},...opts});const d=await r.json();if(!r.ok)throw Error(d.detail||'Erro na operação');return d};
function notice(msg){$('notice').textContent=msg;$('notice').style.display='block';setTimeout(()=>$('notice').style.display='none',2600)}
function tab(name){document.querySelectorAll('.panel').forEach(x=>x.classList.add('hidden'));$(name).classList.remove('hidden');document.querySelectorAll('.tab').forEach(x=>x.classList.toggle('active',x.dataset.tab===name))}
document.querySelectorAll('.tab').forEach(b=>b.onclick=()=>tab(b.dataset.tab));
async function loadAll(){try{[students,classes]=await Promise.all([api('/students'),api('/classes')]);const alerts=await api('/alerts');$('studentCount').textContent=students.length;$('classCount').textContent=classes.length;$('alertCount').textContent=alerts.length;
$('studentsBody').innerHTML=students.map(s=>`<tr><td>${esc(s.name)}</td><td>${esc(s.registration)}</td><td>${esc(s.class_name)}</td><td><button class="action" onclick="removeStudent(${s.id})">Inativar</button></td></tr>`).join('')||'<tr><td colspan="4">Nenhum estudante cadastrado.</td></tr>';
$('classesList').innerHTML=classes.map(c=>`<span class="chip">${esc(c.name)}</span>`).join('')||'<p class="hint">Nenhuma turma cadastrada.</p>';
const options=classes.map(c=>`<option value="${c.id}">${esc(c.name)}</option>`).join('');$('studentClass').innerHTML='<option value="">Sem turma</option>'+options;$('attendanceClass').innerHTML='<option value="">Turma</option>'+options;
$('attendanceStudent').innerHTML='<option value="">Estudante</option>'+students.map(s=>`<option value="${s.id}">${esc(s.name)}</option>`).join('');
$('alertsList').innerHTML=alerts.map(a=>`<div class="alert"><b>${esc(a.student)}</b> — ${a.consecutive_absences} faltas consecutivas. Última ausência: ${a.last_absence}</div>`).join('')||'<div class="empty">Nenhum alerta no momento.</div>';
}catch(e){notice(e.message)}}
function esc(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
$('studentForm').onsubmit=async e=>{e.preventDefault();try{await api('/students',{method:'POST',body:JSON.stringify({name:$('studentName').value,registration:$('registration').value,class_id:$('studentClass').value?Number($('studentClass').value):null})});e.target.reset();notice('Estudante cadastrado');loadAll()}catch(x){notice(x.message)}};
$('classForm').onsubmit=async e=>{e.preventDefault();try{await api('/classes',{method:'POST',body:JSON.stringify({name:$('className').value})});e.target.reset();notice('Turma criada');loadAll()}catch(x){notice(x.message)}};
$('attendanceForm').onsubmit=async e=>{e.preventDefault();try{await api('/attendance',{method:'POST',body:JSON.stringify({class_id:Number($('attendanceClass').value),student_id:Number($('attendanceStudent').value),day:$('attendanceDay').value,present:$('present').value==='true'})});notice('Frequência salva');loadAll()}catch(x){notice(x.message)}};
async function removeStudent(id){if(!confirm('Inativar este estudante?'))return;try{await api('/students/'+id,{method:'DELETE'});notice('Estudante inativado');loadAll()}catch(e){notice(e.message)}}
$('today').textContent=new Intl.DateTimeFormat('pt-BR',{dateStyle:'full'}).format(new Date());$('attendanceDay').value=new Date().toISOString().slice(0,10);loadAll();
