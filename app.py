import streamlit as st
import pandas as pd

# Set Page Config
st.set_page_config(page_title="Decatur Baptist TT League", layout="wide")

st.title("🏓 Decatur Baptist TT League")
st.subheader("Paperless League Management")

# Setup for 3 Groups
cols = st.columns(3)
group_names = ["Group A", "Group B", "Group C"]

for i, col in enumerate(cols):
    with col:
        st.header(group_names[i])
        size = st.selectbox(f"Players in {group_names[i]}", [6, 7, 8], key=f"size_{i}")
        
        # Player Input
        player_list = []
        for p in range(size):
            name = st.text_input(f"P{p+1}", f"Player {p+1}", key=f"p_{i}_{p}")
            player_list.append(name)
            
        # Match Recording
        st.markdown("---")
        st.write("**Record Result (Winner gets 1pt)**")
        wins = {player: 0 for player in player_list}
        
        # Simple Match Grid (1 vs 2, 1 vs 3, etc.)
        import itertools
        matches = list(itertools.combinations(player_list, 2))
        
        for m_idx, (p1, p2) in enumerate(matches):
            winner = st.radio(f"{p1} vs {p2}", ["None", p1, p2], horizontal=True, key=f"match_{i}_{m_idx}")
            if winner != "None":
                wins[winner] += 1
        
        # Display Leaderboard for this Group
        st.markdown("---")
        st.write(f"🏆 **{group_names[i]} Standings**")
        df = pd.DataFrame(list(wins.items()), columns=["Player", "Pts"]).sort_values("Pts", ascending=False)
        st.table(df)

st.sidebar.info("Tip: Bookmark this URL on your phone to use it during the league!")
