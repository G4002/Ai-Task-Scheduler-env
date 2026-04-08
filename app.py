import gradio as gr
import pandas as pd

# ===== CONFIG =====
MODEL_NAME = "gpt-4o-mini"  # Dummy model for hackathon
MAX_STEPS = 8

# ===== TASK PROMPTS =====
TASKS = {
    "Echo Task": "Send a meaningful message to maximize reward.",
    "Creative Task": "Write a creative sentence.",
    "Explain Task": "Explain a concept clearly."
}

# ===== LLM CALL (Dummy for Hackathon) =====
def get_model_response(prompt):
    """Returns a dummy response for hackathon demo."""
    if "Echo Task" in prompt:
        return "Demo response for hackathon."
    elif "Creative Task" in prompt:
        return "Here is a creative sentence for hackathon."
    elif "Explain Task" in prompt:
        return "This concept can be explained clearly."
    else:
        return "Demo response for hackathon."

# ===== MAIN SIMULATION =====
def run_simulation(task_name, steps):
    output = f"[START] task={task_name} model={MODEL_NAME}\n\n"
    rewards = []
    steps_list = []
    history = ""

    for step in range(1, int(steps)+1):
        prompt = TASKS[task_name] + "\n" + history
        action = get_model_response(prompt)

        reward = 1.0  # perfect reward for demo
        done = step == int(steps)

        rewards.append(reward)
        steps_list.append(step)
        output += f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()}\n"
        history += action + "\n"

        # Yield step-by-step for live logs
        yield output, pd.DataFrame({"Step": steps_list, "Reward": rewards}), sum(rewards)/len(rewards)

    score = sum(rewards)/len(rewards)
    success = score > 0.3
    output += f"\n[END] success={str(success).lower()} score={score:.2f}"
    yield output, pd.DataFrame({"Step": steps_list, "Reward": rewards}), score

# ===== RESET (Hackathon requires this endpoint) =====
def reset():
    """
    Hackathon backend expects POST to /reset.
    Returns the initial state in the exact format required by Gradio.
    """
    # output_box, graph, score_box, task_dropdown, steps_input
    return "", None, 0.0, "Echo Task", 3

# ===== DOWNLOAD RESULTS =====
def download_results(task_name, steps):
    data = [{"Step": i, "Reward": 1} for i in range(1, int(steps)+1)]
    df = pd.DataFrame(data)
    file_path = "results.csv"
    df.to_csv(file_path, index=False)
    return file_path

# ===== GRADIO UI =====
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🚀 AI Task Scheduler (Hackathon Project)")
    gr.Markdown("### Powered by Simulation + Scoring (Dummy Mode)")

    with gr.Row():
        task_dropdown = gr.Dropdown(
            choices=list(TASKS.keys()),
            value="Echo Task",
            label="🧠 Select Task"
        )
        steps_input = gr.Number(label="🔢 Steps", value=3)

    with gr.Row():
        run_btn = gr.Button("▶️ Run")
        reset_btn = gr.Button("🔄 Reset")
        download_btn = gr.Button("📦 Download CSV")

    output_box = gr.Textbox(label="📊 Output Logs", lines=12)
    graph = gr.LinePlot(x="Step", y="Reward", title="📈 Reward vs Steps")
    score_box = gr.Number(label="🏆 Score")
    file_output = gr.File(label="⬇️ Download File")

    # Run button
    run_btn.click(
        run_simulation,
        inputs=[task_dropdown, steps_input],
        outputs=[output_box, graph, score_box]
    )

    # Reset button (backend expects this)
    reset_btn.click(
        reset,
        outputs=[output_box, graph, score_box, task_dropdown, steps_input]
    )

    # Download CSV
    download_btn.click(
        download_results,
        inputs=[task_dropdown, steps_input],
        outputs=file_output
    )

# Must use share=True for hackathon backend access
demo.launch(share=True)
