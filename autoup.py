import requests
from google_play_scraper import app
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def AuToUpDaTE():
    print("🔍 Fetching live global version from Play Store...")
    # 1. Scrape Play Store (France) for the global APK version
    result = app('com.dts.freefireth', lang="fr", country='fr')
    version = result['version']
    
    # 2. Add a mobile User-Agent so Garena doesn't block the Python script
    headers = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/QKQ1.190825.002)"
    }
    
    try:
        # We use the ME region just to trick the API into giving us the JSON with the OB version
        print("📡 Querying Garena Version API...")
        r = requests.get(
            f'https://bdversion.ggbluefox.com/live/ver.php?version={version}&lang=ar&device=android&channel=android&appstore=googleplay&region=ME&whitelist_version=1.3.0&whitelist_sp_version=1.0.0&device_name=google%20G011A&device_CPU=ARMv7%20VFPv3%20NEON%20VMH&device_GPU=Adreno%20(TM)%20640&device_mem=1993',
            headers=headers,
            verify=False,
            timeout=10
        )
        data = r.json()
        ob = data['latest_release_version']
        print(f"✅ Live Version Detected: {ob} ({version})")
    except Exception as e:
        print(f"⚠️ API blocked the request. Raw response: {r.text if 'r' in locals() else 'None'}")
        print("🛡️ Engaging Fail-Safe: Defaulting to OB53")
        ob = "OB53" # Fallback if API fails
    
    # 3. THE MASTER OVERRIDE: Force the IND Server URL
    # We ignore the ME URL from the JSON and strictly return the Indian Polarbear endpoint
    login_url = "https://loginbp.ggpolarbear.com/"
    
    return login_url, ob, version
