# tweets-getter
This program gets a list of your tweets and puts them all into a file.
## Steps
1. Download an archive of your twitter data
2. Go into the archive, and get `tweet.js` from the `data/` directory
3. Copy that file into this directory and rename it `tweets.py`
4. Open `tweets.py` and rename `window.YTD.tweet.part0` to `raw_tweets`
5. Replace every instance of `false` with `False` to make it compatible
with Python