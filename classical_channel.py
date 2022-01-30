import tweepy


USERS = {'AG' : '1487725830419914754',
         'RK' : '942611539042877440',
         'GP' : '1487706234040229894',
         'QM' : '1487721422151913473'
        }

def authenticate(user):
    if user==USERS['QM']:
        #quantum master details
        auth = tweepy.OAuthHandler("M1JiB0ALf3SgKoLkpfo2xf1ll", "SCsDjJhNFTngxj0xusKiXiIAM80yImhu5swHVWWANENT8RyfoP")
        auth.set_access_token("1487721422151913473-fP1zCmzRVJUItQyWFPPUprfeRnEAFj", "aXiBWJO0gcTV0vZHHIRIcEqQsu2Z9jv5YxSpTEUvVKlZo")
    elif user==USERS['RK']:
        #rupeshknn details
        auth = tweepy.OAuthHandler("AS4Dvzlr27meAV6NAmYY2bITY", "duqwqGV8HSgLprZnEMiUbVO8p7klnnUHh4UqxJAxSMyw0WMRfB")
        auth.set_access_token("942611539042877440-RG0z3ySCvPhRcfR5oek1ngHCt8Lsjcv", "5idekPwy8iBxYO3cXZUS4UfhAFseenh8uVSUGKNiZp181")
    else:
        print
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
        return api, int(api.get_direct_messages()[0].created_timestamp)
    except:
        print("Error during authentication")
        return None