from sec_api import ExtractorApi

# set sec-api key
sec_api_key = os.env("sec-api-key")
extractorApi = ExtractorApi(sec_api_key)

def get_section_html(url, section):
    return extractorApi.get_section(url, section, "html")

def get_section_text(url, section):
    return extractorApi.get_section(url, section, "text")