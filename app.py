import streamlit as st
import serpapi
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="E-Pharmacy",
    page_icon="💊",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

/* BACKGROUND */
.stApp{
    background:
    linear-gradient(rgba(0,0,0,0.45),
    rgba(0,0,0,0.45)),
    url("https://images.unsplash.com/photo-1587854692152-cbe660dbde88");

    background-size: cover;
    background-attachment: fixed;
}

/* TEXT */
h1,h2,h3,h4,h5,h6,p,label,span{
    color:white !important;
}

/* SEARCH BOX */
.stTextInput input{
    background-color:white !important;
    color:black !important;
    border-radius:10px;
    height:50px;
    font-size:18px;
}

/* BUTTON */
.stButton>button{
    width:100%;
    border-radius:10px;
    background-color:#00b894;
    color:white;
    margin-top:5px;
}

/* EXPANDER */
.streamlit-expanderHeader{
    font-size:18px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
col1, col2 = st.columns([1,5])

with col1:
    st.image("e_pharmacy.png", width=120)

with col2:
    st.markdown("""
    <h1 style='margin-top:30px;'>
    💊 E-Pharmacy Price Comparison
    </h1>
    """, unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "selected_medicine" not in st.session_state:
    st.session_state.selected_medicine = ""

# ---------------- SEARCH BAR ----------------
st.markdown("## 🔍 Search Medicines")

search_input = st.text_input(
    "",
    value=st.session_state.selected_medicine,
    placeholder="Search medicines like Dolo 650, Vitamin C..."
)

if search_input:
    st.session_state.selected_medicine = search_input

# ---------------- CATEGORY MENUS ----------------
st.markdown("## 🩺 Shop By Category")

# ROW 1
c1, c2, c3, c4 = st.columns(4)

# ---------------- HAIR CARE ----------------
with c1:

    with st.expander("💇 Hair Care ▼"):

        if st.button("Minoxidil"):
            st.session_state.selected_medicine = "Minoxidil"

        if st.button("Biotin"):
            st.session_state.selected_medicine = "Biotin"

        if st.button("Hair Serum"):
            st.session_state.selected_medicine = "Hair Serum"

        if st.button("Hair Growth Oil"):
            st.session_state.selected_medicine = "Hair Growth Oil"

# ---------------- FITNESS ----------------
with c2:

    with st.expander("🏋️ Fitness & Health ▼"):

        if st.button("Whey Protein"):
            st.session_state.selected_medicine = "Whey Protein"

        if st.button("Creatine"):
            st.session_state.selected_medicine = "Creatine"

        if st.button("Mass Gainer"):
            st.session_state.selected_medicine = "Mass Gainer"

        if st.button("Fish Oil"):
            st.session_state.selected_medicine = "Fish Oil"

# ---------------- SEXUAL ----------------
with c3:

    with st.expander("❤️ Sexual Wellness ▼"):

        if st.button("Condom"):
            st.session_state.selected_medicine = "Condom"

        if st.button("Lubricant"):
            st.session_state.selected_medicine = "Lubricant"

        if st.button("Delay Spray"):
            st.session_state.selected_medicine = "Delay Spray"

# ---------------- VITAMINS ----------------
with c4:

    with st.expander("💊 Vitamins & Nutrition ▼"):

        if st.button("Vitamin C"):
            st.session_state.selected_medicine = "Vitamin C"

        if st.button("Vitamin D"):
            st.session_state.selected_medicine = "Vitamin D"

        if st.button("Zinc Tablet"):
            st.session_state.selected_medicine = "Zinc Tablet"

        if st.button("Multivitamin"):
            st.session_state.selected_medicine = "Multivitamin"

# ROW 2
c5, c6, c7, c8 = st.columns(4)

# ---------------- SUPPORTS ----------------
with c5:

    with st.expander("🦴 Supports & Braces ▼"):

        if st.button("Knee Support"):
            st.session_state.selected_medicine = "Knee Support"

        if st.button("Ankle Support"):
            st.session_state.selected_medicine = "Ankle Support"

        if st.button("Back Support"):
            st.session_state.selected_medicine = "Back Support"

# ---------------- IMMUNITY ----------------
with c6:

    with st.expander("🛡️ Immunity Boosters ▼"):

        if st.button("Giloy"):
            st.session_state.selected_medicine = "Giloy"

        if st.button("Ashwagandha"):
            st.session_state.selected_medicine = "Ashwagandha"

        if st.button("Chyawanprash"):
            st.session_state.selected_medicine = "Chyawanprash"

# ---------------- HOMEOPATHY ----------------
with c7:

    with st.expander("🌿 Homeopathy ▼"):

        if st.button("Arnica"):
            st.session_state.selected_medicine = "Arnica"

        if st.button("Belladonna"):
            st.session_state.selected_medicine = "Belladonna"

        if st.button("Nux Vomica"):
            st.session_state.selected_medicine = "Nux Vomica"

# ---------------- PET CARE ----------------
with c8:

    with st.expander("🐶 Pet Care ▼"):

        if st.button("Dog Shampoo"):
            st.session_state.selected_medicine = "Dog Shampoo"

        if st.button("Pet Vitamins"):
            st.session_state.selected_medicine = "Pet Vitamins"

        if st.button("Tick Powder"):
            st.session_state.selected_medicine = "Tick Powder"

# ---------------- SHOW SELECTED ----------------
selected_medicine = st.session_state.selected_medicine

if selected_medicine:
    st.success(f"Selected Medicine: {selected_medicine}")

# ---------------- NUMBER OF RESULTS ----------------
number = st.slider(
    "Number of Results",
    1,
    10,
    5
)

# ---------------- SERP API FUNCTION ----------------
def compare(name):

    params = {
        "engine": "google_shopping",
        "q": f"{name} medicine",
        "api_key": st.secrets["SERPAPI_KEY"],
        "gl": "in",
        "hl": "en"
    }

    try:

        search = serpapi.GoogleSearch(params)

        results = search.get_dict()

        shopping_results = results.get(
            "shopping_results",
            []
        )

        return shopping_results

    except:
        return []

# ---------------- AUTO SEARCH ----------------
if selected_medicine:

    with st.spinner("Searching medicines..."):

        inline_shopping_results = compare(
            selected_medicine
        )

    # NO RESULT
    if not inline_shopping_results:

        st.error("No medicine found.")

    else:

        # ---------------- IMAGE ----------------
        st.image(
            inline_shopping_results[0].get(
                "thumbnail"
            ),
            width=250
        )

        med_name = []
        med_price = []

        lowest_price = 999999
        lowest_price_index = 0

        # ---------------- RESULTS ----------------
        for i in range(
            min(number, len(inline_shopping_results))
        ):

            item = inline_shopping_results[i]

            st.markdown("---")

            st.subheader(f"💊 Option {i+1}")

            col1, col2 = st.columns(2)

            source = item.get("source", "N/A")
            title = item.get("title", "N/A")
            price = item.get("price", "₹0")
            link = item.get("link", "#")

            try:
                current_price = float(
                    price.replace("₹", "").replace(",", "")
                )
            except:
                current_price = 0

            med_name.append(source)
            med_price.append(current_price)

            col1.write("### Company")
            col2.write(source)

            col1.write("### Medicine")
            col2.write(title[:60])

            col1.write("### Price")
            col2.write(price)

            col1.write("### Buy Link")
            col2.markdown(f"[Click Here]({link})")

            if current_price < lowest_price:
                lowest_price = current_price
                lowest_price_index = i

        # ---------------- BEST DEAL ----------------
        st.markdown("---")

        st.header("🏆 Best Deal")

        best = inline_shopping_results[lowest_price_index]

        c1, c2 = st.columns(2)

        c1.write("### Company")
        c2.write(best.get("source"))

        c1.write("### Price")
        c2.write(best.get("price"))

        c1.write("### Buy Link")
        c2.markdown(
            f"[Buy Now]({best.get('link')})"
        )

        # ---------------- BAR CHART ----------------
        st.markdown("---")

        st.header("📊 Price Comparison")

        fig, ax = plt.subplots(figsize=(10,5))

        ax.bar(med_name, med_price)

        ax.set_xlabel("Company")
        ax.set_ylabel("Price")
        ax.set_title("Medicine Price Comparison")

        plt.xticks(rotation=20)

        st.pyplot(fig)