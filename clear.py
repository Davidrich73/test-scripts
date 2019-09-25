#!/usr/bin/env python
# coding=utf-8
import logging


chars_to_remove = "‘’'1234567890"

#merged_chat_file = "C:\\Users\\david.richards\\Documents\\Rss-imports\\New folder\\newphrases.chat"

p1 = "C:\\Users\\david.richards\\Documents\\Rss-imports\\newphrases.chat"
p2 = "C:\\Users\\david.richards\\Documents\\Rss-imports\\newphrases1.chat"
merged_chat_file = "C:\\Users\\david.richards\\Documents\\Rss-imports\\New folder\\newphrases.chat"


########################################################################################################################
def main():
########################################################################################################################

    if p1.endswith('.chat') and p2.endswith('.chat'):

        mergeandsort(p1, p2, merged_chat_file)
        cleaned_up_array = cleanup(merged_chat_file)

        logging.debug("cleaned up input contains:\n {}".format("\n".join(cleaned_up_array)))
        with open(merged_chat_file, 'w') as fp:
            fp.writelines(cleaned_up_array)
    else:
        logging.error("didn't find two chat files to merge")


########################################################################################################################
def cleanup(merged_chat_file):
########################################################################################################################

    cleaned_up_array = []
    for word in open(merged_chat_file).readlines():
        for c in chars_to_remove: word = word.replace(c, "")
        cleaned_up_array.append(word)

    return cleaned_up_array


########################################################################################################################
def mergeandsort(file1, file2, output):
########################################################################################################################
    # below to merge new.chat file with the old file from previous week

    with open(file1, 'r') as fp1, open(file2, 'r') as fp2:
        merge_data = [x.strip() for x in fp1.readlines() + fp2.readlines()]


    merge_data = sorted(merge_data, reverse=True)
    logging.debug("merged input files contain:\n {}".format("\n".join(merge_data)))

    with open(output, 'w') as output_chat_file:
        output_chat_file.write("\n".join(merge_data))


########################################################################################################################
if __name__ == "__main__":
########################################################################################################################

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')
    main()
