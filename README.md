# brand-compliance-ai
Automated brand-compliance checker for ad creatives—combining computer-vision analysis and LLM reasoning to validate assets against the Neurons brand guidelines.


## Problem & Approach

### Problem  
Marketing teams and creative agencies often struggle to ensure that ad creatives strictly adhere to brand guidelines—mistakes in logo placement, color usage or typography can dilute brand equity and cost time in manual reviews. As campaigns scale across channels, manual QA becomes a bottleneck, leading to inconsistencies and missed deadlines.

### Approach  
We build an end-to-end, automated brand-compliance checker that combines classical computer-vision techniques with LLM-powered reasoning to validate any static ad asset against the Neurons brand kit.  

1. **Brand-Kit Ingestion**  
   - Parse the official PDF to extract logo safe-zone rules, primary/secondary font names, and color palettes (hex codes).  
   - Store assets (logo PNG, fonts, colors) in a structured JSON schema.

2. **Image Asset Ingestion & CV Checks**  
   - Normalize uploaded creatives (resize, format).  
   - Detect and template-match the logo to verify safe-zone margins.  
   - Cluster pixel colors to compare against the approved palette.  
   - OCR-scan text snippets to flag off-brand fonts.

3. **LLM Compliance Assessment**  
   - Feed the pre-computed CV metrics plus the brand-kit JSON and image URL into a GPT-4V (or comparable) prompt.  
   - Generate a pass/fail score (0–4) with concise reasoning for each compliance dimension.

4. **Results & Reporting**  
   - Expose a FastAPI endpoint for synchronous or asynchronous `/assess` jobs.  
   - Provide a Streamlit frontend to upload files, visualize CV overlays, and download a consolidated report.  

By combining deterministic checks with AI-driven judgment, this solution delivers fast, reproducible, and explainable compliance scores—freeing creative teams to focus on what they do best.  
