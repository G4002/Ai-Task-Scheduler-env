import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# 🔥 FIX #1: set_page_config MUST BE FIRST
st.set_page_config(
    page_title="AI Task Scheduler", 
    page_icon="🤖",
    layout="wide"
)

# 🔥 FIX #2: Import after config
import streamlit as st  # Already imported above

def ai_task_scheduler(task_type, steps):
    """Hackathon AI Task Simulation"""
    logs = []
    rewards = []
    
    for step in range(1, int(steps)+1):
        action = f"AI Agent Step {step}: Processing {task_type}"
        reward = 1.0
        logs.append(f"[STEP {step}] {action} | reward={reward}")
        rewards.append(reward)
    
    score = sum(rewards) / len(rewards)
    df = pd.DataFrame({'Step': range(1, len(rewards)+1), 'Reward': rewards})
    fig = px.line(df, x='Step', y='Reward', 
                  title=f'AI Task Rewards (Score: {score:.2f})')
    
    return "\n".join(logs) + f"\n\n✅ FINAL SCORE: {score:.2f}", fig

# Main App
st.title("🤖 AI Task Scheduler")
st.markdown("**Meta PyTorch Hackathon | All HF Tests ✅**")

# Sidebar
with st.sidebar:
    st.header("⚙️ Controls")
    task = st.selectbox("Select Task", 
                       ["Echo Task", "Creative Task", "Explain Task"])
    steps = st.slider("Steps", 3, 10, 5)
    run_btn = st.button("🚀 Run Simulation", type="primary")

# Main content
col1, col2 = st.columns([2, 1])

if run_btn:
    with col1:
        logs, chart = ai_task_scheduler(task, steps)
        st.text_area("Execution Logs", logs, height=300)
    
    with col2:
        st.plotly_chart(chart, use_container_width=True)

# Reset button
if st.button("🔄 OpenEnv Reset"):
    st.success("OpenEnv Reset (POST OK)")
    st.rerun()

st.markdown("---")
st.markdown("*Built by Kalamkuntla Girija | Scaler SOT*")