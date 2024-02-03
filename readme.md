# OpenAI Python Interaction Example

This repository contains a simple Python script and a YAML configuration file that demonstrate how to interact with the OpenAI API, specifically using the GPT-4 model. The script allows you to send messages to the OpenAI API and receive responses, with the API parameters (like the API key and model settings) being configurable through a YAML file.

## Setup

Before running the script, you need to set up your environment:

1. **Install Dependencies**: Ensure you have Python 3.6+ installed. Then, install the required Python packages:

    ```bash
    pip install pyyaml openai
    ```

2. **Configuration**: Create a `config.yaml` file in the project directory with your OpenAI API key and desired settings. An example configuration looks like this:

    ```yaml
    openai:
      api_key: "YOUR_API_KEY_HERE"
      model: "gpt-4"
      temperature: 0.7
      max_tokens: 150
    ```

    Replace `"YOUR_API_KEY_HERE"` with your actual OpenAI API key.

## Usage

To use the script, run it from the terminal and enter your message when prompted:

```bash
python openai.py
