# brand-compliance-ai

A FastAPI service to validate marketing assets against your Neurons brand-kit PDF, returning a compliance score (0–4) with detailed breakdown.

## Features
- Upload a Neurons brand-kit PDF and extract:
  - Logo safe-zone (px)
  - Primary color palette (hex codes)
  - Typography (primary & secondary fonts)
- Upload image assets to assess:
  - Usage of approved fonts
  - Logo placement safe-zone
  - Logo color accuracy
  - Overall palette consistency

## Tech Stack
- Python 3.10+
- FastAPI
- PyMuPDF for PDF parsing
- Pillow for image handling
- (Optional) OpenAI or your chosen LLM for multimodal checks

## Setup

1. **Clone the repo**  
   ```bash
   git clone <your-url> brand-compliance-ai
   cd brand-compliance-ai
