var btnAbrirPopup = document.getElementById('btn-abrir-popup'),
    overlay = document.getElementById('overlay'),
    popup = document.getElementById('popup'),
    btnCerrarPopup = document.getElementById('btn-cerrar-popup'),
    btnAbrirPopupReg = document.getElementById('btn-abrir-popupReg'),
    overlay2 = document.getElementById('overlay2'),
    popupReg = document.getElementById('popupReg'),
    btnCerrarPopupReg = document.getElementById('btn-cerrar-popupReg');


btnAbrirPopup.addEventListener('click', function(){
    overlay.classList.add('active');
});

btnCerrarPopup.addEventListener('click', function(){
    overlay.classList.remove('active');
});

btnAbrirPopupReg.addEventListener('click', function(){
    overlay2.classList.add('active2');
});

btnCerrarPopupReg.addEventListener('click', function(){
    overlay2.classList.remove('active2');
});