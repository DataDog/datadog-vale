import os
import yaml
from datetime import datetime

def generate_rule_markdown(rule_data):
    message = rule_data['message']
    markdown = f"### {message}\n\n"
    markdown += f"**Level:** *{rule_data['level']}*\n\n"
    if 'link' in rule_data:
        markdown += f"[Link]({rule_data['link']})\n\n"
    if 'tokens' in rule_data:
        markdown += "**Tokens:**\n"
        for token in rule_data['tokens']:
            markdown += f"- `{token}`\n"
    if 'exceptions' in rule_data:
        markdown += "\n**Exceptions:**\n"
        for exception in rule_data['exceptions']:
            markdown += f"- `{exception}`\n"
    if 'swap' in rule_data:
        markdown += "\n**Swap:**\n"
        if isinstance(rule_data['swap'], dict):
            for key, value in rule_data['swap'].items():
                markdown += f"- `{key}` -> `{value}`\n"
        elif isinstance(rule_data['swap'], list):
            for item in rule_data['swap']:
                markdown += f"- `{item}`\n"
    if 'ignorecase' in rule_data:
        markdown += f"\n**Ignore Case:** {rule_data['ignorecase']}\n"
    markdown += "\n"
    return markdown

def process_subfolder(subfolder_path):
    markdown_content = ""
    for root, dirs, files in os.walk(subfolder_path):
        for file in files:
            if file.endswith('.yml'):
                with open(os.path.join(root, file), 'r') as f:
                    rule_data = yaml.safe_load(f)
                    markdown_content += generate_rule_markdown(rule_data)
    return markdown_content

def generate_table_of_contents(style_folders):
    toc = "## Table of Contents\n"
    for folder in style_folders:
        toc += f"- [{folder}](#{folder.lower()})\n"
    return toc

def main():
    styles_folder = 'styles'
    style_folders = [folder for folder in os.listdir(styles_folder) if os.path.isdir(os.path.join(styles_folder, folder))]

    markdown_content = "# Vale Linter Rules\n\n"
    markdown_content += "This page provides a comprehensive list of the Vale linter rules used in Datadog documentation.\n\n"
    markdown_content += f"Last Updated: {datetime.now().strftime('%Y-%m-%d')}\n\n"
    markdown_content += generate_table_of_contents(style_folders)

    for style_folder in style_folders:
        subfolder_path = os.path.join(styles_folder, style_folder)
        markdown_content += f"\n## {style_folder}\n\n"
        markdown_content += process_subfolder(subfolder_path)

    with open('rules_overview.md', 'w') as file:
        file.write(markdown_content)

if __name__ == '__main__':
    main()