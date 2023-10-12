import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

xml_url = "https://www.tcmb.gov.tr/kurlar/today.xml"
df = pd.read_xml(xml_url)
dfUSD = df.query('Kod == "USD"')
dfEUR = df.query('Kod == "EUR"')
usdSatis = float(dfUSD["BanknoteSelling"].iloc[0])
eurSatis = float(dfEUR["BanknoteSelling"].iloc[0])

print("usdSatis:", usdSatis, "-- eurSatis:", eurSatis)
