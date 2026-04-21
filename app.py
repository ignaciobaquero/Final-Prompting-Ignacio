import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

st.title("ChiterAI 🧢")
st.subheader("Generador de descripciones para productos streetwear")

st.write("Ingresá un producto y generá contenido automáticamente")

producto = st.text_input("Ej: Gorra New Era Yankees negra 9FORTY")

if st.button("Generar contenido"):
    prompt = f"""
    Actúa como un experto en marketing de e-commerce especializado en streetwear.

    Genera:
    1. Una descripción atractiva del producto
    2. Un copy corto para Instagram
    3. 5 hashtags relevantes

    Producto: {producto}

    Usa un tono moderno, juvenil y persuasivo.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    st.write(response.output_text)