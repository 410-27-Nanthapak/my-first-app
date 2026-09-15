import time
import streamlit as st

st.title("⏱️ เกมทายศิลปิน SM Entertainment")

# ----------------------------------------------------
# 1. กำหนดค่าเริ่มต้นใน session_state
# ----------------------------------------------------
for i in range(1, 11):
    if f"ans{i}_val" not in st.session_state:
        st.session_state[f"ans{i}_val"] = ""

if "start" not in st.session_state:
    st.session_state.start = None

if "is_ended" not in st.session_state:
    st.session_state.is_ended = False


# ----------------------------------------------------
# ฟังก์ชันเริ่มเกมใหม่
# ----------------------------------------------------
def reset_game():
    for i in range(1, 11):
        st.session_state[f"ans{i}_val"] = ""

    st.session_state.start = time.time()
    st.session_state.is_ended = False


# ----------------------------------------------------
# ฟังก์ชันแสดงผลคะแนน
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(answers):
    st.balloons()

    correct_answers = [
        "aespa",
        "riize",
        "shinee",
        "wayv",
        "nct wish",
        "nct",
        "dearalice",
        "naevis",
        "exo",
        "H.O.T."   
    ]

    score = 0

    for i in range(10):
        user_answer = answers[i].strip().lower()
        correct = correct_answers[i]

        if user_answer == correct:
            st.success(f"✅ ข้อ {i+1}: ถูกต้อง")
            score += 1
        else:
            st.error(
                f"❌ ข้อ {i+1}: ยังไม่ถูกต้อง "
                f"(คำตอบที่ถูกคือ {correct_answers[i]})"
            )

    st.info(f"🏆 ได้คะแนนรวม: {score}/10 คะแนน")

    if score == 10:
        st.success("🎉 PERFECT! You win!")
    elif score >= 5:
        st.success("🎊 You win!")
    else:
        st.error("💀 You lose!")


# ----------------------------------------------------
# 2. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)


# ----------------------------------------------------
# 3. แสดงเวลานับถอยหลัง
# ----------------------------------------------------
if st.session_state.start is not None and not st.session_state.is_ended:

    time_left = int(
        180 - (time.time() - st.session_state.start)
    )

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()


st.divider()


# ----------------------------------------------------
# 4. คำถามและช่องรับคำตอบ
# ----------------------------------------------------

questions = [
    "ข้อ 1: สมาชิกวงผู้หญิง มี 4 คน มาจากค่าย SM",
    
    "ข้อ 2: อดีตมีสมาชิก 7 คน ปัจจุบันเหลือ 6 คน gen 5 ",
    
    "ข้อ 3: เจ้าของเพลง Replay",
    
    "ข้อ 4: NCT unit ใดเป็น unit ที่มีฐานในจีน",
    
    "ข้อ 5: ยูนิตสุดท้ายของจักรวาล NCT เน้นทำกิจกรรมในประเทศญี่ปุ่นเป็นหลัก",
    
    "ข้อ 6: วงบอยแบนด์ที่มีสมาชิกเยอะที่สุดในค่าย "
    "(มีมากกว่า 20 คน) และแบ่งกลุ่มย่อยออกไปเป็นหลาย ๆ ยูนิต",
    
    "ข้อ 7: วงบอยแบนด์สัญชาติอังกฤษวงแรกของค่าย SM",
    
    "ข้อ 8: ศิลปิน Virtual (เสมือนจริง) หญิงคนแรกของค่าย "
    "ที่เดิมทีเป็นแค่ AI ในมิวสิกวิดีโอของ aespa "
    "แต่ตอนนี้ถูกผลักดันให้ออกผลงานเพลง มีอัลบั้ม "
    "และมีแท่งไฟเป็นของตัวเองแล้ว",
    
    "ข้อ 9: วงบอยแบนด์วงไหนของ SM ที่มิวสิกวิดีโอเพลง "
    '"Love Shot" สร้างสถิติเป็น MV ที่มียอดวิวสูงที่สุด '
    "ตลอดกาลของค่าย SM Entertainment บน YouTube",
    
    "ข้อ 10: วงบอยแบนด์วงไหนคือวงแรกสุดในประวัติศาสตร์ "
    "ของค่าย SM Entertainment ที่เดบิวต์ในปี 1996 "
    "และได้รับการบันทึกว่าเป็นวงที่เปิดประวัติศาสตร์ "
    "วัฒนธรรมไอดอลเคป็อปยุค Gen"
]


answers = []

for i in range(10):
    answer = st.text_input(
        questions[i],
        value=st.session_state[f"ans{i+1}_val"],
        key=f"input_{i+1}"
    )

    st.session_state[f"ans{i+1}_val"] = answer
    answers.append(answer)


# ----------------------------------------------------
# 5. ปุ่มส่งคำตอบ
# ----------------------------------------------------
if st.session_state.start is not None and not st.session_state.is_ended:

    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    # ทำให้เวลานับต่อเนื่อง
    time.sleep(1)
    st.rerun()


# ----------------------------------------------------
# 6. แสดงผลลัพธ์
# ----------------------------------------------------
if st.session_state.is_ended:
    show_result_dialog(answers)
