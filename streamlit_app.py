import streamlit as st
import requests
import time

API_URL = "http://127.0.0.1:7860"

st.set_page_config(page_title="RL Mini-Game", page_icon="🎮")

st.title("🎮 RL Mini-Game Environment")

if "steps" not in st.session_state:
    st.session_state.steps = 0
    st.session_state.reward = 0.0
    st.session_state.done = False

def reset_env():
    try:
        res = requests.post(f"{API_URL}/reset")
        if res.status_code == 200:
            obs = res.json()["observation"]
            st.session_state.obs = obs
            st.session_state.steps = obs["steps_taken"]
            st.session_state.reward = 0.0
            st.session_state.done = False
    except Exception as e:
        st.error("Failed to connect to API. Is FastAPI running on port 7860?")

def step_env(direction: str):
    if st.session_state.done:
        st.warning("Game is Over! Please reset.")
        return
        
    try:
        res = requests.post(f"{API_URL}/step", json={"direction": direction})
        if res.status_code == 200:
            data = res.json()
            st.session_state.obs = data["observation"]
            st.session_state.reward += data["reward"]
            st.session_state.steps = data["observation"]["steps_taken"]
            st.session_state.done = data["done"]
    except Exception as e:
        st.error(f"Error stepping environment: {e}")

if "obs" not in st.session_state:
    reset_env()

col_btn, col_stats = st.columns([1, 1])

with col_btn:
    st.button("🔄 Reset Game", on_click=reset_env)
    
    st.write("### Controls")
    c1, c2, c3 = st.columns(3)
    with c2:
        st.button("⬆️", on_click=step_env, args=("up",))
    c4, c5, c6 = st.columns(3)
    with c4:
        st.button("⬅️", on_click=step_env, args=("left",))
    with c5:
        st.button("⬇️", on_click=step_env, args=("down",))
    with c6:
        st.button("➡️", on_click=step_env, args=("right",))

with col_stats:
    st.metric("Steps Taken", st.session_state.steps)
    st.metric("Total Reward", f"{st.session_state.reward:.1f}")
    if st.session_state.done:
        st.success("Goal Reached!")

st.write("### Grid View")
if "obs" in st.session_state:
    obs = st.session_state.obs
    grid_size = obs["grid_size"]
    ax, ay = obs["agent_position"]
    gx, gy = obs["goal_position"]
    
    grid_html = '<div style="display: grid; grid-template-columns: repeat({cols}, 30px); gap: 2px;">'
    grid_html = grid_html.format(cols=grid_size)
    
    for y in range(grid_size):
        for x in range(grid_size):
            cell_color = "#333333"
            text = ""
            if (x, y) == (ax, ay):
                cell_color = "#3498db"
                text = "🤖"
            elif (x, y) == (gx, gy):
                cell_color = "#2ecc71"
                text = "🎯"
            
            grid_html += f'<div style="width: 30px; height: 30px; background-color: {cell_color}; display: flex; align-items: center; justify-content: center; font-size: 18px; border-radius: 4px;">{text}</div>'
    
    grid_html += '</div>'
    st.markdown(grid_html, unsafe_allow_html=True)
