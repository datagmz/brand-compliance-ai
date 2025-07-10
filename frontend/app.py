import streamlit as st
import requests
import json

API_BASE = "http://localhost:8000/v1"

st.set_page_config(page_title="Brand Compliance AI", layout="wide")

st.title("🚦 Brand Compliance AI")

# Two‐column layout
col1, col2 = st.columns(2)

with col1:
    st.header("1️⃣ Upload Brand Kit")
    brand_file = st.file_uploader("Choose Neurons_brand_kit.pdf", type=["pdf"])
    if st.button("Parse Brand Kit") and brand_file:
        with st.spinner("Extracting guidelines…"):
            resp = requests.post(
                f"{API_BASE}/upload-brand-kit",
                files={"pdf_file": ("brandkit.pdf", brand_file, "application/pdf")},
            )
        if resp.ok:
            brand_info = resp.json()["brand_info"]
            st.success("✅ Parsed brand info!")
            st.json(brand_info)
            # store in session for next step
            st.session_state["brand_info"] = brand_info
        else:
            st.error(f"Error: {resp.status_code} – {resp.text}")

with col2:
    st.header("2️⃣ Assess Compliance")
    img_file = st.file_uploader("Choose an image (PNG/JPG)", type=["png", "jpg", "jpeg"])
    if st.button("Check Compliance") and img_file:
        if "brand_info" not in st.session_state:
            st.warning("Please upload & parse a brand kit first.")
        else:
            with st.spinner("Analyzing image…"):
                files = {"image_file": (img_file.name, img_file, img_file.type)}
                # Optionally send brand_info as JSON form field:
                data = {"brand_info": json.dumps(st.session_state["brand_info"])}
                resp = requests.post(f"{API_BASE}/assess-compliance", files=files, data=data)
            if resp.ok:
                result = resp.json()
                st.success(f"Score: {result['score']} / 4")
                st.json(result["details"])
            else:
                st.error(f"Error: {resp.status_code} – {resp.text}")

# Footer link
st.markdown("---")
st.markdown("[View API docs](http://localhost:8000/docs)  |  Powered by Neurons AI")
