import instaloader
import pandas as pd

def get_instagram_followers(user_list):
    icerik = []
    L = instaloader.Instaloader()
    
    for username in user_list:
        try:
            profile = instaloader.Profile.from_username(L.context, username)
            icerik.append({'Company': username, 'Followers': profile.followers})
        except instaloader.ProfileNotExistsException:
            print(f"Profile '{username}' not found.")
            icerik.append({'Company': username, 'Followers': 0})

    df = pd.DataFrame(icerik)
    return df

# Kullanım örneği
user_list = ['vodafonetr', 'turkcell', 'akbank', 'netastr', 'teknosa', 'havelsan_resmi', 'kvkturkiye', 
             'bilkom', 'pentateknoloji', 'ziraatbankasi', 'garantibbva', 'isbankasi', 'papara', 
             'turksatkablo', 'kocsistem', 'innova_bilisim', 'logoyazilim', 'mobilteltr']

df = get_instagram_followers(user_list)