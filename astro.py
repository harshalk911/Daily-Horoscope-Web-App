import requests
import selectorlib
import streamlit as st

aries_url = "https://www.ganeshaspeaks.com/horoscopes/daily-horoscope/aries/"
taurus_url = "https://www.ganeshaspeaks.com/horoscopes/daily-horoscope/taurus/"
gemini_url = "https://www.ganeshaspeaks.com/horoscopes/daily-horoscope/gemini/"
cancer_url = "https://www.ganeshaspeaks.com/horoscopes/daily-horoscope/cancer/"
leo_url = "https://www.ganeshaspeaks.com/horoscopes/daily-horoscope/leo/"
virgo_url = "https://www.ganeshaspeaks.com/horoscopes/daily-horoscope/virgo/"
libra_url = "https://www.ganeshaspeaks.com/horoscopes/daily-horoscope/libra/"
scorpio_url = "https://www.ganeshaspeaks.com/horoscopes/daily-horoscope/scorpio/"
sagittarius_url = "https://www.ganeshaspeaks.com/horoscopes/daily-horoscope/sagittarius/"
capricorn_url = "https://www.ganeshaspeaks.com/horoscopes/daily-horoscope/capricorn/"
aquarius_url = "https://www.ganeshaspeaks.com/horoscopes/daily-horoscope/aquarius/"
pisces_url = "https://www.ganeshaspeaks.com/horoscopes/daily-horoscope/pisces/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrape_astro(url):
    response = requests.get(url, headers=HEADERS)
    source_data = response.text
    return source_data

def extract_aries(source):
    extractor = selectorlib.Extractor.from_yaml_file("horoscope.yaml")
    value = extractor.extract(source)["aries"]
    return value

def extract_taurus(source):
    extractor = selectorlib.Extractor.from_yaml_file("horoscope.yaml")
    value = extractor.extract(source)["taurus"]
    return value

def extract_gemini(source):
    extractor = selectorlib.Extractor.from_yaml_file("horoscope.yaml")
    value = extractor.extract(source)["gemini"]
    return value

def extract_cancer(source):
    extractor = selectorlib.Extractor.from_yaml_file("horoscope.yaml")
    value = extractor.extract(source)["cancer"]
    return value

def extract_leo(source):
    extractor = selectorlib.Extractor.from_yaml_file("horoscope.yaml")
    value = extractor.extract(source)["leo"]
    return value

def extract_virgo(source):
    extractor = selectorlib.Extractor.from_yaml_file("horoscope.yaml")
    value = extractor.extract(source)["virgo"]
    return value

def extract_libra(source):
    extractor = selectorlib.Extractor.from_yaml_file("horoscope.yaml")
    value = extractor.extract(source)["libra"]
    return value

def extract_scorpio(source):
    extractor = selectorlib.Extractor.from_yaml_file("horoscope.yaml")
    value = extractor.extract(source)["scorpio"]
    return value

def extract_sagittarius(source):
    extractor = selectorlib.Extractor.from_yaml_file("horoscope.yaml")
    value = extractor.extract(source)["sagittarius"]
    return value

def extract_capricorn(source):
    extractor = selectorlib.Extractor.from_yaml_file("horoscope.yaml")
    value = extractor.extract(source)["capricorn"]
    return value

def extract_aquarius(source):
    extractor = selectorlib.Extractor.from_yaml_file("horoscope.yaml")
    value = extractor.extract(source)["aquarius"]
    return value

def extract_pisces(source):
    extractor = selectorlib.Extractor.from_yaml_file("horoscope.yaml")
    value = extractor.extract(source)["pisces"]
    return value

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0e6d6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1 , col2 = st.columns(2)
with col2:
    st.image("images/logo.png", width=215,)
with col1:
    st.markdown(
        """
        <style>
        .fancy-header {
            color: #A0522D;
            font-size: 50px;
            font-weight: bold;
            text-shadow: 1px 1px 2px #000000;
        }
        </style>
        <div class='fancy-header'>AstroVed Daily Horoscope</div>
        """,
        unsafe_allow_html=True
    )
st.write("\n\n")
option = st.selectbox("Select your Zodiac Sign to know what is there for you in your horoscope today:",
             ("Aries","Taurus", "Gemini", "Cancer", "Leo",
              "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn","Aquarius", "Pisces"))

if option == "Gemini":
    try:
        scraped = scrape_astro(gemini_url)
        extracted = extract_gemini(scraped)
        result = "\n".join(extracted)

        st.header(f"{extracted[0]}")
        st.image("images/gemini.png", width=100)
        st.subheader(f"{extracted[1]} : {extracted[2]}")
        st.subheader(f"'{extracted[3]}'")
        st.subheader(f"'{extracted[4]}'")
    except IndexError:
        st.write("end of page")

if option == "Aries":
    try:
        scraped = scrape_astro(aries_url)
        extracted = extract_aries(scraped)
        result = "\n".join(extracted)

        st.header(f"{extracted[0]}")
        st.image("images/aries.png", width=100)
        st.subheader(f"{extracted[1]} : {extracted[2]}")
        st.subheader(f"'{extracted[3]}'")
        st.subheader(f"'{extracted[4]}'")
    except IndexError:
        st.write("end of page")

if option == "Taurus":
    try:
        scraped = scrape_astro(taurus_url)
        extracted = extract_taurus(scraped)
        result = "\n".join(extracted)

        st.header(f"{extracted[0]}")
        st.image("images/taurus.png", width=100)
        st.subheader(f"{extracted[1]} : {extracted[2]}")
        st.subheader(f"'{extracted[3]}'")
        st.subheader(f"'{extracted[4]}'")
    except IndexError:
        st.write("end of page")

if option == "Cancer":
    try:
        scraped = scrape_astro(cancer_url)
        extracted = extract_cancer(scraped)
        result = "\n".join(extracted)

        st.header(f"{extracted[0]}")
        st.image("images/cancer.png", width=100)
        st.subheader(f"{extracted[1]} : {extracted[2]}")
        st.subheader(f"'{extracted[3]}'")
        st.subheader(f"'{extracted[4]}'")
    except IndexError:
        st.write("end of page")

if option == "Leo":
    try:
        scraped = scrape_astro(leo_url)
        extracted = extract_leo(scraped)
        result = "\n".join(extracted)

        st.header(f"{extracted[0]}")
        st.image("images/leo.png", width=100)
        st.subheader(f"{extracted[1]} : {extracted[2]}")
        st.subheader(f"'{extracted[3]}'")
        st.subheader(f"'{extracted[4]}'")
    except IndexError:
        st.write("end of page")

if option == "Virgo":
    try:
        scraped = scrape_astro(virgo_url)
        extracted = extract_virgo(scraped)
        result = "\n".join(extracted)

        st.header(f"{extracted[0]}")
        st.image("images/virgo.png", width=100)
        st.subheader(f"{extracted[1]} : {extracted[2]}")
        st.subheader(f"'{extracted[3]}'")
        st.subheader(f"'{extracted[4]}'")
    except IndexError:
        st.write("end of page")

if option == "Libra":
    try:
        scraped = scrape_astro(libra_url)
        extracted = extract_libra(scraped)
        result = "\n".join(extracted)

        st.header(f"{extracted[0]}")
        st.image("images/libra.png", width=100)
        st.subheader(f"{extracted[1]} : {extracted[2]}")
        st.subheader(f"'{extracted[3]}'")
        st.subheader(f"'{extracted[4]}'")
    except IndexError:
        st.write("end of page")

if option == "Scorpio":
    try:
        scraped = scrape_astro(scorpio_url)
        extracted = extract_scorpio(scraped)
        result = "\n".join(extracted)

        st.header(f"{extracted[0]}")
        st.image("images/scorpio.png", width=100)
        st.subheader(f"{extracted[1]} : {extracted[2]}")
        st.subheader(f"'{extracted[3]}'")
        st.subheader(f"'{extracted[4]}'")
    except IndexError:
        st.write("end of page")

if option == "Sagittarius":
    try:
        scraped = scrape_astro(sagittarius_url)
        extracted = extract_sagittarius(scraped)
        result = "\n".join(extracted)

        st.header(f"{extracted[0]}")
        st.image("images/sagittarius.png", width=100)
        st.subheader(f"{extracted[1]} : {extracted[2]}")
        st.subheader(f"'{extracted[3]}'")
        st.subheader(f"'{extracted[4]}'")
    except IndexError:
        st.write("end of page")

if option == "Aquarius":
    try:
        scraped = scrape_astro(aquarius_url)
        extracted = extract_aquarius(scraped)
        result = "\n".join(extracted)

        st.header(f"{extracted[0]}")
        st.image("images/aquarius.png", width=100)
        st.subheader(f"{extracted[1]} : {extracted[2]}")
        st.subheader(f"'{extracted[3]}'")
        st.subheader(f"'{extracted[4]}'")
    except IndexError:
        st.write("end of page")

if option == "Capricorn":
    try:
        scraped = scrape_astro(capricorn_url)
        extracted = extract_capricorn(scraped)
        result = "\n".join(extracted)

        st.header(f"{extracted[0]}")
        st.image("images/capricorn.png", width=100)
        st.subheader(f"{extracted[1]} : {extracted[2]}")
        st.subheader(f"'{extracted[3]}'")
        st.subheader(f"'{extracted[4]}'")
    except IndexError:
        st.write("end of page")

if option == "Pisces":
    try:
        scraped = scrape_astro(pisces_url)
        extracted = extract_pisces(scraped)
        result = "\n".join(extracted)

        st.header(f"{extracted[0]}")
        st.image("images/pisces.png", width=100)
        st.subheader(f"{extracted[1]} : {extracted[2]}")
        st.subheader(f"'{extracted[3]}'")
        st.subheader(f"'{extracted[4]}'")
    except IndexError:
        st.write("end of page")

