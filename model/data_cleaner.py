import glob.glob
from random import shuffle
import


def text_loader(folder_list):
    DATA={}
    for folders in folder_list:
        folder = []
        books=glob("dataset/"+folders+"/*.txt")
        shuffle(books)
        for files in books:
            if not files:
                continue
            book=open(files).read()
            if len(book)<500:
                continue
            folder.append(book)
        DATA[folders]=folder
    print(folder_list)
    return DATA

def genre_type_compressor(data_dic):
    compressed_data = {}
    for keys in data_dic.keys():
        genre=""
        for files in data_dic[keys]:
            genre=genre+files+"\n"
        compressed_data[keys]=genre
    return compressed_data

def serializer(text):
    serialized_text = text
    # lot of - and then new lines, ie. "Mass-\n\nchusetts" truncate that
    # have to use sub instead of replace because replace catches false positives in page numbers
    serialized_text = re.sub("[a-zA-Z]-\n\n", "", serialized_text)
    serialized_text = re.sub("[a-zA-Z]-\n", "", serialized_text)

    # some texts will combine both \f\r\n ... only care for one
    serialized_text = serialized_text.replace("\r", " ").replace("\f", " ")

    # the new lines are just all over the place from legal documents, compromise and strip them all out (sorry)
    # maybe come back to this later and think about something more optimal to do instead
    serialized_text = serialized_text.replace("\n", " ")

    # remove \xa0
    serialized_text = serialized_text.replace("\xa0", " ")

    # remove another weird pattern
    serialized_text = re.sub("- [- ]{3,100}", " ", serialized_text)

    # remove any page numbers that look like this -3-, -4-, etc, go up to -99-
    # didn't see anymore than 100
    serialized_text = re.sub("-(\d{1,3})-", " ", serialized_text)

    # and then there's page numbers that look like this - 3 - (as opposed to -3-)
    serialized_text = re.sub("- \d{1,3} -", " ", serialized_text)

    # and sometimes they like to write lot of long dashes. i haven't seen more than 90. only catch when at least 3 dashes are used
    serialized_text = re.sub("[-]{3,90}", " ", serialized_text)

    # but even baffling, sometimes they prefer underscores
    serialized_text = re.sub("[_]{3,90}", " ", serialized_text)

    # some texts have 20+ spaces randomly
    serialized_text = re.sub(" +", " ", serialized_text)

    # remove any multiple \n\n in the text. legal seems to really like new lines??
    serialized_text = re.sub("\\n[\\n]{0,10}\\n", "\n", serialized_text)

    # lot of extra spaces at the beginning of many dockets ..
    serialized_text = serialized_text.strip()

    return serialized_text

def data_loader(folder_list):
    if(type(folder_list)==str):
        f=[]
        f.append(folder_list)
        folder_list=f
    data_dic = text_loader(folder_list)
    for types in data_dic.keys():
        for book in types:
            book = serializer(book)
    genre_wise_data = genre_type_compressor(data_dic)
    for genre in genre_wise_data.keys():
        with open("dataset/filter_"str(genre)+".txt",w+) as opened_file:
            opened_file.write(genre_wise_data[genre])
    print("Done!")
    return genre_wise_data
