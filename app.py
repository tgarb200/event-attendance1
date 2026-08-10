import streamlit as st

st.set_page_config(
    page_title="نظام حضور الفعاليات", page_icon="🎫", layout="centered"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #e2e8f0;
    }
    h3, h1 {
        color: #1e293b;
        text-align: center;
        font-family: Tahoma, sans-serif;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    "<div style='background-color: #ff8a65; padding: 12px; border-radius: 12px;"
    " text-align: center; color: white; font-weight: bold; font-size: 16px;'>إشراف:"
    " المهندس / خالد الشميري</div>",
    unsafe_allow_html=True,
)

st.markdown("### ✨ نظام حضور الفعاليات ✨")

if "count" not in st.session_state:
  st.session_state.count = 0
if "attendees" not in st.session_state:
  st.session_state.attendees = set()

st.markdown(f"<h1>عدد الحضور: {st.session_state.count}</h1>", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align: center;'>📸 وجه الكاميرا نحو باركود الكرت</p>",
    unsafe_allow_html=True,
)
picture = st.camera_input("التقاط الكود", label_visibility="collapsed")

if picture is not None:
  st.session_state.count += 1
  st.success(
      f"تم تسجيل الحضور بنجاح! الإجمالي الحالي: {st.session_state.count}"
  )
  st.rerun()
  
