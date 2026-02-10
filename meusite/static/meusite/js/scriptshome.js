async function atualizarCambio() {
    const dolarEl = document.getElementById('preco-dolar');
    const guaraniEl = document.getElementById('preco-guarani');
    if (!dolarEl || !guaraniEl) return;

    dolarEl.innerText = "Carregando...";
    guaraniEl.innerText = "Carregando...";

    try {
        const response = await fetch('https://economia.awesomeapi.com.br/last/USD-BRL,PYG-BRL');
        const data = await response.json();
        
        const dolar = parseFloat(data.USDBRL.bid).toFixed(2);
        const guarani = parseFloat(data.PYGBRL.bid).toFixed(4);

        dolarEl.innerText = `R$ ${dolar}`;
        guaraniEl.innerText = `R$ ${guarani}`;
    } catch (error) {
        dolarEl.innerText = "Erro";
        guaraniEl.innerText = "Erro";
    }
}

function falarTexto(texto) {
    window.speechSynthesis.cancel();
    if (!texto) return;
    const mensagem = new SpeechSynthesisUtterance(texto);
    mensagem.lang = 'pt-BR';
    mensagem.rate = 1.0;
    window.speechSynthesis.speak(mensagem);
}

function abrirMapa(localizacao) {
    if (!localizacao || localizacao === "None") {
        alert("Localização não disponível.");
        return;
    }
    const url = `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(localizacao)}`;
    window.open(url, '_blank');
}

function trocarTela(idDaTela) {
    window.speechSynthesis.cancel();
    document.querySelectorAll('.tela').forEach(tela => tela.classList.remove('ativa'));
    const telaAlvo = document.getElementById(idDaTela);
    if (telaAlvo) {
        telaAlvo.classList.add('ativa');
    }
    if (idDaTela === 'cambio') {
        atualizarCambio();
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function iniciarRelogio() {
    setInterval(() => {
        const relogioEl = document.getElementById('relogio');
        if (relogioEl) {
            relogioEl.innerText = new Date().toLocaleTimeString('pt-BR');
        }
    }, 1000);
}

document.addEventListener('DOMContentLoaded', () => {
    iniciarRelogio();
    atualizarCambio();
    setInterval(atualizarCambio, 300000);
    
    document.getElementById('form-login')?.addEventListener('submit', (e) => {
        e.preventDefault();
        const email = e.target.querySelector('input[type="email"]')?.value || "Usuário";
        alert(`Login realizado com sucesso!\nBem-vindo, ${email}`);
    });
});