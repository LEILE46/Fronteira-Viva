function trocarTela(idDaTela) {
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
        const agora = new Date();
        const tempo = agora.toLocaleTimeString('pt-BR');
        document.getElementById('relogio').innerText = tempo;
    }, 1000);
}
 
async function atualizarCambio() {
    const dolarEl = document.getElementById('preco-dolar');
    const guaraniEl = document.getElementById('preco-guarani');
    dolarEl.innerText = "Carregando...";
    guaraniEl.innerText = "Carregando...";
 
    try {
        const response = await fetch('https://economia.awesomeapi.com.br/last/USD-BRL,PYG-BRL');
        const data = await response.json();
        dolarEl.innerText = `R$ ${parseFloat(data.USDBRL.bid).toFixed(2)}`;
        guaraniEl.innerText = `R$ ${parseFloat(data.PYGBRL.bid).toFixed(4)}`;
    } catch (error) {
        dolarEl.innerText = "Erro";
        guaraniEl.innerText = "Erro";
    }
}
 
document.addEventListener('DOMContentLoaded', () => {
    iniciarRelogio();
    document.getElementById('form-login')?.addEventListener('submit', (e) => {
        e.preventDefault();
        const email = e.target.querySelector('input[type="email"]').value;
        alert(`Login realizado com sucesso!\nBem-vindo, ${email}`);
    });
});
 
setInterval(atualizarCambio, 300000);