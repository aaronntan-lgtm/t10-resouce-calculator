import streamlit as st
import pandas as pd

# --- Page Setup ---
st.set_page_config(page_title="🪖 T10 Grind", layout="centered")

# --- Apply Green Border ONLY to Language Dropdown ---
st.markdown("""
    <style>
    div[data-testid="stSelectbox"][id^="language_selector"] > div {
        border: 1px solid #28a745 !important;
        box-shadow: 0 0 0 1px #28a745 !important;
    }
    div[data-testid="stSelectbox"][id^="language_selector"] > div:focus, 
    div[data-testid="stSelectbox"][id^="language_selector"] > div:focus-within {
        border: 1px solid #28a745 !important;
        box-shadow: 0 0 0 1px #28a745 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Language Toggle (Top-Aligned, Green Styled) ---
languages = {
    "English": "en",
    "Tiếng Việt": "vi",
    "繁體中文": "zh"
}
lang_choice = st.selectbox("🌐 Select Language / Chọn ngôn ngữ / 選擇語言",
                           list(languages.keys()), key="language_selector")
lang = languages[lang_choice]


# --- Localized Text ---
text = {
    "title": {
        "en": "🪖 T10 Grind",
        "vi": "🪖 Leo Đến T10",
        "zh": "🪖 T10 研發之路"
    },
    "subtitle": {
        "en": "Select your current research levels below to calculate remaining resources needed to unlock Tier 10 units.",
        "vi": "Chọn cấp nghiên cứu hiện tại để tính toán tài nguyên còn thiếu để mở khóa đơn vị T10.",
        "zh": "選擇你目前的研究等級，計算解鎖 T10 單位所需的剩餘資源。"
    },
    "total": {
        "en": "🧾 Total Resources Needed",
        "vi": "🧾 Tổng Tài Nguyên Cần Thiết",
        "zh": "🧾 所需總資源"
    },
    "breakdown": {
        "en": "🔍 Research Cost Breakdown",
        "vi": "🔍 Chi Tiết Chi Phí Nghiên Cứu",
        "zh": "🔍 研究資源明細"
    }
}

# --- Header ---
st.title(text["title"][lang])
st.markdown(text["subtitle"][lang])

# --- Research Cost Data ---
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
    "HP Boost III": [
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
    "Attack Boost III": [
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
    "Defense Boost III": [
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

# --- Dropdown Inputs ---
levels = {}
for tech, data in cost_data.items():
    max_level = len(data)
    if tech == "Unit X":
        selected = st.selectbox("Unit X Status", ["Not Researched", "Researched"], index=0)
        levels[tech] = 0 if selected == "Not Researched" else 1
    else:
        level_options = list(range(0, max_level + 1))
        levels[tech] = st.selectbox(f"{tech} Current Level", level_options, index=0,
                                    format_func=lambda x: f"{x} (Max)" if x == max_level else str(x),
                                    key=tech)

# --- Calculation ---
remaining = {"Iron": 0, "Bread": 0, "Gold": 0}
breakdown = []

for tech, data in cost_data.items():
    current = levels[tech]
    level_counter = 1
    for i in range(current, len(data)):
        iron, bread, gold = data[i]
        remaining["Iron"] += iron
        remaining["Bread"] += bread
        remaining["Gold"] += gold
        label = "Unit X" if tech == "Unit X" else f"{tech} {level_counter}"
        breakdown.append((label, iron, bread, gold))
        level_counter += 1

# --- Format helper ---
def fmt(n):
    if n >= 1_000_000_000:
        return f"{n/1_000_000_000:.1f}G"
    return f"{n/1_000_000:.1f}M"

# --- Display Totals ---
st.subheader(text["total"][lang])
col1, col2, col3 = st.columns(3)
col1.metric("Iron", fmt(remaining["Iron"]))
col2.metric("Bread", fmt(remaining["Bread"]))
col3.metric("Gold", fmt(remaining["Gold"]))

# --- Display Breakdown Table ---
if breakdown:
    st.markdown(f"### {text['breakdown'][lang]}")
    df = pd.DataFrame(breakdown, columns=["Research", "Iron", "Bread", "Gold"])
    df.index = df.index + 1  # Start index at 1
    df[["Iron", "Bread", "Gold"]] = df[["Iron", "Bread", "Gold"]].applymap(fmt)
    st.dataframe(df.set_index(df.index.rename("")), use_container_width=True)
