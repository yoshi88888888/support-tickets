import streamlit as st
from datetime import datetime
import pandas as pd
import os

st.title("🧪 試験運用ログ 登録")

# 入力フォーム
title = st.text_input("🔖 ログタイトル（例：AI_B 精度検証 07/08）")
comment = st.text_area("💬 気づきや状況のメモ")
priority = st.selectbox("⚙️ 優先度", ["Low", "Medium", "High"])
date = datetime.now().strftime("%Y-%m-%d %H:%M")

# 保存先のファイル
log_file = "logs.csv"

# 登録処理
if st.button("✅ 登録"):
    new_log = {"日時": date, "タイトル": title, "コメント": comment, "優先度": priority}
    df = pd.DataFrame([new_log])

    if os.path.exists(log_file):
        df.to_csv(log_file, mode='a', header=False, index=False)
    else:
        df.to_csv(log_file, index=False)

    st.success("📝 試験運用ログが登録＆保存されました！")

# 一覧表示
if os.path.exists(log_file):
    st.subheader("📋 登録済みログ一覧")
    logs_df = pd.read_csv(log_file)
    st.dataframe(logs_df)
