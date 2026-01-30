import streamlit as st
from json_to_abap import AbapStructureGenerator 

st.set_page_config(page_title="JSON to ABAP Pro", layout="wide", page_icon="🚀")

st.title("🚀 JSON to ABAP Deep Structure Generator (Pro)")
st.markdown("JSON verisini ABAP Structure'ına çevirir. Akıllı tip tahmini ve isimlendirme düzeltmesi içerir.")
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Girdi")
    
    # --- YENİ EKLENEN ÖZELLİK ---
    st.markdown("##### ⚙️ Ayarlar")
    use_snake_case = st.checkbox(
        "CamelCase -> SNAKE_CASE Dönüşümü Yap", 
        value=True,
        help="Örn: 'orderId' alanını 'ORDER_ID' olarak tanımlar ve pretty_name parametresini ayarlar."
    )
    # ----------------------------
    
    json_input_abap = st.text_area("JSON:", height=500, key="input_abap", placeholder='{ "orderId": 10020, "isVerified": true }')
    btn_generate = st.button("ABAP Kodunu Oluştur ⚡", type="primary", use_container_width=True)

with col2:
    st.subheader("📤 ABAP Kodu")
    if btn_generate and json_input_abap:
        gen = AbapStructureGenerator()
        # Checkbox değerini gönderiyoruz
        abap_code = gen.generate_abap_types(json_input_abap, convert_names=use_snake_case)
        
        if "Hata" in abap_code:
            st.error(abap_code)
        else:
            st.code(abap_code, language="abap")
            st.success("Kod hazır! Tip dönüşümleri (INT4, BOOL) ve isimlendirmeler uygulandı.")