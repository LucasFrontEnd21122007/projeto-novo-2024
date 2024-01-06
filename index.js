// static/script.js

document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('form').onsubmit = function () {
        const nome = document.querySelector('#nome').value;
        const tipo = document.querySelector('#tipo').value;
        const data = document.querySelector('#data').value;

        if (!nome || !tipo || !data) {
            alert('Por favor, preencha todos os campos.');
            return false;
        }

        return true;
    };
});