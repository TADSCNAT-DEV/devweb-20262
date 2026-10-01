    // Script para ativar o burger menu no mobile
    document.addEventListener('DOMContentLoaded', () => {
        const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
        
        $navbarBurgers.forEach( el => {
            el.addEventListener('click', () => {
                const target = el.dataset.target;
                const $target = document.getElementById(target);
                el.classList.toggle('is-active');
                $target.classList.toggle('is-active');
            });
        });
        (document.querySelectorAll('.notification .delete') || []).forEach(($delete) => {
            const $notification = $delete.parentNode;
            $delete.addEventListener('click', () => {
                $notification.parentNode.removeChild($notification);
            });
        });
    });
    // Adiciona efeito visual ao clicar nos cards
    document.querySelectorAll('.hover-card').forEach(card => {
        card.addEventListener('click', function(e) {
            // Permite que os links funcionem normalmente
            if (!e.target.closest('a')) {
                console.log('Card clicado:', this.querySelector('.title').textContent);
            }
        });
    });