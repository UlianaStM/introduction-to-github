import streamlit as st
import random

# Función para generar personajes aleatorios
def generar_personaje():
    nombres = ["Emma", "Olivia", "Noah", "Liam", "Ava", "Sophia", "William", "Mason", "Mia", "Isabella"]
    descripciones_fem = ["Una niña aventurera con cabello castaño y ojos verdes.", "Una joven talentosa con pasión por la música."]
    descripciones_masc = ["Un chico inteligente con gafas y pecas.", "Un joven talentoso con pasión por la música."]
    personalidades = ["Optimista y valiente", "Tímido pero creativo", "Amigable y extrovertida"]
    
    nombre = random.choice(nombres)
    descripcion = random.choice(descripciones_fem if nombre in ["Emma", "Olivia", "Ava", "Sophia", "Mia", "Isabella"] else descripciones_masc)
    personalidad = random.choice(personalidades)
    
    return nombre, descripcion, personalidad

# Título y descripción de la aplicación
st.title("Creador de Historias para Niños con Asperger")
st.markdown("""
## ¡Hola a todos los niños y niñas con Asperger!

**Esta aplicación está creada especialmente para ustedes.** Aquí pueden dejar volar su imaginación y crear historias increíbles de amor, aventura, ciencia ficción, terror, comedia y mucho más.

**¿Qué están esperando?**

Empiecen a crear sus propias aventuras llenas de personajes fantásticos, emociones y lugares mágicos.

**¡Diviértanse y expresen su creatividad sin límites!**
""")

# Selección de franja de edad
franja_edad = st.selectbox("Selecciona tu rango de edad:", ["De 4 a 6 años", "De 7 a 9 años", "De 10 a 12 años", "De 13 a 15 años", "De 16 a 18 años", "De 19 a 25 años", "Más de 25 años"])

# Adaptación de la experiencia según la franja de edad
plantillas = {
    "De 4 a 6 años": """**Título:** Mi historia

**Introducción:**
Un día, yo estaba jugando en el parque... (Describe el inicio de la historia de forma sencilla, utilizando frases cortas y lenguaje familiar.)

**Desarrollo:**
... (Narra los eventos principales de la historia, incluyendo un conflicto o desafío simple y un final feliz. Utiliza un lenguaje sencillo y descriptivo.)

**Desenlace:**
Al final, ... (Describe la resolución de la historia de forma clara y concisa, enfatizando el aprendizaje o la moraleja.)

**Reflexión:**
¿Te gustó tu historia? ¿Qué aprendiste con ella? (Opcional: Invita al niño a reflexionar sobre su historia de forma sencilla y divertida.)
""",
    "De 7 a 9 años": """**Título:**

**Introducción:**
En un lugar lejano llamado... (Describe el inicio de la historia de forma más elaborada, utilizando descripciones vívidas e introduciendo a los personajes principales.)

**Desarrollo:**
... (Narra los eventos principales de la historia, incluyendo un conflicto o desafío más complejo y un desenlace emocionante. Utiliza un lenguaje descriptivo y variado.)

**Desenlace:**
Al final, ... (Describe la resolución de la historia de forma creativa y satisfactoria, enfatizando el aprendizaje o la moraleja.)

**Reflexión:**
¿Qué te pareció tu historia? ¿Qué te hubiera gustado cambiar? ¿Qué mensaje quieres transmitir con ella? (Opcional: Invita al niño a reflexionar sobre su historia de forma más profunda y creativa.)
""",
    # Agrega más plantillas según las edades
}

plantilla = plantillas.get(franja_edad, "")

# Selección de género
generos = ["Amor", "Aventura", "Ciencia Ficción", "Terror", "Comedia", "Romántica", "Thriller"]
genero_elegido = st.selectbox("Elige un género para tu historia:", generos)

# Generación de personajes aleatorios
if st.button("Generar personajes aleatorios"):
    nombre_personaje1, descripcion_personaje1, personalidad_personaje1 = generar_personaje()
    nombre_personaje2, descripcion_personaje2, personalidad_personaje2 = generar_personaje()
    
    st.write("### Personaje 1")
    st.write(f"**Nombre:** {nombre_personaje1}")
    st.write(f"**Descripción:** {descripcion_personaje1}")
    st.write(f"**Personalidad:** {personalidad_personaje1}")
    
    st.write("### Personaje 2")
    st.write(f"**Nombre:** {nombre_personaje2}")
    st.write(f"**Descripción:** {descripcion_personaje2}")
    st.write(f"**Personalidad:** {personalidad_personaje2}")

# Creación de personajes personalizados
st.markdown("## Crear tu propio personaje")
nombre_personalizado = st.text_input("Nombre del personaje")
descripcion_personalizada = st.text_input("Descripción del personaje")
personalidad_personalizada = st.text_input("Personalidad del personaje")

if st.button("Agregar personaje personalizado"):
    st.write("### Personaje Personalizado")
    st.write(f"**Nombre:** {nombre_personalizado}")
    st.write(f"**Descripción:** {descripcion_personalizada}")
    st.write(f"**Personalidad:** {personalidad_personalizada}")

# Mostrar plantilla de historia según la franja de edad
st.markdown("## Plantilla de Historia")
st.markdown(plantilla)

# Editor de texto para escribir la historia
historia = st.text_area("Escribe tu historia aquí:")

# Herramientas de escritura (simplificado)
st.markdown("### Herramientas de Escritura")
st.write("Aquí puedes utilizar herramientas de escritura como negrita, cursiva, corrector ortográfico, etc.")

# Opciones de formato
if st.button("Guardar historia"):
    st.write("¡Tu historia ha sido guardada con éxito!")
    # Aquí puedes añadir código para guardar la historia en un formato seguro