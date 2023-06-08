let boton = document.getElementById("generarBoton")

boton.addEventListener("click", function(evento){
    evento.preventDefault()
    let reporte = document.getElementById("reporte")
    reporte.classList.remove("d-none")
})

let botonPdf = document.getElementById("generarPdf");

botonPdf.addEventListener("click", function(e){

    let nuevaVentana = window.open('../pdf/archivo.pdf', '_blank');

      if (nuevaVentana) {
        nuevaVentana.focus();  // Dar foco a la nueva ventana
    } else {
        alert('No se pudo abrir la ventana del PDF');
    }
}); 


let botonY = document.getElementById("pdfYarumal");

function yarumal(){
    let nuevaVentana = window.open('../pdf/archivoYarumal.pdf', '_blank');

          if (nuevaVentana) {
        nuevaVentana.focus();  // Dar foco a la nueva ventana
    } else {
        alert('No se pudo abrir la ventana del PDF');
    }

}

let botonCaucasia = document.getElementById("pdfCaucasia")

function caucasia(){

    let nuevaVentana = window.open('../pdf/archivoCaucasia.pdf', '_blank');

          if (nuevaVentana) {
        nuevaVentana.focus();  // Dar foco a la nueva ventana
    }else{alert('No se pudo abrir la ventana del PDF')}
}

let botonBelmira = document.getElementById("pdfBelmira")

function belmira(){

    let nuevaVentana = window.open('../pdf/archivoBelmira.pdf', '_blank');

          if (nuevaVentana) {
        nuevaVentana.focus();  // Dar foco a la nueva ventana
    }else{alert('No se pudo abrir la ventana del PDF')}
}


let botonCaramanta = document.getElementById("pdfCaramanta")

function caramanta(){

    let nuevaVentana = window.open('../pdf/archivoCaramanta.pdf', '_blank');

        if(nuevaVentana){
        nuevaVentana.focus();
    }else {alert("No se ha podido abrir la ventana del PDF")}
}

let botonBello = document.getElementById("pdfBello")

function bello(){

let nuevaVentana = window.open('../pdf/archivoBello.pdf', '_blank');

          if (nuevaVentana) {
        nuevaVentana.focus();  // Dar foco a la nueva ventana
    }else{alert('No se pudo abrir la ventana del PDF')}
}
