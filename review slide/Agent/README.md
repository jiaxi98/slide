# Agent Review Slide

Below is a synopsis I made for the agent review slide. Your task is to generated a more
detailed slide with each specific pages required for each 

## Why agent? (5 pages)
- Tool use is a signal for early intelligence --- think of anthropic history
- Tool use can help LLM eliminate hallucination
- Tool using is a kind of interaction with the environment: Web search, etc
and thus RL can illustrate their power.

## How to build agent? (5 pages)
- Tool use
- MCP
- Workflow

## Agent literuature reivew (5 pages)
- [ReACT]
- [MemGPT]
- Pls add more famous agent literatures

## Case study: Claude Code (15 pages)
- Intro to CC
- reverse engineering of CC: https://github.com/Yuyz0112/claude-code-reverse, e.g.
system prompts, agentic workflow 
- TODO list
- Examples analysis, percentage indicating the score by myself
* Scientific computing code reading (99\%)
* Modify docker file and environment (99\%)
* Write unit test given clear interface and complete instructions
* Debug my hand-written spectral solver for 2D NS equation (40\%)
* Set hydra for multiple run experiments (20\%)
* Write Poisson solver over radial grid (NA)
- CC as a tool for human: Many people may ignore or even realize: Claude Code highly
decrease the barrier for most of the tasks: Learn a heavy repo,
handle the environment setup.