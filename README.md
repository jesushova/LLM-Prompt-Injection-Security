# LLM Prompt Injection Security Lab

![Python](https://img.shields.io/badge/Python-3.11-blue) ![License](https://img.shields.io/badge/License-MIT-green) ![Platform](https://img.shields.io/badge/Platform-SecureFlag-blueviolet) ![Status](https://img.shields.io/badge/Status-Completed-success) ![OWASP](https://img.shields.io/badge/OWASP-LLM%20Top%2010-orange)

> Research and defense implementation for prompt injection vulnerabilities in LLM applications.  
> Hands-on lab work completed using SecureFlag; defenses implemented with the `llm_guard` toolkit.

---

## Overview
Completed SecureFlag professional security lab demonstrating prompt injection vulnerabilities and defenses for LLM applications. This repo documents attack reproduction, mitigation design, and verification for the Prompt Injection — Leaks Sensitive Content lab (and provides a pattern you can reuse across other OWASP LLM Top 10 labs).

## Project Highlights
- **Platform:** SecureFlag professional security training  
- **Completion Date:** October 17, 2025  
- Reproduced system-prompt exfiltration via a reflection/structured-output attack  
- Implemented a model-based defense using **LLM Guard** and added output sanitization  
- Delivered a test suite, write-up, and reusable prompt-security module

## What I Learned
- How to identify and reproduce prompt injection attacks that lead to information exfiltration.  
- Attack vectors: direct override, role manipulation, context switching, and reflection.  
- How to integrate ML-based defenses (`llm_guard`) as a pre-LLM gate and programmatic output sanitizers.  
- Practice in secure-by-design LLM handling and defense-in-depth.

## Repository Contents
- `/vulnerability-research` - Attack patterns and exploitation techniques
- `/defense-implementation` - Security controls using LLM Guard
- `/documentation` - Detailed write-ups and analysis
- `/test-cases` - Sample prompts for testing defenses

## Key Achievements
✅ Successfully extracted system prompts from vulnerable LLM  
✅ Implemented prompt injection detection with LLM Guard  
✅ Created comprehensive documentation of attack patterns  
✅ Developed reusable security module

## Technologies Used
- Python 3.x
- LLM Guard Security Toolkit
- OWASP Security Methodology

## Getting Started
```bash
pip install -r requirements.txt
python test-cases/injection_tests.py
```
