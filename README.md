# Neurons Brand Compliance

## Problem & Approach

### Problem  
Marketing teams and creative agencies often struggle to ensure that ad creatives strictly adhere to brand guidelines—mistakes in logo placement, color usage or typography can dilute brand equity and cost time in manual reviews. As campaigns scale across channels, manual QA becomes a bottleneck, leading to inconsistencies and missed deadlines.

### Approach  
We build an end-to-end, automated brand-compliance checker that combines classical computer-vision techniques with LLM-powered reasoning to validate any static ad asset against the Neurons brand kit.

1. **Brand-Kit Ingestion**: parse the PDF to extract safe-zone rules, fonts, colors, logo.  
2. **Image Asset Ingestion & CV Checks**: normalize, template-match logos, cluster colors, OCR fonts.  
3. **LLM Compliance Assessment**: feed CV metrics + brand JSON + image URL into GPT-4V for a 0–4 score & explanations.  
4. **Results & Reporting**: FastAPI /assess endpoint + Streamlit frontend for uploads, overlays & downloadable reports.  
