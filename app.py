import streamlit as st

st.set_page_config(page_title="God Loves You", page_icon="🤍", layout="centered")

sections = [
    {
        "title": "Nothing can separate you from His love",
        "reference": "Romans 8:38–39 (NLT)",
        "text": '"And I am convinced that nothing can ever separate us from God’s love. Neither death nor life, neither angels nor demons, neither our fears for today nor our worries about tomorrow—not even the powers of hell can separate us from God’s love. No power in the sky above or in the earth below—indeed, nothing in all creation will ever be able to separate us from the love of God that is revealed in Christ Jesus our Lord."',
        "note": "Sometimes through life's challenges, it can feel like we are alone, but this verse reminds us that God's love is unwavering.",
    },
    {
        "title": "He Loved You First",
        "reference": "1 John 4:19 (NLT)",
        "text": '"We love each other because he loved us first."',
        "note": "Jesus showed us what perfect love looks like. He loved us first, and that love serves as the foundation of our own love for others. There are days I fail to love my neighbor the same way, there are probably days you probably stumble as well, but His love remains constant and for that there is hope indeed.",
    },
    {
        "title": "You Can Always Come Home",
        "reference": "Luke 15:20-24 (NLT)",
        "text": '"So he returned home to his father. And while he was still a long way off, his father saw him coming. Filled with love and compassion, he ran to his son, embraced him, and kissed him. His son said to him, ‘Father, I have sinned against both heaven and you, and I am no longer worthy of being called your son.’ “But his father said to the servants, ‘Quick! Bring the finest robe in the house and put it on him. Get a ring for his finger and sandals for his feet. And kill the calf we have been fattening. We must celebrate with a feast, for this son of mine was dead and has now returned to life. He was lost, but now he is found.’ So the party began."',
        "note": "As much as I hate to admit it, I'm crying as I write this because it reminds me of how deeply God loves us, even when we feel unworthy. You will never be beyond the reach of His love. You will never be abandoned by Him. You will never be forsaken. You will never be left alone. You will never be without His presence. Each time you stray, he will welcome you into His loving embrace, and Heaven will rejoice over your return.",
    },
]

if "page" not in st.session_state:
    st.session_state.page = 0

page = st.session_state.page
total = len(sections)


# Welcome screen
if page == 0:
    st.title("God Loves You So Much~ ")
    st.write(
        "Hey Aralynn, recently you reminded me of just how much "
        "God loves us, so I decided to give you this as well :)"
    )

    if st.button("First Note →"):
        st.session_state.page = 1
        st.rerun()


# Verse and note screens
elif 1 <= page <= total:
    s = sections[page - 1]

    reveal_key = f"revealed_{page}"
    if reveal_key not in st.session_state:
        st.session_state[reveal_key] = False

    st.caption(f"{page} of {total}")
    st.header(s["title"])
    st.markdown(f"> {s['text']}")
    st.caption(s["reference"])

    if st.session_state[reveal_key]:
        st.write(s["note"])
    else:
        if st.button("Open Note", key=f"reveal_btn_{page}"):
            st.session_state[reveal_key] = True
            st.rerun()

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("← Back"):
            st.session_state.page -= 1
            st.rerun()

    with col2:
        if page < total:
            if st.button("Next →", type="primary"):
                st.session_state.page += 1
                st.rerun()
        else:
            if st.button("One Last Thing →", type="primary"):
                st.session_state.page = total + 1
                st.rerun()


# Closing screen
elif page == total + 1:
    st.title("For You, Aralynn~")

    st.write(
        "Thank you for reminding me of how much God loves us. "
        "I wanted to give you a little, but very much permanent reminder of that love too."
    )

    st.write(
        "I hope you enjoyed reading these as much as "
        "I enjoyed putting them together for you :)"
    )

    st.caption("Made for you and whoever you may share it with, with love and a little Python 🐍")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("← Last Note"):
            st.session_state.page = total
            st.rerun()

    with col2:
        if st.button("Read Again ↺", type="primary"):
            st.session_state.page = 0

            for verse_page in range(1, total + 1):
                reveal_key = f"revealed_{verse_page}"
                st.session_state.pop(reveal_key, None)

            st.rerun()