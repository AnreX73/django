
/* библиотека для закрытия модальных окон без гемора*/
!function(e){"function"!=typeof e.matches&&(e.matches=e.msMatchesSelector||e.mozMatchesSelector||e.webkitMatchesSelector||function(e){for(var t=this,o=(t.document||t.ownerDocument).querySelectorAll(e),n=0;o[n]&&o[n]!==t;)++n;return Boolean(o[n])}),"function"!=typeof e.closest&&(e.closest=function(e){for(var t=this;t&&1===t.nodeType;){if(t.matches(e))return t;t=t.parentNode}return null})}(window.Element.prototype);
/* Получаем массив кнопок */
document.addEventListener('DOMContentLoaded', function() {
    var modalButtons = document.querySelectorAll('.js-open-modal'),
        closeButtons = document.querySelectorAll('.js-modal-close'),
        overlay      = document.querySelectorAll('.js-overlay-modal')
    /* Перебираем массив кнопок */
    modalButtons.forEach(function(item){
    /* Назначаем каждой кнопке обработчик клика */
    item.addEventListener('click', function(e) {
        e.preventDefault();
        /* ищем модальное окно по атрибуту кнопки */
        var modalId = this.getAttribute('data-modal');
        modalElem = document.querySelector('.js-overlay-modal[data-modal="' + modalId + '"]');
        modalElem.style.display = 'block';
     });
});
closeButtons.forEach(function(item){
    item.addEventListener('click', function(e) {
       var parentModal = this.closest('.modal');
       parentModal.style.display = 'none';  
    });

 });
 document.body.addEventListener('keyup', function (e) {
    var key = e.keyCode;
    if (key == 27) {
        openModal = document.querySelectorAll('.modal');
        openModal.forEach(function(item){
            item.style.display = 'none';
        });
    };
}, false);

overlay.forEach(function(item){
    /* Назначаем каждой кнопке обработчик клика */
    item.addEventListener('click', function(e) {
        e.preventDefault();
        /* ищем модальное окно по атрибуту кнопки */
        var closeModal = this.closest('.modal');
        closeModal.style.display = 'none';
     });
});

});


