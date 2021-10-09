function validarRegistro() {
    
    var nombre = document.formularioRegistro.nombre.value;
    var apellido = document.formularioRegistro.apellido.value;
    var cedula = document.formularioRegistro.cedula;
    var password = document.formularioRegistro.password.value;
    var password1 = document.formularioRegistro.passwordC.value;
    var opcionr = document.formularioRegistro.condicionesr;
    var opcionesRadio = document.formularioRegistro.tipoId;
    var lista = document.getElementById("sexo");
    var dir = document.formularioRegistro.direccion.value;
    var tel = document.formularioRegistro.telefono.value;
    var email = document.formularioRegistro.correo;
    
    if(nombre == null || nombre.length < 2 || /^\s+$/.test(nombre)){
        alert("Se debe ingresar un nombre valido");
        return false;
    }

    if(apellido == null || apellido.length < 2 || /^\s+$/.test(apellido)){
        alert("Se debe ingresar un apellido valido");
        return false;
    }

    if(lista.selectedIndex == null || lista.selectedIndex == 0){
        alert ("Debes seleccionar tu sexo");
        return false;
    }
        
    var pulsado = false;
    var elegido = -1;
    for(i = 0; i < opcionesRadio.length; i++){
        if(opcionesRadio[i].checked == true){
            pulsado = true;
            elegido = i;
        }
    }
    if (pulsado == true){
        miOpcion = opcionesRadio[elegido].value
        /*alert("has elegido la opción: " + miOpcion + 
        "\n es correcto?")*/
    }
    else{
        alert("no has elegido ninguna opción de tipo de documento")
        return false
    }

    var cedula_len = cedula.value.length;
    if(cedula_len < 8 || cedula_len > 10 || isNaN(cedula.value)){
        alert("Se debe ingresar un número de identificación valido");
        return false;
    }

    if(dir == null || dir.length < 2 || /^\s+$/.test(dir)){
        alert("Se debe ingresar una dirección valida");
        return false;
    }

    if(!(/^\d{10}$/.test(tel)) && !(/^\d{1}\s\d{7}$/.test(tel))){
        alert("Se debe ingresar un número de teléfono valido");
        return false;
    }

    var formato_email = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;
    if (!email.value.match(formato_email)) {
        alert("Se debe ingresar un email con formato válido");
        return false;
    }

    if(password.length < 8){
        alert("Se debe ingresar un password con mas de 8 carateres");
        return false;
    }
    if (password != password1){
        alert("Las contraseñas deben coincidir")
        return false
    }
    
    if (opcionr.checked == true){
        alert("tu registro ha sido exitoso")
        window.open("/inicio/IniciarSesion")
    }
    else{
        alert("Debes aceptar nuestras politicas de privacidad")
        return false
    }
    
}

function validarLogin(){

    var cedula = document.formularioLogin.cedula.value;
    var password = document.formularioLogin.password.value;
    var opcion = document.formularioLogin.condiciones;

    if(cedula.length < 8 || cedula.length > 10 || isNaN(cedula)){
        alert("Se debe ingresar un número de identificación valido");
        return false;
    }

    if(password.length < 8){
        alert("Se debe ingresar un password con mas de 8 carateres");
        return false;
    }

    if (opcion.checked == true){
        window.open("/inicio/IniciarSesion/Paciente");
    }
    else{
        alert("Debes aceptar nuestras politicas de privacidad")
        return false
    }
}