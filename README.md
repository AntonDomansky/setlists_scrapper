# Setlist.fm Setlist Scraper

## Description

This script is designed for parsing concert setlists of artists from [Setlist.fm](https://www.setlist.fm/).

## Features

- Search for an artist's concerts by name.
- Select one of the latest concerts.
- Retrieve the setlist (list of songs) for the selected concert.
- Error handling and logging.

## Requirements

- Python 3.x
- Installed dependencies (listed in `requirements.txt`)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/AntonDomansky/setlists_scrapper.git
   cd setlist_scraper
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```sh
   python main.py
   ```
2. Enter the artist's name.
3. Select a concert from the suggested list.
4. View the list of songs performed at that concert.
5. Decide whether you want to continue searching.

## Error Handling

- If the artist is not found, the script will notify you.
- If there is no setlist for the concert, the script will inform you.
- In case of parsing errors, the information is logged.
