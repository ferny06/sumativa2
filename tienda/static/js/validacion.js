document.addEventListener('DOMContentLoaded', function() {

    if (!document.getElementById('alerta')) {
        const alertaContainer = document.createElement('div');
        alertaContainer.id = 'alerta';
        alertaContainer.className = 'alert visually-hidden';
        alertaContainer.style.position = 'fixed';
        alertaContainer.style.top = '20px';
        alertaContainer.style.right = '20px';
        alertaContainer.style.zIndex = '1000';
        document.body.appendChild(alertaContainer);
    }

    const ocultarAlerta = () => {
        const alerta = document.getElementById("alerta");
        alerta.classList.add("visually-hidden");
    };

    const mostrarAlerta = (tipo, mensaje) => {
        const alerta = document.getElementById("alerta");
        alerta.innerHTML = mensaje;
        alerta.className = "alert alert-" + tipo;
        alerta.classList.remove("visually-hidden");
        setTimeout(ocultarAlerta, 5000);
    };

    const formularioRegistro = document.querySelector('form[action="/enviar-mensaje"]'); 
    const formularioLogin = document.querySelector('form:not([action])'); 
    const formularioContacto = document.querySelector('form[action="/enviar-mensaje"]'); 
    
    if (formularioRegistro && document.querySelector('h3').textContent.includes('Regístrate')) {
        configurarValidacionRegistro(formularioRegistro);
    } else if (formularioLogin && document.querySelector('h3').textContent.includes('Inicia sesión')) {
        configurarValidacionLogin(formularioLogin);
    } else if (formularioContacto && document.querySelector('h3').textContent.includes('Contacto')) {
        configurarValidacionContacto(formularioContacto);
    }

    function configurarValidacionRegistro(formulario) {
        formulario.addEventListener('submit', function(event) {
            event.preventDefault();
            
            const nombre = document.getElementById('nombre');
            const email = document.getElementById('email');
            const telefono = document.getElementById('telefono');
            const pais = document.getElementById('pais');
            const ciudad = document.getElementById('ciudad');
            const password = document.getElementById('password');
            
            let valido = true;
            limpiarErrores();
            

            if (!nombre.value.trim()) {
                mostrarError(nombre, 'Por favor ingresa tu nombre completo');
                document.getElementById('fb-nombre').style.display = 'block';
                valido = false;
            } else if (nombre.value.trim().length < 3) {
                mostrarError(nombre, 'El nombre debe tener al menos 3 caracteres');
                valido = false;
            }
            

            if (!email.value.trim()) {
                mostrarError(email, 'Por favor ingresa tu correo electrónico');
                document.getElementById('fb-email').style.display = 'block';
                valido = false;
            } else if (!validarEmail(email.value)) {
                mostrarError(email, 'Por favor ingresa un correo electrónico válido');
                valido = false;
            }
   
            if (telefono.value.trim() && !validarTelefono(telefono.value)) {
                mostrarError(telefono, 'Por favor ingresa un número de teléfono válido (ej: +56912345678 o 912345678)');
                valido = false;
            }
            

            if (!pais.value.trim()) {
                mostrarError(pais, 'Por favor ingresa tu país');
                document.getElementById('fb-pais').style.display = 'block';
                valido = false;
            }
            

            if (!ciudad.value.trim()) {
                mostrarError(ciudad, 'Por favor ingresa tu ciudad');
                document.getElementById('fb-ciudad').style.display = 'block';
                valido = false;
            }

            if (password && !validarPasswordCompleja(password.value)) {
                mostrarError(password, 'La contraseña no cumple con los requisitos de seguridad');
                valido = false;
            }
            
            if (!valido) {
                mostrarAlerta('warning', 'Por favor, completa todos los campos correctamente.');
                return false;
            }
            
            mostrarAlerta('success', 'Registro completado correctamente.');

            return false;
        });
    }

    function configurarValidacionLogin(formulario) {
        formulario.addEventListener('submit', function(event) {
            event.preventDefault();
            
            const email = document.getElementById('email');
            const password = document.getElementById('password');
            
            let valido = true;
            limpiarErrores();
            

            if (!email.value.trim()) {
                mostrarError(email, 'Por favor ingresa tu correo electrónico');
                document.getElementById('fb-email').style.display = 'block';
                valido = false;
            } else if (!validarEmail(email.value)) {
                mostrarError(email, 'Por favor ingresa un correo electrónico válido');
                valido = false;
            }

            if (!password.value.trim()) {
                mostrarError(password, 'Por favor ingresa tu contraseña');
                document.getElementById('fb-password').style.display = 'block';
                valido = false;
            }
            
            if (!valido) {
                mostrarAlerta('warning', 'Por favor, completa todos los campos.');
                return false;
            }
            
            mostrarAlerta('success', 'Inicio de sesión exitoso. Redireccionando...');

            return false;
        });
    }

    function configurarValidacionContacto(formulario) {
        formulario.addEventListener('submit', function(event) {
            event.preventDefault();
            
            const nombre = document.getElementById('nombre');
            const email = document.getElementById('email');
            const telefono = document.getElementById('telefono');
            const pais = document.getElementById('pais');
            const ciudad = document.getElementById('ciudad');
            const mensaje = document.getElementById('mensaje');
            
            let valido = true;
            limpiarErrores();
            

            if (!nombre.value.trim()) {
                mostrarError(nombre, 'Por favor ingresa tu nombre completo');
                document.getElementById('fb-nombre').style.display = 'block';
                valido = false;
            } else if (nombre.value.trim().length < 3) {
                mostrarError(nombre, 'El nombre debe tener al menos 3 caracteres');
                valido = false;
            }


            if (!email.value.trim()) {
                mostrarError(email, 'Por favor ingresa tu correo electrónico');
                document.getElementById('fb-email').style.display = 'block';
                valido = false;
            } else if (!validarEmail(email.value)) {
                mostrarError(email, 'Por favor ingresa un correo electrónico válido');
                valido = false;
            }
            

            if (telefono.value.trim() && !validarTelefono(telefono.value)) {
                mostrarError(telefono, 'Por favor ingresa un número de teléfono válido (ej: +56912345678 o 912345678)');
                valido = false;
            }
            

            if (!pais.value.trim()) {
                mostrarError(pais, 'Por favor ingresa tu país');
                document.getElementById('fb-pais').style.display = 'block';
                valido = false;
            }
            

            if (!ciudad.value.trim()) {
                mostrarError(ciudad, 'Por favor ingresa tu ciudad');
                document.getElementById('fb-ciudad').style.display = 'block';
                valido = false;
            }


            if (!mensaje.value.trim()) {
                mostrarError(mensaje, 'Por favor ingresa tu mensaje');
                document.getElementById('fb-mensaje').style.display = 'block';
                valido = false;
            } else if (mensaje.value.trim().length < 10) {
                mostrarError(mensaje, 'El mensaje debe tener al menos 10 caracteres');
                valido = false;
            }
            
            if (!valido) {
                mostrarAlerta('warning', 'Por favor, completa todos los campos correctamente.');
                return false;
            }
            
            mostrarAlerta('success', 'Mensaje enviado correctamente.');

            return false;
        });
    }


    function validarEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
    
    function validarTelefono(telefono) {
        const re = /^(\+56|56)?[\s-]?[9][\s-]?[0-9]{4}[\s-]?[0-9]{4}$/;
        return re.test(telefono);
    }
    
    function validarPasswordCompleja(password) {
        const validations = [
            password.length >= 8,
            password.length <= 20,
            /[A-Z]/.test(password),
            /[0-9]/.test(password),
            /[^A-Za-z0-9]/.test(password)
        ];
        return validations.every(validation => validation);
    }
    
    function mostrarError(input, mensaje) {
        const formGroup = input.closest('.mb-3') || input.closest('.col-md-6');
        const errorText = document.createElement('div');
        errorText.className = 'text-danger mt-1';
        errorText.textContent = mensaje;
        formGroup.appendChild(errorText);
        input.classList.add('is-invalid');
    }
    
    function limpiarErrores() {

        document.querySelectorAll('[id^="fb-"]').forEach(el => {
            el.style.display = 'none';
        });
        

        document.querySelectorAll('.text-danger').forEach(el => el.remove());
        document.querySelectorAll('.is-invalid').forEach(el => el.classList.remove('is-invalid'));
    }
});