Scrapes the Billboard Hot 100 for a given date and creates a **private** Spotify playlist.

## Features
- Prompts you for a date (`YYYY-MM-DD`)
- Scrapes the Billboard Hot 100 titles for that date
- Searches Spotify for each track and collects their URIs
- Creates a **private** playlist in your account and adds the tracks

## Requirements
- Python 3.10+  
- A Spotify account and a Spotify Developer App (free)

## Setup

1. **Clone & enter the project**
   ```bash
   git clone https://github.com/<you>/Spotify-webscraping.git
   cd Spotify-webscraping

2. **Install dependencies**
   ```bash
   python3 -m pip install -r requirements.txt

3. **Create a Spotify app**
   - Go to https://developer.spotify.com → Dashboard → Create an app
   - Copy your Client ID and Client Secret
  
4. **Create your .env file**
   - SPOTIPY_CLIENT_ID=your_client_id
   - SPOTIPY_CLIENT_SECRET=your_client_secret
   - SPOTIPY_REDIRECT_URI=https://example.com/callback
   - Do not commit .env (already ignored by .gitignore)

5. **Run main.py**
   - When prompted, log in to Spotify in the browser window that opens.
   - Enter a date like 2020-07-01 when asked.
   - The script will create a private playlist named YYYY-MM-DD Billboard 100

   
