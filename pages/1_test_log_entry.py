import streamlit as st
from datetime import datetime

st.title("🧪 試験運用ログ 登録")

title = st.text_input("🔖 ログタイトル（例：AI_B 精度検証 07/08）")
comment = st.text_area("💬 気づきや状況のメモ")
priority = st.selectbox("⚙️ 優先度", ["Low", "Medium", "High"])
date = datetime.now().strftime("%Y-%m-%d %H:%M")

if st.button("✅ 登録"):
    st.success("📝 試験運用ログが登録されました")
    st.info(f"📅 {date}\n\n🔖 {title}\n\n💬 {comment}\n\n🚦 優先度: {priority}")
