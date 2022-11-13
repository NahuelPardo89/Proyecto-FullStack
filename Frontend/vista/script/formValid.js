const formulario = document.getElementById('formRegistro');
const formularioLog = document.getElementById('formLogin');
const inputs = document.querySelectorAll('#formRegistro input');
const inputs2 = document.querySelectorAll('#formLogin input');



const expresiones = {                                       //Expresiones regulares
	usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
	password: /^.{6,16}$/, // 6 a 16 digitos.
	correo: /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i
}
const campos = {
    usuario : false,
    contraseña : false,
    email : false
}

const validarFormulario = (e) => {
   switch (e.target.name) {
        case 'usuarioLog':
            if(expresiones.usuario.test(e.target.value)){  
                document.getElementById('grupo__usuarioLog').classList.remove('formulario__grupo-incorrecto');
                document.getElementById('grupo__usuarioLog').classList.add('formulario__grupo-correcto');
                document.querySelector('#grupo__usuarioLog i').classList.add('fa-check-circle');
                document.querySelector('#grupo__usuarioLog i').classList.remove('fa-times-circle');
                document.querySelector('#grupo__usuarioLog .formulario__input-errorLog').classList.remove('formulario__input-error-activo');
                campos[usuario] = True;


            } else {
              document.getElementById('grupo__usuarioLog').classList.add('formulario__grupo-incorrecto');
              document.getElementById('grupo__usuarioLog').classList.remove('formulario__grupo-correcto');
              document.querySelector('#grupo__usuarioLog i').classList.add('fa-times-circle');
              document.querySelector('#grupo__usuarioLog i').classList.remove('fa-check-circle');
              document.querySelector('#grupo__usuarioLog .formulario__input-errorLog').classList.add('formulario__input-error-activo');   
              campos[usuario] = False;
            }
        
                    
        break;
        case 'contraseñaLog':
            if(expresiones.usuario.test(e.target.value)){  
                document.getElementById('grupo__contraseñaLog').classList.remove('formulario__grupo-incorrecto');
                document.getElementById('grupo__contraseñaLog').classList.add('formulario__grupo-correcto');
                document.querySelector('#grupo__contraseñaLog i').classList.add('fa-check-circle');
                document.querySelector('#grupo__contraseñaLog i').classList.remove('fa-times-circle');
                document.querySelector('#grupo__contraseñaLog .formulario__input-errorLog').classList.remove('formulario__input-error-activo');
                campos[contraseña] = True;

            } else {
              document.getElementById('grupo__contraseñaLog').classList.add('formulario__grupo-incorrecto');
              document.getElementById('grupo__contraseñaLog').classList.remove('formulario__grupo-correcto');
              document.querySelector('#grupo__contraseñaLog i').classList.add('fa-times-circle');
              document.querySelector('#grupo__contraseñaLog i').classList.remove('fa-check-circle'); 
              document.querySelector('#grupo__contraseñaLog .formulario__input-errorLog').classList.add('formulario__input-error-activo'); 
              campos[contraseña] = False;  
            }
        
        
        break;
        case 'usuarioReg':
            validarCampo(expresiones.usuario, e.target,'usuario')
            
                        
        break;
        case 'contraseñaReg':
            validarCampo(expresiones.password, e.target, 'contraseña')
            
        break;
        case 'contraseñaReg2':
            
            
        
            validarContraseña2()
            
        break;
        case 'emailReg':
            validarCampo(expresiones.correo, e.target, 'email')
        break;
        
   }
};

const validarContraseña2 = () => {
    const inputPass1 = document.getElementById('passReg')
    const inputPass2 = document.getElementById('passReg2')
    if(inputPass1.value !== inputPass2.value){
                document.getElementById('grupo__contraseña2').classList.add('formulario__grupo-incorrecto')
                document.getElementById('grupo__contraseña2').classList.remove('formulario__grupo-correcto')
                document.querySelector('#grupo__contraseña2 i').classList.remove('fa-check-circle')
                document.querySelector('#grupo__contraseña2 i').classList.add('fa-times-circle')
                document.querySelector('#grupo__contraseña2 .formulario__input-error').classList.add('formulario__input-error-activo')
                campos[password] = false
                

    } else {
        document.getElementById('grupo__contraseña2').classList.remove('formulario__grupo-incorrecto')
        document.getElementById('grupo__contraseña2').classList.add('formulario__grupo-correcto')
        document.querySelector('#grupo__contraseña2 i').classList.add('fa-check-circle')
        document.querySelector('#grupo__contraseña2 i').classList.remove('fa-times-circle')
        document.querySelector('#grupo__contraseña2 .formulario__input-error').classList.remove('formulario__input-error-activo')
        campos[password] = true
        

    }
};



inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);
});
inputs2.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);
});




const validarCampo = (expresion, input, campo) => {
	if(expresion.test(input.value)){
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto');
		document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-times-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos[campo] = true
		
	} else {
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto');
		document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo');
        campos[campo] = False
        		
	}
}


formulario.addEventListener('submit', (e) => {
	e.preventDefault();

	if(campos.usuario && campos.contraseña && campos.email){
        formulario.reset();
        document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo')
        document.getElementById('formulario__mensaje').classList.remove('formulario__mensaje-error-activo')
    } else {
        document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-error-activo')
        document.getElementById('formulario__mensaje-exito').classList.remove('formulario__mensaje-exito-activo')
    }
});

