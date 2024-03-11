const btnsEliminacion=document.querySelectorAll('.btnEliminacion');

(function () {
    
    btnsEliminacion.forEach(btn => {
        btn.addEventListener('click', function(e) {
            let confirmacion=confirm("Borrado prro");
            if (!confirmacion){
                e.preventDefault();
            }
        })
    })

})();