from collections import Counter
import requests
import sys
import bs4
import urllib.parse
import pickle

#################################################################
# FILE : moogle.py
# WRITER : Tomer Titinger , tomer.titinger , 208611939
# EXERCISE : intro2cs2 ex6 2021
# DESCRIPTION: Program the acts as a search engine
# for given sites, urls, and queries.
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################

def get_lines(index_file):
    '''Function that gets the index file,
    returns a list of all the lines in the file'''
    lines_list = open(index_file, 'r').read().strip().split('\n')
    return lines_list


def create_full_links(base_url, index_file):
    '''Function that gets a base url, the index file,
    returns a new list of all the links.'''
    lines_list = get_lines(index_file)
    links = []
    for line in lines_list:
        links.append(urllib.parse.urljoin(base_url, line))
    return links


def elements_in_site(site, lines_list):
    '''Fuction that gets a page,
    returns a dictionary of how many times sent to each of other sites'''
    temp_dict = {}
    for line in lines_list:
        temp_dict[line] = 0

    response = requests.get(site)
    html = response.text

    soup = bs4.BeautifulSoup(html, features="html.parser")
    paragraphs = soup.find_all("p")

    for paragraph in paragraphs:
        for link_in_paragraph in paragraph.find_all("a"):
            target = link_in_paragraph.get("href")

            if target in temp_dict:
                temp_dict[target] += 1
    for line in lines_list:
        if temp_dict[line] == 0:
            temp_dict.pop(line)
    return temp_dict


def create_dict(base_url, index_file):
    '''Function that gets index file and base url, creates a dictionary
    of all the sites with number of links sent to each of the other
    sites in the index file.'''
    traffic_dict = dict()
    lines_list = get_lines(index_file)

    for line in lines_list:
        site = urllib.parse.urljoin(base_url, line)
        traffic_dict[line] = elements_in_site(site, lines_list)
    return traffic_dict


def crawl():
    '''Function that gets base url, index file and output location,
    saves a pickle file of the dict made as asked in part A
    in the given location '''
    base_url = sys.argv[2]
    index_file = sys.argv[3]
    out = sys.argv[4]

    traffic_dict = (create_dict(base_url, index_file))

    with open(out, 'wb') as f:
        pickle.dump(traffic_dict, f)


def get_list_of_index(original_dict):
    '''Function that gets original dict,
    returns a list of indexes of the dict'''
    index_list = []
    for key in original_dict:
        index_list.append(key)
    return index_list


def how_many_out(original_dict):
    '''Function that gets original dict,
    returns a dict of key -> links out'''
    links_amount = {}
    for key in original_dict:
        counter = 0
        for amount in original_dict[key].values():
            counter += amount
        links_amount[key] = counter
    return links_amount


def give_rank(giver, taker, original_dict):
    '''Function that gets a giver, taker, and original dict,
    returns the value to give to the taker'''
    links_amount = how_many_out(original_dict)
    num_to_give = (original_dict[giver][taker]) / links_amount[giver]
    return num_to_give


def reset_dict_values(original_dict, num):
    '''Function that resets dict values as 0/1'''
    reset_dict = dict()
    for page in original_dict:
        if num == 0:
            reset_dict[page] = 0
        else:
            reset_dict[page] = 1
    return reset_dict


def page_rank():
    '''Function that ranks the pages, returns a pickle file'''
    iterations = int(sys.argv[2])
    dict_file = sys.argv[3]
    out_b = sys.argv[4]

    with open(dict_file, "rb") as f:
        original_dict = pickle.load(f)

    r = reset_dict_values(original_dict, 1)
    for i in range(iterations):
        new_r = reset_dict_values(original_dict, 0)
        for giver in r:
            for taker in original_dict[giver]:
                new_r[taker] += r[giver] * \
                                give_rank(giver, taker, original_dict)
        r = new_r.copy()

    with open(out_b, 'wb') as f:
        pickle.dump(r, f)


def dict_of_words(lines, base_url):
    '''Gets sites list (endings) and base url, iterates over the pages
    after concatenating the strings, returns a dict that for each
    word in pages, shows the number of times that word was in the pag '''
    temp_dict = {}
    for line in lines:
        site = urllib.parse.urljoin(base_url, line)
        response = requests.get(site)
        html = response.text

        soup = bs4.BeautifulSoup(html, features="html.parser")
        paragraphs = soup.find_all("p")

        for paragraph in paragraphs:
            content = paragraph.text
            content_list = content.split()
            for word in content_list:
                word = word.strip()
                if word in temp_dict:
                    if line in temp_dict[word]:
                        temp_dict[word][line] += 1
                    else:
                        temp_dict[word][line] = 1
                else:
                    temp_dict[word] = dict()
                    temp_dict[word][line] = 1

    return temp_dict


def words_dict():
    '''Function that gets a base url, index file, output location
    does calculations and saves a pickle file of a dict that for each
    word in pages, shows the number of times that word was in the page'''
    base_url = sys.argv[2]
    index_file = sys.argv[3]
    out_c = sys.argv[4]
    lines = get_lines(index_file)
    dict_words = dict_of_words(lines, base_url)
    with open(out_c, 'wb') as f:
        pickle.dump(dict_words, f)

def words_in_site(words_lst, words_dict, lines):
    '''Gets a words list, returns list of the sites where the
     words are inside'''
    good_sites = []
    for line in lines:
        is_inside = True
        for word in words_lst:
            if word not in words_dict:
                words_lst.remove(word)
                continue
            if line not in words_dict[word]:
                is_inside = False
        if is_inside and len(words_lst) > 0:
            good_sites.append(line)
    return good_sites


def good_sites_dict(good_sites, rank_dict):
    '''Gets a list of good sites and gives back a dictionary
    of their ranks'''
    good_sites_dict = dict()
    for site in good_sites:
        good_sites_dict[site] = rank_dict[site]
    return good_sites_dict


def sortby_rank(good_sites_dict, max_result):
    '''Gets a dictionary of good sites, gives back top results'''
    newsorted = dict(Counter(good_sites_dict).most_common(max_result))
    return newsorted


def howmany_in_site(word, site, words_dict):
    '''Gets a word and a site, returns how many times the word
    was in the site'''
    return words_dict[word][site]


def minimal_in_site(words_lst, site, words_dict):
    '''Gets a words list, site and words dictionary,
    returns the minimal times one of the words was in the site'''
    minimal_times = howmany_in_site(words_lst[0], site, words_dict)
    for word in words_lst:
        amount = howmany_in_site(word, site, words_dict)
        if amount < minimal_times:
            minimal_times = amount
    return minimal_times


def calculate_values(words_lst, words_dict, best_dict):
    '''Gets a words list, words dict, and sorted by rank dict of
    sites where the words appear in, returns a dict of values per
    dict by rank'''
    values_dict = dict()
    for site in best_dict:
        values_dict[site] =best_dict[site] *\
                           minimal_in_site(words_lst, site, words_dict)
    return values_dict


def search():
    '''Function that gets a word/s, max number of watned results, rank
    file and words dict file, prints the sites for the search
    with score by given formula'''
    query = sys.argv[2]
    rank_file = sys.argv[3]
    words_file = sys.argv[4]
    max_result = int(sys.argv[5])
    lines = []
    lst_of_queries = query.split()

    with open(rank_file, "rb") as f:
        rank_dict = pickle.load(f)

    with open(words_file, "rb") as f:
        words_dict = pickle.load(f)

    for key in rank_dict:
        lines.append(key)

    good_sites = words_in_site(lst_of_queries, words_dict, lines)
    good_dict = good_sites_dict(good_sites, rank_dict)
    best_dict = sortby_rank(good_dict, max_result)
    values_dict = calculate_values(lst_of_queries, words_dict, best_dict)
    sorted_last = sortby_rank(values_dict,max_result)
    for key in sorted_last:
        print(key, sorted_last[key])


def main():
    command = sys.argv[1]
    if command == "crawl":
        crawl()
    if command == "page_rank":
        page_rank()
    if command == "words_dict":
        words_dict()
    if command == "search":
        search()


if __name__ == "__main__":
    main()