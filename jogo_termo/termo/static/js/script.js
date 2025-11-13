// Força o input a ficar em maiúsculas
document.querySelector('input[name="palpite"]').addEventListener('input', (e) => {
    e.target.value = e.target.value.toUpperCase();
});

// Foco automático ao carregar
window.onload = () => {
    document.querySelector('input[name="palpite"]').focus();
};
