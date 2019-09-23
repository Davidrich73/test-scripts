# This Python file uses the following encoding: utf-8

import re


-- coding: utf-8 --
########################################################################################################################
def main():
########################################################################################################################


   # p1 = 'c:\\users\\david.richards\\Documents\\Rss-import\\newphrases.chat'
    p1 = "C:\\Users\\david.richards\\Documents\\Rss-imports\\newphrases.chat"
#    p2 = 'c:\\users\\david.richards\\Documents\\Rss-import\\newphrases1.chat'
    p2 = "C:\\Users\\david.richards\\Documents\\Rss-imports\\newphrases1.chat"

    if is_chat(p1) and is_chat(p2):
        merged_chat_file = "C:\\Users\\david.richards\\Documents\\Rss-imports\\New folder\\newphrases.chat"
        mergeandsort(p1, p2, merged_chat_file)
        cleaned_up_array = cleanup(merged_chat_file)

        print "cleaned_up_array: {}".format(cleaned_up_array)
        with open(merged_chat_file, 'w') as fp:
            for word in cleaned_up_array:
                fp.write(word)


########################################################################################################################
def cleanup(merged_chat_file):
########################################################################################################################

    cleaned_up_array = []
    chat_words = open(merged_chat_file).readlines()

    for word in chat_words:
        clear_word = remove_invalid_chars(word)
        cleaned_up_array.append(clear_word)

    return cleaned_up_array


########################################################################################################################
def remove_invalid_chars(word):
########################################################################################################################

    chars_to_remove = "‘’ '1234567890"
    new_word=word
    for ch in chars_to_remove:
        #print (ch)
        new_word = new_word.replace(ch,"")
    return new_word


########################################################################################################################
def is_chat(file):
########################################################################################################################

    return file.endswith('.chat')


########################################################################################################################
def remove_character(chars_to_remove, content):
########################################################################################################################

    cleanedup_string = re.sub('<(.|\n)*?>', '', content)
    cleanedup_string = cleanedup_string.translate(None, chars_to_remove)
    return cleanedup_string


########################################################################################################################
# def digits_to_text(s):
########################################################################################################################
    # below is to remove numbers if they exist within .chat file

   # isdigit = str.isdigit
   #  return any(map(isdigit, s))


########################################################################################################################
def mergeandsort(file1, file2, output):
########################################################################################################################
    # below to merge new.chat file with the old file from previous week

    fp1, fp2 = open(file1, 'r'), open(file2, 'r')
    merge_data = fp1.read().strip().split("\n") + fp2.read().strip().split("\n")
    fp1.close()
    fp2.close()
    #print output of file1 and file2

    merge_data = sorted(merge_data, reverse=True)
    print (merge_data)
    fp = open(output, 'w')
    for word in merge_data:
        fp.write(word + "\n")

    fp.close()

    return True


########################################################################################################################
if __name__ == "__main__":
########################################################################################################################

    main()
