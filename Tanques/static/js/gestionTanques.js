const btnsEliminacion=document.querySelectorAll('.btnEliminacion');

(function () {
    
    btnsEliminacion.forEach(btn => {
        console.log(btn)
        btn.addEventListener('click', function(e) {
            let confirmacion=confirm("Borrado prro");
            if (!confirmacion){
                e.preventDefault();
            }
        })
    })

})();