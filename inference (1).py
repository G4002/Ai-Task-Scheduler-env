import gradio as gr
import pandas as pd

# ===== CONFIG =====
MODEL_NAME = "gpt-4o-mini"
MAX_STEPS = 8

TASKS = {
    "Echo Task": "Send a meaningful message to maximize reward.",
    "Creative Task": "Write a creative sentence.",
    "Explain Task": "Explain a concept clearly."
}

# ===== Dummy LLM Response =====
def get_model_response(prompt):
    if "Echo Task" in prompt:
        return "Demo response for hackathon."
    elif "Creative Task" in prompt:
        return "Here is a creative sentence for hackathon."
    elif "Explain Task" in prompt:
        return "This concept can be explained clearly."
    return "Demo response for hackathon."

# ===== Main Simulation =====
def run_simulation(task_name, steps):
    output = f"[START] task={task_name} model={MODEL_NAME}\n\n"
    rewards, steps_list, history = [], [], ""
    for step in range(1, int(steps)+1):
        prompt = TASKS[task_name] + "\n" + history
        action = get_model_response(prompt)
        reward = 1.0
        done = step == int(steps)
        rewards.append(reward)
        steps_list.append(step)
        output += f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()}\n"
        history += action + "\n"
        yield output, pd.DataFrame({"Step": steps_list, "Reward": rewards}), sum(rewards)/len(rewards)
    score = sum(rewards)/len(rewards)
    success = score > 0.3
    output += f"\n[END] success={str(success).lower()} score={score:.2f}"
    yield output, pd.DataFrame({"Step": steps_list, "Reward": rewards}), score

# ===== Reset =====
def reset():
    return "", None, 0.0, "Echo Task", 3

# ===== Download CSV =====
def download_results(task_name, steps):
    df = pd.DataFrame([{"Step": i, "Reward": 1} for i in range(1, int(steps)+1)])
    file_path = "results.csv"
    df.to_csv(file_path, index=False)
    return file_path

# ===== UI =====
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🚀 AI Task Scheduler (Hackathon)")
    gr.Markdown("### Dummy Mode – Ready for Hackathon Submission")

    with gr.Row():
        task_dropdown = gr.Dropdown(list(TASKS.keys()), value="Echo Task", label="Select Task")
        steps_input = gr.Number(label="Steps", value=3)

    with gr.Row():
        run_btn = gr.Button("Run")
        reset_btn = gr.Button("Reset")
        download_btn = gr.Button("Download CSV")

    output_box = gr.Textbox(label="Output Logs", lines=12)
    graph = gr.LinePlot(x="Step", y="Reward", title="Reward vs Steps")
    score_box = gr.Number(label="Score")
    file_output = gr.File(label="Download File")

    run_btn.click(run_simulation, inputs=[task_dropdown, steps_input], outputs=[output_box, graph, score_box])
    reset_btn.click(reset, outputs=[output_box, graph, score_box, task_dropdown, steps_input])
    download_btn.click(download_results, inputs=[task_dropdown, steps_input], outputs=file_output)

demo.launch()
