import requests
from google_play_scraper import app
import urllib3

# Suppress the insecure request warnings in the console
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def AuToUpDaTE():
    # Scrape the Indian Play Store for the live version
    result = app('com.dts.freefireth', lang="en", country='in')
    version = result['version']
    
    # 💀 THE FIX: Switched to region=IND, lang=en, and added verify=False
    r = requests.get(
        f'https://bdversion.ggbluefox.com/live/ver.php?version={version}&lang=en&device=android&channel=android&appstore=googleplay&region=IND&whitelist_version=1.3.0&whitelist_sp_version=1.0.0&device_name=google%20G011A&device_CPU=ARMv7%20VFPv3%20NEON%20VMH&device_GPU=Adreno%20(TM)%20640&device_mem=1993',
        verify=False
    ).json()
    
    url = r['server_url']
    ob = r['latest_release_version']
    return url, ob, version
