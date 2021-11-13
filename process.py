log_file = open("um-server-01.txt")
# i think line 1 is connecting the .txt file to this .py file, needed in order to use python to get/manipulate data

#line 5 is defining a variable called sales_report to the .txt file that has been named log_file
def sales_reports(log_file):
    #line 7 is asking for data from each line, with more specifications to follow
    for line in log_file:
        #.rstrip() is used to remove any trailing characters at the end of a string, in line 9 i believe it is removing whitespace after each line in the .txt, but i'm not sure because when the code runs you can't see any missing whitespace and there is no puncuation to remove
        line = line.rstrip()
        #line 11 is assigning the first 4 characters in each line as the "day" by saying that day equals line[0:3] 
        day = line[0:3]
        #line 13 is saying to print out the lines only if the day is equal to Tue
        if day == "Tue":
            #line 14 is saying to print the lines that meet the criteria above
            print(line)

#this is calling the file log_file in the function sales_reports that is coded above
sales_reports(log_file)
