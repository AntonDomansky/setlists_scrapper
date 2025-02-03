from utils import get_soup, save_to_logs, change_symbols
from settings import re_pattern

def main():
    def one_more():
        question = input(f"\nOne more time? (y/n): ").strip().lower()
        if question == 'y':
            main()
        elif question == 'n':
            return
        else:
            one_more()




    artist_name = input('Enter artist name: ').lower().strip()

    def get_setlist(show_link):
        soup = get_soup(show_link)
        try:
            if soup:
                empty_setlist = soup.find('div', class_='emptySetlist')
                if empty_setlist and 'no songs in this setlist' in empty_setlist.text:
                    print(f"{empty_setlist.find('div').find('p').text.replace(', but ', '').strip()}")
                    one_more()
                else:
                    songs_wrapper = soup.find('ol', class_='songsList')
                    songs_list = songs_wrapper.find_all('div', class_='songPart')
                    for i, song_name in enumerate(songs_list):
                        print(f"{i + 1}. {song_name.text.strip()}")
                        pass
                    one_more()
            else:
                one_more()
        except Exception as e:
            save_to_logs(f"Error while parsing setlist:\n{e}")
            one_more()

    def get_show_link(band_name):
        # soup = get_soup(f"https://www.setlist.fm/search?query={band_name.replace(' ', '+').replace('-', '+')}")
        soup = get_soup(f"https://www.setlist.fm/search?query={change_symbols(re_pattern, '+', band_name)}")
        error_message = soup.find('div', class_='alert alert-danger')
        if error_message:
            print(f"{error_message.find('p').text} Make sure all words are spelled correctly.")
            one_more()
        else:
            try:
                content_wrapper = soup.find('div', class_='row contentBox visiblePrint')
                shows_list = content_wrapper.find_all('h2')

                print(f"\nLast {len(shows_list)} {artist_name.title()}'s shows list:")
                for i, show in enumerate(shows_list):
                    print(f"{i + 1}. {show.text}")

                while True:
                    try:
                        show_num = int(input(f"\nEnter the number of the show whose setlist you'd like to see: "))
                    except:
                        show_num = False

                    if isinstance(show_num, int) and show_num > 0 and show_num <= len(shows_list):
                        try:
                            show_link = f"https://www.setlist.fm/{shows_list[show_num - 1].find('a').get('href')}"
                            return show_link
                        except Exception as e:
                            save_to_logs(f"Error:\n{e}")
                            continue
                    print(f"Entered number of the show should be number between 1 und {len(shows_list)}")
            except Exception as e:
                save_to_logs(f"Error:\n{e}")
                one_more()

    get_setlist(get_show_link(artist_name))


if __name__ == '__main__':
    main()
