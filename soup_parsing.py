'''
Description: This file parses text elements from BeatifulSoup webpage outputs.
'''


###########################
### DEF NEW FUNCTION: 3 ###
# Parsing soup for list data

def soup_parsing(general_soup, credits_soup):

    # Setting up an iterative variable "j" and empty lists to append in
    # while loop:
    j = 0
    ranking_list = []
    song_list = []
    artist_list = []
    feature_list = []
    weeks_list = []

    # First main loop to parse data from general "songs" soup:
    while j in range(len(general_soup) - 1):
        
        # Strip text before splitting:
        ranking_element = general_soup[j].text.strip()
        
        # Split rankings that contain the string "NEW", to strip from
        # the ranking_element text:
        if "NEW" in ranking_element:
            ranking_element, remove_NEW = ranking_element.split("NEW")
        
        # Split rankings that contain the string "RE-", to strip from
        # the ranking_element text:
        if "RE-" in ranking_element:
            ranking_element, remove_RE = ranking_element.split("RE-")
        
        # Split rankings that contain the string "ENTRY", to strip from
        # the ranking_element text:
        if "ENTRY" in ranking_element:
            ranking_element, remove_ENTRY = ranking_element.split("ENTRY")

        # Strip text after splitting:
        ranking_element = ranking_element.strip()

        # Print individual ranking lines to check for extra text, before
        # converting ranking to type int:
        # print(ranking_element)

        ranking_element = int(ranking_element)

        song_element = general_soup[j+3].text.strip("")
        try:
            song, artist = song_element.split("\t\t\n\t\n\n\n\t\n\t")
            song = song.strip()
            artist = artist.strip()
            weeks_element = general_soup[j+13].text.strip()
            weeks_element = int(weeks_element)

            # There should be 1400 results, i.e. 14 for each of 100 song entries,
            # so new song entries begins at intervals of 14:
            j = j + 14

        except:
            song, artist = ["[Page format error]", "[Page format error]"]
            
            weeks_element = general_soup[j+13].text.strip()
            weeks_element = int(weeks_element)
        
            # Some webpages only have 13 pieces of data, rather than 14:
            j = j + 13

        ranking_list.append(ranking_element)
        
        song_list.append(song)
        artist_list.append(artist)
        weeks_list.append(weeks_element)



    # For loop to separate title artists from feature artists:
    k = 0
    for artist_item in artist_list:

        if 'Featuring' in artist_item:
            artist, feature = artist_item.split("Featuring ")
            feature = feature.strip("\n\n")

            # Replace artists instances, rather than appending new instances:
            artist_list[k] = artist.rstrip(" (")

        else:
            feature = ''

        feature_list.append(feature)

        k = k + 1


    # Testing length of title artists list (should be 100) and feature artists:
    # print(len(artist_list))
    # print(feature_list)
    # print(ranking_list)
    # print(weeks_list)


    ########################
    # After getting song data, go back to get song credits/labels info:
    ########################

    # Setting an iterable var "i_c" to grab every 3rd element
    # (Imprint/Promotion Label shows up 3rd after Songwriter(s) and Producer(s)):
    i_c = 0
    labels_list = []

    # Second main loop to parse data from "credits" soup:
    for i_c in range(0, len(credits_soup)):

        # Get the artist's promotion label:
        c_text = credits_soup[i_c]
        # find("p", string=c)
        # print(c_text)

        promo_label_element = c_text.text.strip()

        try:
            remove_credits, label = promo_label_element.split(
                "Imprint/Promotion Label:")
            label = label.strip()
        except:
            label = "[Unknown]"


        labels_list.append(label)


    # Remove first element to start the loop at the second song entry,
    # since first one shows up twice:
    labels_list.pop(0)


    print('Successful soup parsing!')

    return ranking_list,song_list,artist_list,feature_list,weeks_list,labels_list
