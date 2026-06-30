const API = '';
let token = null;
let usuarioAtual = null;

function showSection(id) {
    document.querySelectorAll('main > section').forEach(s => s.style.display = 'none');
    document.getElementById(id + '-section').style.display = 'block';
}

function showRegister() { showSection('register'); }
function showRecuperar() { showSection('recuperar'); }

async function api(method, path, body = null) {
    const opts = { method, headers: {} };
    if (token) opts.headers['Authorization'] = `Bearer ${token}`;
    if (body && !(body instanceof FormData)) {
        opts.headers['Content-Type'] = 'application/json';
        opts.body = JSON.stringify(body);
    } else if (body instanceof FormData) {
        opts.body = body;
    }
    const res = await fetch(API + path, opts);
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || 'Erro na requisição');
    return data;
}

document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    try {
        const data = await api('POST', '/auth/login', { email: document.getElementById('login-email').value, senha: document.getElementById('login-senha').value });
        token = data.access_token;
        usuarioAtual = data.usuario;
        document.getElementById('main-nav').style.display = 'flex';
        document.querySelector('#home-section h1').textContent = `Bem-vindo, ${usuarioAtual.nome}!`;
        showSection('home');
    } catch (err) { document.getElementById('login-error').textContent = err.message; }
});

document.getElementById('register-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    try {
        await api('POST', '/auth/register', {
            nome: document.getElementById('reg-nome').value,
            email: document.getElementById('reg-email').value,
            curso: document.getElementById('reg-curso').value,
            senha: document.getElementById('reg-senha').value,
            pergunta_seguranca: document.getElementById('reg-pergunta').value,
            resposta_seguranca: document.getElementById('reg-resposta').value,
        });
        alert('Cadastro realizado! Faça login.');
        document.getElementById('register-form').reset();
        showSection('login');
    } catch (err) { document.getElementById('register-error').textContent = err.message; }
});

document.getElementById('recuperar-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    try {
        await api('POST', '/auth/recuperar-senha', {
            email: document.getElementById('rec-email').value,
            resposta_seguranca: document.getElementById('rec-resposta').value,
            nova_senha: document.getElementById('rec-nova-senha').value,
        });
        alert('Senha redefinida!');
        showSection('login');
    } catch (err) { document.getElementById('recuperar-error').textContent = err.message; }
});

function logout() {
    token = null; usuarioAtual = null;
    document.getElementById('main-nav').style.display = 'none';
    showSection('login');
}

async function renderProjects() {
    const tbody = document.getElementById('projects-tbody');
    const tituloFilter = document.getElementById('filter-titulo').value.toLowerCase();
    const statusFilter = document.getElementById('filter-status').value;
    try {
        let url = '/projects/';
        if (statusFilter) url += '?status=' + statusFilter;
        const projects = await api('GET', url);
        tbody.innerHTML = projects.filter(p => !tituloFilter || p.titulo.toLowerCase().includes(tituloFilter))
            .map(p => `<tr><td>${p.titulo}</td><td><span style="background:#eee;padding:2px 8px;border-radius:4px">${p.status}</span></td>
            <td><button onclick="viewProject(${p.id})">Ver</button> <button onclick="editProject(${p.id})">Editar</button> <button onclick="deleteProject(${p.id})">Excluir</button></td></tr>`).join('');
    } catch (err) { tbody.innerHTML = `<tr><td colspan="3">Erro: ${err.message}</td></tr>`; }
}

function showProjectForm(project) {
    showSection('project-form');
    document.getElementById('project-form-title').textContent = project ? 'Editar Projeto' : 'Novo Projeto';
    ['pf-id','pf-titulo','pf-resumo','pf-periodo','pf-equipe'].forEach(id => document.getElementById(id).value = project ? (project[id.replace('pf-','')] || '') : '');
    document.getElementById('pf-status').value = project ? (project.status || 'em-desenvolvimento') : 'em-desenvolvimento';
}

document.getElementById('project-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const id = document.getElementById('pf-id').value;
    const data = {
        titulo: document.getElementById('pf-titulo').value,
        resumo: document.getElementById('pf-resumo').value,
        periodo: document.getElementById('pf-periodo').value,
        equipe: document.getElementById('pf-equipe').value,
        status: document.getElementById('pf-status').value,
    };
    try {
        if (id) await api('PUT', `/projects/${id}`, data);
        else await api('POST', '/projects/', data);
        document.getElementById('project-form').reset();
        showSection('projects');
    } catch (err) { document.getElementById('project-form-error').textContent = err.message; }
});

async function editProject(id) { try { showProjectForm(await api('GET', `/projects/${id}`)); } catch (err) { alert(err.message); } }
async function deleteProject(id) { if (!confirm('Excluir?')) return; try { await api('DELETE', `/projects/${id}`); renderProjects(); } catch (err) { alert(err.message); } }

async function viewProject(id) {
    try {
        const p = await api('GET', `/projects/${id}`);
        document.getElementById('detail-content').innerHTML = `<h2>${p.titulo}</h2>
        <p><strong>Status:</strong> ${p.status} | <strong>Período:</strong> ${p.periodo || '-'} | <strong>Equipe:</strong> ${p.equipe || '-'}</p>
        <p><strong>Resumo:</strong> ${p.resumo || '-'}</p>`;
        showSection('project-detail');
    } catch (err) { alert(err.message); }
}

document.getElementById('contact-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    try {
        await api('POST', '/support/contact', {
            nome: document.getElementById('ct-nome').value,
            email: document.getElementById('ct-email').value,
            assunto: document.getElementById('ct-assunto').value,
            mensagem: document.getElementById('ct-mensagem').value,
        });
        document.getElementById('contact-form').reset();
        document.getElementById('contact-success').style.display = 'block';
        setTimeout(() => document.getElementById('contact-success').style.display = 'none', 3000);
    } catch (err) { alert(err.message); }
});

showSection('login');