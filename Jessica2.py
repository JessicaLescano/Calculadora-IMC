import flet as ft

# Función para validar los datos y procesarlos (incluye cálculo de IMC)
def procesar_datos(nombre, edad, peso, altura):
    try:
        edad = int(edad)
        peso = float(peso)
        altura = float(altura) / 100  # Convertir de cm a metros para el cálculo del IMC
        imc = peso / (altura ** 2)

        # Definir el mensaje de mayor o menor de edad
        if edad >= 18:
            mensaje_edad = f"{nombre}, eres mayor de edad."
        else:
            mensaje_edad = f"{nombre}, eres menor de edad."

        # Calcular el IMC y agregar mensaje
        mensaje_imc = f"Tu IMC es: {imc:.2f}. "
        if imc < 18.5:
            mensaje_imc += "Estás por debajo del peso normal."
        elif 18.5 <= imc < 24.9:
            mensaje_imc += "Tienes un peso normal."
        elif 25 <= imc < 29.9:
            mensaje_imc += "Tienes sobrepeso."
        else:
            mensaje_imc += "Tienes obesidad."

        return f"{mensaje_edad}\n{mensaje_imc}"

    except ValueError:
        return "Por favor, introduce valores válidos en todos los campos."

# Función que se activa cuando el usuario hace clic en 'Enviar'
def enviar_click(e, page):
    nombre = nombre_input.value
    edad = edad_input.value
    peso = peso_input.value
    altura = altura_input.value

    if not nombre or not edad or not peso or not altura:
        resultado_text.value = "Por favor, completa todos los campos."
    else:
        resultado_text.value = procesar_datos(nombre, edad, peso, altura)

    page.update()

# Función que se activa cuando el usuario hace clic en 'Limpiar'
def limpiar_click(e, page):
    nombre_input.value = ""
    edad_input.value = ""
    peso_input.value = ""
    altura_input.value = ""
    resultado_text.value = ""
    page.update()

# Función para mostrar la ventana principal con el formulario y la calculadora de IMC
def mostrar_calculadora(page):
    global nombre_input, edad_input, peso_input, altura_input, resultado_text

    # Limpiar la ventana actual
    page.controls.clear()

    # Crear elementos de la calculadora
    nombre_input = ft.TextField(label="Nombre", width=250)
    edad_input = ft.TextField(label="Edad", keyboard_type=ft.KeyboardType.NUMBER, width=250)
    peso_input = ft.TextField(label="Peso (kg)", keyboard_type=ft.KeyboardType.NUMBER, width=250)
    altura_input = ft.TextField(label="Altura (cm)", keyboard_type=ft.KeyboardType.NUMBER, width=250)
    resultado_text = ft.Text()

    enviar_boton = ft.ElevatedButton(text="Enviar", on_click=lambda e: enviar_click(e, page))
    limpiar_boton = ft.ElevatedButton(text="Limpiar", on_click=lambda e: limpiar_click(e, page))

    # Agregar los elementos a la página, centrados
    page.add(
        ft.Column(
            [
                ft.Text("Formulario de Usuario y Calculadora de IMC", style="headlineMedium", text_align="center"),
                nombre_input,
                edad_input,
                peso_input,
                altura_input,
                enviar_boton,
                limpiar_boton,
                resultado_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    page.update()

# Función que se activa cuando el usuario acepta los términos
def aceptar_terminos(e, page):
    # Redirigir a la ventana principal de la calculadora
    mostrar_calculadora(page)

# Interfaz de usuario inicial (ventana de bienvenida)
def main(page: ft.Page):
    page.title = "Bienvenido a la Aplicación"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Crear ventana de bienvenida
    bienvenida_text = ft.Text("¡Bienvenido a la aplicación!", style="headlineMedium", text_align="center")
    terminos_text = ft.Text("Al usar esta app, aceptas nuestros términos y condiciones.", text_align="center")
    aceptar_boton = ft.ElevatedButton(text="Aceptar y Continuar", on_click=lambda e: aceptar_terminos(e, page))

    # Añadir los elementos de bienvenida a la página, centrados
    page.add(
        ft.Column(
            [
                bienvenida_text,
                terminos_text,
                aceptar_boton,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# Iniciar la aplicación
ft.app(target=main)
