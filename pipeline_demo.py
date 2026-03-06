import json
import os
from extractor import extract_account_data

INPUT_FOLDER = "../dataset/demo_calls"
OUTPUT_FOLDER = "../outputs/accounts/account_001/v1"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for file in os.listdir(INPUT_FOLDER):

    with open(f"{INPUT_FOLDER}/{file}", "r") as f:
        text = f.read()

    data = extract_account_data(text)

    memo = {
        "account_id": "account_001",
        "company_name": data["company_name"],
        "business_hours": data["business_hours"],
        "office_address": data["office_address"],
        "services_supported": [],
        "emergency_definition": data["emergency_definition"],
        "emergency_routing_rules": [],
        "non_emergency_routing_rules": [],
        "call_transfer_rules": [],
        "integration_constraints": [],
        "after_hours_flow_summary": "",
        "office_hours_flow_summary": "",
        "questions_or_unknowns": [],
        "notes": data["notes"]
    }

    with open(f"{OUTPUT_FOLDER}/account_memo.json", "w") as out:
        json.dump(memo, out, indent=4)

    agent_spec = {
        "agent_name": "Customer Support Agent",
        "voice_style": "professional",
        "system_prompt": "You are an AI receptionist. Collect caller name and number and route calls.",
        "version": "v1"
    }

    with open(f"{OUTPUT_FOLDER}/agent_spec.json", "w") as out:
        json.dump(agent_spec, out, indent=4)

print("Pipeline A completed (Demo → Agent v1)")