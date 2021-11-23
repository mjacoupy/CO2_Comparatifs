# #######################################################################################################################
#                                              # === LIBRAIRIES === #
# #######################################################################################################################
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import textwrap


# #######################################################################################################################
#                                              # === FUNCTIONS === #
# #######################################################################################################################
def side_bar():
    """..."""
    end = '<p style="font-family:Avenir; font-weight:bold; color:#FCBA28; font-size:12px; ">©2021 Positive Thinking Company et/ou ses affiliés. Tous droits réservés. Produit par le PTC Tech Lab.</p>'
    st.sidebar.markdown("""---""")
    st.sidebar.image(image1, width=50)
    st.sidebar.markdown(end, unsafe_allow_html=True)


def camembert(iratio, datacenter, reseau, device, appareil, color1, color2):
    """..."""
    pie = plt.figure(figsize=(4, 4))
    bilan_conso = round((datacenter+reseau+device) * iratio / 1000, 1)
    sizes = [bilan_conso, round(appareil/life_time, 1)]
    patches, texts = plt.pie(sizes, startangle=90, colors=[color1, color2])
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
    st.pyplot(pie)
    return sizes

# #######################################################################################################################
#                                              # === CONSTANTES === #
# #######################################################################################################################
MINUTES_PAR_JOUR = 480
JOURS_PAR_SEMAINE = 5
SEMAINE_PAR_AN = 47

# From ADEME
FABRICATION_LAPTOP = 156
FABRICATION_LAPTOP_ECRAN = 156 + 336
FABRICATION_FIXE_ECRAN17 = 169 + 336
FABRICATION_FIXE_PUISSANT_ECRAN24 = 296 + 431
FABRICATION_SMARTPHONE = 39.1

# From Carbonalyser (1 kWh -> 1 gCO2)
RATIO_GCO2_KWH_WORLD = 519
RATIO_GCO2_KWH_CHINE = 681
RATIO_GCO2_KWH_USA = 493
# from https://www.edf.fr/groupe-edf/agir-en-entreprise-responsable/rapports-et-indicateurs/emissions-de-gaz-a-effet-de-serre (2021)
RATIO_GCO2_KWH_FRANCE = 22.25
# from https://www.eea.europa.eu/data-and-maps/daviz/co2-emission-intensity-9/download.table (2020)
RATIO_GCO2_KWH_EUROPE = 256
RATIO_GCO2_KWH_ALLEMAGNE = 311


# From One-byte_model
CONSO_ETHERNET = 0.000000000429
CONSO_WIFI = 0.000000000152
CONSO_MOBILE = 0.000000000884

CONSO_LAPTOP = 0.000319415925165412
CONSO_FIXE = None
CONSO_SMARTPHONE = 0.000107688797627196

CONSO_DC_WORLD = 0.000000000072
# Calculé
CONSO_DC_EUROPE = RATIO_GCO2_KWH_EUROPE * CONSO_DC_WORLD / RATIO_GCO2_KWH_WORLD
CONSO_DC_CHINE = RATIO_GCO2_KWH_CHINE * CONSO_DC_WORLD / RATIO_GCO2_KWH_WORLD
CONSO_DC_USA = RATIO_GCO2_KWH_USA * CONSO_DC_WORLD / RATIO_GCO2_KWH_WORLD
CONSO_DC_FRANCE = RATIO_GCO2_KWH_FRANCE * CONSO_DC_WORLD / RATIO_GCO2_KWH_WORLD



# #######################################################################################################################
#                                              # === ALGO === #
# #######################################################################################################################
image1 = Image.open("app_logos/PTCtechLab.png")
image2 = Image.open("app_logos/PTC.png")
europe = Image.open("app_logos/Europe.jpg")
usa = Image.open("app_logos/USA.jpg")
chine = Image.open("app_logos/Chine.png")
france = Image.open("app_logos/France.png")
allemagne = Image.open("app_logos/Allemagne.png")
terre = Image.open("app_logos/Terre.png")
base_conso = Image.open("app_logos/Conso.png")
base_conso2 = Image.open("app_logos/Conso2.png")

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
        loc = st.radio("Lieu de travail", ['France', 'Europe', 'Allemagne', 'Monde', 'USA', 'Chine'])

    if weight and time:
        if appareil == "Smartphone":
            conso_appareil = CONSO_SMARTPHONE
        elif appareil in ['Laptop', 'Laptop + Ecran', 'Ordinateur Fixe + Ecran']:
            conso_appareil = CONSO_LAPTOP

        if network == "Ethernet":
            conso_network = CONSO_ETHERNET
        elif network == "WIFI":
            conso_network = CONSO_WIFI
        elif network == "Mobile":
            conso_network = CONSO_MOBILE

        datacenter = weight * 1e6 * CONSO_DC_WORLD
        reseau = weight * 1e6 * conso_network
        device = time * conso_appareil
        consommation_totale = datacenter + reseau + device

        if loc == "Monde":
            ratio = RATIO_GCO2_KWH_WORLD
        elif loc == "Europe":
            ratio = RATIO_GCO2_KWH_EUROPE
        elif loc == "USA":
            ratio = RATIO_GCO2_KWH_USA
        elif loc == "Chine":
            ratio = RATIO_GCO2_KWH_CHINE
        elif loc == "France":
            ratio = RATIO_GCO2_KWH_FRANCE
        elif loc == "Allemagne":
            ratio = RATIO_GCO2_KWH_ALLEMAGNE
        bilan = consommation_totale * ratio
        st.markdown("""---""")

        # Metrics
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Bilan Carbone", value=str(round(bilan, 3))+" gCO2e", delta=0)
        with col2:
            st.metric(label="Consommation électrique", value=str(round(consommation_totale, 3))+" kWh", delta=0)

        # Plots
        names = ['DATA CENTER', 'RESEAU', 'APPAREIL']

        col1, col2 = st.columns(2)

        with col1:
            values = [datacenter * RATIO_GCO2_KWH_WORLD, reseau * RATIO_GCO2_KWH_WORLD, device * ratio]

            barplot_2 = plt.figure(figsize=(6, 3.5))
            ax = sns.barplot(names, values, palette='viridis')
            ax.set_xticklabels(labels=[textwrap.fill(iLabel, 25) for iLabel in names],
                               rotation=60, fontsize=10, horizontalalignment="right")
            ax.set_title("Repartition des emission de CO2")
            ax.set(xlabel=None)
            ax.set_ylabel('gCOEe')
            st.pyplot(barplot_2)
        with col2:
            values = [datacenter, reseau, device]

            barplot_1 = plt.figure(figsize=(6, 3.5))
            ax = sns.barplot(names, values, palette='viridis')
            ax.set_xticklabels(labels=[textwrap.fill(iLabel, 25) for iLabel in names],
                               rotation=60, fontsize=10, horizontalalignment="right")
            ax.set_title("Repartition des consommations energétiques")
            ax.set(xlabel=None)
            ax.set_ylabel('kWh')
            st.pyplot(barplot_1)


elif analysis == "Comparatifs":
    st.header("Comparatifs")
    st.markdown("""---""")

    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Consommation quotidienne de données (GB)", step=0.1, min_value=0.0, value=1.0)
    with col2:
        life_time = st.slider("Age du matériel (années)", step=0.5, min_value=0.5, max_value=10.0, value=4.0)
    with st.expander("Base de calculs"):
        st.image(base_conso)
        st.image(base_conso2)
        st.write("[Lien vers la page de calculs](https://www.orange.ma/Offres-services/Simulateur)")
    st.markdown("""---""")
    st.markdown("Légende (couleurs modifiables)")
    col1, col2, col3 = st.columns([2, 2, 6])

    with col1:
        color1 = st.color_picker("Consommation", '#250044')
    with col2:
        color2 = st.color_picker("Hardware", '#fcba28')
    st.markdown("""---""")
    # Comparatif des types
    weight_byte = weight*1e9

    ratios = [RATIO_GCO2_KWH_FRANCE, RATIO_GCO2_KWH_EUROPE, RATIO_GCO2_KWH_ALLEMAGNE, RATIO_GCO2_KWH_WORLD, RATIO_GCO2_KWH_USA, RATIO_GCO2_KWH_CHINE]
    fabrications = [FABRICATION_LAPTOP, FABRICATION_LAPTOP_ECRAN, FABRICATION_FIXE_PUISSANT_ECRAN24, FABRICATION_SMARTPHONE]

    reseau = weight_byte * CONSO_WIFI * JOURS_PAR_SEMAINE * SEMAINE_PAR_AN
    datacenter = weight_byte * CONSO_DC_WORLD * JOURS_PAR_SEMAINE * SEMAINE_PAR_AN
    device_ordi = CONSO_LAPTOP * MINUTES_PAR_JOUR * JOURS_PAR_SEMAINE * SEMAINE_PAR_AN
    device_tel = CONSO_SMARTPHONE * MINUTES_PAR_JOUR * JOURS_PAR_SEMAINE * SEMAINE_PAR_AN

    col0, col1, col2, col3, col4, col5, col6 = st.columns(7)
    with col1:
        st.markdown("**LAPTOP SEUL**")
    with col2:
        st.markdown('**LAPTOP + ECRAN 17"**')
    with col3:
        st.markdown('**FIXE PUISSANT + ECRAN 24"**')
    with col4:
        st.markdown('**SMARTPHONE >5,5"**')
    with col5:
        st.markdown('**TOTAL**')


    col0, col1, col2, col3, col4, col5, col6 = st.columns(7)
    with col0:
        for iRegion in [france, europe, allemagne, terre, usa, chine]:
            st.image(iRegion)
    for iCol, iProduct in zip([col1, col2, col3], [FABRICATION_LAPTOP, FABRICATION_LAPTOP_ECRAN, FABRICATION_FIXE_PUISSANT_ECRAN24]):
        with iCol:
            for iRatio in ratios:
                sizes = camembert(iRatio, datacenter, reseau, device_ordi, iProduct, color1, color2)


    with col4:
        for iRatio in ratios:
            sizes = camembert(iRatio, datacenter, reseau, device_tel, FABRICATION_SMARTPHONE, color1, color2)

    values_fra = []
    values_eur = []
    values_all = []
    values_ter = []
    values_usa = []
    values_chi = []
    for iProduct in fabrications:
        if iProduct != FABRICATION_SMARTPHONE:
            values_fra.append(((datacenter+reseau+device_ordi) * RATIO_GCO2_KWH_FRANCE / 1000) + (iProduct/life_time))
            values_eur.append(((datacenter+reseau+device_ordi) * RATIO_GCO2_KWH_EUROPE / 1000) + (iProduct/life_time))
            values_all.append(((datacenter+reseau+device_ordi) * RATIO_GCO2_KWH_ALLEMAGNE / 1000) + (iProduct/life_time))
            values_ter.append(((datacenter+reseau+device_ordi) * RATIO_GCO2_KWH_WORLD / 1000) + (iProduct/life_time))
            values_usa.append(((datacenter+reseau+device_ordi) * RATIO_GCO2_KWH_USA / 1000) + (iProduct/life_time))
            values_chi.append(((datacenter+reseau+device_ordi) * RATIO_GCO2_KWH_CHINE / 1000) + (iProduct/life_time))
        else:
            values_fra.append(((datacenter+reseau+device_tel) * RATIO_GCO2_KWH_FRANCE / 1000) + (iProduct/life_time))
            values_eur.append(((datacenter+reseau+device_tel) * RATIO_GCO2_KWH_EUROPE / 1000) + (iProduct/life_time))
            values_all.append(((datacenter+reseau+device_tel) * RATIO_GCO2_KWH_ALLEMAGNE / 1000) + (iProduct/life_time))
            values_ter.append(((datacenter+reseau+device_tel) * RATIO_GCO2_KWH_WORLD / 1000) + (iProduct/life_time))
            values_usa.append(((datacenter+reseau+device_tel) * RATIO_GCO2_KWH_USA / 1000) + (iProduct/life_time))
            values_chi.append(((datacenter+reseau+device_tel) * RATIO_GCO2_KWH_CHINE / 1000) + (iProduct/life_time))


    with col5:
        names = ['1', '2', '3', '4']
        barplot = plt.figure(figsize=(3, 3))
        ax = sns.barplot(names, values_fra, palette='viridis')
        ax.set_xticklabels(labels=[textwrap.fill(iLabel, 25) for iLabel in names],
                          rotation=60, fontsize=15, horizontalalignment="right")
        ax.set_title("Emissions totales")
        ax.set(xlabel=None)
        ax.set_ylabel('KgCO2e')
        st.pyplot(barplot)



# #######################################################################################################################

#                                          # === END OF FILE === #

# #######################################################################################################################

# Carbonalyser
#


