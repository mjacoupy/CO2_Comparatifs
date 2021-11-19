# #######################################################################################################################
#                                              # === LIBRAIRIES === #
# #######################################################################################################################
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt


# #######################################################################################################################
#                                              # === FUNCTIONS === #
# #######################################################################################################################
def side_bar():
    """..."""
    end = '<p style="font-family:Avenir; font-weight:bold; color:#FCBA28; font-size:12px; ">©2021 Positive Thinking Company et/ou ses affiliés. Tous droits réservés. Produit par le PTC Tech Lab.</p>'
    st.sidebar.markdown("""---""")
    try:
        st.sidebar.image(image1, width=50)
    except Exception as e:
        pass

    st.sidebar.markdown(end, unsafe_allow_html=True)


def camembert(iratio, datacenter, reseau, device, appareil, color1, color2):
    """..."""
    pie = plt.figure(figsize=(4, 4))
    bilan_conso = (datacenter+reseau+device) * iratio / 1000
    sizes = [bilan_conso, appareil/life_time]
    patches, texts = plt.pie(sizes, startangle=90, colors=[color1, color2])
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
    st.pyplot(pie)

# #######################################################################################################################
#                                              # === CONSTANTS === #
# #######################################################################################################################

# From ADEME
FABRICATION_LAPTOP = 156
FABRICATION_FIXE = 296
FABRICATION_LAPTOP_ECRAN = 156 + 300
FABRICATION_FIXE_ECRAN = 296 + 300
SMARTPHONE = 30

JOURS_PAR_SEMAINE = 5
SEMAINE_PAR_AN = 52

# From Carbonalyser
RATIO_GCO2_KWH_WORLD = 519
RATIO_GCO2_KWH_EUROPE = 276
RATIO_GCO2_KWH_CHINE = 681
RATIO_GCO2_KWH_USA = 493
RATIO_GCO2_KWH_FRANCE = 35

# From One-byte_model
CONSO_ETHERNET = 0.000000000429
CONSO_WIFI = 0.000000000152
CONSO_MOBILE = 0.000000000884

CONSO_ORDI = 0.000319415925165412
CONSO_SMARTPHONE = 0.000107688797627196

CONSO_DS_WORLD = 0.000000000072
# Calculé
CONSO_DS_EUROPE = RATIO_GCO2_KWH_EUROPE * CONSO_DS_WORLD / RATIO_GCO2_KWH_WORLD
CONSO_DS_CHINE = RATIO_GCO2_KWH_CHINE * CONSO_DS_WORLD / RATIO_GCO2_KWH_WORLD
CONSO_DS_USA = RATIO_GCO2_KWH_USA * CONSO_DS_WORLD / RATIO_GCO2_KWH_WORLD
CONSO_DS_FRANCE = RATIO_GCO2_KWH_FRANCE * CONSO_DS_WORLD / RATIO_GCO2_KWH_WORLD



# #######################################################################################################################
#                                              # === ALGO === #
# #######################################################################################################################
image1 = Image.open("app_logos/PTCtechLab.png")
image2 = Image.open("app_logos/PTC.png")
europe = Image.open("app_logos/Europe.jpg")
usa = Image.open("app_logos/USA.jpg")
chine = Image.open("app_logos/Chine.png")
france = Image.open("app_logos/France.png")
terre = Image.open("app_logos/Terre.png")

st.sidebar.image(image2, width=200)

analysis = st.sidebar.selectbox('', ["Consommation d'une page web", "Comparatifs"])
side_bar()
st.title("One byte model")

if analysis == "Consommation d'une page web":

    st.header("Consommation d'une page web")
    st.markdown("""---""")
    col1, col2, col3 = st.columns(3)
    with col1:
        weight = st.number_input("Poids de la page (MB)", step=0.1, min_value=0.0, value=1.0)
        time = st.number_input("Temps de lecture (minutes)", step=1, min_value=0, value=5)
    with col2:
        appareil = st.radio("Type d'appareil", ['Laptop', 'Laptop + Ecran', 'Ordinateur Fixe + Ecran', 'Smartphone'])
        network = st.radio("Type de réseau", ['WIFI', 'Ethernet', "Mobile"])
    with col3:
        loc = st.radio("Ou sont stockées les données", ['Monde', 'Europe', 'Chine', 'USA', 'France'])

    button = st.button("Analyse")

    if weight and time and button:
        if appareil == "Smartphone":
            a = CONSO_SMARTPHONE
        elif appareil in ['Laptop', 'Laptop + Ecran', 'Ordinateur Fixe + Ecran']:
            a = CONSO_ORDI

        if network == "Ethernet":
            n = CONSO_ETHERNET
        elif network == "WIFI":
            n = CONSO_WIFI
        elif network == "Mobile":
            n = CONSO_MOBILE

        datacenter = weight * 1e6 * CONSO_DS_WORLD
        reseau = weight * n
        device = time * a
        consumption = datacenter+reseau+device

        if loc == "Monde":
            bilan = consumption * RATIO_GCO2_KWH_WORLD
        elif loc == "Europe":
            bilan = consumption * RATIO_GCO2_KWH_EUROPE
        elif loc == "USA":
            bilan = consumption * RATIO_GCO2_KWH_USA
        elif loc == "Chine":
            bilan = consumption * RATIO_GCO2_KWH_CHINE
        elif loc == "France":
            bilan = consumption * RATIO_GCO2_KWH_FRANCE
        st.markdown("""---""")
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Bilan Carbone", value=str(round(bilan, 3))+" gCO2e", delta=0)
        with col2:
            st.metric(label="Consommation électrique", value=str(round(consumption, 3))+" kWh", delta=0)

        # st.subheader("Si Data stockée dans le monde")
        # st.markdown('Bilan carbone par semaine : **'+str(round((bilan*5), 1))+"** gCO2e")
        # st.markdown('Bilan carbone par an : **'+str(round((bilan*5*47/1000), 1))+"** kgCO2e")
        # st.markdown("""---""")

        # st.subheader("Si Data stockée en France")
        # st.markdown('Bilan carbone par semaine : **'+str(round((bilan*5), 1))+"** gCO2e")
        # st.markdown('Bilan carbone par an : **'+str(round((bilan*5*47/1000), 1))+"** kgCO2e")
        # st.markdown("""---""")

elif analysis == "Comparatifs":
    st.header("Comparatifs")
    st.markdown("""---""")

    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Consommation quotidienne de données (GB)", step=1, min_value=0, value=1)
    with col2:
        life_time = st.slider("Durée de vie du matériel (années)", step=1, min_value=0, max_value=10, value=4)
    st.markdown("""---""")
    st.markdown("Legend")
    col1, col2, col3 = st.columns([2, 2, 4])

    with col1:
        color1 = st.color_picker("Consommation", '#250044')
    with col2:
        color2 = st.color_picker("Hardware", '#fcba28')
    st.markdown("""---""")
    # Comparatif des types
    weight_byte = weight*1e9

    ratios = [RATIO_GCO2_KWH_WORLD, RATIO_GCO2_KWH_EUROPE, RATIO_GCO2_KWH_CHINE, RATIO_GCO2_KWH_USA, RATIO_GCO2_KWH_FRANCE]
    fabrications = [FABRICATION_LAPTOP, FABRICATION_LAPTOP_ECRAN, FABRICATION_FIXE, FABRICATION_FIXE_ECRAN, SMARTPHONE]

    datacenter = weight_byte * CONSO_DS_WORLD * JOURS_PAR_SEMAINE * SEMAINE_PAR_AN
    reseau = weight_byte * CONSO_WIFI * JOURS_PAR_SEMAINE * SEMAINE_PAR_AN
    device = CONSO_ORDI * JOURS_PAR_SEMAINE * SEMAINE_PAR_AN

    col0, col1, col2, col3, col4, col5 = st.columns(6)
    with col1:
        st.markdown("**LAPTOP**")
    with col2:
        st.markdown("**LAPTOP + ECRAN**")
    with col3:
        st.markdown("**FIXE**")
    with col4:
        st.markdown("**FIXE + ECRAN**")
    with col5:
        st.markdown("**SMARTPHONE**")

    col0, col1, col2, col3, col4, col5 = st.columns(6)
    with col0:
        st.image(terre)
        st.image(europe)
        st.image(chine)
        st.image(usa)
        st.image(france)
    with col1:
        for iRatio in ratios:
            camembert(iRatio, datacenter, reseau, device, FABRICATION_LAPTOP, color1, color2)
    with col2:
        for iRatio in ratios:
            camembert(iRatio, datacenter, reseau, device, FABRICATION_LAPTOP_ECRAN, color1, color2)
    with col3:
        for iRatio in ratios:
            camembert(iRatio, datacenter, reseau, device, FABRICATION_FIXE, color1, color2)
    with col4:
        for iRatio in ratios:
            camembert(iRatio, datacenter, reseau, device, FABRICATION_FIXE_ECRAN, color1, color2)
    with col5:
        for iRatio in ratios:
            camembert(iRatio, datacenter, reseau, device, SMARTPHONE, color1, color2)
