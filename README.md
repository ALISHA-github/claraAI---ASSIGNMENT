# Clara AI – Automation Pipeline Assignment

## Overview

This project implements a **zero-cost automation pipeline** that converts demo call transcripts into a preliminary Retell AI agent configuration and then updates that agent after onboarding calls.

The system processes transcripts, extracts structured business information, and generates agent configuration files with versioning.

---

# Architecture

The pipeline consists of two main workflows:

### Pipeline A – Demo Call → Agent v1

1. Demo call transcript is read from the dataset folder
2. Information is extracted using rule-based parsing
3. A structured **Account Memo JSON** is created
4. A **Retell Agent Draft Spec** is generated
5. Files are stored in the output directory as **version v1**

### Pipeline B – Onboarding Call → Agent v2

1. Onboarding transcript is processed
2. Existing account memo is updated
3. Agent configuration is regenerated
4. Version is upgraded from **v1 to v2**
5. Changes are documented in the changelog

---

# Tech Stack

This project uses only **free and open tools**:

- Python
- JSON for structured storage
- Rule-based data extraction
- Local filesystem for storage
- GitHub for version control

No paid APIs or services are used.

---

# Project Structure
