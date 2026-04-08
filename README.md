---
license: mit
title: AI Task Scheduler Env
sdk: gradio
emoji: 🚀
colorFrom: blue
colorTo: purple
pinned: true
short_description: LLM task scheduler with real-time scoring.
sdk_version: 6.11.0
---
# 🚀 AI Task Scheduler (Hackathon Project)

A hackathon-ready AI task simulation system where an LLM-like agent interacts with an environment step-by-step, generates actions, and is scored with a reward-based mechanism.

> ⚠️ This version uses **dummy responses** for fast hackathon demos — no API keys required.

---

## 📌 Overview
This project demonstrates how an AI agent can:

- Understand tasks  
- Take sequential actions  
- Receive rewards  
- Optimize performance over multiple steps  

The system simulates a simple environment where responses are generated and evaluated based on a scoring mechanism.

---

## 🧠 Features
- 🔄 Step-by-Step Execution  
- 📊 Reward-based Scoring System  
- 📈 Graph Visualization (Reward vs Steps)  
- 🎯 Multiple Task Modes:
  - Echo Task  
  - Creative Task  
  - Explain Task  
- 📦 Download Results (CSV)  
- 🌐 Deployed using **Gradio**  

---

## ⚙️ How It Works
1. User selects a task and number of steps.  
2. The dummy model generates a meaningful response at each step.  
3. The environment assigns a **perfect reward** (1.0) for each step.  
4. Rewards are accumulated into a final score.  
5. Results are displayed in logs and visualizations.

---

## 🧪 Example Output

```text
[START] task=Echo Task model=gpt-4o-mini

[STEP] step=1 action=Demo response for hackathon. reward=1.00 done=false
[STEP] step=2 action=Demo response for hackathon. reward=1.00 done=false
[STEP] step=3 action=Demo response for hackathon. reward=1.00 done=true

[END] success=true score=1.00

---

## 📊 Scoring Mechanism
- Reward is **fixed to 1.0** per step (dummy demo)  
- Normalized score range: 0 to 1  
- Success is determined by a threshold score  

---

## 🛠️ Tech Stack
- Python  
- Gradio  

---

## 🚀 Deployment
This project can be deployed on **Hugging Face Spaces** or run locally.  

---

## 🔐 Environment Variables
- **None required** for dummy mode — runs out-of-the-box.  

---

## 🎯 Use Cases
- Hackathon demo for AI task simulation  
- Demonstration of reward-based evaluation  
- Prototype for multi-step AI agents  

---

## 🏆 Hackathon Submission
Built for the **Scaler Meta PyTorch Hackathon**, showcasing:

- Step-by-step AI + environment interaction  
- Real-time scoring visualization  
- Clean, hackathon-ready dummy demo  

---

## 👨‍💻 Author
Kalamkuntla Girija  

---

## 🌟 Future Improvements
- Connect to real OpenAI/Hugging Face APIs  
- Add dynamic reward functions  
- Expand tasks and environments  
- Multi-agent simulations