import os
import sys

def generate_reverse_shell_prompt(os_name: str, start_index: int, batch_size: int = 50) -> str:
    end_index = start_index + batch_size - 1
    prompt = f"""You are a cybersecurity assistant. Generate part of a structured JSON dataset of reverse shell payloads. Do NOT summarize, skip, or omit entries. Only output valid JSON. No explanations. No comments.

🔹 Output only {batch_size} payload entries per request in this format:

{{
  "payloads": [
    {{
      "os": "{os_name}",
      "language": "PowerShell" | "Python" | "PHP" | "Perl" | "Ruby" | "Java" | "Bash" | "Netcat" | etc,
      "description": "Brief summary of the payload.",
      "template": "Code/command using {{ip}} and {{port}}",
      "usage": "How to use this payload and what listener it needs.",
      "tags": ["reverse_tcp", "interactive", "encoded", "fileless", "one-liner", ...]
    }},
    ...
  ]
}}

Generate ONLY payloads {start_index} to {end_index} for **{os_name}** in this request.

⚠️ Do NOT write “...more entries follow” or summarize the rest. Output {batch_size} complete and distinct payloads in full JSON format.

When finished, I will ask for the next {batch_size}.
"""
    # Debug print to verify correct OS and range
    print(f"[DEBUG] Generated prompt for OS: {os_name}, entries: {start_index} to {end_index}")
    return prompt

def generate_all_prompts(os_list=None, total_per_os=200, batch_size=50):
    if os_list is None:
        os_list = ["Windows", "Linux", "macOS", "Android"]

    all_prompts = []
    for os_name in os_list:
        for start in range(1, total_per_os + 1, batch_size):
            prompt = generate_reverse_shell_prompt(os_name, start, batch_size)
            all_prompts.append(prompt)
    return all_prompts


if __name__ == "__main__":
    prompts = generate_all_prompts()
    print(f"Total prompts generated: {len(prompts)}\n")

    # Print the first prompt for each OS (batch 1 only)
    os_names = ["Windows", "Linux", "macOS", "Android"]
    batches_per_os = 200 // 50  # 4 batches per OS
    for i, os_name in enumerate(os_names):
        index = i * batches_per_os  # index of batch 1 of current OS
        print(f"=== Prompt for {os_name} batch 1 ===")
        print(prompts[index])
        print("=" * 50)
        input("Press Enter to continue...\n")

    # Optionally, print more batches or all prompts with a loop if you want
