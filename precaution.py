import streamlit as st

def main():
    st.header("🛑 Standard Operating Procedures (SOPs) for Different Disaster")

    col1, col2, col3= st.columns(3)

    with col1:
        st.subheader("🌍 Earthquake")
        st.markdown("""
        - Identify safe spots (under sturdy furniture, near inner walls).  
        - Drop, Cover, and Hold during shaking.  
        - Stay indoors unless it's unsafe (collapsing structures, fire).  
        - Aftershocks may follow—stay alert and check for injuries.
        """)
        st.subheader("🌊 Tsunami")
        st.markdown("""
        - Move to higher ground immediately after strong coastal earthquakes.  
        - Follow official tsunami warnings and sirens.  
        - Avoid beaches and harbors until an all-clear is given.  
        - Expect multiple waves, not just one.  

        """)
        

    with col2:
        st.subheader("🌪 Cyclone/Hurricane")
        st.markdown("""
        - Secure windows, doors, and outdoor objects before impact.  
        - Stay indoors and away from windows.  
        - Move to higher ground in case of storm surges.  
        - Avoid flooded areas and downed power lines after the storm.  
        """)
        st.subheader("🔥 Wildfire")
        st.markdown("""
        - Create a fire-safe zone around your home (clear dry vegetation).  
        - Evacuate early if wildfires approach your area.  
        - Wear a damp cloth or mask to filter smoke.  
        - Avoid hot ash and smoldering areas after the fire.  
        """)
        
        st.subheader("💥 Industrial Accidents (Chemical Leaks, Gas Explosions)")
        st.markdown("""
        - *Evacuate immediately* and move upwind.  
        - Cover your *nose and mouth with a damp cloth*.  
        - Avoid *touching contaminated surfaces*.  
        - Follow *official decontamination instructions*.  

        """)
        
    with col3:
        st.subheader("🏔 Landslide")
        st.markdown("""
        - Watch for cracks, leaning trees, or unusual ground movement.  
        - Move away from the landslide path as fast as possible.  
        - Take cover under sturdy furniture if indoors.  
        - Stay away from unstable slopes after the event.  
        """)
        st.subheader("🌊 Flood")
        st.markdown("""
        - Move valuables and electrical items to higher ground.  
        - Avoid walking or driving through floodwaters.  
        - Turn off electricity and gas if water enters your home.  
        - Drink only safe, clean water after flooding recedes.  
        """)
if __name__ == "__main__":
    main()
