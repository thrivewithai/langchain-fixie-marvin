# Comparing LangChain, Fixie, and Marvin

## Task:
1. Load the "State of the Union" file locally (or remotely) and store them into a vector db (Chroma) 
2. Ask questions for the document 

## Analysis

### [LangChain](https://github.com/hwchase17/langchain) 

Pros: 
- Most powerful option among the three options 
- You can create your own tool. 
- Supports many third-party library integrations, different language models, [tracing](https://python.langchain.com/en/latest/tracing.html), and much more. 

Cons:
- Not much complains, but their example notebooks are sometimes broken. 

### [Fixie](https://github.com/fixie-ai/fixie-sdk)

Pros: 
- You can quickly generate and deploy your custom agent 
- You can add your own tool (e.g., `@agent.register_func`) 

Cons:
- It seems like you cannot choose how the text should be splitted (e.g., text-splitter in LangChain) 
- More examples will be great (i.e., Chat with PDF) 
- Ability to easily add third-party libraries 

Misc:
- [Here](https://app.fixie.ai/agents/0xhiroki/state-of-the-union) is a link to my agent. 
- There are no tools for LLM output evaluation at the time of writing this (Apr 23, 2023). However you could add your own validation/evaluation function by integrating a third-party library like [Guardrails](https://github.com/ShreyaR/guardrails) or [Evals](https://github.com/openai/evals). 

### [Marvin](https://github.com/PrefectHQ/marvin) 

Pros:
- AI functions are super cool. (I didn't touch on it in this repo) 
- You can use the [LangChain document loader](https://github.com/PrefectHQ/marvin/blob/main/src/marvin/loaders/langchain_documents.py). 
- Interactive option that runs on a terminal is useful. 
- You can add your custom "plugin"s. 

Cons:
- More examples will be great (e.g., Chat with PDF) 
- Ability to easily add third-party libraries 
