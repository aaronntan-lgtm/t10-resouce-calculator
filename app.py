
import streamlit as st

# Page layout
st.set_page_config(page_title="🪖 T10 Grind", layout="centered")

# Header
st.title("🪖 T10 Grind")
st.markdown("Select your current research levels below to calculate remaining resources needed to unlock Tier 10 units.")

# Research cost data (Iron, Bread, Gold)
cost_data = {
    "Advanced Protection": [
        (31_000_000, 31_000_000, 91_000_000),
        (53_000_000, 53_000_000, 158_000_000),
        (53_000_000, 53_000_000, 158_000_000),
        (74_000_000, 74_000_000, 221_000_000),
        (74_000_000, 74_000_000, 221_000_000),
        (96_000_000, 96_000_000, 287_000_000),
        (96_000_000, 96_000_000, 287_000_000),
        (134_000_000, 134_000_000, 403_000_000),
        (134_000_000, 134_000_000, 403_000_000),
        (175_000_000, 175_000_000, 522_000_000)
    ],
    "HP Boost": [
        (31_000_000, 31_000_000, 91_000_000),
        (53_000_000, 53_000_000, 158_000_000),
        (53_000_000, 53_000_000, 158_000_000),
        (74_000_000, 74_000_000, 221_000_000),
        (74_000_000, 74_000_000, 221_000_000),
        (96_000_000, 96_000_000, 287_000_000),
        (96_000_000, 96_000_000, 287_000_000),
        (134_000_000, 134_000_000, 403_000_000),
        (134_000_000, 134_000_000, 403_000_000),
        (175_000_000, 175_000_000, 522_000_000)
    ],
    "Attack Boost": [
        (31_000_000, 31_000_000, 91_000_000),
        (53_000_000, 53_000_000, 158_000_000),
        (53_000_000, 53_000_000, 158_000_000),
        (74_000_000, 74_000_000, 221_000_000),
        (74_000_000, 74_000_000, 221_000_000),
        (96_000_000, 96_000_000, 287_000_000),
        (96_000_000, 96_000_000, 287_000_000),
        (134_000_000, 134_000_000, 403_000_000),
        (134_000_000, 134_000_000, 403_000_000),
        (175_000_000, 175_000_000, 522_000_000)
    ],
    "Defense Boost": [
        (31_000_000, 31_000_000, 91_000_000),
        (53_000_000, 53_000_000, 158_000_000),
        (53_000_000, 53_000_000, 158_000_000),
        (74_000_000, 74_000_000, 221_000_000),
        (74_000_000, 74_000_000, 221_000_000),
        (96_000_000, 96_000_000, 287_000_000),
        (96_000_000, 96_000_000, 287_000_000),
        (134_000_000, 134_000_000, 403_000_000),
        (134_000_000, 134_000_000, 403_000_000),
        (175_000_000, 175_000_000, 522_000_000)
    ],
    "Unit X": [
        (187_000_000, 187_000_000, 560_000_000)
    ]
}

# Dropdowns for selecting current level
levels = {}
for tech, data in cost_data.items():
    max_level = len(data)
    label = f"{tech} Current Level"
    if tech == "Unit X":
        options = ["Not Researched", "Researched"]
        selected = st.selectbox("Unit X Status", options, index=0)
        levels[tech] = 0 if selected == "Not Researched" else 1
    else:
        level_options = list(range(0, max_level + 1))
        levels[tech] = st.selectbox(label, level_options, index=0,
                                    format_func=lambda x: f"{x} (Max)" if x == max_level else str(x),
                                    key=tech)

# Calculate remaining costs
remaining = {"Iron": 0, "Bread": 0, "Gold": 0}
breakdown = []

for tech, data in cost_data.items():
    current = levels[tech]
    for i in range(current, len(data)):
        iron, bread, gold = data[i]
        remaining["Iron"] += iron
        remaining["Bread"] += bread
        remaining["Gold"] += gold
        breakdown.append((f"{tech} {i+1}", iron, bread, gold))

# Format helper
def fmt(n):
    if n >= 1_000_000_000:
        return f"{n/1_000_000_000:.1f}G"
    return f"{n/1_000_000:.1f}M"

# Display total
st.subheader("🧾 Total Resources Needed")
st.markdown(f"**Iron:** {fmt(remaining['Iron'])} | **Bread:** {fmt(remaining['Bread'])} | **Gold:** {fmt(remaining['Gold'])}")

# Display research breakdown
if breakdown:
    st.markdown("### 🔍 Research Cost Breakdown")
    for name, iron, bread, gold in breakdown:
        st.markdown(f"- **{name}** → Iron: {fmt(iron)}, Bread: {fmt(bread)}, Gold: {fmt(gold)}")

