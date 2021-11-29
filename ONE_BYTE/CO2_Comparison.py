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
# From https://pdf.sciencedirectassets.com/277910/1-s2.0-S1876610217X00398/1-s2.0-S1876610217361714/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIDkaQzi735mnUew6z6%2B2mo8eEO3mEr9NTQU6aedgapZJAiEAtUVrvZTrJxqshoQ6sFu9jqF7VKjMt5PzOqDAQAZamPgq%2BgMIdhAEGgwwNTkwMDM1NDY4NjUiDJT6%2BuKeC4mxfsMxOCrXA7ZU0pWwi%2Fd9%2FvNsTAIkOyQ4HQtqnWGOFcRg90xYdB1nO1e5KEgU3ZobeHRPd50nAJUqvBC5YX9qbY8QdzyTpKJFfjgC8lrJklXDr54d4UNl6xLw4C3Kvku4KKL17adenNLgYvGwaX1Aa9G%2FXwsTX1mJwtajKeOvDnQEOk9sWqN3OvLO7FZmir1X4SUlDPj8JF4SyziN8v7R9%2FoVXO9K6s%2FvEt2rfDDqlTvFe%2FlVPUNK9RGbW5pzBFqvv4GQ4QA2C2ZtfrxLuwUmHIUSbc1UrnNYn%2FWzqdAD82E%2Fcx7PriK6WdT%2BTGGl%2FPoOD52DdbeTgRnacx85WgdmeHbCjmtiSBKXImbI1DjXb8Jj7foEH7%2F%2BQETG2qWFNyhXasqI5FAVYG%2FcCAq76toSf74QFPaqMPcKQFiqFAah6Qt77L99l%2BW1onr2ybvSoETL3MRHY%2FJGPWIcIPh5fkb1xcdGlcVpyoxc7JOtcwyEl1kHi8%2FVkC2GHCPOiJpq1Y4IW8inQGyJ0qSM1nkBunn6CvuXDSqRFZasjhmJM8iu5D01oZpnLZwLlW%2F998ss8GF3JD%2F2g%2FE31NfwX0ykiChdYbflCG7grK4Wf7zm%2FoskvttQSN3EAPFpRVeUYrCaczC2mf6MBjqlAT0zINwqkYr5gTHb7U%2BkSQloZRR8w8Pw174KASsNCdeR0cCUJ6xH8qU8o3mVW03%2FkUWNZOluLYjPz3gTLESV7CegNJy5naRo7uNpETqXGrwCIA%2FklWqA5STe7f99yS2cQ7F0wu7EZatGmeNfq58qf5Qx9v3rQQMBY1%2BWRehlHloxkqfuxWPCp9G9UpnZuoeqGScwL8ryBe9hhbakrnHujtdTUUcx%2Bg%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20211125T133719Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTY7JTY2Y4O%2F20211125%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=04c1f7095a58c244a2ae2a9c6962bac7a88cb21803645d7f800f9ff4023cf073&hash=b70389cd820d2c596cb90d8762e8c4d916b89b12a16b9261fe91607827b57ced&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S1876610217361714&tid=spdf-0d5a4a62-7e5e-43fa-8a4d-6774cf4794d3&sid=57766df38ea78944b71b22f-6c2d82ab2269gxrqb&type=client
RATIO_GCO2_KWH_CHINE = 681
RATIO_GCO2_KWH_USA = 493
# from https://www.edf.fr/groupe-edf/agir-en-entreprise-responsable/rapports-et-indicateurs/emissions-de-gaz-a-effet-de-serre (2021)
RATIO_GCO2_KWH_FRANCE = 22.25
# from https://www.eea.europa.eu/data-and-maps/daviz/co2-emission-intensity-9/download.table (2020)
RATIO_GCO2_KWH_EUROPE = 256
RATIO_GCO2_KWH_ALLEMAGNE = 311


# From One-byte_model
CONSO_ETHERNET = 0.000000000429
CONSO_WIFI1 = 0.000000000152
CONSO_MOBILE = 0.000000000884

CONSO_LAPTOP = 0.000319415925165412
CONSO_FIXE = None
CONSO_SMARTPHONE = 0.000107688797627196

# From One byte model
CONSO_DS_KWH = 894 * 1e9
CONSO_DS_BYTE = 17.1 * 1e21
CONSO_DC_WORLD1 = CONSO_DS_KWH / CONSO_DS_BYTE

# #### NEW #####
# From IEA analysis based on Masanet et al. (2020) and Malmodin (2020).
CONSO_DS_KWH = 225 * 1e9
# # From https://techjury.net/blog/how-much-data-is-created-every-day/#gref
# CONSO_DS_BYTE = 44 * 1e21
# From https://www.globenewswire.com/fr/news-release/2021/03/08/2188582/28124/en/Data-Center-IP-Traffic-Estimated-to-Reach-20-6-Zettabytes-by-the-End-of-2021.html
CONSO_DS_BYTE = 20.8 * 1e21
CONSO_DC_WORLD2 = CONSO_DS_KWH / CONSO_DS_BYTE

# IEA analysis based on Coroamă (2021), ITU (2020) and Malmodin and Lundén (2018).
CONSO_NETWORK_KWH = 300 * 1e9
# # From https://techjury.net/blog/how-much-data-is-created-every-day/#gref
# CONSO_DS_BYTE = 44 * 1e21
# From https://www.globenewswire.com/fr/news-release/2021/03/08/2188582/28124/en/Data-Center-IP-Traffic-Estimated-to-Reach-20-6-Zettabytes-by-the-End-of-2021.html
CONSO_DS_BYTE = 20.8 * 1e21
CONSO_WIFI2 = CONSO_NETWORK_KWH / CONSO_DS_BYTE

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
st.title("1-byte-model")

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
        value = st.radio("Source de données", ["1-byte-model", "Research Papers 2020-21"])
        if value == "1-byte-model":
            CONSO_WIFI = CONSO_WIFI1
            CONSO_DC_WORLD = CONSO_DC_WORLD1
        else:
            CONSO_WIFI = CONSO_WIFI2
            CONSO_DC_WORLD = CONSO_DC_WORLD2

    if weight and time:
        if appareil == "Smartphone":
            conso_appareil = CONSO_SMARTPHONE
        elif appareil in ['Laptop', 'Laptop + Ecran', 'Ordinateur Fixe + Ecran']:
            conso_appareil = CONSO_LAPTOP

        if network == "Ethernet":
            conso_network = CONSO_ETHERNET
        elif network == "WIFI":
            conso_network = CONSO_WIFI1
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
        with col2:
            st.metric(label="Emprinte Carbone", value=str(round(bilan, 3))+" gCO2e", delta=0)
        with col1:
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
    st.header("Bilan Carbone - Comparatifs")
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
    col1, col2, col3, col4 = st.columns([2, 2, 2, 4])

    with col1:
        color1 = st.color_picker("Consommation", '#250044')
    with col2:
        color2 = st.color_picker("Hardware", '#fcba28')
    with col4:
        value = st.radio("Source de données", ["1-byte-model", "Research Papers 2020-21"])
        if value == "1-byte-model":
            CONSO_WIFI = CONSO_WIFI1
            CONSO_DC_WORLD = CONSO_DC_WORLD1
        else:
            CONSO_WIFI = CONSO_WIFI2
            CONSO_DC_WORLD = CONSO_DC_WORLD2
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
        for iVal in [values_fra, values_eur, values_all, values_ter, values_usa, values_chi]:
            names = ['1', '2', '3', '4']
            barplot = plt.figure(figsize=(3.6, 4))
            ax = sns.barplot(names, iVal, palette='viridis')
            ax.set_xticklabels(labels=[textwrap.fill(iLabel, 25) for iLabel in names],
                              rotation=60, fontsize=15, horizontalalignment="right")
            ax.set(xlabel=None)
            ax.set_ylabel('KgCO2e')
            st.pyplot(barplot)



# #######################################################################################################################

#                                          # === END OF FILE === #

# #######################################################################################################################

