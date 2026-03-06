import re

def extract_account_data(text):

    data = {
        "company_name": None,
        "business_hours": None,
        "office_address": None,
        "services_supported": [],
        "emergency_definition": [],
        "notes": ""
    }

    # Company Name
    company_match = re.search(r"(company|business) name is ([A-Za-z ]+)", text, re.I)
    if company_match:
        data["company_name"] = company_match.group(2)

    # Business Hours
    hours_match = re.search(r"(\d{1,2}\s*(am|pm)\s*to\s*\d{1,2}\s*(am|pm))", text, re.I)
    if hours_match:
        data["business_hours"] = hours_match.group(1)

    # Address
    address_match = re.search(r"located at ([A-Za-z0-9 ,]+)", text, re.I)
    if address_match:
        data["office_address"] = address_match.group(1)

    # Emergency
    if "emergency" in text.lower():
        data["emergency_definition"].append("customer reported emergency")

    data["notes"] = "Auto extracted from transcript"

    return data