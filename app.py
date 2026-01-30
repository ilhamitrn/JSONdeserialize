import streamlit as st
from json_to_abap import AbapStructureGenerator 

st.set_page_config(page_title="JSON to ABAP Pro", layout="wide", page_icon="🚀")

st.title("🚀 JSON to ABAP Deep Structure Generator (Pro)")
st.markdown("Converts JSON data into ABAP Deep Structure. Features smart type inference, auto-mapping, and naming corrections.")
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Input")
    
    # --- SETTINGS ---
    st.markdown("##### ⚙️ Settings")
    use_snake_case = st.checkbox(
        "Convert CamelCase -> SNAKE_CASE", 
        value=True,
        help="Example: Defines 'orderId' field as 'ORDER_ID' to follow ABAP naming conventions."
    )
    # ----------------
    
    json_input_abap = st.text_area("JSON:", height=500, key="input_abap", placeholder='{ "orderId": 10020, "isVerified": true }')
    btn_generate = st.button("Generate ABAP Code ⚡", type="primary", use_container_width=True)

with col2:
    st.subheader("📤 ABAP Code")
    if btn_generate and json_input_abap:
        gen = AbapStructureGenerator()
        
        # Generate code with settings
        abap_code = gen.generate_abap_types(json_input_abap, convert_names=use_snake_case)
        
        # Check for "Error" (since backend returns "Error: ...")
        if abap_code.startswith("Error"):
            st.error(abap_code)
        else:
            st.code(abap_code, language="abap")
            st.success("Code ready! Type conversions (INT4, BOOL) and Mapping Logic applied.")