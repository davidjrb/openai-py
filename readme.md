# Terminal Chat with OpenAI GPT-4

This Python script provides an interactive terminal interface to chat with OpenAI's GPT-4 model directly from your terminal.

## Setup

### Clone the Repository

```sh
git clone https://github.com/davidjrb/openai-py
```

### Install Dependencies

Ensure you have Python 3.7+ installed, then run:

```sh
pip install openai
```

### Configure API Key

#### Bash/Zsh

```sh
export OPENAI_API_KEY='your_api_key_here'
```

---

#### Fish Shell

For Fish shell users, add your API key to your `config.fish`:

1. Open or create your config file: `nano ~/.config/fish/config.fish`
2. Add the line: `set -x OPENAI_API_KEY 'your_api_key_here'`
3. Apply changes: `source ~/.config/fish/config.fish`
4. Verify: `echo $OPENAI_API_KEY`

---

## Usage

Run the script from the terminal:

```sh
python3 chat_with_gpt4.py
```

Type your messages after the "You:" prompt. Type "exit" to end the chat.

---

```bash
> python3 chat_with_gpt4.py                                                            
You: say something clever GPT
AI: "Artificial intelligence is like a sharp tool. It's brilliant at carving solutions, but only if there's a human hand guiding it."
You: touché
AI: Touché is a French term, often used in English conversation, to acknowledge a clever point made at someone's expense or a good comeback. It's often used during debates or arguments. The term originally comes from fencing, where it means you've been touched by your opponent's sword. So if someone makes a point you can't argue with, you'd respond with "touché" as a way to concede that they've 'struck' you with a good argument or witty response.
```

---

## Important Information

- **OpenAI Service**: This script utilizes OpenAI's GPT-4 model, a paid service. You'll need to [create an account with OpenAI](https://openai.com/signup) and subscribe to a plan.
- **API Token**: After account creation, generate an OpenAI API token from the [API settings](https://platform.openai.com/account/api-keys) page to authenticate your requests.
- **Subscription and Credits**: OpenAI requires a subscription ($20/month) and a pre-paid API credit balance. A minimum deposit of $10 is required to start, and unused credits expire monthly. For more details, visit the [pricing page](https://openai.com/pricing).

